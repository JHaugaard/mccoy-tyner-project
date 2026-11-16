---
title: Canon-council Mistral Large 4 A/B — 2026-11-16
date: 2026-11-16
type: evaluation
status: complete — quality acceptance withheld; extended trial recommended
---

# Canon-council Mistral Large 4 A/B

## Question and scope

Does replacing `nous:minimax/minimax-m3` with `nous:mistralai/mistral-large-4-0` improve the council's independent judgment, factual reliability, and productive disagreement without disturbing ballot delivery or rubric calibration?

John authorized a bounded two-dossier before/after rehearsal. @the-super changed only the first reference model and route-verified Mistral; Gemini 4 Hydrogen, GPT-6.1 Sol, prompts, and other preset settings remained unchanged. The rehearsals used `canon-council.py --raw` on *Thelonious Himself* and *Return to Forever*. No ballot was attached to either dossier, nothing was staged, and both input hashes remained identical before and after. The-super separately noted that preset normalization drops the stored token-limit fields; that pre-existing behavior was left untouched in both arms and is not evaluated as a model-quality variable here.

## Artifacts

Raw ballots and full reference arguments are preserved in `/home/john/temporary/canon-council-mistral-large-4-ab-2026-11-16/`, with `.before.` and `.after.` filenames for `thelonious-himself` and `return-to-forever`.

Input SHA-256 values, unchanged across the rehearsals:

- *Thelonious Himself*: `16840ce0b9e185d122d5494962feb158447f6d3469f509e8c465b98bb7b2a1b1`
- *Return to Forever*: `f5efa1d5d9ee077f51deb751eb66e555f861b2d4d63d1af31a0b991d04f2c3e0`

## Delivery and ballot stability — obs

All four councils exited 0 with 2/2 references answered and valid aggregator JSON. The final tier, priority, and confidence did not change in either case:

| Dossier | MiniMax + Hydrogen | Mistral + Hydrogen |
|---|---|---|
| *Thelonious Himself* | `consensus_core / strong / high` | `consensus_core / strong / high` |
| *Return to Forever* | `scope_call / strong / high` | `scope_call / strong / high` |

The final ballots' substantive reasoning remained sound. Mistral's incorrect *Solo Monk* date was explicitly identified as an error by the aggregator, not adopted as fact; its unsupported American-availability assertion was not carried into the final recommendation. On *Return to Forever*, the aggregator correctly distinguished the historical split recorded in the supplied dossier from the current references' shared `scope_call / strong` judgment.

## Factual reliability — obs

Mistral did **not** pass a clean factual-reliability gate on *Thelonious Himself*. It called *Solo Monk* a 1959 album; the actual record is from 1965, recorded in 1964–65. It also turned the dossier's unsupported first-American-availability formulation into the categorical claim that this was "the first solo Monk an American listener could actually walk into a store and buy." Baseline MiniMax handled that formulation more carefully, saying the broader claim required sourcing. Sources: Mistral after-reference, lines 9 and 17; the after-ballot's correction; [Solo Monk](https://en.wikipedia.org/wiki/Solo_Monk).

MiniMax was not clean on *Return to Forever*. It offered a supposed dossier correction saying that "Sometime Ago" is by Miles Davis. ECM instead identifies "Sometime Ago" as a Corea theme introduced on *Piano Improvisations Vol. 1*, and Corea's official discography describes all four pieces on the album as his compositions. Mistral did not repeat that false correction. Sources: MiniMax before-reference, line 16; [ECM's Chick Corea account](https://ecmrecords.com/artists/chick-corea/); [Corea's official album page](https://chickcorea.com/discography/return-to-forever/).

Mistral improved the ratings-source attribution on *Return to Forever*: it correctly located the reported AllMusic, Rolling Stone, and Penguin ratings in S1 rather than assigning them directly to S2. Its treatment of S2 as metadata/credits rather than a directly checked review matches the dossier's source description. This is a real source-fidelity gain, but not enough to erase the Monk errors.

Both models repeated or reshaped the dossier's broader Miles-circle lineage language around Stanley Clarke. That is a shared GATHER-to-JUDGE propagation problem, not evidence of a Mistral-specific regression.

## Independent judgment and disagreement — obs / inf

Neither arm produced a substantive tier or priority split on these two dossiers. Both pairs of references independently reached the same verdicts while still supplying genuine counterarguments and source-hygiene objections. Mistral therefore does not show an agreement-collapse problem, but it also did not supply a distinctive tier challenge in this sample.

The before/after ballots contain different `disagreement` text, but that text is mostly factual correction and characterization of the historical ballot embedded in the dossier, not new productive disagreement between the live judges. It should not be scored as an improvement in panel diversity.

## Recommendation

**Quality acceptance is withheld. My recommendation is an extended, explicitly unratified trial rather than immediate adoption or immediate rollback.**

Immediate adoption is rejected because Mistral introduced a verifiably wrong album date and repeated an unsupported availability claim; the original clean-acceptance condition was not met. Immediate rollback is rejected because delivery and final judgments were stable, the aggregator contained the errors, and MiniMax itself made a substantive false composer correction in the baseline. The two-dossier result is therefore inconclusive about net quality, not a demonstration that either reference is factually reliable.

The proposed next gate is three additional post-swap full-council rehearsals on *Impressions*, *Bass on Top*, and *Concierto*, saving raw references and comparing against their existing archived ballots. Accept Mistral only if all three return 2/2 references, valid ballots, no new unsupported factual assertion from Mistral, and rubric-grounded reasons for any tier or priority change. Roll back if another unsupported assertion appears, if one reaches the final ballot's substantive reasoning, or if delivery degrades. Extending the trial is a new decision for John, not a retroactive declaration that this two-dossier test passed.

## Limitations

Two non-deterministic councils per roster are enough to test routing and expose obvious reasoning defects, not to estimate hallucination rates or long-run panel behavior. The archived historical ballots do not preserve raw MiniMax arguments for the three proposed follow-up dossiers, so that extension would assess Mistral's raw arguments against existing final ballots rather than create three new matched MiniMax baselines. The council judges canonicity, never correctness; the source checks above are evaluation checks for this trial, not a new authority for any model panel over discographic evidence.
