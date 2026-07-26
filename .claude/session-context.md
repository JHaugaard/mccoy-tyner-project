# Session Context

## Session Name
schema-update

## Current Focus
Execute `docs/handoffs/2026-07-26-ballot-fields-into-db.md` — promote council ballot
prose (`case_for`, `case_against`) from dossier JSON into `_jazzcanon.album`, backfill
the 21 ballot-bearing dossiers, patch the staging + embedding pipeline so future
candidates carry the fields, and keep the site export unchanged.

Indexed 2026-07-26, uuid `1cdf2f30-3aac-481a-a6bf-07c18eda970a`.

## Honcho Context
peer=john, reasoning_level=low. Confirms: `_jazzcanon` is the canonical schema and the
site is a read-only consumer of exported JSON; the council produces a ballot
(`tier`, `priority`, `case_for`, `case_against`) but include/reject stays John's;
v1 albums without ballots keep NULL ballot fields rather than retrofitted judgments;
schema changes go through real, reversible migrations that update the staging code in
the same change and are verified against exports/search before being called complete.

**Divergence noted:** Honcho recalls the documented semantic-search recommendation as
Option B (a separate council-search surface), with "A now, B later" as fallback. The
handoff's binding Answers section (John, 2026-07-26) directs Option A — append ballot
text inside `embed.py`. Newer instruction wins; recording that it departs from the
earlier written recommendation.

## Key Decisions
- Columns: `case_for`, `case_against` only. No `council_tier` (duplicates
  `album.canon_tier`), no new rationale column (`inclusion_rationale` already covers it).
- DDL runs as `sudo -u postgres` (album is owned by `_jazzcanon_role`); backfill runs
  as `_jazzcanon_app` with one `edit_log` row per album per field.
- `embed.py` gets `--only-ids` for targeted regeneration; no `--force`, no hand-nulling
  of `search_document`/`embedding`.
- `v_album_search_source` left alone; report as suspected dead/drifted.
- `v_album_detail` gets the two columns appended **after** `leader_name`.
- 21 ballot dossiers (19 archive + 2 inbox), not 19.

## Notes
- Session started: 2026-07-26

## Previous session (2026-07-15, `mccoy-build`) — carried-forward open items
- Deferred: per-line citation backfill; `_jazzcanon_ro` password rotation.
