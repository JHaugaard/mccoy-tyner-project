---
title: Canon-council prosecutor/defense A/B — 2026-08-20
date: 2026-08-20
type: evaluation
status: complete — John to rule adopt/discard
---

# Canon-council prosecutor/defense A/B

**Question:** does giving the canon-council's two reference voices assigned
sides (one prosecutes, one defends) produce better ballots than the current
design, where both voices see the same both-sides brief?

**Design:** 2x2 over 5 dossiers (control + two treatment arms, roles swapped).
Reference models: DeepSeek V4-Pro + Gemini 3.1 Pro Preview (Nous). Aggregator:
kimi-k3. Same rubric, temps, ballot shape throughout. Control re-ran fresh
(historical ballots predate the kimi-k3 aggregator; they were aggregated by
gpt-5.6-terra). No staging, no DB writes.

**Dossiers** (all archived, all with John's verdict where present):
Black Saint (consensus_core, included) · Extensions (contested, included) ·
Bright Size Life (scope_call, included) · Head Hunters (scope_call, included) ·
Heliocentric Worlds Vol.1 (scope_call/consider, never landed).

---

## The method defect the experiment exposed (production finding)

Round 1 self-destructed and, in doing so, exposed a defect in the *live drip*:
DeepSeek V4-Pro is a reasoning model whose reasoning tokens count against the
preset's `reference_max_tokens: 2000`. On dense dossiers it occasionally burned
the whole budget thinking and returned `finish_reason=length` with **empty
content** — which `moa_loop` then placeholder-fills as the literal string
`"(empty response)"`. The live-check in canon-council.py was
`text and text.strip()`, and `"(empty response)"` is non-empty, so a dead
reference was counted as answered. Result: 12 of 15 round-1 councils were
single-voice councils masquerading as two-voice, and the drip has been able to
stage them silently.

**Remediation applied (ratification requested):**
- Both scripts now carry `--ref-max-tokens` (override) and a guard that treats
  `"(empty response)"` / `"[failed"` as unanswered.
- BUT the drip invokes canon-council.py with no flag, so it still runs at 2000.
  The actual production fix is raising the preset's `reference_max_tokens`
  from 2000 → 8000 in the mccoy profile config. Left for John to rule.

Round 2 re-ran all 15 councils at 8000 tokens: zero empty responses, all
ballots parsed, both references live in every council.

---

## Results

| Dossier | Historical / John | Control | TreatA (DS=pros) | TreatB (Gem=pros) |
|---|---|---|---|---|
| Black Saint | consensus_core / included | consensus_core·must_have | contested·must_have | contested·strong |
| Extensions | contested / included | contested·strong | contested·strong | contested·strong |
| Bright Size Life | scope_call / included | scope_call·strong | scope_call·strong | scope_call·strong |
| Head Hunters | scope_call·must_have / included | scope_call·must_have | scope_call·strong | scope_call·strong |
| Heliocentric V1 | scope_call·consider / unbriefed | scope_call·consider | scope_call·consider | contested·consider |

Disagreement recorded: control 2/5, adversarial 8/10.

---

## Scoring

**1. Tier/priority match vs John's verdict (historical ≈ John, 5/5 included).**
Control matched all five historical tiers and priorities. Adversarial drifted
on two tiers (Black Saint → contested in both arms; Heliocentric → contested in
treatB) and demoted Head Hunters must_have → strong in both arms. Adversarial
is systematically **more conservative**; its errors are false-negative
(demoting strong candidates), never false-positive.

**2. New-argument yield.** Adversarial reliably adds one species of argument the
control produces only weakly: the *consensus-evidence audit* — enumerating that
a dossier's sources are discographic/metadata (AllMusic/Wikipedia/Discogs/
MusicBrainz/iTunes) and that no canon-making citation (Penguin, DownBeat,
JazzTimes, NPR) actually appears in the source map. This is the single
consistent, durable new contribution.

**3. Invented claims.** Low in both arms. Spot-checked the load-bearing case:
the Black Saint treatment's central claim — that the rationale asserts
Penguin Crown / AllMusic 5★ / Rolling Stone 5★ / 1001 Albums but none appears
in S1–S6 — is **true** (rationale text vs source map verified). It is a real
data-hygiene defect, not a hallucination. No fabricated facts found.

**4. Disagreement fidelity.** 8/10 vs 2/5; the aggregator's `disagreement`
fields are substantive and correctly attribute the split to specific sides.

---

## Reading

The adversarial design works, but its effect is **conservative tier attrition
driven by a legitimate-but-misplaced signal.** The prosecution keeps auditing
*whether the dossier's sources prove the rubric's #1 signal*, then lets that
audit drive the tier — when the rubric intends tier to reflect canonical
*status*, not dossier completeness. The clearest case: Black Saint is a
consensus masterpiece the canon already includes; the adversarial arms demoted
it to contested because its *dossier* under-cites it, not because the
consensus is weak. The honesty thread that catches this already exists in the
control prompt ("where sourcing is thin, say so") — the control caught the
contaminated S2 reissue on its own; it just didn't rachet the tier.

**Recommendation:**
- Do **not** adopt prosecution/defense as the drip default: it buys stronger
  disagreement at the cost of tier drift on exactly the candidates the canon
  wants to catch cleanly.
- Take the one durable lesson upstream: **consensus claims must be cited in the
  dossier's source map, not asserted in the rationale.** That's a GATHER-step
  requirement plus a cheap pre-judge check (ballot already warns on thin
  sourcing), not a council redesign.
- Keep the adversarial script as a non-default tool for contested/boundary
  cases where a harder prosecution is wanted.
- Repair Black Saint's dossier sourcing (its accolades are real and deserve
  actual citations) regardless of the above.

Artifacts: ballots + full reference arguments in
`~/temporary/canon-council-ab-2026-08-20/run2/`. Variant script:
`~/.hermes/profiles/mccoy/scripts/canon-council-adversarial.py`.