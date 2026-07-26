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
