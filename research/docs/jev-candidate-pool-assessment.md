# Jev and the Curated Candidate Pool — an assessment

Prepared 2026-10-19 by McCoy, at the curator's request. Status: study document — no changes to any pipeline, configuration, or cron job are proposed for execution without the curator's explicit ruling. Nothing in this document has been built.

---

## 1. Purpose

To assess whether Jev (TypeSafe AI's "System One" decision
model) has a useful role in building and maintaining a *curated
candidate pool* for the canon — the mechanism identified in the
selection-methodology document (§9, "Known limitations") as the
true fix for the drip's front-loading bias, identified in
August 2026 and deliberately never built.

The curator's framing, which this document adopts: the
attraction is not cost (existing canon volumes are already
inexpensive) but learning the typed-decision pattern, and the
ambition is to narrow the estimated ~30,000-album universe of
1945–1985 jazz LPs into a working target list so that the
drip's nightly selection is better focused.

## 2. What Jev is (verified 2026-10-19)

Jev is a decision-only model from TypeSafe AI (founded by
former OpenAI researcher Diogo Almeida), released 2026-09-15.
It is not an LLM: it generates no prose, gives no explanations,
and holds no conversations. A caller submits a block of "state"
(text/JSON) plus typed questions; Jev returns structured
decisions in a single parallel pass (reported latency
70–500 ms).

Three question primitives:

- **Choice** — select exactly one of 1–255 caller-defined
  categories. Returns the selection plus a probability
  distribution. The output structurally cannot invent a
  category outside the supplied set.
- **Score** — assign one of 2–10 caller-defined ordered levels.
- **Noul** — a yes/no question; returns a single probability
  that the statement is true (name derived from Bernoulli). No
  separate confidence field; 0.5 signifies uncertainty.

Practical facts: listed price $0.042 per million input tokens,
output free; available through OpenRouter as
`typesafe-ai/jev-latest` (a route the canon fleet already
uses); not open source; TypeSafe publishes a per-version
"jaggedness list" documenting known failure modes.

Caveats on the evidence: calibration quality is vendor-claimed
and unverified by us. A published third-party tutorial shows a
Noul and its negation returning 0.72 and 0.47 on the same item
(summing to 1.19, not 1.0), so probabilistic consistency across
independent questions is not guaranteed.

## 3. The problem the pool would solve

The drip selects two candidates nightly from what the agent can
bring to mind; there is no enumerated pool. The acknowledged
consequence (accepted by the curator as a standing ruling) is a
nomination bias: celebrated records are proposed early and
obscure-but-worthy records are under-weighted, independent of
merit. Judging downstream is unbiased; the bias is entirely in
which albums are nominated.

Two separable halves define any fix:

1. **Enumeration** — produce the actual list of albums in
   scope. This is data engineering, not AI: harvest release
   records from structured sources (MusicBrainz release-groups
   by type/date/tag; Discogs by genre/year; label discographies
   for gaps) into a table of artist, title, year, label, style
   tags, and identifiers. No model can do this; a harvested
   list owes nothing to anyone's recall.
2. **Triage** — attach signals to each enumerated row so the
   nightly draw can be better than uniform. This is where Jev
   is a candidate tool.

## 4. Proposed architecture (for study only)

```
   ENUMERATE (scripts, no AI)            TRIAGE (Jev, offline)
   MusicBrainz release-groups            per row: Score 1–5
   Discogs genre/year queries            "canonical promise"
   label discographies                   per row: Noul flags
          │                              (e.g. "documented in
          ▼                               major reference
   UNIVERSE TABLE                          traditions"?)
   artist/title/year/label/tags               │
   (est. 25–40k rows)                          ▼
          │                              POOL FILE (data/)
          └────────── merge ───────────► every row retained;
                                         signals attached,
                                         never filtered
                                                 │
                                                 ▼
   NIGHTLY DRIP (changed lane 1 only): draw 2 from pool,
   weighted by signals; low-signal rows still surface over
   time. Gate, gather, council, staging, verdicts UNCHANGED.
```

Design principles:

1. **Completeness defeats the bias, not the triage.** The pool
   fixes nomination bias structurally because selection draws
   from an enumerated universe by rule. Triage signals only
   order the draw; they never exclude.
2. **Jev's score is a signal, never a gate.** On the obscure
   tail (private-press dates, regional sessions) Jev — like any
   model — has thin knowledge and its scores will cluster near
   uninformative. Filtering on its score would rebuild the
   popularity bias at a new layer.
3. **Doctrine is untouched.** The pool feeds selection; it
   decides nothing. The mechanical gate, the council (with
   written ballots), and the curator's verdicts operate exactly
   as today. This is a change to how candidates are *found*,
   not to how they are *judged* or *admitted*.
4. **Every stage is reversible and independently valuable.**
   The universe table alone is a project asset even if the
   experiment stops there.
