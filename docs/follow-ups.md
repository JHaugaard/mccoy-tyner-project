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

**RESOLVED 2026-07-26 (Claude Code, schema-update session).** All 121 albums
and all 629 persons now carry `embedding` + `search_document`; zero NULLs in
either table. The 94 missing persons were the people added by the 21 staged
candidates, filled by a no-flag `embed.py` run at John's instruction.
Verified: `canon-search.py --people` surfaces the newly-embedded (Booker
Little, from the staged *We Insist!*).

The sudo-postgres execution path that was declined in-session on 2026-07-25
ran clean:
`sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/embed.py` — `sudo` is
passwordless on vps8 and Ollama on vps4 answered. One gotcha: **`/tmp/pg-venv`
does not survive a reboot intact.** It was found with the directory present
but `psycopg2` gutted, which fails at import rather than at connect. Rebuild
rather than debug:
`sudo rm -rf /tmp/pg-venv && sudo -u postgres python3 -m venv /tmp/pg-venv &&
sudo -u postgres /tmp/pg-venv/bin/pip install psycopg2-binary`

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

---

# Added 2026-07-26 (Claude Code, ballot-fields migration)

## 5. `v_album_search_source` is dead or drifted — decide which
There are two divergent definitions of an album's "search document" and they
do not agree:

- `scripts/embed.py` builds its doc in Python — title/artist/year, style,
  performers, `description`, and (since migrate-4a) `case_for` /
  `case_against`. **This is the one that actually produces embeddings.**
- the view `_jazzcanon.v_album_search_source` builds a different one — it
  adds `label` and `notes`, omits `description`, and knows nothing about the
  ballot columns.

`embed.py` has never read the view. So the view is either dead code left from
an earlier design, or an intended definition that embed.py silently diverged
from. Deliberately left untouched by migrate-4a — reconciling them is a
design decision, not migration work. Options: drop the view; or make
`embed.py` read it and delete the Python doc-building. Whichever John picks,
the two should not both exist.

## 6. `inclusion_rationale` on the 21 ballot rows was repointed
Before migrate-4a, `stage-candidate.py` wrote the ballot's `case_for` into
`inclusion_rationale`, so that column meant "what the council argued" on
ballot-staged rows and "what the album is" on the original 100. The backfill
repointed all 21 to the dossier's top-level `rationale`, and the staging
script now does the same on both paths. The displaced values are in
`edit_log.old_value` (reason `ballot backfill 2026-07-26 (Claude Code
handoff)`) — recoverable, not lost. No action needed; recorded so the
`edit_log` churn on 2026-07-26 has an explanation attached.

Logged by Claude Code, 2026-07-26.
