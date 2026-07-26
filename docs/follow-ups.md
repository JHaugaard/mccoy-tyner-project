# Open Follow-ups — surfaced 2026-07-25 (post first ship of 19)

Captured after the first post-launch batch ship (100 → 119 albums). None
blocking. John asked these be re-surfaced when canon ops resume.

## 1. Embeddings backfill for the 19 shipped albums
The 19 albums shipped 2026-07-25 have `embedding`/`search_document` NULL.
`scripts/embed.py` must run as the postgres OS user
(`sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/embed.py`) and calls Ollama
on vps4 — the sudo-postgres execution path was declined in-session and John
deferred it. Until done, canon-search (platform semantic search) will not
see these albums. Site is unaffected.
Also note: `scripts/cover-art-fetch.py` has the same sudo-postgres pattern,
so the same path question applies next time it's needed.

## 2. Apple preview backfill (3 albums)
No `apple_album_id` on: `thelonious-monk-brilliant-corners-1956`,
`kenny-dorham-whistle-stop-1961`, `mccoy-tyner-inception-1962` (plus two
pre-launch albums: `lee-konitz-subconscious-lee-1950`,
`modern-jazz-quartet-django-1955`). These ship without preview buttons.
Fix: iTunes lookup → update `apple_album_id` via edit contract → re-run
`enrich-previews.mjs` on next ship.

## 3. Drip staging: source_map/sources key mismatch
`stage-candidate.py` expects `source_map`; drip dossiers carry token-keyed
`sources`, so citation rows are skipped at staging (benign warning, nothing
fabricated). Decide: patch the script to read `sources`, or patch the drip
prompt to emit `source_map`. Also: the drip prompt still cites
`~/.hermes/scripts/canon-council.py` — real path is
`/home/john/.hermes/profiles/mccoy/scripts/canon-council.py`.

## 4. Review-process rethink (John's item)
The 2026-07-25 ship executed a 19-album blanket verdict ("I accept all 19"),
which the edit contract's "one album per instruction, no bulk flips" rule
was stretched to cover (each album got its own edit_log row with John's
words). John wants to redesign the review/acceptance process — how verdicts
are given, batched, and recorded. Revisit edit-contract.md status-transition
section when he does.

---
Logged by mccoy, 2026-07-25.
