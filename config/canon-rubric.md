---
# ── Hard gates — machine-read by canon-drip-precheck.py and canon-council.py.
# Edit these lines to steer McCoy; no code or schema change is ever needed.
year_min: 1940
year_max: 1979
excluded_styles: []     # opened 2026-07-28 — see "The opened genre gates" below
drip_size: 2            # candidates per nightly drip
backlog_cap: 10         # stop proposing when this many sit unreviewed
min_sources: 3          # target sources per candidate (1 acceptable if complete+reliable)
---

# The Canon Rubric

This file is the Canon Builder's working brief. McCoy loads it on every
mission and every nightly drip; the canon-council reads it before judging
any candidate. John edits it freely — the frontmatter numbers are hard
gates the machinery enforces, the prose below is the judgment it applies.

## What "canonical" means here

This is a **personal discovery canon**, not an academic one. An album
belongs when it is a load-bearing record of the post-bebop tradition —
the album you would hand someone to explain what this music is. Signals,
strongest first:

1. **Consensus** — it keeps appearing: Penguin Guide core collection,
   NPR/JazzTimes/DownBeat canon lists, label-anthology status, the
   records musicians themselves cite. Consensus across *independent*
   traditions of listing is the strongest single signal.
2. **A defining statement** — the artist's (or a scene's) definitive
   record, the one that fixed a sound: *Saxophone Colossus*, *Moanin'*,
   *The Sidewinder*. One artist may have several; most have one or none.
3. **Lineage** — records that changed what came after: who studied it,
   what it made possible. Influence audible in other albums already in
   the canon counts double.
4. **Session gravity** — the personnel network. A date that pulled
   together players who define the era is evidence even when the album
   title is less famous; this canon is *about* the musicians.
5. **It still plays** — the discovery test. Would a curious listener,
   sent to this album cold, understand why jazz matters? Historical
   importance alone, with no living pleasure in it, is a weak case.

## Scope discipline

- The window is **year_min–year_max** (frontmatter, currently 1940–1979),
  by original recording/release year. Outside the window: refuse, no
  exceptions in conversation — the window moves only by editing this file.
- **The 1940–1948 band (added 2026-07-26, window lowered from 1949):**
  the early window exists to catch the **bebop-to-post-bebop transition** —
  the records where the post-bebop language is audible forming (Monk,
  the young Miles and the Birth of the Cool adjacency, Hawkins' forward
  edges, the pianists bridging Powell to the 1950s). **Pure bebop is not
  yet in scope:** dates whose organizing idiom is bebop itself (early
  Parker, Gillespie small groups) are out even inside the window, pending
  a future rubric revision — one line here when John decides the day has
  come. Transition vs. pure-bebop borderline records are **scope_call**,
  argued in the ballot; John rules.
- **The 1973–1979 band (added 2026-07-25):** the window was raised from
  1972 to admit the ECM first decade and its kin. Albums recorded 1973+
  are judged on **continuity**: does the record extend the post-bebop /
  modal / post-bop tradition the canon is built on (the 1960s lineage
  reaching forward), rather than found something new? The canonical
  example is Keith Jarrett's *The Köln Concert* (1975) — late modal,
  continuous. Early Pat Metheny Group (*American Garage*, 1979) is the
  border case: acoustic, swinging, song-form = arguable; electric-rock
  vocabulary = the fusion exclusion bites. 1973+ arrivals should lean
  **scope_call** or **contested** by default and name the boundary in
  the ballot; John rules.
