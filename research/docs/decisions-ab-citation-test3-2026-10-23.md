# A:B Test 3 — Citation-Audit False-Alarm Rate on Clean Dossiers

2026-10-23 · McCoy · authorized by John, same day ("Let's run Test 3 now, then we'll have testing behind us for now.")

Completes the series begun in `decisions-ab-style-test-2026-10-23.md` (Test 1) and `decisions-ab-citation-test-2026-10-23.md` (Test 2). Same two models, same endpoint, same Noul question wording as Test 2.

## What was tested

Test 2 showed both models catch the planted defect perfectly on one bad dossier. The open question was the other side of the ledger: how often does the audit flag claims that ARE evidenced — false alarms that would send healthy dossiers back for homework? Four archived dossiers with no known defects were drawn across eras and styles — Blakey's *Buhaina's Delight* (1963), Evans/Hall's *Undercurrent* (1962), Alice Coltrane's *Journey in Satchidananda* (1970), Ervin's *The Freedom Book* (1963) — and 20 claims hand-labeled against their source maps (`research/citation-ab-claims-test3.json`): 10 evidenced, 10 not. The 10 unevidenced split into CLEAN cases (no such source exists — Pitchfork, Rolling Stone, Penguin claims) and EDGE cases (the source exists but its map description is sparse — a bare "Wikipedia album article" asked to carry a rating). The edges were deliberate: they measure how much the audit depends on the richness of the map's descriptions, not just on the model. Flag threshold: p < 0.5. All figures obs from `research/citation-ab-results-test3-*.jsonl`.

## Scoreboard at threshold 0.5

| | Jev 1.14 | Decisions (Luna) |
|---|---|---|
| Unevidenced claims correctly flagged (defect catch) | **10/10** | **10/10** |
| Evidenced claims falsely flagged (false alarms) | 4/10 | **9/10** |
| Combined with Test 2 — defect catch | 14/14 | 14/14 |
| Combined with Test 2 — false alarms | 4/15 | 11/15 |

Luna flagged every evidenced claim except B1 (the Van Gelder date, p=1.0) — an unusable false-alarm rate. Jev's four false alarms: B2 (release date + catalog numbers, 0.15), B4 (the three Shorter compositions, 0.09), A5 (instrumentation blend, 0.15), F1 (the Ervin quartet, 0.25).

## The honest paragraph

Jev's false alarms are not random. B4 asked "S2 carries a track list" to evidence "these three tracks are Shorter *compositions*" — a track list is not composer attribution, and a case can be made that Jev's 0.09 was right and my label generous (my `why` is in the claims file for John to judge). B2, A5, F1 similarly sit on claims where the map's evidence is implied rather than explicit. The pattern, both directions: this instrument measures the *explicitness of the map*, and it is unforgiving about it (inf). Two consequences. First, the audit doubles as a map-quality check — a flag often means "the dossier's source description is thin," which is itself worth knowing before a dossier reaches John. Second, threshold is a real dial for Jev: at p < 0.1 the false-alarm count drops from 4 to 1 (only B4) while all 10 defect flags (max p = 0.38) stay flagged. Luna offers no such dial — its outputs saturate at 0/1 in both tests (obs).

Also observed: neither model overreached on B6 ("the canon already carries Moanin', Mosaic, Ugetsu, Free for All" — a claim about our own database). Both correctly ruled that no source-map entry can evidence it (Jev 0.12, Luna 0.00). Instruction-following held on the one claim designed to bait world-knowledge.

## Series verdict (Tests 1–3 combined)

- **Defect catch: 14/14 both models, zero misses.** The Black Saint failure class is detectable, cheaply, every time we looked.
- **False alarms: Jev 4/15, Luna 11/15** at the 0.5 threshold; Jev tunable down to ~1/15 at 0.1 with no loss of defect catches in this sample.
- **Across three tasks now, the same temperament split (inf):** Luna is stronger on open knowledge (Test 1 accuracy) but saturates and false-alarms; Jev's probabilities are graded, strict, and steerable. For a flag-for-review layer, Jev is the instrument.

## Recommendation (final, for John's ruling)

Build the staging-time audit with Jev: one Noul per rationale-level claim against the dossier's source map, flags rendered on the review card with claim text and probability, nothing auto-edited. On threshold: no value separates perfectly in this sample — observed defects reach p=0.38 (U4) while observed false alarms go down to p=0.09 (B4). Since a flag costs John a glance and a missed defect costs a dossier's integrity, bias toward catching: flag at p < 0.5, accept the ~4-in-15 false-alarm rate, and revisit the dial after a few weeks of live flags. Estimated cost: under one cent per drip day. Luna stays in reserve as the second voice for style concordance (Test 1) — its temperament disqualifies it as the auditor. The enumeration/pool work is untouched by these results and awaits its own ruling.
