# Canon Orchestrator — Agent Brief

> **Superseded 2026-06-11** by the first-class agent `~/.claude/agents/jazz-canon-orchestrator.md` (self-contained, model-scoped: Opus). This brief is retained as design history; the agent file is canonical.

**Phase:** 1 (Canon Assembly)
**Role type:** Orchestrator / synthesis — runs *after* the three style specialists, *before* John's selection gate.
**Status:** Spec — not yet dispatched. No agents launched and no albums selected as of 2026-06-10.

---

## Why this agent exists

The original Phase 1 flow was: three specialists compile candidate lists → John reads ~150–250 raw
candidates and culls to ~100. John is a curious lover of jazz, not a jazz professional, and reading
hundreds of raw records is the slowest, least leveraged use of his judgment.

The Orchestrator fixes the *right* bottleneck. It does **not** replace John's taste. There is no
ground truth the canon converges toward — the target is John's preference, which no agent can see
better than he can. So the Orchestrator is a **decision-compression layer**: it absorbs the
mechanical and knowledge-bound 90% (dedup, overlap resolution, scope arbitration, marshalling the
case for each contested album) and hands John a small, pre-argued **ballot** — the irreducible 10%
that is genuinely his to decide.

**Design principle:** delegate the knowledge-bound and clerical work; reserve the taste-bound and
scope-defining decisions for John. The Orchestrator makes John faster at his job, not absent from it.

### What this agent is NOT

- **NOT a god-mode selector.** It must never free-select albums from its own parametric memory.
  That is exactly the ungrounded, hallucination-prone mode this project was built to avoid. Every
  album it advances traces to a specialist's sourced record. Canon selection is held to the same
  source-grounded, epistemic-labelled bar as everything else in this project.
- **NOT the final authority.** It proposes; John disposes. Its output is a ballot, not a canon.
- **NOT a debate generator.** Multi-agent "give-and-take" must stay pinned to real decisions
  (dedup, overlap, scope, ranking the margin). Deliberation for its own sake — agents performing
  agreement, padding justifications — is waste. If a round changes no outcome, skip it.

---

## Inputs

| Input | Source | Notes |
|-------|--------|-------|
| Hard Bop candidates | `research/hard-bop-candidates.md` | Specialist output, candidate-schema format |
| Cool Jazz candidates | `research/cool-jazz-candidates.md` | Specialist output |
| Modal Jazz candidates | `research/modal-jazz-candidates.md` | Specialist output (absorbs Post-Bop) |
| Candidate schema | `research/candidate-schema.md` | The record contract — fields it consumes |
| Genre definitions | `docs/genre-definitions.md` | Scope authority (post-bop / pre-fusion / no free jazz) |
| Conventions | `docs/conventions.md` | Epistemic labelling standard |

The Orchestrator consumes the existing `candidate-schema` fields — **no new fields are added to the
specialists' contract.** Its raw material is already there: `priority` (`must_have` / `strong` /
`consider`), `overlap_risk`, `scope_flag`, `sources`, `epistemic`, `rationale`.

---

## Round structure

A bounded deliberation — at most two specialist touchpoints, then assembly. The Orchestrator runs
the rounds; specialists re-engage only where their judgment is actually contested.

### Round 0 — Merge & deduplicate (Orchestrator, no specialists)

- Match records across the three files on `(artist, album, year)`. Treat near-matches
  (reissue titles, year drift of ±1 between recording/release) as candidates for the same album
  and merge them, recording the merge in `merge_notes`.
- For each merged album, union the `sources`, collect every specialist's `priority` vote, and
  union `style_tags`. Keep the highest-confidence `epistemic`.
- Produce the **tier assignment** (see Tiers below).

### Round 1 — Surface the contested set (Orchestrator → specialists)

- The Orchestrator identifies the **contested margin**: albums that are not clear consensus-core
  and not clear-cut excludes. Triggers for "contested": single-source; `priority: consider`;
  any non-empty `scope_flag`; non-empty `overlap_risk`; or a style disagreement between specialists.
- For each contested album, the Orchestrator drafts a neutral **case-for / case-against** (one
  sentence each), grounded strictly in the specialists' cited sources and rationale — never in
  outside knowledge.
- Where an album sits on a style border, the Orchestrator asks the relevant specialist(s) for a
  one-line **rebuttal or concession**: "Cut candidate? Defend or release." This is the only
  give-and-take, and it is scoped to genuine disputes.

### Round 2 — Assemble the ballot (Orchestrator, no specialists)

- Fold specialist rebuttals into each contested record.
- Emit the **decision ballot** (schema below) and the human-readable `canon-synthesis.md`.
- Stop. John decides at the gate.

> If Round 1 surfaces no genuine disputes (no rebuttals would change a tier), collapse to Round 0 →
> Round 2. Do not manufacture a deliberation.

---

## Tiers

The Orchestrator sorts every merged album into exactly one tier. Tiers are what compress John's work.

