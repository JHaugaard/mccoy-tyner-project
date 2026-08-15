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

## 2. Apple preview backfill — 3 of 5 done, 2 need a hand search
**Partly resolved 2026-07-26 (Claude Code).** Was 5 albums with no
`apple_album_id`; now 2. Written via the edit contract as `_jazzcanon_app`,
one `edit_log` row each, `epistemic` untouched (a catalog pointer is not a
claim about the music — matches what `mbid-apple-lookup.py` does):

| Album | Apple ID | Verified as |
|---|---|---|
| `kenny-dorham-whistle-stop-1961` | 1443927557 | 7 tracks, Remastered 2014 |
| `mccoy-tyner-inception-1962` | 1890340978 | McCoy Tyner Trio, rel. 1962-03-20, 6 tracks |
| `thelonious-monk-brilliant-corners-1956` | 1440942347 | rel. 1957, 6 tracks (LP is 5 + alt take) |

Live-album coverage is now 116/119. Previews do not appear on the site until
an export + `apple_previews.py` + a ship; `exports/` is stale against the DB
until then, which is the normal between-ships state.

**Still open, and neither is a script's job:**

- `modern-jazz-quartet-django-1955` — **`mbid-apple-lookup.py` proposes
  1191353582, which is WRONG.** That ID is *"Django - Single"*: one track,
  $0.99, released 2016 — not the 1955 Prestige LP. The script takes the top
  iTunes search hit and there is no album-vs-single guard, so an unattended
  re-run will write this bad ID again. Needs a hand search for a legitimate
  album or reissue, or leave NULL.
- `lee-konitz-subconscious-lee-1950` — no iTunes match at all. Plausible for
  a 1950 Prestige date; may genuinely not exist on Apple Music as an album.

**General caution on `mbid-apple-lookup.py`:** its matches are top-search-hit
guesses and need eyes before they land. Verify a proposed ID with
`https://itunes.apple.com/lookup?id=<id>&entity=song` and check artist,
title, release date and track count against the album before writing.

## 2b. Shorty Rogers has no MusicBrainz MBID

`shorty-rogers-and-his-giants-1953` — `musicbrainz_release_group_mbid` is
NULL and MusicBrainz returns no match for it. Surfaced 2026-07-26 by a dry
run of `mbid-apple-lookup.py`; it is the only album in the DB missing an
MBID. This is the first real drip-staged candidate, so it may simply be a
harder release to match than the original bulk-ingested 100. Not blocking
anything — MBID feeds enrichment, not the site.

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

## 5. `v_album_search_source` is dead or drifted — RESOLVED: dropped
**RESOLVED 2026-07-26** — John's call: dead, so drop. `migrate-4b` dropped
BOTH `v_album_search_source` and `v_person_search_source` (the person view had
the identical problem). `_jazzcanon` is down to 11 views. Verified after the
drop: export byte-stable, `canon-search.py` works on both albums and people,
`stage-candidate.py` dry-run clean, all 121 album + 629 person
`search_document` values intact. Rollback exists but recreates the *drifted*
definitions — if a view should ever become the real source, write a new one
that matches `embed.py` and change `embed.py` to read it.

**One loose end outside this repo:** McCoy's Hermes config
(`~/.hermes/profiles/mccoy/config.yaml`, line 10-13) still tells him the DB has
"the 13 v_* views" and lists both dropped names. Harmless — he'd get a
relation-does-not-exist if he tried — but his orientation text is now wrong.
Fix when McCoy's config is next touched: change "13" to "11" and delete the two
names.

Original entry follows.
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

---

# Added 2026-08-14 (Claude Code, studios-map session)

Context: the studios cleanup + geocoding + `places.json` export (worksheet at
`research/studios-cleanup-worksheet.md`, ratified in full; commits 54e1865 →
e4dde39). None blocking; the site's Studios build is live against the export.

