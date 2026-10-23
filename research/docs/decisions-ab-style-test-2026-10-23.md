# A:B Test — Decision Models vs. Curated Style Labels

2026-10-23 · McCoy · authorized by John, same day ("go on the A:B test … take it end-to-end")

## What was tested

Test 1 from the Jev evaluation, now run as a head-to-head: can a decision model recover the canon's own style labels from enumeration metadata alone? Each of the 297 published albums (`canon_status='included'`, verified against the live DB this morning) was presented to two models as a `state` object carrying only title, artist, year, label, and catalog number — the fields a future candidate-pool row would carry. Each model answered one Choice question over the 12 style codes actually in use in the canon (bebop, cool-jazz, hard-bop, soul-jazz, modal-jazz, post-bop, free-jazz, avant-garde-jazz, spiritual-jazz, european-jazz, fusion, jazz-rock), with the `_jazzcanon.style` descriptions as criteria. The instructions read: "Which single primary style best describes this jazz album? Judge the music on the record, not the artist's general reputation." Agreement with the curated `style_primary_id` is the score.

Both models were called through the same OpenRouter Decisions API (`POST /api/alpha/decisions`), differing only in the model string: `typesafe/jev-1.14` (served as snapshot jev-1.14-20261014) and `openai/gpt-6-luna-decisions` (snapshot -20261006). 297 calls per model, 594 total, zero failures, ~13 seconds of wall clock, total cost $0.0199. Harness: `scripts/style-ab-test.py`; ground truth: `research/style-ab-ground-truth.tsv`; raw responses: `research/style-ab-results-{typesafe-jev-1.14,openai-gpt-6-luna-decisions}.jsonl`. All figures below are obs from those files.

## Headline numbers

| Metric | Jev 1.14 | Decisions (GPT-6 Luna) |
|---|---|---|
| Top-1 agreement with canon | 184/297 = **62.0%** | 196/297 = **66.0%** |
| Truth in top 2 | 243/297 = 81.8% | 247/297 = 83.2% |
| Mean P(truth) | 0.474 | 0.619 |
| Mean confidence, all | 0.585 | 0.814 |
| Mean confidence when correct | 0.628 | 0.866 |
| Mean confidence when wrong | 0.517 | 0.713 |
| High-confidence (≥0.8) errors | **10** | **42** |
| Cost (297 calls) | $0.0086 | $0.0113 |
| Input tokens (297 calls) | 205,875 | 112,989 |

Cross-model: the two agree with each other on 195/297 (65.7%); where they agree, they match the canon 150/195 (76.9%). Jev was right where Luna was wrong 34 times; the reverse 46 times.

## Per-style breakdown (correct/total)

| Style | n | Jev | Luna |
|---|---|---|---|
| hard-bop | 109 | 63 | **92** |
| post-bop | 83 | **55** | 34 |
| cool-jazz | 38 | 33 | **34** |
| modal-jazz | 31 | 6 | **10** |
| soul-jazz | 11 | 10 | **9** |
| free-jazz | 8 | 5 | **6** |
| bebop | 7 | 7 | 7 |
| fusion | 4 | **4** | 3 |
| avant-garde-jazz | 2 | 0 | 0 |
| jazz-rock | 2 | 0 | 0 |
| jazz-funk | 1 | 0 | 0 |
| european-jazz | 1 | 1 | 1 |

Jev's largest confusion family is hard-bop → bebop (19) — it hears the 1952–55 Blue Note lineage as the founding idiom. Luna's is post-bop → hard-bop (27) — it steamrolls the eclectic 1960s into the harder bin, which is exactly where its hard-bop advantage comes from. Modal-jazz is the hardest category for both (6/31 and 10/31), scattering across post-bop, cool-jazz, and spiritual-jazz.

## The honesty paragraph

Some "errors" are defensible alternative labels, not model failure. Both models called Alice Coltrane's *Journey in Satchidananda* and *Ptah, the El Daoud* spiritual-jazz at 0.96–1.00 confidence where the canon files them modal-jazz — a label many discographers would endorse. Jev filed both *Amazing Bud Powell* volumes as bebop at 0.98–1.00 where the canon says hard-bop — a genuinely arguable call for 1952–54 Powell. The canon labels are curatorial judgments, and the gap between ~66% and 100% is partly the distance between two reasonable taxonomies, not two levels of competence. This test measures agreement with the house's filing system, which is precisely what a check layer needs — but it should not be read as "the models misjudge jazz a third of the time" (inf).

## What this means for the planned uses

**Style cross-check (the check-layer role): viable, and Jev is the better instrument for it (inf).** The job is not to label albums but to flag gatherer/DB disagreements for review. Jev's errors arrive carrying lower confidence (0.517 mean when wrong; only 10 errors ≥0.8), so a disagreement with a high-confidence Jev verdict is a strong review signal, and a low-confidence disagreement can be safely ignored. Luna is more often right but confidently wrong four times as often (42 errors ≥0.8, mean 0.713 when wrong) — its flags would cry wolf. TypeSafe's "calibrated decisions" training claim is consistent with what we observed (inf from our data, not vendor literature).

**Neither model is an authority.** At 62–66% top-1 against curated labels, neither output may ever write a style field. Both are cheap signals — which is all the candidate-pool architecture ever asked for. The design principle "score is a signal, never a gate" survives contact with data.

**The ensemble is the interesting number.** Where the two models agree, they are right 76.9% of the time; where they disagree (102 albums), the disagreement itself is a reliable "this album's style is genuinely contested" marker. A two-model concordance check on a dossier's declared style would cost about $0.00007 per candidate and would have flagged every Alice Coltrane filing in the canon for a second look.

**Cost and speed are non-issues.** The entire 297-album canon cost two cents and thirteen seconds. Even the 30,000-album pool triage at these rates is ~$1–2 per full pass per model.

## Caveats

One question, one pass, one draw — decision models are not documented as deterministic, and re-runs may wobble a point or two (unk). The state included label and catalog number, which leak style information (Blue Note → hard bop); that is deliberate — a pool row would carry them — but it means these numbers overstate what title/artist/year alone would do. The `~typesafe/jev-latest` alias currently resolves to the same snapshot we pinned; the pinned IDs above are the reproducibility anchor.

## Recommendation

Adopt Jev as the check-layer instrument where one model is wanted; keep Luna in reserve for the two-model concordance flag, which looks more valuable than either alone. Proceed to Test 2 (citation-audit Nouls on an archived dossier) when John rules. The pool-triage architecture is unaffected: this test neither strengthens nor weakens the case for enumeration, which was always about recall bias, not label accuracy.

---

*Reproduce: `OPENROUTER_API_KEY=… python3 scripts/style-ab-test.py --model typesafe/jev-1.14` (and `openai/gpt-6-luna-decisions`), then any JSONL-aware diff against `style-ab-ground-truth.tsv`. Ground truth snapshot: 297 included albums, 2026-10-23.*
