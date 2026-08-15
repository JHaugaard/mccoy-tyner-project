# Session Context

## Current Focus
Studios map — platform-side data work (handoff from jazz-canon `studios` branch).
Make `_jazzcanon` able to answer "where was every session recorded, at what
coordinates, with what confidence," then export it as `places.json` for the
site's new D3 time-scrubber Studios view. Full handoff brief was pasted at
session start (7 decisions for John, one at a time; site repo stays read-only
consumer).

## Honcho Context
Honcho (peer=john) already holds the design-session record and it matches the
handoff: self-drawn D3 map, all recording places (studios + live venues,
visually distinguished), time scrubber; ~42 raw studio strings mentioned in
design (verify against live DB); cleanup via per-item worksheet (raw → canonical
→ merge/split/exclude → evidence), item-by-item first, bulk-accept only after
John sees the pattern; location labels `obs` (documented address) vs `inf`
(city centroid), never invent precision; proposed `kind` column and epistemic
storage location are OPEN, need John's explicit schema approval; Van Gelder
Hackensack-vs-Englewood-Cliffs is the one-place-or-two test case; export
principle "loose on membership, never loose on facts" — albums without places
still ship. No prior curation of studios work in the honcho-memory log (this is
its first platform-side session).

## Key Decisions
- Cross-session messaging channel established with the site session
  (`jazz-canon-07`, John's first use of the feature). Ground rule ratified on
  both sides: factual coordination direct, decisions through John.
- Site-side contract requirements received in full (they had NOT arrived via
  John — assumed-pasted gap caught and closed):
  R1 single unambiguous precision field per place (address|city semantics,
  no cross-entity joins to recover it); R2 one coordinate per exported place
  (moved venues = distinct exported places; renderer constraint, informs but
  does not decide the Van Gelder ruling); R3 deterministic slug ids
  export-to-export, merge survivor keeps one id. Optional non-contractual
  4th: one-line editorial note per place from studio.notes.
- Site falls back to album canon year when session dates are NULL — no
  platform requirement.

## Survey (live DB, 2026-08-12, read-only)
- 46 studio rows, all lat/lon NULL. 263 sessions; 14 unlinked to a studio;
  7 undated. Exactly 5 canon albums have no studio-linked session:
  Subconscious-Lee 1950, Something Cool 1955, What Is There to Say? 1959,
  Sahara 1972, Let My Children Hear Music 1972 — ship placeless.
- Van Gelder row (id 137, "Englewood Cliffs") holds 100 sessions / 73 albums
  and certainly includes pre-1959 Hackensack sessions → a split ruling means
  date-based session reassignment, not just a new row. Row 128 is a compound
  string already holding Hackensack dates.
- Schema notes: session.epistemic exists (default obs) — it labels the
  session claim, not location; studio has UNIQUE(name,city) and
  UNIQUE(name_slug) — merges must respect both; studio has no kind or
  location-epistemic column (decisions 2/3).

## Status: DONE (2026-08-14)
All seven handoff decisions ratified and executed. 47 canonical places
(migration 5a; worksheet ratified in full; Seven Steps follow-up split),
all geocoded with citations (34 obs / 13 inf), places.json contract
confirmed with site session and landed in app/public/data (46 places —
RLA awaits its album's include gate). Commits 54e1865, 37ae9e7, e4dde39.
Open flags recorded in memory/studios-map-complete.md (note-field curation,
Tristano obs override, Bauer merge caveat, drip adds messy studio rows).

## Notes
- Session started: 2026-08-12
- Done means: studio table cleaned + geocoded, kind + location-epistemic
  ratified somewhere, exporter emits places.json, fresh export in site's
  app/public/data/. jazz-canon `studios` branch parked until then.
- Decisions queue (ask one at a time): 1 canonical place set, 2 venue kind
  storage, 3 location epistemic storage, 4 bare-city entries, 5 moved venues,
  6 export contract shape, 7 geocoding method.
- Constraint reminders: schema changes propose-first; `_jazzcanon_app` has no
  DELETE grant; every coordinate/merge needs evidence.
