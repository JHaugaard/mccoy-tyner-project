# Free Jazz Specialist — Agent Brief

> **Canonical agent:** `~/.claude/agents/jazz-free-jazz-researcher.md` (self-contained, model-scoped: Opus).
> Written 2026-07-28, alongside the agent — unlike the 2026-06-11 briefs, this one was
> never the operative document. It is the **design record**: why the gate opened, what was
> decided, and what stayed open. The agent file is authoritative on behaviour; when the two
> disagree, the agent file wins and this brief is stale.

## Why this gate opened

Free jazz was an excluded style in `config/canon-rubric.md` from the project's start, for
the same reason fusion was: it didn't resonate, and John felt he did not understand it.

**Unlike fusion, half of that is still true.** John has said plainly that free jazz does
not currently resonate with or even appeal to him. He opened the gate anyway, because he
decided to **study** the idiom rather than dismiss it — and he asked the load-bearing
question: how many free-jazz records might be canon-worthy at all? Twenty? Fifty? A
hundred? That question is open, and it is the reason this agent exists in the shape it does.

This is the hardest of the three gates, and the one most likely to produce culls. That is
the system working, not failing.

## Design decisions

**1. The agent proposes records that *teach*.** The strongest case a record can make here is
legibility: it opens the idiom to a listener who does not yet hear it, and it connects
audibly to music already in the canon. *The Shape of Jazz to Come* teaches; a forty-minute
energy blowout does not teach first, whatever its merits.

*Rationale:* John is studying. A specialist optimizing for the field's historical
importance would hand him a reading list for someone who already loves this music.

**2. Two required fields, not one.**

- **`bridge_case`** — what in the existing canon the record grows out of, and what it opens
  onto. Same discipline as the fusion agent. "Landmark of the New Thing" is a historical
  claim, not a case for *this* canon.
- **`accessibility`** — `gateway` | `intermediate` | `demanding`. Unique to this agent.
  It exists so John can sequence his own listening, and the agent is instructed to be blunt
  to the point of costing a record its inclusion. A record mislabeled `gateway` wastes a
  listening session and costs trust on the next ten.

*Rationale:* the accessibility field is the single most consequential design choice in this
brief. It converts the agent from an advocate into a guide, and it makes dishonesty
detectable — John will hear the mismatch immediately.

**3. Default run size 5 — the smallest of any specialist.** Deliberately below fusion's 6
and the established specialists' 10.

**4. Energy-music maximalism is admissible but named as the hardest case.** *Machine Gun*,
late Ayler, full abstraction — in scope, and the agent must make the real argument or not
propose them. Explicitly forbidden from smuggling them in under a mild description. The
rubric carries the same line.

**5. Genre advocacy is a guardrail violation** — as with fusion, and more sharply here.
Given John's stated taste, arguing that the canon needs free jazz for completeness or
credibility is actively counterproductive.

**6. An eighth synthesis section: The Listening Path.** A proposed order in which the run's
records might be heard, starting from one or two named albums already in the canon. John is
studying deliberately; a path is worth more than a pile.

**7. Personnel contract stress noted, not amended.** This idiom strains the contract more
than any other:
- Multi-instrumentalism as norm (AACM "little instruments") — taxonomy where a term exists,
  the source's exact wording in notes where it does not.
- Leaderless collectives — recorded as such; the leader-name `id` convention gets an
  explicit note rather than a manufactured leader.
- Continuous suites and untitled improvisations weaken the "track" abstraction — record
  what the issue states, `unk` where composition credit genuinely is not documented.
- FMP, BYG Actuel, Incus, ESP-Disk are thinly documented — report gaps rather than filling
  them from inference. This is where fabrication is most tempting and least detectable.

## Scope absorbed into this agent

Four wings, rather than four agents — the gate is too new to fragment:

| Wing | Era | `style_primary` |
|------|-----|-----------------|
| American free jazz / the New Thing | 1959–1970s | `free-jazz` |
| AACM & the Chicago/St. Louis avant-garde | ~1965–1979 | `avant-garde-jazz` |
| European free improvisation | ~1966–1979 | `free-improvisation` |
| The loft era | ~1972–1979 | `free-jazz` + `loft-jazz` tag |

The AACM wing is called out as disproportionately valuable here: composition and silence
given equal standing with intensity makes it the most legible entry point for a listener
coming from the composed tradition. The European wing is called out as the weakest
continuity claim on a canon built from the American post-bebop tradition — propose sparingly,
always with an explicit bridge.

## Boundary ownership

| Border | Ruling |
|--------|--------|
| **ECM releases** | Belong to `jazz-ecm-researcher` — including the free-adjacent catalogue (*Conference of the Birds* 1972, Old and New Dreams 1979, the Art Ensemble's ECM sides). Handed off in Gaps Noticed. |
| **Post-bop avant** | *Out to Lunch!*, *Point of Departure*, the Blue Note avant sides — shared with the modal specialist, some already standing `scope_call`s in the rubric. Argue as bridges, set `overlap_risk`. |
| **Coltrane** | Classic quartet through *A Love Supreme* (1964) → modal specialist, likely already in canon. *Ascension* (1965) forward → this agent. Named as the clearest test of whether this gate can carry the canon's most-loved musician into territory John finds hard. |
| **Spiritual jazz** | Claimed here (*Karma*, *Journey in Satchidananda*), tagged `spiritual-jazz`. Frequently the most accessible door into the idiom; the bridge case must say plainly that modal continuity is what carries them. |

## Open questions

- **How many?** John's own question — 20 / 50 / 100 — is unanswered and the agent does not
  answer it. It will be answered empirically by cull rate over the first several runs.
  Worth revisiting after ~20 candidates have been through the council.
- **Does a high cull rate need its own signal?** `research/cull-notes.md` currently records
  culls with a one-line reason. If this gate produces a run of rejections, the notes will
  become the most important calibration document in the project — they may need more
  structure than one line (e.g. *why* it didn't land: too abstract, no continuity, just
  didn't like it).
- **Is `accessibility` worth promoting into the schema?** It is candidate-only today. If it
  proves useful for sequencing John's listening, it is a natural `_jazzcanon.album` column —
  and would be useful for the site, not just the pipeline. Deferred, not proposed.
