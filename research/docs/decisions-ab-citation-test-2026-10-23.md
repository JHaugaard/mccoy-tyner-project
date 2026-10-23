# A:B Test 2 — Citation-Audit Nouls on a Known-Defect Dossier

2026-10-23 · McCoy · authorized by John, same day ("Let's run Test 2, again as an A:B.")

Companion to `decisions-ab-style-test-2026-10-23.md` (Test 1). Same two models, same OpenRouter Decisions API endpoint, same day.

## What was tested

Test 2 from the Jev evaluation: can a decision model audit a dossier's evidence hygiene — does the rationale assert only what the source map carries? Subject: the archived *Black Saint and the Sinner Lady* dossier (`research/candidates-archive/charles-mingus-the-black-saint-and-the-sinner-lady-1963.json`), the project's documented defect case — its rationale asserts Penguin Guide four-stars-plus-Crown, an AllMusic five-star rave, five stars from the Rolling Stone Jazz Record Guide, and a place in *1001 Albums You Must Hear Before You Die*, while its source map (S1–S6) contains only Wikipedia (liner-notes personnel), an AllMusic *credits* page for a combined reissue, a Mingus-site session-date note, MusicBrainz, Apple Music, and a weak Facebook post. Not one accolade is evidenced.

Ten atomic claims were drawn from the dossier and hand-labeled with ground truth (`research/citation-ab-claims.json`): five evidenced (C1–C5: session date, personnel, label/catalog, Apple Music, MusicBrainz), four unevidenced accolades (C6–C9, the defect), and one deliberate strict-reading edge case (C10: "single continuous through-composed suite" — the map evidences the eleven-piece ensemble but no entry describes the work's form). Each model saw the same Noul per claim against the source map alone: "Is the claim explicitly evidenced by at least one entry in the dossier's source map? Judge only whether the source map carries this claim — not whether the claim is true in the world." All figures below are obs from the raw responses (`research/citation-ab-results-*.jsonl`).

## Results — p(yes) per claim

| Claim | Truth | Jev 1.14 | Decisions (Luna) |
|---|---|---|---|
| C1 session date, Jan 20 1963 | evidenced | 0.50 | **0.08 ✗** |
| C2 personnel (Byard/Richmond/Ervin/Mariano/Richardson) | evidenced | 0.56 | **0.01 ✗** |
| C3 Impulse! AS-35 | evidenced | 0.98 | 0.99 |
| C4 listed on Apple Music | evidenced | 0.98 | 1.00 |
| C5 MusicBrainz release group | evidenced | 0.90 | 1.00 |
| C6 Penguin Guide 4★ + Crown | **not evidenced** | 0.01 | 0.00 |
| C7 AllMusic 5★ + quote | **not evidenced** | 0.03 | 0.00 |
| C8 Rolling Stone Jazz Record Guide 5★ | **not evidenced** | 0.01 | 0.00 |
| C9 1001 Albums book | **not evidenced** | 0.01 | 0.00 |
| C10 through-composed suite (edge) | not evidenced | 0.06 | 0.00 |

Cost: 10 claims × 2 models = $0.0008 total. Wall clock: seconds.

## Reading

**Both models catch the defect class perfectly.** C6–C9 — the exact GATHER failure the audit role exists to catch — score 0.00–0.03 under both models. C7 deserves a note: S2 *is* an AllMusic page, so a lazy audit could have waved the five-star claim through; both models read the map entry's description ("credits; combined 2011 reissue") and correctly ruled that a credits page does not evidence a rating. That is the subtle case, and both passed it.

**The separation tells the models apart.** Jev's outputs split cleanly: evidenced claims ≥0.50, unevidenced ≤0.06 — a wide, empty middle where a threshold rule lives comfortably. It was lukewarm on C1 (0.50, likely the "single session" nuance) and C2 (0.56) but landed on the right side. Luna saturated at the extremes (0.00/1.00 everywhere except C1/C3) and — the important failure — *false-rejected two genuinely evidenced claims*: the session date (0.08, despite S3 being titled "session date confirmation") and the personnel list (0.01, despite S1 being titled "personnel from original liner notes"). In an audit role those are false alarms: good dossiers sent back for homework.

**This matches Test 1's signature.** Luna is often stronger on the merits but overconfident; Jev's probabilities behave like measurements. For a flag-for-review layer, behaved probabilities are the product. Consistent across two very different tasks now (inf — two data points, not a law).

## Caveats

Ten claims on one dossier is a smoke test, not a validated instrument. Ground truth is my hand-labeling under the house rule (a claim is evidenced only if a source-map entry's description explicitly carries it); C10's "false" is a strictness choice a reasonable auditor could argue. The models judged the *source map's descriptions*, not the sources themselves — a map with dishonest descriptions would defeat both. That is a dossier-integrity problem, not a model problem, and it is why the audit belongs inside staging, not instead of gathering discipline.

## Recommendation

The citation audit is viable and should be built as a staging-time flag: every rationale-level claim in a dossier gets a Jev Noul against the source map; p < 0.5 sends the claim back for a source token or a downgrade to `inf`, and the flag lands in the review card, never silently. Use Jev for it (clean separation, no observed false rejections); Luna's saturation at 0/1 leaves no threshold to tune and it false-flagged supported claims here. Before adoption: extend the claim set to three or four clean dossiers to measure the false-alarm rate properly — that extension is the natural next test when John rules.
