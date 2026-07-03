# Data Pipeline — "Once and Right" Design

**Date:** 2026-07-03
**Status:** Approved (design), pending implementation plan
**Owner repo:** `mccoy-tyner` (the data platform / granite foundation)
**Consumer repo:** `jazz-canon` (jazzcanon.com — first UI, not the only future one)

---

## 1. Purpose

Establish one solid, foolproof, long-lived pipeline that carries a data change
from the system of record to the live site with minimal steps, no scratch files,
and no staleness traps. The data platform is the durable asset; jazzcanon.com is
the first tenant on top of it. The pipeline must let a self-described zero-coder
operate it confidently for years, learning the model as they go rather than
memorizing commands.

### Non-goals (YAGNI)

- No neutral/normalized "universal" contract layer yet — the platform publishes
  **app-shaped** JSON (`albums/details/graph.json`). Revisit only when a second UI
  actually needs a different shape.
- No push-to-deploy CI/CD switch (runbook Appendix B). Stay on manual
  deploy-from-vps8. The design keeps that switch reversible.
- No new services/daemons. Cron/script-only, per platform health metrics.

---

## 2. Problem statement (why today is fragile)

| Concern | Today |
|---|---|
| Export data source | Reads `jazzcanon_fable`, a scratch DB that is a **frozen snapshot** of the real data — it stranded the 2026-07-03 Giant Steps fix (14 `performance_track` rows behind). |
| Refresh step | Getting the system of record into `jazzcanon_fable` (runbook Step B2) is **manual and unscripted**. |
| Two exporters | `jazz-canon/scripts/export.sh` (right output shape, wrong source) and `mccoy-tyner/scripts/export.py` (right source, **old** output shape: `album/{slug}.json`, `network.json`, `musicians.json`). Ambiguous which is real. |
| Count guard | `export.sh` hardcodes `100/567/666/670`; it must be hand-edited every time the canon grows — a foot-gun. |
| Ship | ~10 manual commands across two repos; `git push` does **not** deploy (Cloudflare via `wrangler`), a known surprise. |

---

## 3. Target architecture

```
  postgres._jazzcanon   (SYSTEM OF RECORD — the granite; unchanged)
        │  read-only role _jazzcanon_ro, directly, on vps8
        ▼
  publish  ──►  mccoy-tyner/exports/jazz-canon/{albums,details,graph}.json
        │            ▲ CANONICAL published contract, COMMITTED in the platform.
        │            │ Its git history is the record of "the canon grew."
        ├────────────┴───────────────┐
        ▼                            ▼
  copy → jazz-canon/app/public/data/ copy → mccoy-tyner/snapshots/canon-YYYY-MM-DD/
        │  (generated, GITIGNORED)         (+ MANIFEST: date + counts — eval bundle)
        ▼
  build → preview → deploy → https://jazzcanon.com
```

**One canonical contract, fanned out to N read-only consumers** (live site, eval
challengers, future UIs). The platform is agnostic to how many read it; none can
write back.

### Accepted decisions

- **(A) Contract home:** canonical copy committed in the **platform**
  (`mccoy-tyner/exports/jazz-canon/`). The **site's** `app/public/data/*.json`
  becomes a **generated, gitignored** build input, copied fresh by `ship`.
  - Consequence: a pure data change commits **only the platform repo** → honors
    the commit-scope rule (one repo per change). Deploy is a `wrangler` push, not
    a git act.
  - Reversibility: switching to Cloudflare push-to-deploy later would require the
    site to commit its JSON again (Cloudflare's cloud build can't reach vps8).
    Un-ignoring the site data dir is a one-line reversal when/if that day comes.
- **(B) Read privilege:** use **`_jazzcanon_ro`** (login role, NOT superuser),
  password sourced from the already-gitignored `.env.local` (`JAZZCANON_DB_URL`).
  Least privilege — the exporter physically cannot write to the system of record.

---

## 4. Components

### 4.1 The single exporter — `mccoy-tyner/scripts/export.sh`

- **Basis:** the proven SQL from the current `jazz-canon/scripts/export.sh`
  (produces the exact `albums.json` / `details.json` / `graph.json` shapes the app
  consumes today — including the Giant-Steps-correct `v_track_personnel` join).
- **Change 1 — source:** read `postgres._jazzcanon` directly via `_jazzcanon_ro`
  (from `.env.local`), not `jazzcanon_fable`.
- **Change 2 — guard:** replace the hardcoded count check with structural
  invariants (§4.2).
- **Output:** writes the three files into `mccoy-tyner/exports/jazz-canon/`
  (the canonical committed contract), then the copy step distributes them.
- **Retired:** `mccoy-tyner/scripts/export.py` (old shape) deleted;
  `jazz-canon/scripts/export.sh` removed (logic now lives in the platform).

### 4.2 Structural invariants (replace `100/567/666/670`)

Assertions that hold at **any** canon size and never need editing:

1. every album has ≥1 track, ≥1 performance, and a non-null primary art URL
2. every performance resolves to a real person **and** a real instrument (no orphan FKs)
3. `albums.json` length == number of keys in `details.json` == `SELECT count(*) FROM _jazzcanon.album`
4. required app fields non-null: album `title`, `artist_name`, `year`; person `canonical_name`
5. `graph.json` `people` and `edges` are non-empty and every edge's `person`/`album` id exists

Any failure aborts the export before writing anything the site would consume.
(These are stated as post-export JSON validations and/or pre-export SQL checks;
the plan will assign each to the cheaper side.)

