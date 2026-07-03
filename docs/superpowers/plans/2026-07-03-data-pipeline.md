# Data Pipeline "Once and Right" — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the two-exporter/scratch-DB pipeline with one platform-owned exporter that reads the system of record directly, plus a transparent `publish`/`ship` flow and a committed eval-snapshot byproduct.

**Architecture:** The data platform (`mccoy-tyner`) reads `postgres._jazzcanon` through the read-only role `_jazzcanon_ro`, writes the canonical app-shaped contract to `exports/jazz-canon/`, and fans it out to the live site (`jazz-canon`) and to dated eval snapshots. The `jazzcanon_fable` scratch DB and both old exporters are retired. Deploy stays manual (`wrangler` from vps8); `git push` never deploys.

**Tech Stack:** bash, PostgreSQL 16 (`psql`, port 5433, vps8), `node` (JSON validation, already used), `npm`/Vite (site build), `wrangler` (Cloudflare Pages deploy), `jq` (verification only).

## Global Constraints

- Source of truth is `_jazzcanon` schema in the **`postgres`** database on `vps8:5433`. Never read `jazzcanon_fable` (it is being deleted).
- Read access uses role **`_jazzcanon_ro`** via the connection URL in `mccoy-tyner/.env.local` key `JAZZCANON_DB_URL`. Verified working: `psql "$JAZZCANON_DB_URL"` connects and is write-denied.
- Never print or commit secrets. `.env.local` (platform) and `.env` (site) are already gitignored; keep them so.
- Commit scope: one data change commits **only the platform repo**. Deploy is a `wrangler` push, not a git act.
- Deploying to jazzcanon.com and dropping any database are **human-only** acts — the tasks that do them (Task 5, Task 6) must not run without the operator's explicit go-ahead.
- The contract shape (`albums.json` / `details.json` / `graph.json` field names) must stay byte-for-byte compatible with what the current live app consumes — this plan changes the data *source* and *home*, not the shape.
- All new scripts: `#!/usr/bin/env bash` + `set -euo pipefail`.

---

## File Structure

- Create `mccoy-tyner/scripts/export.sh` — reads system of record, validates invariants, writes `exports/jazz-canon/*.json`.
- Create `mccoy-tyner/scripts/publish.sh` — runs export, cuts dated snapshot + MANIFEST, commits the platform data.
- Create `mccoy-tyner/scripts/ship.sh` — runs publish, copies contract into the site, builds, previews (default), deploys, verifies.
- Create `mccoy-tyner/exports/jazz-canon/` — canonical committed contract (dir + generated JSON).
- Create `mccoy-tyner/snapshots/` — committed dated eval bundles.
- Modify `jazz-canon/.gitignore` — ignore only the three **generated** files (`albums.json`, `details.json`, `graph.json`). NOT `*.json`: `recently-added.json` is hand-authored editorial data owned by the site and stays committed.
- Delete `mccoy-tyner/scripts/export.py` (old shape) and `jazz-canon/scripts/export.sh` (wrong source).
- Move `~/dev/active/jazz-canon-site` → `~/dev/paused/` (dead repo).
- Drop database `jazzcanon_fable` (gated, last).

---

### Task 1: Platform exporter reading the system of record

**Files:**
- Create: `mccoy-tyner/scripts/export.sh`
- Create: `mccoy-tyner/exports/jazz-canon/` (output dir)

**Interfaces:**
- Consumes: `JAZZCANON_DB_URL` from `mccoy-tyner/.env.local`; schema `_jazzcanon` in DB `postgres`.
- Produces: `exports/jazz-canon/albums.json`, `details.json`, `graph.json` — same field shapes the live app reads. Exit 0 on success, non-zero (with `INVARIANT FAILED: …`) on a bad export.

- [ ] **Step 1: Write the exporter script**

Create `mccoy-tyner/scripts/export.sh` with exactly this content:

