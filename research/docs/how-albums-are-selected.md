# How Albums Are Selected for A Jazz Canon

A methodological description of the selection process behind jazzcanon.com.

Prepared 2026-10-18 by McCoy (the project's curator-assistant agent), at the request of the curator; revised for register 2026-10-20. All figures were verified against the live database on 2026-10-20. The document is a standing private reference: the curator draws short public descriptions from it, and it records the reasoning and safeguards that the short versions omit.

---

## 1. What the canon is

A Jazz Canon is a personal discovery canon of jazz albums recorded between 1945 and 1985: bebop through the first ECM decade and its kin. It is not an academic canon and not a comprehensive catalog. Its test, stated in the project's standing rubric, is whether an album is a *load-bearing record of the tradition*: the record you would hand someone to explain what this music is.

The website is a static public export of a private PostgreSQL database in which every album, track, performance, session, and recording site is stored with its sources. The public site is a gallery; the database is the system of record. This document describes how records enter it.

As of 2026-10-20 the canon holds **297 published albums**, drawn from a database of 1,362 persons, 2,097 tracks, 2,267 performance records, 548 recording sessions, and 81 recording sites, supported by 1,193 distinct source records and 1,421 individual citations.

## 2. The scale of the selection problem

A reasonable estimate of the original jazz LPs (10" and 12") issued worldwide between 1945 and 1985 is **on the order of 25,000–40,000**; roughly 30,000 serves as the working figure.

This is an inference, not a count. The reasoning, in keeping with the project's evidence standards:

- *Anchor (observed):* Tom Lord's Jazz Discography, the standard session-level authority, indexes approximately 456,000 jazz record releases across all eras (1896–present) and formats, including reissues, international pressings, and compilations.
- *Anchor (observed):* Discogs, which attempts to catalog every physical release ever made, holds over 19 million releases across all genres, of which jazz is roughly 5–8%.
- *Reduction (inferred):* The 1945–1985 window contains the LP era essentially whole and the peak decades of jazz recording activity. Applying an estimated releases-to-original-albums ratio of 3–4 (each original album generates several cataloged releases over its lifetime) and excluding singles, EPs, and compilations of older material yields the 25,000–40,000 band.
- *Cross-check (inferred):* Label arithmetic. The major US jazz labels of the period (Blue Note, Prestige, Riverside, Columbia, Impulse!, Atlantic, Verve, EmArcy, Contemporary, Pacific Jazz, Savoy, Fantasy, CTI, Milestone) account for roughly 8,000–12,000 original jazz LPs in the window; doubling for European, Japanese, and independent labels lands in the same range.

The exact figure is unknown; this set has never been counted precisely. The order of magnitude is solid: tens of thousands, not thousands, not hundreds of thousands.

Against that pool, 297 albums represent a selection of roughly one record in a hundred. The methodology below exists to make that hundredth defensible.

## 3. The division of labor

The process has three participants with strictly separated powers:

1. **The curator (John).** The only decision-maker. He listens to every candidate and rules: include, exclude, or defer. No album enters the canon by any other path.
2. **The builder agent (McCoy) and its nightly pipeline.** Proposes candidates, researches them, and stages them for review. It cannot advance any album past "candidate."
3. **The canon council.** A panel of independent AI judges that evaluates each candidate dossier against the written rubric and issues a ballot: a tier, a priority, a case for, a case against, and any disagreement among the judges. The council only proposes; it has never admitted an album.

The design principle: machines do the librarian's work (finding, fetching, cross-checking, formatting) and the human does the critic's work (listening and deciding).

## 4. The nightly pipeline (the "drip")

A scheduled job runs every morning at 06:00 (US Eastern). Its budget is exactly **two candidates per night**, a fixed rule chosen so the canon grows at the pace of listening rather than the pace of computing. The pipeline has five lanes:

### 4.1 Gate (mechanical, pre-research)

Before any research begins, a small deterministic program checks each proposed album against hard gates read from the rubric's configuration block:

- **Window:** original recording/release year must fall within 1945–1985. Outside the window the candidate is refused with no exceptions; the window moves only by editing the rubric file, never by conversation.
- **Style:** the album's primary style must be admissible under the current rubric. No style is currently excluded; the vocabulary carries 17 codes, from bebop through fusion and the European wing, and ECM remains a label tag rather than a primary style.
- **Deduplication:** the album is checked against every album already in the database *in any status*: included, candidate, excluded. A rejected album is never re-proposed; nothing reaches the curator twice.

### 4.2 Selection (judgment, free choice)

The agent chooses the two candidates itself, by judgment, roaming freely across the admissible styles with no quotas, rotations, or pairings. The acknowledged consequence, accepted by the curator as a standing ruling, is a *front-loading bias*: selection draws on what the agent can bring to mind, so the consensus spine of the tradition is proposed early and obscure records are under-weighted. Genuine discovery of the obscure would require a different mechanism (a curated candidate pool); this limitation is recorded in §9.

### 4.3 Gather (source-grounded dossier)

For each chosen album the agent builds a complete dossier from live sources, never from model memory, which the project treats as the primary source of transcription errors. The dossier records, at minimum:

- full personnel, instrument by instrument, track-level where the sources allow;
- production credits (producer, engineer) and label identity;
- recording dates and recording sites, one entry per session;
- catalog and streaming identifiers (MusicBrainz, Apple);
- cover art provenance;
- a source map in which **every claim carries a citation token and an epistemic label** (see §5);
- a rationale arguing the album's canonical case, with every accolade it cites (e.g. a Penguin Guide crown) itself sourced. An unsourced consensus claim is treated as a defect, not an argument.

Each fetched page is verified to actually concern the album in question before it is cited, because deep-link identifiers at source sites occasionally rot and silently re-point at unrelated records. The standing target is a minimum of three independent sources per album.

### 4.4 Judge (the canon council)

The dossier goes to a panel of independent AI models that vote blind against the rubric; a separate aggregator model synthesizes their votes into a structured ballot: a tier (from consensus core down through strong, contested, and scope call), a priority, a case for, a case against, and a record of disagreement. The pipeline enforces quorum: if fewer than two judges answer, the night's run fails honestly and stages nothing rather than lowering the standard. The council runs exactly once per candidate; its ballot is archived verbatim with the dossier.

### 4.5 Stage and report

A ballot-carrying dossier is inserted into the database with the status **candidate**: parked for review, not admitted. The pipeline is structurally incapable of advancing it further. The night ends with a compact report to the curator (one line per album plus the pending-queue count, and a flag when no streaming copy could be found, so no candidate arrives unlistenable).

## 5. The evidence standard (obs / inf / unk)

Every factual claim in the canon carries one of three labels:

- **obs** — a named source states it outright (e.g. a label discography lists the engineer).
- **inf** — reasoned from pattern or synthesis across sources.
- **unk** — the sources conflict or are silent.

Two rules enforce the labels:

1. **Conflicts are preserved, never resolved silently.** When two reputable sources disagree (about a studio, a date, a sideman) the dossier records both claims, marks the fact unk, and explains the conflict in notes. The database records what is uncertain; that record is what makes its positive claims trustworthy.
2. **Precision is never invented.** A city-level recording site labeled inf is preferred to a fabricated street address; an undocumented location is recorded as unknown rather than guessed. New recording sites are created complete (name, city, kind, coordinates, epistemic label, source) or not at all.

## 6. Human review: the verdicts

Candidates wait in the review queue until the curator listens and rules. The possible verdicts:

- **Include.** The album's canon status advances to *included*; it awaits the next publication run.
- **Exclude.** The album is marked *excluded* — never deleted. The dossier, the council ballot, and the reasoning remain in the archive permanently, so the canon remembers what was weighed, not only what was chosen.
- **Defer ("later").** The album remains a candidate, parked. Nothing auto-resurfaces; a quiet monthly watchdog report lists parked albums with the curator's own reasons, and only the curator can un-park one.

Every verdict is executed through the project's edit contract: one audited log row per album, carrying the curator's words verbatim, in an append-only audit table. The log is the permanent record of who decided what, when, and why.

Two limits govern the queue:

- **Backlog cap (10).** When ten candidates sit unreviewed, the drip stages nothing until the curator clears room. Selection waits on listening, never the reverse.
- **Availability flag.** Candidates with no findable streaming copy are flagged, never filtered; unavailability is information for the curator, not a selection criterion.

## 7. Publication

On the curator's explicit word (ad hoc, never on a schedule) approved albums are exported from the database, enriched with cover art and 30-second Apple Music preview clips, built into the static site, and deployed to jazzcanon.com. Each status transition (candidate → included → approved → live) is executed through the edit contract and logged; the final "live" flip is performed only by the deploy pipeline itself, never by hand.

## 8. Integrity mechanisms (summary)

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

1. **Front-loading bias.** Selection draws on agent recall, so consensus-spine albums arrive early and the genuinely obscure are under-proposed. Mitigation: directed gap-fill missions in which the curator names a target (a year range, a label, an artist) and the pipeline works that target.
2. **The estimate in §2 is inference.** The anchors are observed; the reductions are reasoned. The true LP count for the window is unknown and probably unknowable.
3. **Sources decay.** Deep links rot; storefront availability varies by country (an album absent from Apple's US catalog may exist in other storefronts); community-edited sources (Discogs, Wikipedia) can drift. The citation trail allows any claim to be re-checked at any time.
4. **The canon is personal.** The rubric's test ("the record you would hand someone") is a human judgment. The methodology guarantees the integrity of the evidence and the process; it does not pretend the final taste is mechanical.

## 10. The sources relied upon

Counted from the live database (2026-10-20): 1,193 distinct source records supporting 1,421 citations, in these families:

- **Discographies (the largest family).** jazzdisco.org's label and artist discographies (the Blue Note and Prestige catalogs, artist session catalogs); the Tom Lord Jazz Discography tradition; The Jazz Discography Project; Mosaic Records session discographies. The factual backbone for dates, studios, personnel.
- **Release databases.** AllMusic album entries and credits pages; Discogs master/release pages (corroborated, treated one notch below discographies); MusicBrainz release groups.
- **Reference works.** The Penguin Guide to Jazz (Cook & Morton; 33 citations to a single edition record, the primary external consensus signal); the All Music Guide to Jazz.
- **Encyclopedic layer.** Wikipedia album articles (track lists, dates, reception), checked against the discographies.
- **Catalog and art services.** iTunes Search/Lookup API (streaming identifiers, high-resolution artwork); the Cover Art Archive.
- **Critical lists.** uDiscover, Jazzwise, JazzFuel, WBGO, eJazzNews features; the DownBeat/JazzTimes/NPR poll tradition, used to evidence consensus claims, each individually cited.
- **Liner notes.** The album's own sleeve, whenever digitized: the closest thing to a primary source a record has.

## 11. The one-paragraph account

> Albums are chosen by a process that reserves judgment to a human and everything else to software. Every night, an agent selects two candidates from the tens of thousands of jazz LPs recorded between 1945 and 1985, researches each from primary discographic sources with every fact labeled by how well it is known, and submits the dossier to a panel of AI judges that writes a formal case for and against. Then the machinery stops: the curator listens to the records and rules — include, exclude, or defer — with every decision logged verbatim. No album has ever entered the canon except through a human verdict after listening. As of October 2026 the canon holds 297 albums, each supported by cited sources, with all rejected candidates preserved on record rather than deleted.

---

*Document history: prepared 2026-10-18 from the live rubric (`config/canon-rubric.md`), the operating skills, and direct queries against the `_jazzcanon` schema. Revised 2026-10-20 for register (more objective, conversational phrasing removed) and figures refreshed to that date. Figures marked as of a date are observed; the LP-population estimate is inference built on observed anchors, per §2.*

---

# Appends

Follow-up questions and answers, appended verbatim with timestamps. The main text above is not edited by appends; each append is grounded in live configuration at the time it was written.

## Append A — 2026-10-19 08:28 EDT — Agents, aggregators, council members by model

Question (curator): "As of today, list all agents, aggregators, and council members by model being." All entries below were read from live configuration (`cron/jobs.json`, profile `config.yaml`) at the time noted.

| Role | Model | Provider/route | Where configured |
|---|---|---|---|
| Curator's assistant (McCoy, interactive) | kimi-k3 | kimi-coding | profile `config.yaml` `model.default` |
| Nightly drip agent (selects, gathers, stages) | deepseek/deepseek-flash-latest (recorded in the job as `~deepseek/deepseek-flash-latest`) | deepseek | cron job `9c3376aac79a` (`canon-drip`) |
| Council reference #1 (judge) | minimax/minimax-m3 | OpenRouter | MoA preset `canon-council`, `reference_models[0]` |
| Council reference #2 (judge) | google/gemini-3.8-flash | OpenRouter | MoA preset `canon-council`, `reference_models[1]` |
| Council aggregator (chair) | openai/gpt-6-luna | Nous | MoA preset `canon-council`, `aggregator` |
| Wings-report job (Sundays 08:00) | none — deterministic script | n/a | cron job `1c20dab36950` (`no_agent: true`) |
| Embeddings (canon-search; not selection) | nomic-embed-text | Ollama on vps4 | `scripts/embed.py` |
| Profile fallback (any lane) | z-ai/glm-5.3-flash | OpenRouter | profile `fallback_providers` |

Gather-lane children (delegated research agents) inherit the dispatching agent's model unless a dispatch pins otherwise; the steady drip does not pin, so they run on the drip job's model.

Council preset parameters (live): `reference_temperature: 0.6`, `reference_max_tokens: 8000`, `max_tokens: 8192` (aggregator), `degraded_reference_policy: loud`, `fanout: user_turn`.

Historical note (auditable, not current): the drip job's model pin has changed over time (kimi-k3 was an earlier pin); the council aggregator was upgraded from gpt-5.6-luna to gpt-6-luna on 2026-09-28. The table above is the state on the date of this append; model identity is configuration, not a constant, and is re-read from the live files on every such question.

**Update — 2026-10-19 (later the same day):** the council roster changed. Both reference judges moved from OpenRouter to Nous with models unchanged (minimax-m3, gemini-3.8-flash); the aggregator changed from openai/gpt-6-luna to openai/gpt-6.1-sol, also via Nous. Before adoption the new roster was rehearsed on an existing dossier and returned an identical verdict to the prior roster's ballot.

## Append B — 2026-10-19 08:28 EDT — Flow / decision tree

Question (curator): "Show me a flow or decision tree — ascii diagram will do."

```
                    HUMAN LANE (John) — the only decision-maker
  ┌────────────────────────────────────────────────────────────────┐
  │  listens to candidates ──► verdict: INCLUDE / EXCLUDE / DEFER  │
  │         │                                                      │
  │         ▼  (verdicts executed via edit contract, 1 log row     │
  │             per album, append-only audit)                      │
  │   include ──► approved ──► SHIP (ship.sh: export → previews    │
  │             → build → deploy ──► site_status: live)            │
  │   exclude ──► record preserved, never deleted                  │
  │   defer   ──► stays candidate; monthly wings report reminds    │
  └─────────▲──────────────────────────────────────────────────────┘
            │  06:05–06:15 compact Telegram report
            │  (names + queue count + no-streaming flags)
 ═══════════╧═══════════════ MACHINE LANE ═════════════════════════
            │
   [06:00 cron: canon-drip, 2 candidates/night, drip model]
            │
            ▼
   PRECHECK (canon-drip-precheck.py — deterministic script)
     • inject guardrails (window, styles, drip size, dedup list)
     • sweep stale inbox → archive decided dossiers
     • backlog check: unreviewed candidates ≥ 10 ?
            │ yes                    │ no
            ▼                        ▼
      [SILENT — no new         SELECT 2 candidates
       candidates tonight]     (agent judgment, free choice,
            │                  no quotas; must not duplicate
            │                  anything in DB, any status)
            │                        │
            │                        ▼
            │               GATE (check-candidate.py — per album)
            │                 • year inside 1945–1985?
            │                 • style admissible?
            │                 • not already present?
            │                     │ pass        │ fail
            │                     ▼             ▼
            │               GATHER            refuse; pick another
            │   (research agents fetch live sources —
            │    discographies, AllMusic, Discogs, MusicBrainz,
            │    Wikipedia, iTunes, Cover Art Archive;
            │    ≥3 sources; every claim cited + labeled
            │    obs/inf/unk; memory forbidden)
            │                     │
            │                     ▼
            │               dossier written → candidates-inbox/
            │                     │
            │                     ▼
            │               JUDGE (canon-council.py → MoA preset)
            │                 ┌─ reference 1: minimax-m3 ────┐
            │                 ├─ reference 2: gemini-3.8-flash┤ blind votes
            │                 └─► aggregator: gpt-6-luna      │ vs rubric
            │                     synthesizes ballot          │
            │                     (tier, priority, case for,  │
            │                      case against, disagreement)│
            │                     │
            │              judges answered ≥ 2 ?
            │                │ yes            │ no
            │                ▼                ▼
            │           STAGE          DRIP FAILED — report
            │  (stage-candidate.py     honestly, stage NOTHING
            │   --ballot-inline)       (no self-judging, no
            │                │          substitute ballot)
            │                ▼
            │        DB rows: canon_status = candidate
            │                  site_status = found
            │                │
            └────────────────┴──► Telegram report to John
                                    (then machine waits)

  WEEKLY: [Sundays 08:00 — canon-wings-report (script, no AI)]
     first Sunday of month AND deferred candidates exist?
        yes ──► Telegram: each parked album + John's reason
        no  ──► silence
```

## Append C — 2026-10-19 08:28 EDT — Presets and skills

Question (curator): "List any presets or skills used."

Presets (live, from profile `config.yaml`):

- **MoA preset `canon-council`** — the only mixture-of-agents preset; it is the JUDGE lane. Composition and parameters are listed in Append A. Set as the profile's `default_preset`.
- A non-default variant, `canon-council-adversarial.py` (prosecutor/defender role-weighting), exists in reserve for contested boundary cases; it is not used by the drip.

Skills (installed on the mccoy profile; they load into McCoy sessions on relevance — they are the operating manuals, not the machinery):

- `mccoy-tyner` — project constitution: genre definitions, source catalog, dossier contract, epistemic discipline, place hygiene.
- `canon-drip-operations` — the drip playbook: pipeline shape, failure modes, recovery procedures, verdict execution, publishing path.
- `canon-ship-operations` — the publish/deploy runbook for jazzcanon.com.
- `discographic-source-research` — discography/personnel/session research method.
- `album-candidate-dossier` — the single-album dossier build workflow.
- `research-workflows` — general source-grounded compilation method.

Configuration documents the pipeline reads on every run (the true steering surfaces, all in the project repo):

- `config/canon-rubric.md` — window, gates, drip size, backlog cap, the five judgment signals. Machine-read by the precheck, the gate, and the council.
- `config/edit-contract.md` — whitelisted editable fields, the audit protocol, the append-only rule.
- `docs/personnel-contract.md` — the dossier shape every gatherer must produce.

Executable machinery (deterministic scripts, no AI):

- `scripts/canon-drip-precheck.py` (profile) — guardrails, inbox lifecycle, backlog cap, recovery detection.
- `scripts/check-candidate.py` — the gate.
- `scripts/stage-candidate.py` — transactional DB staging (dry-run rehearsal supported; rolls back whole on any defect).
- `scripts/canon-wings-report.py` (profile) — the Sunday deferred-verdicts watchdog.
- Publishing path: `scripts/ship.sh` → `publish.sh` → `export.sh` → site repo `enrich-previews.mjs` → `npm run build` → wrangler deploy → `scripts/deploy.sh`.
- Support: `scripts/embed.py` (embeddings for canon-search), `scripts/geocode-place.py`, `scripts/cover-art-fetch.py`.


## Append D — 2026-10-30 — The evaluation rubric, complete text

Question (curator): "Offer a complete statement of the rubric used by the judges for album evaluation."

Answer: the judges (both reference judges and the aggregator) read `config/canon-rubric.md` before judging any candidate. Reproduced below in full, verbatim, as it stood on 2026-10-30. The frontmatter block is the hard-gate configuration the machinery enforces; the prose is the judgment the council applies.

---

---
# ── Hard gates — machine-read by canon-drip-precheck.py and canon-council.py.
# Edit these lines to steer McCoy; no code or schema change is ever needed.
year_min: 1945
year_max: 1985
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
belongs when it is a load-bearing record of the bebop / post-bebop
tradition — the album you would hand someone to explain what this music
is. Signals, strongest first:

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

- The window is **year_min–year_max** (frontmatter, currently 1945–1985),
  by original recording/release year. Outside the window: refuse, no
  exceptions in conversation — the window moves only by editing this file.
- **The 1945–1949 band — bebop is in scope (2026-09-24, floor raised
  1940→1945):** the old "pure bebop is not yet in scope" clause is
  retired — John ruled the day has come. Bebop itself now belongs to the
  canon: Parker, Gillespie, Monk, Powell, the founding records, not only
  the transition out of them. 1945–49 bebop arrivals are argued on the
  five signals like everything else, not as **scope_call** — the idiom is
  no longer a boundary. `bebop` joins the style vocabulary as a primary
  style. Pre-1945 transition records fall outside the window; the canon
  held none at the move (verified against `_jazzcanon.album`).
- **The 1973–1985 band (added 2026-07-25 as 1973–1979; extended to 1985
  on 2026-09-24):** the window was raised from 1972 to admit the ECM
  first decade and its kin, then pushed out to 1985. Albums recorded
  1973+ are judged on **continuity**: does the record extend the
  post-bebop / modal / post-bop tradition the canon is built on (the
  1960s lineage reaching forward), rather than found something new? The
  canonical example is Keith Jarrett's *The Köln Concert* (1975) — late
  modal, continuous. Early Pat Metheny Group (*American Garage*, 1979) is
  the border case: acoustic, swinging, song-form = arguable;
  electric-rock vocabulary = the fusion exclusion bites. All 1973+
  arrivals should lean **scope_call** or **contested** by default and
  name the boundary in the ballot — the 1980–85 tail doubly so; John
  rules.
- **The opened genre gates (2026-07-28).** `excluded_styles` is now empty:
  free jazz, fusion, and the ECM catalogue are **admissible**, and each has
  a dedicated style module of `jazz-style-researcher` (`style=fusion`,
  `style=free-jazz`, `style=ecm` — see `config/style-research/`). This is a *permeable
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
       (Directed bulk missions like the 2026-09-24 bebop/ECM ten are
       John's word, not a floodgate.)
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
  is now a candidate, argued, not a wall. The 1980–85 window tail is deep
  fusion territory — the bridge test decides, never the decade.
- **ECM — runs with the window (extended 2026-09-24).** The ECM gate runs
  **1969–1985** (it was 1969–1979 until the 2026-09-24 window move — the
  "small step" John always said he would extend later). ECM albums are
  judged on continuity with the 1960s modal tradition, never accepted or
  rejected by label or decade alone; 1980s ECM leans **scope_call** /
  **contested** by default. *The Köln Concert* (1975) is the anchor. ECM
  stays a label tag, never style_primary.
- **`excluded_styles` is prose-enforced.** `check-candidate.py` and
  `stage-candidate.py` read `year_min`/`year_max` from this frontmatter and
  nothing else. Style scope lives in agent and council judgment — this
  section *is* the enforcement.
- **No style quotas.** Sixty modal albums is fine if each earns its place.
  Never propose a weaker album to balance a genre.
- **The drip's pace is deliberate (affirmed 2026-07-26).** The widened
  window (1945–1985) makes a fast build to 1,000+ albums technically
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