- **The opened genre gates (2026-07-28).** `excluded_styles` is now empty:
  free jazz, fusion, and the ECM catalogue are **admissible**, and each has
  a dedicated specialist agent (`jazz-fusion-researcher`,
  `jazz-free-jazz-researcher`, `jazz-ecm-researcher`). This is a *permeable
  boundary*, not an annexation. The canon's center of gravity stays in the
  post-bebop / hard-bop / modal tradition; these three gates exist to test
  continuities the old blanket exclusions hid. Three standing rules:
    1. **Arrivals from these three gates lean `scope_call` or `contested`
       by default.** `consensus_core` from a newly opened gate needs an
       exceptional for-case. Name the boundary in the ballot; John rules.
    2. **The bridge test outranks the genre label.** Ask what a record
       connects to — not what bin a source files it in. A fusion album
       earns its place by being a load-bearing link in the lineage
       (Miles' sidemen dispersing; the road toward Charles Lloyd and
       Kamasi Washington), not by being good fusion.
    3. **Incremental, not floodgate.** These gates open a few records at a
       time. Do not propose a burst to "cover" a newly opened genre; the
       drip pace in this file governs all three (see *The drip's pace*).
  Borderline modal / avant records (*Out to Lunch!*, *The Shape of Jazz to
  Come*) remain **scope_call**: argue them, tier them, let John rule.
- **Free jazz — the standing taste note.** John has said plainly that free
  jazz does not currently resonate with him, and that he is studying it
  rather than dismissing it. Treat that as calibration, not as a veto:
  propose the records that *teach* the idiom and connect to what is
  already in the canon, argue them honestly, and expect a high cull rate.
  Energy-music maximalism (*Machine Gun*, late Ayler) is admissible but
  is the hardest case in the project — make the argument or don't propose it.
- **Fusion — the anti-drift note.** This is not becoming a fusion canon.
  Electric-rock instrumentation and backbeat as the organizing idea is
  still a case-*against*, no longer an auto-exclusion. *Bitches Brew* (1970)
  is now a candidate, argued, not a wall.
- **ECM — window-bound for now.** The ECM gate runs **1969–1979 only**;
  `year_max` stays at 1979 (John, 2026-07-28, deliberately a small step —
  he expects to push the end date out later). ECM albums are judged on
  continuity with the 1960s modal tradition, never accepted or rejected by
  label or decade alone. *The Köln Concert* (1975) is the anchor.
- **`excluded_styles` is prose-enforced.** `check-candidate.py` and
  `stage-candidate.py` read `year_min`/`year_max` from this frontmatter and
  nothing else. Style scope lives in agent and council judgment — this
  section *is* the enforcement.
- **No style quotas.** Sixty modal albums is fine if each earns its place.
  Never propose a weaker album to balance a genre.
- **The drip's pace is deliberate (affirmed 2026-07-26).** The widened
  window (1940–1979) makes a fast build to 1,000+ albums technically
  easy — and John has explicitly declined it. drip_size stays 2: each
  morning's two candidates get read, listened to, and thought about.
  Reaching 200 in a year or more is the intended tempo, not a backlog
  failure. Do not propose raising drip_size for throughput reasons;
  mastery of the collection outranks growth of it.
- **No artist-concentration penalty.** The first-100 phase guarded against
  a canon one-third Davis and Coltrane; the canon is now open-ended and
  John has directed the dial turned down (2026-07-20). Repeat appearances
  by an already-included artist are not a case-against argument — an
  album earns its place on its own merits.

## Priority (how urgent for THIS canon)

- **must_have** — the canon is visibly incomplete without it; a jazz
  person browsing the site would notice the hole.
- **strong** — clearly canon-worthy; strengthens an era or a musician's
  arc already present.
- **consider** — legitimate case, real trade-offs; include if the mood
  of the collection wants it.

## Tier (how the council reads the evidence)

- **consensus_core** — for-case overwhelming, against-case thin.
- **contested** — real cases both ways; preserve the disagreement in
  the ballot rather than flattening it.
- **scope_call** — the argument is about the window/style boundary, not
  quality. Flag exactly which boundary.
- **exclude_suggested** — the against-case wins; recorded so it isn't
  re-proposed (see cull-notes loop).

## Candidate hygiene (non-negotiable, enforced by machinery)

- Dedup against every `album` row (any canon_status) AND the known
  next-batch list before surfacing.
- Full personnel_record per docs/personnel-contract.md, gathered by tool
  work with sources — never from model memory.
- Every claim labeled obs/inf/unk with a source token. When sources
  conflict, both are recorded; the conflict is content, not noise.
- Backlog cap (frontmatter): when ≥ backlog_cap candidates sit
  unreviewed (`canon_status='candidate' AND site_status='found'`),
  the drip stays silent.

## Learning loop

When John rejects a candidate, the reason goes to
`research/cull-notes.md`. Read it before every mission: a pattern in the
culls (too bebop, too obscure, wrong kind of famous) is a standing
instruction until this rubric absorbs it in prose.