## 7. Ingest does NOT capture place data — the pipeline needs teaching
**The big one.** Everything the studios session accomplished was retroactive
cleanup. The drip/staging path (`gather-mission.md` → dossier →
`stage-candidate.py`) still writes raw studio strings exactly as researchers
emit them: compound strings, bare cities, name variants, no `kind`, no
`address`, no `location_epistemic`, no `location_source`, no coordinates.
*Seven Steps to Heaven* proved it mid-session — it arrived 2026-08-13 with a
compound row and needed its own mini-ruling. Until the pipeline is taught:
**every drip arrival with a new place needs a mini-worksheet pass** (match
against existing canonical places first; new places need kind + address
research + geocode per the ratified method in the worksheet header and
`scripts/studio-geocode-2026-08-14.sql`). The real fix is upstream: extend
the gather mission / personnel contract so researchers emit a canonical-place
match (or a flagged new-place record with address + source) at ingest time,
and extend `stage-candidate.py` to resolve against `studio.name_slug` instead
of blind-inserting name/city strings. That is a spec change → John's approval.

## 8. Per-place editorial note field (site's optional 4th ask) — deferred
The site has a venue-card slot for a one-line editorial note (e.g. "Rudy Van
Gelder's parents' living room"). `studio.notes` now holds good material but
mixed with internal caveats (merge markers, worksheet refs, source-conflict
notes). Shipping it raw would leak plumbing. Needs: a John-reviewed curation
pass over 47 places (many notes are already display-grade), then a purely
additive `note` field in the `places.json` exporter block. Site confirmed
non-blocking; no shape change when it lands.

## 9. Tristano coordinate override — John's option, open
`lennie-tristanos-home-studio`: address (317 E 32nd St) is documented — the
track names it — but the 300-block was swallowed by the Kips Bay Towers
superblock and the address is extinct in OSM, Census, and NYC GeoSearch.
Coordinate is block-approximate (3 decimals, anchored to 252 E 32nd) and
`location_epistemic` was degraded obs→inf so the map never implies a
street-grade pin. John may override back to obs (one UPDATE + edit_log);
flagged at execution, not yet ruled either way.

## 10. Bauer merge is a medium-confidence inference
`studio-bauer-ludwigsburg` merged "Musikstudio Bauer" (1969, engineer Kurt
Rapp) and "Tonstudio Bauer" (1975, engineer Martin Wieland) on same-city/
same-surname/same-producer inference — no source confirms one physical room
vs. a family business with two facilities. Noted on the row. If an ECM
history source ever settles it and the answer is "two rooms," the split is:
new row, reassign one session, both stay city-precision (no address known
for either).

## 11. Out of the Cool full session normalization — optional
Option 1 (year-prefix on the two date strings) executed 2026-08-14. The
proper fix remains available: four dated session rows (1960-11-18, -11-30,
-12-10, -12-15) with the album's 5 tracks researched onto their actual days
and FKs reassigned. Cosmetic for the map (year-grade is all the scrubber
uses); worth doing only if track-level session data matters elsewhere.

## 12. Small data checks surfaced by the worksheet, unruled
- Pershing (`At the Pershing`): sources say Jan 16–17 1958; DB holds only
  Jan 16. Adding a session row is new data → needs a source + John's nod.
- Atlantic Feb-1959 session (*Blues & Roots* bundle): place identity solid,
  but the address is ambiguous between 157 W 57th and 1841 Broadway (move
  month undocumented). Noted on the studio row; affects nothing unless
  per-session address precision ever matters.
- Two Van Gelder sessions carry dates matching no documented session
  (1954-01-06 Brookmeyer, 1956-01-22 Fontessa — nearest documented dates are
  days off). Epistemic degraded to inf; a discography deep-dive could fix
  the dates properly.
- RLA Studios (`rla-studios`) is fully researched + geocoded but absent from
  `places.json` until its only album (*Heliocentric Worlds Vol. 1*,
  candidate/found) passes John's include gate. Nothing to do — it appears
  automatically with a stable id.

Logged by Claude Code, 2026-08-14.
