# Session Context

## Current Focus

Between-phase refinement (Phase 3 → Phase 4). Five directives from John:

1. **Architect for the future** — structure in place to grow beyond 100 albums (more albums, artists, styles) without rework.
2. **Treat the 100-album project as a robust, well-architected proof of concept** — built to extend without practical limits, usable for years in unforeseen ways.
3. **Research agents as first-class tools** — each of the 3 style specialists (and all project agents) well-spec'd, named, standalone, and scoped to the best-suited Claude model.
4. **Evaluate an API** for the database/data resource (blends into Phase 4).
5. **All agents created so far become first-class Claude Agents** that function outside the confines of this project.

Goal: end-to-end plan through Phase 4 rock solid, capable of being run with a one-shot prompt. Still in planning/architecting — no implementation.

## Honcho Context

Dialectic chat timed out (8s plugin limit); hook + curation log used instead. Relevant from curation log (2026-06-09 session): three parallel style specialists chosen over one general researcher; priority field (must_have/strong/consider) enables advocacy step; advocacy workflow planned but not written — Canon Orchestrator brief has since absorbed this. Subagent model preference on record: Haiku for mechanical/parallel work, Sonnet/Opus for judgment.

## Key Decisions

All four decision points approved as recommended (AskUserQuestion, 2026-06-11):

- **Collections now** — `collection` + `album_collection` added (schema v1.1); the ~100 canon = first collection `core-canon`. `album.year` CHECK widened 1940–1990 → 1900–2100.
- **Five named standalone agents** in `~/.claude/agents/`: jazz-hard-bop-researcher, jazz-cool-jazz-researcher, jazz-modal-jazz-researcher, jazz-canon-orchestrator (Opus), jazz-personnel-researcher (Sonnet). Self-contained, dispatch-parameterized; briefs marked superseded.
- **Staged serving** — static export default; PostgREST read-only over `_jazzcanon` views when a live consumer appears; MCP server banked. Views = the API contract.
- **Model posture** — Opus where research judgment concentrates; Sonnet for high-volume extraction; Haiku for mechanical steps.
- Plan bumped to v1.4; `docs/runbook.md` created (Segments A–D, gates as hard stops).
- Stale `~/.claude/agents/jazz-researcher.md` flagged for John to delete (predates specialist design).

## Notes

- Session started: 2026-06-11
- Current state: plan v1.3, Phase 3 schema design complete (docs/schema.md, data/schema.sql), 5 agent briefs in research/agent-briefs/, no agents dispatched yet
- Existing global agent ~/.claude/agents/jazz-researcher.md is a stale generalist (predates the 3-specialist design, references moved/missing files: plan-v1.md at root, initial.questions.md) — needs replacement or retirement as part of point 5
- Prior session (2026-06-10) deliverables were committed: 6d66e62, a8cbcf6

## Session Status
Completed: 2026-06-11
Servers cleaned: none added this session
Honcho curation: 4 items written (collections-as-platform-extension, model posture confirmed, staged serving posture, runbook gate pattern); 3 rejected (timing/date-bound, stale agent cleanup task, bug fix already captured)