```bash
#!/usr/bin/env bash
# Export The Jazz Canon contract from the SYSTEM OF RECORD (postgres._jazzcanon)
# via the read-only role, into app-shaped JSON consumed by jazz-canon and evals.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL="$(grep -E '^JAZZCANON_DB_URL=' "$ROOT/.env.local" | cut -d= -f2-)"
[ -n "$URL" ] || { echo "✗ JAZZCANON_DB_URL not found in .env.local" >&2; exit 1; }
PSQL=(psql "$URL" -v ON_ERROR_STOP=1 -X -q -At)
OUT="$ROOT/exports/jazz-canon"
mkdir -p "$OUT"

# --- pre-flight referential integrity (abort before writing anything) ---
orphans=$("${PSQL[@]}" -c "SELECT count(*) FROM _jazzcanon.performance p
  LEFT JOIN _jazzcanon.person pe ON pe.id=p.person_id
  LEFT JOIN _jazzcanon.instrument i ON i.id=p.instrument_id
  WHERE pe.id IS NULL OR i.id IS NULL")
[ "$orphans" = "0" ] || { echo "✗ INVARIANT FAILED: $orphans performance rows with orphan person/instrument FK" >&2; exit 1; }
noperf=$("${PSQL[@]}" -c "SELECT count(*) FROM _jazzcanon.album a
  WHERE NOT EXISTS (SELECT 1 FROM _jazzcanon.performance p WHERE p.album_id=a.id)")
[ "$noperf" = "0" ] || { echo "✗ INVARIANT FAILED: $noperf albums with zero performances" >&2; exit 1; }

# --- albums.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/albums.json"
SELECT json_agg(r ORDER BY r.year, r.id)
FROM (
  SELECT a.id, a.title, a.artist_name AS artist, a.year,
         l.name AS label, a.catalog_number AS catalog,
         s.display_name AS style, s.code AS "styleCode",
         aa.source_url AS "artUrl", a.apple_album_id AS "appleAlbumId"
  FROM _jazzcanon.album a
  LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
  JOIN _jazzcanon.style s ON s.id = a.style_primary_id
  LEFT JOIN _jazzcanon.album_art aa ON aa.album_id = a.id AND aa.is_primary
) r;
SQL

# --- details.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/details.json"
SELECT json_object_agg(a.id, json_build_object(
  'description', a.description,
  'recordingDates', a.recording_dates_text,
  'leader', lead.canonical_name,
  'studios', (
     SELECT coalesce(json_agg(DISTINCT st.name), '[]'::json)
     FROM _jazzcanon.session se
     JOIN _jazzcanon.studio st ON st.id = se.studio_id
     WHERE se.album_id = a.id),
  'tracks', (
     SELECT coalesce(json_agg(json_build_object(
              'n', t.track_number, 'title', t.title, 'side', t.side,
              'duration', t.duration_text, 'appleTrackId', t.apple_track_id,
              'e', t.epistemic_track,
              'personnel', (
                 SELECT coalesce(json_agg(json_build_object(
                          'personId', tp.person_id, 'name', tp.canonical_name,
                          'instrument', tp.instrument, 'e', tp.epistemic)
                        ORDER BY fam.ord, tp.instrument, tp.canonical_name), '[]'::json)
                 FROM _jazzcanon.v_track_personnel tp
                 JOIN _jazzcanon.instrument ins ON ins.name = tp.instrument
                 CROSS JOIN LATERAL (SELECT array_position(
                    ARRAY['brass','woodwinds','keyboards','strings','percussion','other']::text[],
                    ins.family::text) AS ord) fam
                 WHERE tp.track_id = t.id)
            ) ORDER BY t.track_number), '[]'::json)
     FROM _jazzcanon.track t WHERE t.album_id = a.id),
  'personnel', (
     SELECT coalesce(json_agg(json_build_object(
              'personId', row."personId", 'name', row.name,
              'entries', row.entries, 'scope', row.scope)
            ORDER BY row.ord, row.name), '[]'::json)
     FROM (
       SELECT pe.id AS "personId", pe.canonical_name AS name,
              json_agg(json_build_object('instrument', i.name, 'e', p.epistemic)
                       ORDER BY i.name) AS entries,
              min(p.scope::text) AS scope,
              min(array_position(
                 ARRAY['brass','woodwinds','keyboards','strings','percussion','other']::text[],
                 i.family::text)) AS ord
       FROM _jazzcanon.performance p
       JOIN _jazzcanon.person pe ON pe.id = p.person_id
       JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
       WHERE p.album_id = a.id
       GROUP BY pe.id, pe.canonical_name
     ) row)
))
FROM _jazzcanon.album a
LEFT JOIN _jazzcanon.person lead ON lead.id = a.leader_person_id;
SQL

# --- graph.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/graph.json"
SELECT json_build_object(
  'people', (
     SELECT json_object_agg(pe.id, pe.canonical_name)
     FROM _jazzcanon.person pe
     WHERE EXISTS (SELECT 1 FROM _jazzcanon.performance p WHERE p.person_id = pe.id)),
  'edges', (
     SELECT json_agg(e) FROM (
       SELECT p.person_id AS p, p.album_id AS a,
              json_agg(json_build_object('instrument', i.name, 'e', p.epistemic)
                       ORDER BY i.name) AS entries
       FROM _jazzcanon.performance p
       JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
       GROUP BY p.person_id, p.album_id
     ) e)
);
SQL

# --- structural invariants (no magic numbers — hold at any canon size) ---
node - "$OUT" <<'JS'
const fs = require('fs'), path = process.argv[2];
const rd = f => JSON.parse(fs.readFileSync(path + '/' + f, 'utf8'));
const albums = rd('albums.json'), details = rd('details.json'), graph = rd('graph.json');
const fail = m => { console.error('✗ INVARIANT FAILED: ' + m); process.exit(1); };
if (albums.length !== Object.keys(details).length)
  fail(`albums ${albums.length} != details ${Object.keys(details).length}`);
for (const a of albums) {
  for (const k of ['title','artist','year','artUrl'])
    if (!a[k]) fail(`album ${a.id} missing ${k}`);
  const d = details[a.id];
  if (!d) fail(`no details for album ${a.id}`);
  if (!d.tracks || d.tracks.length < 1) fail(`album ${a.id} has no tracks`);
  if (!d.personnel || d.personnel.length < 1) fail(`album ${a.id} has no personnel`);
}
if (Object.keys(graph.people).length < 1) fail('graph.people empty');
if (!graph.edges || graph.edges.length < 1) fail('graph.edges empty');
for (const e of graph.edges) {
  if (!graph.people[e.p]) fail(`edge references unknown person ${e.p}`);
  if (!e.entries || e.entries.length < 1) fail(`edge ${e.p}/${e.a} has no entries`);
}
const kb = f => Math.round(fs.statSync(path + '/' + f).size / 1024);
console.log(`✓ Export valid — albums=${albums.length} people=${Object.keys(graph.people).length} `
  + `edges=${graph.edges.length}  (${kb('albums.json')}+${kb('details.json')}+${kb('graph.json')} KB)`);
JS
```