### 4.3 Two entry points — `publish` and `ship`

Splitting the flow at the contract boundary gives one command for "produce data"
and one for "put it live," which cleanly serves both the site and the eval use case:

- **`publish`** (`mccoy-tyner/scripts/publish.sh`) — read system of record → run
  invariants → write the canonical contract (`exports/jazz-canon/`) → cut the dated
  eval snapshot → **stop.** Touches no site, deploys nothing. This is how you cut a
  fresh eval bundle for challenger models without disturbing the live site.
- **`ship`** (`mccoy-tyner/scripts/ship.sh`) — runs `publish`, then copies the
  contract into the site, builds, previews, deploys, verifies, and commits. This is
  the everyday "get my change live" command.

`ship` is one transparent, self-narrating flow. Default = safe + visible.

```
$ ship
✓ Read system of record directly    (N albums · N people · N track-links)
✓ Structural checks passed          (invariants §4.2)
✓ Published data contract           (exports/jazz-canon/{albums,details,graph}.json)
✓ Snapshot written                  (snapshots/canon-YYYY-MM-DD/)      [see 4.4]
✓ Copied contract into site         (jazz-canon/app/public/data/)
✓ Built site                        (app/dist/)
… Preview at http://vps8-core:4173  — look it over, then: [Enter] deploy · [q] abort
✓ Deployed to jazzcanon.com         (HTTP 200 verified)
✓ Committed the data change         (platform repo: exports/ + snapshots/)
```

- **Flags:**
  - default → preview pause before deploy
  - `--go` (a.k.a. `--no-preview`) → straight through to live, no pause
  - (the eval snapshot is cut by the `publish` stage on every run — no flag needed)
- **Failure behavior:** stop at the named stage with a plain-language message
  (e.g. `✗ Deploy: not authenticated — run: set -a; source .env; set +a`). No
  raw stack traces as the primary signal.
- **Repos touched:** reads/commits the **platform**; copies into + builds +
  deploys the **site**. For a pure data change, only the platform repo is
  committed.
- **Credentials:** DB password from `mccoy-tyner/.env.local`; Cloudflare token
  from `jazz-canon/.env`. Both already gitignored. Never printed, never committed.

### 4.4 Eval snapshot

The `publish` stage copies the just-published contract to
`mccoy-tyner/snapshots/canon-YYYY-MM-DD/` alongside a one-line `MANIFEST`
(date + the §4.2 counts). Purpose: hand every challenger model **byte-identical**
data with **zero credentials** — a fair, reproducible eval harness. Snapshots are
the fan-out's second consumer; they exercise the same "granite, many read-only
UIs" property the live site does.

Snapshots are **committed** in the platform repo (each is only a few hundred KB,
and committing them preserves provenance — exactly what data any given eval saw).
They accumulate deliberately as an audit trail; prune manually if ever needed.

---

## 5. Cleanup / migration (ordered; destructive steps gated)

1. Create `mccoy-tyner/scripts/export.sh` (relocated + repointed + invariants).
2. Create `mccoy-tyner/scripts/publish.sh` and `mccoy-tyner/scripts/ship.sh`
   (`ship` runs `publish`, then build/preview/deploy/commit).
3. Add `mccoy-tyner/exports/jazz-canon/` (committed) and `snapshots/` (committed,
   incl. MANIFEST).
4. Gitignore `jazz-canon/app/public/data/*.json`; keep the dir.
5. Delete `mccoy-tyner/scripts/export.py`; remove `jazz-canon/scripts/export.sh`.
6. **Prove the new pipeline end-to-end** (publish → build → preview → deploy),
   confirming the live site matches a direct-DB read — including the Giant Steps
   4-per-track fix finally going live.
7. **[Destructive / human-only]** Drop the `jazzcanon_fable` database — only after
   step 6 passes and only with explicit go-ahead; show it's unreferenced first.
8. Move `~/dev/active/jazz-canon-site` → `~/dev/paused/` (dead/superseded repo).

---

## 6. Success criteria

- A data change reaches jazzcanon.com via **one command**, with a preview pause by
  default and a `--go` fast path.
- The exporter reads the **system of record**; there is **no** scratch DB and **no**
  refresh step.
- Growing the canon requires **no** edit to any guard.
- Every stage narrates itself; failures name their stage in plain language.
- Handing identical data to an eval challenger is a **one-liner** (a dated snapshot).
- The operator can explain, from memory, how a fact travels DB → contract → live.

---

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Dropping `jazzcanon_fable` prematurely | Gated behind a proven end-to-end run (§5.6) + explicit approval; verify no script/role references it first. |
| `.env.local` / `.env` credential leak | Both already gitignored; `ship` never echoes secrets; DB access is least-privilege read-only. |
| Site needs committed JSON if CI/CD switch happens later | Documented as a one-line reversal (un-ignore site data dir). |
| Invariants too strict / too loose | Start from the app's real requirements (§4.2); tune during the §5.6 proving run. |
| Runbook drift | Scenario B rewrite is an explicit follow-up task once implementation lands. |

---

## 8. Follow-ups (out of scope for this spec, tracked)

- Rewrite `jazz-canon-cicd-runbook.md` **Scenario B** to match the new pipeline
  (requested; do after implementation).
- Optional future: neutral contract layer if/when a second UI needs a different
  shape.
- Optional future: evaluate Cloudflare push-to-deploy (Appendix B) once deploys
  feel routine.