5. **Harvest window-agnostic; filter at draw time** (curator's
   point, 2026-10-19). The source dumps cover all years at equal
   cost, so the universe table carries every jazz album with year
   as a plain column — no rubric window baked into the data.
   The pool draw applies the current window as a live filter,
   exactly as check-candidate.py reads the rubric each run. A
   window move (e.g. 1985 → 1990) then costs one rubric edit
   plus one small Jev triage pass over the newly admitted years
   only — no re-enumeration, ever. The window is movable
   scaffolding; the harvested data must not harden around it.

## 5. Feasibility and cost (estimates, labeled)

- **Enumeration (inf):** MusicBrainz's API supports release-group
  queries by type, date range, and tag; Discogs by genre and
  year. Expected yield is in the tens of thousands of rows for
  1945–1985 jazz. Deduplication against `_jazzcanon.album`
  (all statuses) is mechanical. This is the bulk of the work —
  estimated as a bounded engineering task, not a research
  project. Exact query coverage and tag quality are unk until
  probed.
- **Triage cost (inf, arithmetic shown):** 30,000 rows ×
  ~300 input tokens each ≈ 9M input tokens × $0.042/M ≈
  **$0.40 per full pass.** At 70–500 ms per call with modest
  parallelism, wall time is 1–3 hours.
- **Nightly operating cost:** zero. The pool is a file; the
  drip reads it.

## 6. Validation before commitment

Jev's judgment on jazz records is unknown to us. Two cheap,
offline, fully reversible tests establish whether it deserves
any role:

- **Test 1 — style-agreement.** The canon holds 292 published
  albums with curator-reviewed style labels — ground truth.
  Ask Jev a Choice question per album (8 style codes; state =
  artist/title/year/short description) and measure agreement
  with the curated `style_primary`. A high agreement rate
  licenses further trust; a low rate ends the experiment with
  the pattern learned and nothing lost. Cost: cents.
- **Test 2 — citation audit.** Run one archived dossier's
  claims through Noul questions ("does the cited source
  explicitly state this claim?") and compare flags against the
  record. This evaluates Jev for the separate audit-lane idea
  without touching the pipeline.

Neither test writes to any database, cron job, or config.

## 7. Alternatives considered

1. **Rule-based triage without Jev** (label prestige, artist
   presence in the canon, identifier completeness). Cheapest
   and fully deterministic, but it encodes only what we already
   know how to count; it adds no independent judgment and
   teaches us nothing about typed-decision models. Rejected as
   the sole approach; retained as *complementary* signals in
   the pool.
2. **Embedding-similarity triage** (score albums by similarity
   to the existing canon's embeddings). Rejected as the primary
   signal: it systematically favors more-of-what-we-already-
   have, which is a different bias with the same shape.
3. **Do nothing; keep recall-based selection.** The standing
   ruling accepts the bias; this remains the default if tests
   disappoint. The pool is an improvement, not a repair of a
   failure.

## 8. Risks

| Risk | Assessment | Mitigation |
|---|---|---|
| Jev low-information on obscure records | Expected, structural | Score is signal-never-gate; draw rule guarantees surfacing |
| Calibration vendor-claimed | unk | Tests 1–2 before any pool role |
| Version drift ("jaggedness" per version) | Behavioral | Pin `jev-<version>` in any script; never `latest` in a pipeline |
| Non-open-source dependency | Strategic | Pool is a plain file; Jev is replaceable in the triage step |
| Enumeration data quality (tags, reissues, compilations) | unk until probed | Human review of a sample before first draw; conservative inclusion rules |
| Pool silently becomes a filter | Doctrinal | Design rule 2; drip reads pool with mandatory low-signal surfacing |

## 9. Sequencing, if pursued

1. Curator reviews this document; rules go/no-go on Test 1.
2. Test 1 (style-agreement) — one-off script, report only.
3. Test 2 (citation audit) — optional, independent.
4. Enumeration brief to @coder (bounded: harvest universe
   table; no Jev, no drip changes).
5. Human review of a universe-table sample.
6. One full Jev triage pass; curator reviews output.
7. Curator ruling on whether the drip's lane 1 draws from the
   pool (a cron-prompt change, documented like every other
   drip-ruling change).

## 10. What this document is not

It is not a proposal to change judging, verdicts, the council,
the rubric, or any standing ruling. It is not advocacy for Jev.
It is a study of one possible tool for one identified
limitation, prepared so the curator can rule with the costs,
risks, and alternatives in view.

---

*Sources consulted 2026-10-19: TypeSafe AI Jev documentation
(via GitHub mirror), DataCamp Jev tutorial, Forbes
(2026-09-22), Firecrawl and Requesty technical write-ups,
OpenRouter model listings. Internal references:
research/docs/how-albums-are-selected.md §9 (front-loading
bias, candidate-pool mechanism); canon-drip-operations skill
(drip ritual rulings, free-choice selection ruling).*
