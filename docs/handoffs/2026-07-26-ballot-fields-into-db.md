# Handoff to Claude Code — Promote council ballots into the database

Date: 2026-07-26 (EDT)
From: McCoy (Hermes, mccoy profile), at John's direction
Repo to work in: **mccoy-tyner** (`/home/john/dev/active/mccoy-tyner`)

## How John runs this

1. `cd /home/john/dev/active/mccoy-tyner`
2. Launch Claude Code in that directory.
3. Point it at this file: "Read docs/handoffs/2026-07-26-ballot-fields-into-db.md and execute it."

The database is Postgres on vps8, port 5433, schema `_jazzcanon`.
Read credentials come from `.env.local` in the repo root
(`JAZZCANON_DB_URL`, `JAZZCANON_APP_DB_URL` — parse with Python, not
shell grep; passwords may contain `#`).

## Goal

John enjoys reading the council's `case_for` / `case_against` on each
drip album and wants that deliberation **deeply searchable** — ordinary
SQL today, semantic search as part of the same job. Today those fields
exist only inside ballot blocks of dossier JSON files in
`research/candidates-archive/` and `research/candidates-inbox/`. The
`album` table carries `inclusion_rationale` (populated on all 121 rows)
but has no case_for/case_against columns.

This completes the deferred half of the 2026-07-21 schema discussion.

## Done when

1. `album` carries new nullable text columns: `case_for`, `case_against`
   (and, if trivially cheap, `council_tier`, `council_recommendation`,
   `council_confidence` — McCoy's recommendation, John's call if Claude
   Code sees a reason to trim).
2. A migration script (numbered like the existing `migrate-3b-*.sql`
   pattern) applies the change, with a matching rollback.
3. **Backfill:** every dossier in `research/candidates-archive/` and
   `research/candidates-inbox/` that has a `ballot` block has its
   case_for/case_against (+ council fields) written to the matching
   `album` row (match on `album.id`, which equals the dossier `id`).
   Backfill writes go through the app role with one `edit_log` row per
   album per field, reason: `'ballot backfill 2026-07-26 (Claude Code
   handoff)'`.
4. `scripts/stage-candidate.py` is patched so future staged candidates
   write the ballot fields at staging time — no future backfills needed.
5. **Semantic search:** ballot text is included in the embedding input.
   Per the open 2026-07-21 question, implement option (a): extend
   `search_document` to append `case_for` + `case_against` text, and
   regenerate embeddings for affected rows via `scripts/embed.py`
   (runs as the postgres OS user — see the invocation pattern in the
   canon-drip-operations skill; it is idempotent and skips non-null,
   so the script must null/regenerate the changed rows).
6. `v_album_detail` (and any other view that should expose the fields)
   is updated; `scripts/export.sh` is checked — the site export must NOT
   start emitting case text (deliberation is workshop material, not
   gallery material) unless John later asks. Confirm the export is
   unchanged in output shape.
7. Verification: `SELECT id, left(case_for,60) FROM _jazzcanon.album
   WHERE case_for IS NOT NULL` returns the backfilled set (19 archive
   dossiers as of this writing); a semantic-search smoke test
   (`scripts/canon-search.py`) surfaces a ballot phrase.

## Don't

- Don't delete or rewrite the dossier JSON files — they remain the
  archival source; the DB columns are a projection.
- Don't touch `canon_status` or `site_status` of any row.
- Don't change export.sh's album selection or add ballot fields to the
  site payload.
- Don't hand-edit `embedding`/`search_document` columns outside
  embed.py — derived fields are pipeline-owned.
- Don't advance anything to the website; this is workshop-only work.

## Context Claude Code will want

- Ballot JSON shape (top-level `ballot` key in each dossier):
  `case_for`, `case_against`, `disagreement`, `scope_check`, `tier`,
  `recommendation`, `confidence`, `priority`, `_council`.
- Example dossier:
  `research/candidates-archive/art-blakey-the-jazz-messengers-free-for-all-1964.json`
- Staging script: `scripts/stage-candidate.py` (uses
  `scripts/.venv/bin/python3`; DB URL from `.env.local`).
- Embedding script: `scripts/embed.py`; search: `scripts/canon-search.py`.
- Edit contract: `config/edit-contract.md` governs all writes.
- House rules: never DELETE rows; one edit_log row per change; epistemic
  pairing on fact edits (n/a here — these are prose projections, but the
  edit_log discipline still applies).
- Git ritual: rubric/config edits get their own commit; commit the
  migration, the stage-candidate patch, and the backfill separately;
  push to origin when done.

