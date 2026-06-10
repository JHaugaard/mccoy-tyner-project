# Session Context

## Current Focus
Phase 3 — Data Model & Schema Design (data-platforming). Reviewed the live Postgres infrastructure,
decided where this project's data lives, designed the full relational schema contract-first, and
spec'd a Canon Orchestrator agent to compress John's Phase 1 selection work.

## Honcho Context
- Phase 1 specialist briefs (Hard Bop, Cool Jazz, Modal Jazz) written; agents NOT yet dispatched.
- Post-Bop absorbed into Modal agent (Option A) — confirmed this session.
- Project scope: ~100 canonical post-bebop / pre-fusion albums, no Free Jazz, no style quotas.

## Key Decisions
- **DB home:** project gets its own schema in the shared Postgres on vps8 (127.0.0.1:5433) — not a
  standalone database, not mixed into existing tables. Mirrors the `_foundry` pattern.
- **Namespace:** `_jazzcanon` (decided). `mccoy-tyner` stays the working codename. Product name still open.
- **Semantic search:** two engines — pgvector (similarity/discovery) + relational/recursive (six-degrees,
  timelines). Static export for a simple app; live NL backend deferred to Phase 4.
- **Embedding model:** local `nomic-embed-text` (768) on vps4 — working-first, fully reversible.
- **Canon Orchestrator:** a decision-compression layer (not god-mode); emits a tiered ballot, never sets `include`.
- **Schema design:** unified `person` entity; epistemic + citation provenance on every fact; person
  identity-resolution flagged as Phase 4 ingest work.
- Fixed a stale port (5432 → 5433) in `~/.claude/rules/intent-defaults.md`.

## Notes
- Session started: 2026-06-10
- Deliverables produced: `research/agent-briefs/canon-orchestrator-brief.md`, `docs/schema.md`,
  `data/schema.sql`, `data/seed.json`, `data/data-platform-handoff.json`; refined `plan-v1.md` (v1.2),
  `conventions.md` (v1.1), and the Phase 1 task plan.
- Project memories saved: `foundation-decisions.md`, `canon-orchestrator.md` (+ MEMORY.md index).
- Work is written but UNCOMMITTED — John to decide whether to commit.
- Session indexed as `jazz-data-platforming` (uuid fcc33e4f-9a0f-41ce-9d52-9fb7379f0fce).

## Session Status
Completed: 2026-06-10
Servers cleaned: none added this session (baseline 6-tool config untouched)
