# Status

## Where are we?

The planning and architecture work is complete through Phase 4. Nothing has been dispatched or implemented yet — no agents have run, no albums have been selected, no data has been loaded. What's been built is the complete blueprint.

Specifically, as of this session (2026-06-11):

- The **data schema** is fully designed and ready to apply (not yet in Postgres). It's in `data/schema.sql`. It was updated this session to add a `collection` table — the ~100-album canon will be the first named collection, but the structure supports adding more canons later without any database migration.
- The **five research agents** are now first-class, standalone Claude Agents living in `~/.claude/agents/`. Each one is self-contained — it knows its scope rules, output format, and epistemic discipline without needing to read any project files. The three style researchers and the Canon Orchestrator are scoped to Opus; the ten parallel personnel extractors are scoped to Sonnet.
- The **serving posture** is decided: static JSON export is the default (the web app needs no backend); a read-only PostgREST layer gets added only when a live consumer appears; an MCP server is banked for later agent-facing access.
- The **runbook** (`docs/runbook.md`) describes how to run each phase as a single paste-able prompt, with your decision gates as the only pauses. The plan is at version 1.4.

The old generalist agent `~/.claude/agents/jazz-researcher.md` is stale and should be deleted — it predates the three-specialist design and points to files that no longer exist. That's a one-line file delete when you're ready.

Everything in the project is written but **not yet committed to git** from this session.

## What's unresolved?

Only a few small things remain open:

- **Product name** — the database namespace is locked as `_jazzcanon`, the working codename is `mccoy-tyner`, but the public-facing name for the app is still open. Not urgent until Phase 5.
- **Embeddings scope** — keep vectors local to `_jazzcanon` (recommended, simplest), or also push album/person documents into the shared `_foundry` index for cross-project RAG? Phase 4 decision.
- **June 15 credit upgrade** — your Max plan doubles on June 15. The Segment A dispatch (four Opus agents running deep research) is a good candidate for post-June-15 timing.

## What's next?

Two small housekeeping items first:
1. Delete `~/.claude/agents/jazz-researcher.md` — it's the stale generalist agent that's been superseded.
2. Commit this session's work to git (plan v1.4, schema v1.1, five agent files, the runbook).

Then, when you're ready to run the canon research (ideally after June 15):

Open the runbook at `docs/runbook.md` and use the **Master one-shot prompt** at the bottom of Segment A. That fires the three style specialists in parallel, waits for them to finish, runs the Canon Orchestrator, and stops at your first decision gate — a tiered ballot showing the ~100 consensus albums plus the contested ones pre-argued for your review.