## Open question for John at review time

Whether `disagreement` and `scope_check` should also be columns (they
are part of the ballot prose John reads). McCoy's take: yes eventually,
but case_for/case_against is the 80% win; keep the migration small.

---

# Answers — John, 2026-07-26 (recorded by Claude Code before dispatch)

Four points were unresolved or would have blocked an unattended run.
John's decisions, plus recon findings. **Read this section as binding;
it overrides the body above where they conflict.**

## A. Columns: `case_for` and `case_against` only

Both nullable text. **No `council_tier`** — `album.canon_tier` already
holds the ballot's `tier`, written by `stage-candidate.py`; a second
column would store it twice. **No `rationale` column** — John asked for
one, but `album.inclusion_rationale` already exists and is populated on
all 121 rows from each dossier's top-level `rationale` field. The ask is
already satisfied; don't add a duplicate. `recommendation`,
`confidence`, `disagreement`, and `scope_check` stay in the dossier JSON
for now — the open question above is answered "not yet."

## B. Re-embedding: patch `embed.py` with `--only-ids`

Add targeted regeneration (accept a list of album ids; regenerate those
rows regardless of null-ness). Do **not** null `search_document` /
`embedding` by hand — the body's "Don't" list is correct and the
`--only-ids` patch is how to honor it. Do **not** use `--force`: it
re-embeds all 121 albums *and* 629 persons through Ollama on vps4 for a
21-row change.

## C. Search document: patch `embed.py`, flag the view

**Recon finding — the body's item 5 has no single target.** There are
two divergent search-document definitions:

- `scripts/embed.py` builds its doc string in Python: title/artist/year,
  style, performers, `description`
- the view `_jazzcanon.v_album_search_source` builds a *different* one:
  adds `label` and `notes`, omits `description`

**`embed.py` does not read that view.** Append `case_for` +
`case_against` in `embed.py`, where embeddings are actually built. Leave
the view alone and report it as suspected-dead-or-drifted for John to
decide separately — do not reconcile the two mid-migration.

## D. `v_album_detail`: append the new columns last

The view **enumerates columns explicitly** (not `SELECT a.*`), so new
`album` columns do not propagate automatically. Its column list ends
`label_name, style_primary_name, leader_name` — inserting `case_for`
before those changes column order and `CREATE OR REPLACE VIEW` will fail
with "cannot change name of view column". Append the two new columns
**after** `leader_name`. No `DROP`, no cascade risk. Column order is
cosmetically odd; that's accepted.

## Recon notes that change the body

- **21 dossiers carry a `ballot` block, not 19**: 19 in
  `research/candidates-archive/` + **2 in `research/candidates-inbox/`**.
  The body's verification step (item 7) says 19 — expect 21.
- **Ballot keys confirmed**: `album, scope_check, tier, priority,
  case_for, case_against, disagreement, recommendation, confidence,
  _council`.
- **Item 6's export risk is already structurally closed.**
  `scripts/export.sh` builds explicit `json_build_object` payloads — no
  `SELECT *`, no reference to `v_album_detail`. Ballot text cannot leak
  into the site payload by accident. Still confirm output shape is
  unchanged, but no defensive work is needed.
- **Access is complete; nothing here needs John at the keyboard.**
  Verified 2026-07-26: `sudo` is passwordless on vps8, so the two
  `sudo -u postgres` steps (the migration, per `scripts/run-migrate-3b.sh`,
  and `embed.py`) run unattended. `_jazzcanon_app` connects and holds
  `INSERT, SELECT, UPDATE` on `album` and `INSERT, SELECT` on `edit_log` —
  exactly what the backfill needs. `/tmp/pg-venv/bin/python3` exists and
  Ollama on vps4 answers.
- **The migration cannot run as `_jazzcanon_app`.** `album` is owned by
  `_jazzcanon_role`; grants are not ownership, so `ALTER TABLE` fails as
  the app role regardless of how permissive its grants look. Use
  `sudo -u postgres` for the DDL — the app role is for the backfill only.
- **`edit_log` has no UPDATE grant**, by design. The backfill only
  inserts, which is fine. A later correction must be a new row, never an
  amendment.
- **`/tmp/pg-venv` will not survive a reboot.** If it's gone, rebuild it
  rather than treating it as a blocker.
- **DB `collection.name` stays `'The Jazz Canon'`.** The product was
  renamed to *A Jazz Canon* on 2026-07-26, docs-only, by John's explicit
  decision. Don't "fix" the collection row, and don't change
  `scripts/ingest.py`'s seed text.
