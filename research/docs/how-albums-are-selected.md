# How Albums Are Selected for A Jazz Canon

A methodological description of the selection process behind jazzcanon.com.

Prepared 2026-10-18 by McCoy (the project's curator-assistant agent),
at the request of the curator. All figures were verified against the
live database on the date of writing. The document is intended as a
standing reference: the curator draws short public descriptions from
it, and it records the reasoning and safeguards that the short
versions omit.

---

## 1. What the canon is

A Jazz Canon is a personal discovery canon of jazz albums recorded
between 1945 and 1985 — bebop through the first ECM decade and its
kin. It is not an academic canon and not a comprehensive catalog.
Its test, stated in the project's standing rubric, is whether an
album is a *load-bearing record of the tradition*: the record you
would hand someone to explain what this music is.

The website is a static public export of a private PostgreSQL
database in which every album, track, performance, session, and
recording site is stored with its sources. The public site is a
gallery; the database is the system of record, and this document
describes how records enter it.

As of 2026-10-18 the canon holds **292 published albums**, drawn
from a database of 1,317 persons, 2,013 tracks, 2,175 performance
records, 522 recording sessions, and 79 recording sites, supported
by 1,133 distinct source records and 1,356 individual citations.

## 2. The scale of the selection problem

A reasonable estimate of the original jazz LPs (10" and 12")
issued worldwide between 1945 and 1985 is **on the order of
25,000–40,000** — roughly 30,000 as a working figure.

This is an inference, not a count, and it is presented here with
its reasoning, in keeping with the project's evidence standards:

- *Anchor (observed):* Tom Lord's Jazz Discography, the standard
  session-level authority, indexes approximately 456,000 jazz
  record releases across all eras (1896–present) and formats,
  including reissues, international pressings, and compilations.
- *Anchor (observed):* Discogs, which attempts to catalog every
  physical release ever made, holds over 19 million releases
  across all genres, of which jazz is roughly 5–8%.
- *Reduction (inferred):* The 1945–1985 window contains the LP
  era essentially whole and the peak decades of jazz recording
  activity. Applying an estimated releases-to-original-albums
  ratio of 3–4 (each original album generates several cataloged
  releases over its lifetime) and excluding singles, EPs, and
  compilations of older material yields the 25,000–40,000 band.
- *Cross-check (inferred):* Label arithmetic — the major US jazz
  labels of the period (Blue Note, Prestige, Riverside, Columbia,
  Impulse!, Atlantic, Verve, EmArcy, Contemporary, Pacific Jazz,
  Savoy, Fantasy, CTI, Milestone) account for roughly 8,000–12,000
  original jazz LPs in the window; doubling for European, Japanese,
  and independent labels lands in the same range.

The exact figure is unknown; nobody has counted precisely this
set. What is solid is the order of magnitude: tens of thousands,
not thousands and not hundreds of thousands.

Against that pool, 292 albums represent a selection of roughly
one record in a hundred. The methodology below exists to make
that hundredth defensible.

## 3. The division of labor

The process has three participants with strictly separated powers:

1. **The curator (John).** The only decision-maker. He listens to
   every candidate and rules: include, exclude, or defer. No
   album enters the canon by any other path.
2. **The builder agent (McCoy) and its nightly pipeline.**
   Proposes candidates, researches them, and stages them for
   review. It cannot advance any album past "candidate."
3. **The canon council.** A panel of independent AI judges that
   evaluates each candidate dossier against the written rubric
   and issues a ballot: a tier, a priority, a case for, a case
   against, and any disagreement among the judges. The council
   only proposes; it has never admitted an album.

The design principle: machines do the librarian's work — finding,
fetching, cross-checking, formatting — and the human does the
critic's work — listening and deciding.

## 4. The nightly pipeline (the "drip")

A scheduled job runs every morning at 06:00 (US Eastern). Its
budget is exactly **two candidates per night**, a fixed rule
chosen so the canon grows at the pace of listening rather than
the pace of computing. The pipeline has five lanes:

### 4.1 Gate (mechanical, pre-research)

Before any research begins, a small deterministic program checks
each proposed album against hard gates read from the rubric's
configuration block:

- **Window:** original recording/release year must fall within
  1945–1985. Outside the window the candidate is refused with no
  exceptions; the window moves only by editing the rubric file,
  never by conversation.
- **Style:** the album's primary style must be admissible under
  the current rubric (all eight style codes are currently open,
  including bebop, free jazz, fusion, and ECM-tagged records).
- **Deduplication:** the album is checked against every album
  already in the database *in any status* — included, candidate,
  excluded. A rejected album is never re-proposed; nothing
  reaches the curator twice.

### 4.2 Selection (judgment, free choice)

The agent chooses the two candidates itself, by judgment, roaming
freely across the admissible styles — no quotas, rotations, or
pairings. The acknowledged consequence, accepted by the curator
as a standing ruling, is a *front-loading bias*: selection draws
on what the agent can bring to mind, so the consensus spine of
the tradition is proposed early and obscure records are
under-weighted. Genuine discovery of the obscure would require a
different mechanism (a curated candidate pool); this limitation
is recorded here openly.

### 4.3 Gather (source-grounded dossier)

For each chosen album the agent builds a complete dossier from
live sources — **never from model memory**, which the project
treats as the primary source of transcription errors. The dossier
records, at minimum:

- full personnel, instrument by instrument, track-level where
  the sources allow;
- production credits (producer, engineer) and label identity;
- recording dates and recording sites, one entry per session;
- catalog and streaming identifiers (MusicBrainz, Apple);
- cover art provenance;
- a source map in which **every claim carries a citation token
  and an epistemic label** (see §5);
- a rationale arguing the album's canonical case, with every
  accolade it cites (e.g. a Penguin Guide crown) itself sourced —
  an unsourced consensus claim is a defect, not an argument.

Each fetched page is verified to actually concern the album in
question before it is cited, because deep-link identifiers at
source sites occasionally rot and silently re-point at unrelated
records. A minimum of three independent sources per album is the
standing target.

### 4.4 Judge (the canon council)

The dossier goes to a panel of independent AI models that vote
blind against the rubric; a separate aggregator model synthesizes
their votes into a structured ballot: a tier (from consensus core
down through strong, contested, and scope call), a priority, a
case for, a case against, and a record of disagreement. The
pipeline enforces quorum: if fewer than two judges answer, the
night's run fails honestly and stages nothing rather than
lowering the standard. The council runs exactly once per
candidate; its ballot is archived verbatim with the dossier.

### 4.5 Stage and report

A ballot-carrying dossier is inserted into the database with the
status **candidate** — parked for review, not admitted. The
pipeline is structurally incapable of advancing it further. The
night ends with a compact report to the curator (one line per
album plus the pending-queue count, and a flag when no streaming
copy could be found, so the curator never hunts for an
unlistenable record).

## 5. The evidence standard (obs / inf / unk)

Every factual claim in the canon carries one of three labels:

- **obs** — a named source states it outright (e.g. a label
  discography lists the engineer).
- **inf** — reasoned from pattern or synthesis across sources.
- **unk** — the sources conflict or are silent.

Two rules give the labels teeth:

1. **Conflicts are preserved, never resolved silently.** When two
   reputable sources disagree — about a studio, a date, a
   sideman — the dossier records both claims, marks the fact unk,
   and explains the conflict in notes. The database remembers
   what is uncertain; that is what makes its positive claims
   trustworthy.
2. **Precision is never invented.** A city-level recording site
   labeled inf is preferred to a fabricated street address; an
   undocumented location is recorded as unknown rather than
   guessed. New recording sites are created complete (name, city,
   kind, coordinates, epistemic label, source) or not at all.

## 6. Human review: the verdicts

Candidates wait in the review queue until the curator listens and
rules. The possible verdicts:

- **Include.** The album's canon status advances to *included*;
  it awaits the next publication run.
- **Exclude.** The album is marked *excluded* — never deleted.
  The dossier, the council ballot, and the reasoning remain in
  the archive permanently, so the canon remembers what was
  weighed, not only what was chosen.
- **Defer ("later").** The album remains a candidate, parked.
  Nothing auto-resurfaces; a quiet monthly watchdog report lists
  parked albums with the curator's own reasons, and only the
  curator can un-park one.

Every verdict is executed through the project's edit contract:
one audited log row per album, carrying the curator's words
verbatim, in an append-only audit table. The log is the permanent
record of who decided what, when, and why.

Two safety valves govern the queue:

- **Backlog cap (10).** When ten candidates sit unreviewed, the
  drip goes silent — it stages nothing until the curator clears
  room. The machine waits for the listener, never the reverse.
- **Availability flag.** Candidates with no findable streaming
  copy are flagged, never filtered — unavailability is
  information for the curator, not a selection criterion.

## 7. Publication

On the curator's explicit word — ad hoc, never on a schedule —
approved albums are exported from the database, enriched with
cover art and 30-second Apple Music preview clips, built into the
static site, and deployed to jazzcanon.com. Each status
transition (candidate → included → approved → live) is executed
through the edit contract and logged; the final "live" flip is
performed only by the deploy pipeline itself, never by hand.

## 8. Integrity mechanisms (summary)

The process is defended at every seam:

| Risk | Defense |
|---|---|
| Duplicate proposals | Pre-research dedup against all DB statuses |
| Facts from model memory | Forbidden; live sources only, minimum three |
| Source pages pointing at wrong records | Artist/title verified on every page before citation |
| Unsourced acclaim ("the critics love it") | Every accolade must carry a citation token |
| A malfunctioning judge panel | Quorum rule: fewer than two judges = honest failure, nothing staged |
| Silent conflict resolution | Both claims recorded, marked unk |
| Invented precision | unk preferred to plausible guesses, by rule |
| Agent self-promotion | Structural: pipeline cannot advance past "candidate" |
| Unrecorded decisions | Append-only audit log, one row per album per change |
| Runaway proposal rate | Drip size fixed at 2; backlog cap at 10 |
| Destruction of rejected work | Exclusion preserves the full record; nothing is deleted |

## 9. Known limitations, stated openly

1. **Front-loading bias.** Selection draws on agent recall, so
   consensus-spine albums arrive early and the genuinely obscure
   are under-proposed. Mitigation: directed gap-fill missions in
   which the curator names a target (a year range, a label, an
   artist) and the pipeline works that target.
2. **The estimate in §2 is inference.** The anchors are observed;
   the reductions are reasoned. The true LP count for the window
   is unknown and probably unknowable.
3. **Sources decay.** Deep links rot; storefront availability
   varies by country (an album absent from Apple's US catalog may
   exist in other storefronts); community-edited sources
   (Discogs, Wikipedia) can drift. The citation trail allows any
   claim to be re-checked at any time.
4. **The canon is personal.** The rubric's test — "the record you
   would hand someone" — is a human judgment. The methodology
   guarantees the integrity of the evidence and the process; it
   does not pretend the final taste is mechanical.

## 10. The sources relied upon

Counted from the live database (2026-10-18): 1,133 distinct
source records supporting 1,356 citations, in these families:

- **Discographies (165 distinct sources).** jazzdisco.org's label
  and artist discographies (the Blue Note and Prestige catalogs,
  artist session catalogs); Tom Lord's Jazz Discography
  tradition; The Jazz Discography Project; Mosaic Records session
  discographies. The factual backbone for dates, studios,
  personnel.
- **Release databases.** AllMusic album entries and credits
  pages; Discogs master/release pages (corroborated, treated one
  notch below discographies); MusicBrainz release groups.
- **Reference works.** The Penguin Guide to Jazz (Cook & Morton —
  the most-cited single source, 33 citations, the primary
  external consensus signal); the All Music Guide to Jazz.
- **Encyclopedic layer.** Wikipedia album articles (track lists,
  dates, reception), checked against the discographies.
- **Catalog and art services.** iTunes Search/Lookup API
  (streaming identifiers, high-resolution artwork); the Cover Art
  Archive.
- **Critical lists.** uDiscover, Jazzwise, JazzFuel, WBGO,
  eJazzNews features; the DownBeat/JazzTimes/NPR poll tradition —
  used to evidence consensus claims, each individually cited.
- **Liner notes.** The album's own sleeve, whenever digitized —
  the closest thing to a primary source a record has.

## 11. The one-paragraph account

> Albums are chosen by a process that reserves judgment to a
> human and everything else to software. Every night, an agent
> selects two candidates from the tens of thousands of jazz LPs
> recorded between 1945 and 1985, researches each from primary
> discographic sources with every fact labeled by how well it is
> known, and submits the dossier to a panel of AI judges that
> writes a formal case for and against. Then the machinery stops:
> the curator listens to the records and rules — include,
> exclude, or defer — with every decision logged verbatim. No
> album has ever entered the canon except through a human verdict
> after listening. As of October 2026 the canon holds 292 albums,
> each supported by cited sources, with all rejected candidates
> preserved on record rather than deleted.

---

*Document history: prepared 2026-10-18 from the live rubric
(`config/canon-rubric.md`), the operating skills, and direct
queries against the `_jazzcanon` schema. Figures marked as of the
preparation date are observed; the LP-population estimate is
inference built on observed anchors, per §2.*