| Tier | Definition | What John does |
|------|------------|----------------|
| `consensus_core` | 3+ independent sources **and** no scope/overlap flags **and** ≥2 specialists rate `must_have`/`strong` | Rubber-stamp the block; spot-check only |
| `contested` | Anything with a single source, `priority: consider`, a `scope_flag`, an `overlap_risk`, or a style disagreement | Rule album-by-album on a pre-argued ballot |
| `scope_call` | Album whose in/out status turns on a genre-boundary judgment (too-bebop / too-free / too-fusion / late-modal eligibility) | Decide explicitly — this is a taste/definition call John owns |
| `exclude_suggested` | Orchestrator judges out of scope or too weakly sourced to advance | Skim; override if John disagrees |

`consensus_core` should land near the target count on its own (~60–70 of the ~100). The `contested`
and `scope_call` tiers are where John spends his attention — a few dozen pre-argued decisions, not
hundreds of raw records.

---

## Output 1 — Decision ballot (`data/canon-ballot.json`)

Machine-readable, drives John's review. One object, with albums grouped by tier. Each album:

```json
{
  "id": "lee-morgan-the-sidewinder-1964",
  "artist": "Lee Morgan",
  "album": "The Sidewinder",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "tier": "contested",
  "source_count": 2,
  "sources": ["hard-bop:S1", "hard-bop:S3"],
  "priority_votes": { "hard-bop": "strong" },
  "epistemic": "obs",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "case_for": "Title track is a defining soul-jazz crossover; Penguin Guide core (hard-bop:S1).",
  "case_against": "Borderline soul-jazz groove tips commercial; only two sources advanced it.",
  "specialist_rebuttal": "Hard Bop: defend — pre-fusion, swings with structure, canonical Blue Note.",
  "merge_notes": "",
  "orchestrator_recommendation": "include",
  "include": null
}
```

### Ballot field rules

| Field | Rule |
|-------|------|
| `tier` | One of `consensus_core` \| `contested` \| `scope_call` \| `exclude_suggested`. |
| `source_count` | Count of distinct sources across all specialists after merge. |
| `priority_votes` | Object: each specialist that listed the album → its `priority` value. |
| `case_for` / `case_against` | One sentence each, **grounded only in specialist sources/rationale**. Cite source IDs. Required for `contested` and `scope_call`; may be empty for `consensus_core`. |
| `specialist_rebuttal` | Round 1 defense/concession, prefixed with the specialist name. Empty if not contested. |
| `merge_notes` | How duplicate records were reconciled, if any. Empty otherwise. |
| `orchestrator_recommendation` | `include` \| `exclude` \| `defer` — advisory only. Never sets `include`. |
| `include` | **Always `null` from the Orchestrator.** John sets `true`/`false` at the gate. |

The Orchestrator must never write a non-null `include`. That field is John's alone — it is the
boundary between proposal and decision.

## Output 2 — Synthesis narrative (`research/canon-synthesis.md`)

The human-readable companion to the ballot. Follows the structure already specified in the Phase 1
task plan (`docs/superpowers/plans/2026-06-09-phase1-canon-list.md`, Task 6), plus:

- **Tier counts** table (how many albums in each tier; projected canon size from `consensus_core`).
- **Scope calls** section — every `scope_call` album with the boundary question stated plainly.
- **What I did not decide** — an explicit list of everything handed to John, so nothing is silently
  resolved by the agent.

---

## Guardrails (non-negotiable)

1. **Source-grounded only.** Never advance, argue for, or rank an album using knowledge not present
   in a specialist's cited sources. If the specialists did not surface it, it does not exist to the
   Orchestrator.
2. **`include` stays `null`.** The Orchestrator proposes; John disposes.
3. **No invented albums, years, labels, or personnel.** Pass through specialist data; flag conflicts
   in `merge_notes`, never paper over them.
4. **Preserve dissent.** When specialists disagree on style or scope, record both positions — do not
   collapse to one.
5. **No deliberation theatre.** A round that changes no tier is skipped. Justifications are one
   sentence, sourced, and decision-relevant.
6. **Scope authority is `docs/genre-definitions.md`.** Boundary calls cite it; genuine judgment calls
   go to John as `scope_call`, never auto-resolved.

---

## Where it runs

True live agent-to-agent messaging (Agent Teams: TeamCreate / SendMessage) is CLI-only and unreliable
in John's VS Code. The clean fit is a **Workflow**: the Orchestrator logic lives in a deterministic
script; specialists run as stateless workers across the bounded rounds (compile → surface contested →
rebut → assemble). This delivers the give-and-take without fragile live-team machinery. Implementation
harness is a Phase 1-dispatch decision, not settled here.

---

## Success criterion

John's Phase 1 review collapses from "read ~200 raw records and decide everything" to "rubber-stamp
~65 consensus albums and rule on ~40 pre-argued decisions." Same curatorial authority, a fraction of
the clerical load — and every advanced album still traces to a cited source.