- [ ] **Step 2: Make it executable and run it**

Run:
```bash
chmod +x ~/dev/active/mccoy-tyner/scripts/export.sh
~/dev/active/mccoy-tyner/scripts/export.sh
```
Expected: a line like `✓ Export valid — albums=100 people=… edges=…  (…KB)` and exit 0. Three files now exist in `mccoy-tyner/exports/jazz-canon/`.

- [ ] **Step 3: Verify it read the system of record (the Giant Steps proof)**

Run:
```bash
jq '.["john-coltrane-giant-steps"].tracks[] | {n, personnel: (.personnel|length)}' \
  ~/dev/active/mccoy-tyner/exports/jazz-canon/details.json
```
Expected: every track shows `"personnel": 4` (not 2). This proves the export came from the fixed source of truth, not the stale scratch DB.

- [ ] **Step 4: Verify shape compatibility with the live app**

Run (compares field keys of the new albums.json against the site's current one):
```bash
diff <(jq -S '.[0]|keys' ~/dev/active/mccoy-tyner/exports/jazz-canon/albums.json) \
     <(jq -S '.[0]|keys' ~/dev/active/jazz-canon/app/public/data/albums.json)
```
Expected: no output (identical key sets). Same for `details`/`graph` shape is covered by the app rendering unchanged in Task 5.

- [ ] **Step 5: Verify the invariant guard actually fires (negative test)**

Run (temporarily corrupt a copy, confirm the node guard rejects it):
```bash
cp ~/dev/active/mccoy-tyner/exports/jazz-canon/albums.json /tmp/bad-albums.json
jq 'del(.[0].artUrl)' /tmp/bad-albums.json > /tmp/albums.json
cp ~/dev/active/mccoy-tyner/exports/jazz-canon/{details,graph}.json /tmp/
node -e "process.argv[2]='/tmp'; $(sed -n '/^node - /,/^JS/p' ~/dev/active/mccoy-tyner/scripts/export.sh | sed '1d;$d')" 2>&1 | grep -q 'INVARIANT FAILED: album .* missing artUrl' && echo 'guard works' || echo 'GUARD DID NOT FIRE'
```
Expected: `guard works`. Then clean up: `rm -f /tmp/albums.json /tmp/details.json /tmp/graph.json /tmp/bad-albums.json`.

- [ ] **Step 6: Commit**

```bash
cd ~/dev/active/mccoy-tyner
git add scripts/export.sh exports/jazz-canon
git commit -m "feat: platform exporter reads system of record directly

Reads postgres._jazzcanon via _jazzcanon_ro (read-only), writes the
app-shaped contract to exports/jazz-canon/. Structural invariants replace
the hardcoded count guard. Giant Steps now exports 4 personnel per track.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: `publish` — snapshot + commit the contract

**Files:**
- Create: `mccoy-tyner/scripts/publish.sh`
- Create: `mccoy-tyner/snapshots/` (created on first run)

**Interfaces:**
- Consumes: `scripts/export.sh` (Task 1); `JAZZCANON_DB_URL`.
- Produces: committed `exports/jazz-canon/*.json` + `snapshots/canon-YYYY-MM-DD/{albums,details,graph}.json` + `MANIFEST`. This is the standalone command for cutting an eval bundle without deploying.

- [ ] **Step 1: Write the publish script**

Create `mccoy-tyner/scripts/publish.sh`:

```bash
#!/usr/bin/env bash
# Publish the canon contract from the system of record, cut a dated eval
# snapshot, and commit both. Deploys nothing — safe to run for evals alone.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

"$ROOT/scripts/export.sh"

DATE="$(date +%F)"
SNAP="$ROOT/snapshots/canon-$DATE"
mkdir -p "$SNAP"
cp "$ROOT/exports/jazz-canon/"albums.json "$SNAP/"
cp "$ROOT/exports/jazz-canon/"details.json "$SNAP/"
cp "$ROOT/exports/jazz-canon/"graph.json "$SNAP/"

URL="$(grep -E '^JAZZCANON_DB_URL=' "$ROOT/.env.local" | cut -d= -f2-)"
counts="$(psql "$URL" -X -q -At -c "SELECT
  'albums='||(SELECT count(*) FROM _jazzcanon.album)||
  ' people='||(SELECT count(*) FROM _jazzcanon.person)||
  ' tracks='||(SELECT count(*) FROM _jazzcanon.track)||
  ' performances='||(SELECT count(*) FROM _jazzcanon.performance)||
  ' track_links='||(SELECT count(*) FROM _jazzcanon.performance_track)")"
printf 'The Jazz Canon — data snapshot\ndate: %s\n%s\n' "$DATE" "$counts" > "$SNAP/MANIFEST"

git add exports/jazz-canon "snapshots/canon-$DATE"
if git diff --cached --quiet; then
  echo "✓ Published — no data change since last publish ($DATE snapshot refreshed)"
else
  git commit -q -m "data: publish canon contract + snapshot $DATE

$counts

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
  echo "✓ Published & committed contract + snapshot ($DATE) — $counts"
fi
```

- [ ] **Step 2: Run it**

```bash
chmod +x ~/dev/active/mccoy-tyner/scripts/publish.sh
~/dev/active/mccoy-tyner/scripts/publish.sh
```
Expected: `✓ Published & committed contract + snapshot (YYYY-MM-DD) — albums=100 people=… track_links=495`.

- [ ] **Step 3: Verify the snapshot bundle**

```bash
D="$(date +%F)"
ls ~/dev/active/mccoy-tyner/snapshots/canon-$D/
cat ~/dev/active/mccoy-tyner/snapshots/canon-$D/MANIFEST
```
Expected: `albums.json details.json graph.json MANIFEST`, and the MANIFEST shows the date + counts (including `track_links=495`).

- [ ] **Step 4: Verify it committed (and only the platform repo)**

```bash
cd ~/dev/active/mccoy-tyner && git log --oneline -1 && git status --short
```
Expected: top commit is the publish; working tree clean.

---

### Task 3: `ship` — publish → build → preview → deploy → verify

**Files:**
- Create: `mccoy-tyner/scripts/ship.sh`

**Interfaces:**
- Consumes: `scripts/publish.sh` (Task 2); site at `~/dev/active/jazz-canon` with `.env` (Cloudflare token) and `app/` (Vite).
- Produces: the live site updated. Default run pauses at a preview; `ship --go` (or `--no-preview`) skips the pause. Data is committed by the `publish` stage; deploy is not a git act.

- [ ] **Step 1: Write the ship script**

Create `mccoy-tyner/scripts/ship.sh`:

```bash
#!/usr/bin/env bash
# One transparent command: publish the contract, build the site, (preview),
# deploy to jazzcanon.com, verify. Preview pause is ON by default; pass --go
# to skip it. Data is committed by publish; deploy uses wrangler (not git).
set -euo pipefail

PLATFORM="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$HOME/dev/active/jazz-canon"
GO=0; case "${1:-}" in --go|--no-preview) GO=1 ;; esac

"$PLATFORM/scripts/publish.sh"

cp "$PLATFORM/exports/jazz-canon/"albums.json  "$SITE/app/public/data/"
cp "$PLATFORM/exports/jazz-canon/"details.json "$SITE/app/public/data/"
cp "$PLATFORM/exports/jazz-canon/"graph.json   "$SITE/app/public/data/"
echo "✓ Copied contract into site"

cd "$SITE/app"
npm run build >/dev/null
echo "✓ Built site (app/dist/)"

if [ "$GO" -eq 0 ]; then
  echo "… Preview at http://vps8-core:4173 — review it in your browser."
  npm run preview -- --host >/tmp/jazzcanon-preview.log 2>&1 &
  PREV=$!
  trap 'kill "$PREV" 2>/dev/null || true' EXIT
  read -rp "Press [Enter] to deploy to jazzcanon.com, or Ctrl-C to abort... "
  kill "$PREV" 2>/dev/null || true
  trap - EXIT
fi

set -a; source "$SITE/.env"; set +a
npx wrangler pages deploy dist --branch main
code="$(curl -s -o /dev/null -w '%{http_code}' https://jazzcanon.com/)"
if [ "$code" = "200" ]; then
  echo "✓ Deployed & verified (HTTP $code) — https://jazzcanon.com"
  echo "✓ Done. Data already committed by publish; deploy is not a git act."
else
  echo "✗ Verify FAILED: HTTP $code — check the Cloudflare dashboard / rollback if needed" >&2
  exit 1
fi
```

- [ ] **Step 2: Make executable; test up to the preview WITHOUT deploying**

Deploy is human-only, so this step exercises everything *before* the deploy and then aborts at the pause.
```bash
chmod +x ~/dev/active/mccoy-tyner/scripts/ship.sh
~/dev/active/mccoy-tyner/scripts/ship.sh
```
Expected narration: `✓ Published…`, `✓ Copied contract into site`, `✓ Built site`, then `… Preview at http://vps8-core:4173` and a `Press [Enter]…` prompt. Open http://vps8-core:4173, confirm the site renders and Giant Steps shows 4 musicians per track. **Then press Ctrl-C to abort before deploying.** (The real deploy happens in Task 5.)

- [ ] **Step 3: Confirm no partial git mess**

```bash
cd ~/dev/active/mccoy-tyner && git status --short
```
Expected: clean (publish already committed; the site copy is about to be gitignored in Task 4).

- [ ] **Step 4: Commit the script**

```bash
cd ~/dev/active/mccoy-tyner
git add scripts/ship.sh
git commit -m "feat: transparent ship command (publish→build→preview→deploy→verify)

Preview pause on by default; --go skips it. Deploy via wrangler from vps8.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Retire old exporters; make site data generated

**Files:**
- Modify: `jazz-canon/.gitignore`
- Delete: `mccoy-tyner/scripts/export.py`
- Delete: `jazz-canon/scripts/export.sh`

**Interfaces:**
- Consumes: nothing new.
- Produces: a codebase with exactly one exporter (`mccoy-tyner/scripts/export.sh`) and a site whose three **generated** data files are gitignored. `recently-added.json` (hand-authored editorial data, consumed by `app/src/lib/data.ts`) stays committed and untouched.

- [ ] **Step 1: Gitignore ONLY the three generated files**

`recently-added.json` is hand-authored (curated album ids + "added" dates) and must remain tracked — do NOT ignore or remove it.
```bash
cd ~/dev/active/jazz-canon
cat >> .gitignore <<'EOF'
# Generated by the platform exporter (mccoy-tyner/scripts/export.sh); do not commit.
# NOTE: recently-added.json is hand-authored editorial data and stays committed.
app/public/data/albums.json
app/public/data/details.json
app/public/data/graph.json
EOF
git rm --cached app/public/data/albums.json app/public/data/details.json app/public/data/graph.json
```
Expected: git stages the removal of exactly those three from the index (they remain on disk). `recently-added.json` is not mentioned.

- [ ] **Step 2: Delete the two dead exporters**

```bash
rm ~/dev/active/mccoy-tyner/scripts/export.py
cd ~/dev/active/jazz-canon && git rm scripts/export.sh
```

- [ ] **Step 3: Regenerate site data and confirm the build still works**

Do NOT deploy here (that is Task 5). Regenerate + build only, and confirm the editorial file survived:
```bash
~/dev/active/mccoy-tyner/scripts/export.sh
cp ~/dev/active/mccoy-tyner/exports/jazz-canon/{albums,details,graph}.json ~/dev/active/jazz-canon/app/public/data/
test -f ~/dev/active/jazz-canon/app/public/data/recently-added.json && echo "✓ recently-added.json intact"
cd ~/dev/active/jazz-canon/app && npm run build >/dev/null && echo "✓ site builds with generated data"
```
Expected: `✓ recently-added.json intact` and `✓ site builds with generated data`.

- [ ] **Step 4: Commit each repo separately (commit-scope rule)**

```bash
cd ~/dev/active/jazz-canon
git add .gitignore
git commit -m "chore: site data is generated by the platform exporter, not committed

Removes the site's own export.sh; app/public/data/*.json is now produced by
mccoy-tyner/scripts/export.sh and gitignored.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"

cd ~/dev/active/mccoy-tyner
git add -A scripts/
git commit -m "chore: remove redundant old-shape export.py (single exporter now)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: [HUMAN-ONLY] Prove the pipeline live — land the Giant Steps fix

**Files:** none (operational).

**Interfaces:**
- Consumes: the full pipeline (Tasks 1–4).
- Produces: jazzcanon.com serving the direct-read data, with Giant Steps showing 4 musicians per track.

> ⚠️ This task deploys to production. Do not run it without the operator present and consenting. This is the run that finally puts the Giant Steps fix on the live site.

- [ ] **Step 1: Ship for real, with the preview pause**

```bash
~/dev/active/mccoy-tyner/scripts/ship.sh
```
At the preview (http://vps8-core:4173), open Giant Steps and confirm each track lists 4 musicians. If it looks right, press **[Enter]** to deploy. If not, Ctrl-C and stop.

- [ ] **Step 2: Verify live**

```bash
curl -s -o /dev/null -w "jazzcanon.com -> %{http_code}\n" https://jazzcanon.com/
```
Expected: `200`. Then hard-refresh https://jazzcanon.com (Cmd-Shift-R), open Giant Steps, and confirm 4 musicians per track are visible.

- [ ] **Step 3: Confirm the maintenance log reality**

The maintenance-log Resolved entry for Giant Steps said "NOT YET DEPLOYED." After a successful deploy, that is now live. (The runbook Scenario B rewrite — a separate queued task — will update process docs.)

---

### Task 6: [HUMAN-ONLY / DESTRUCTIVE] Drop the `jazzcanon_fable` scratch DB

**Files:** none (database).

**Interfaces:**
- Consumes: a proven pipeline (Task 5 complete).
- Produces: `jazzcanon_fable` removed; only the system of record remains.

> ⚠️ Destructive and human-only. Only after Task 5 has proven the site runs from the system of record. Requires explicit go-ahead.

- [ ] **Step 1: Confirm nothing references the scratch DB anymore**

```bash
grep -rn "jazzcanon_fable" ~/dev/active/mccoy-tyner ~/dev/active/jazz-canon \
  --include='*.sh' --include='*.py' --include='*.mjs' --include='*.js' --include='*.json' 2>/dev/null
```
Expected: no matches in live scripts. (Doc/runbook mentions are fine and are handled by the runbook rewrite.)

- [ ] **Step 2: Drop the database (only on explicit approval)**

```bash
sudo -n -u postgres psql -p 5433 -c "DROP DATABASE jazzcanon_fable;"
sudo -n -u postgres psql -p 5433 -lqt | cut -d'|' -f1 | grep -qw jazzcanon_fable \
  && echo "STILL PRESENT — investigate" || echo "✓ jazzcanon_fable dropped"
```
Expected: `✓ jazzcanon_fable dropped`.

---

### Task 7: Retire the dead site repo

**Files:**
- Move: `~/dev/active/jazz-canon-site` → `~/dev/paused/jazz-canon-site`

**Interfaces:**
- Consumes: nothing.
- Produces: the superseded repo out of the active tree.

- [ ] **Step 1: Confirm it is the dead one, then move it**

```bash
cd ~/dev/active/jazz-canon-site && git log --oneline -1   # expect the "remove migrated docs and scripts" commit
mv ~/dev/active/jazz-canon-site ~/dev/paused/
ls -d ~/dev/paused/jazz-canon-site && echo "✓ moved to paused"
```
Expected: `✓ moved to paused`. No commit needed (directory move only).

---

## Self-Review

- **Spec coverage:** §3 direct-read + `_jazzcanon_ro` → Task 1; §4.1 single exporter/retire → Tasks 1,4; §4.2 invariants → Task 1 Steps 1,5; §4.3 publish/ship split → Tasks 2,3; §4.4 snapshot → Task 2; §5 cleanup order (incl. gated drop + repo move) → Tasks 4,6,7; §5.6 prove-live → Task 5; §6 success criteria exercised across Tasks 1–5. Follow-up runbook rewrite (spec §8) intentionally out of this plan (queued separately by the operator).
- **Placeholder scan:** no TBD/TODO; all scripts inlined in full; negative test (Task 1 Step 5) shows real code; commands have expected output.
- **Type/name consistency:** `exports/jazz-canon/{albums,details,graph}.json`, `JAZZCANON_DB_URL`, `_jazzcanon_ro`, `snapshots/canon-YYYY-MM-DD/`, `--go`/`--no-preview` used identically across tasks. `publish.sh`→`ship.sh` call chain matches file names.
- **`recently-added.json` (resolved):** confirmed hand-authored editorial data owned by the site (consumed by `app/src/lib/data.ts`), not exporter output. Task 4 gitignores only the three generated files by name and explicitly preserves it; Task 4 Step 3 asserts it survives. Clean platform/site boundary — no action beyond that.
