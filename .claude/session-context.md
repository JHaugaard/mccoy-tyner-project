# Session Context

## Session Name
jazz-canon-app

## Current Focus
Phase 5B — The Public App. Stack decision session first; implementation follows.
Goal this session: produce a Claude/Kimi-neutral app spec that can be presented to both Claude Code Opus 4.8 and Kimi K2.7 for independent stack selection and first-draft implementation.

Side question: is the A/B testing phase (data platform, Kimi twin) done and settled?

## Honcho Context
- Phase 4 complete (2026-06-26): 100 albums, 535 persons, 627 performances in `_jazzcanon` on vps8-core. All enriched: MBIDs, Apple IDs (97/100), catalog numbers, cover art, embeddings. Cannonball duplicate merged; identity resolution clean.
- Phase 5 split: 5A = Hermes admin profile (separate build, not here); 5B = public discovery app (this track).
- Stack decision is the only gate before any Phase 5B build work.
- Hero feature: Personnel Network force-directed graph (D3.js force simulation, `v_sideman_network`).
- Core value proposition (John's words): "Being able to easily find the Paul Chambers nugget is just what I want."
- Execution preference: slow/iterative, human-gated. Do not pitch full-automation runs.
- A/B wall rule: Kimi twin repo (`mccoy-tyner-kc`) is read-only from this side; raw artifacts must stay pristine.
- Stack candidates: Svelte (recommended), React, or static HTML + D3. Hosting: Cloudflare Pages or vps2 + PostgREST.

## Key Decisions
- Hermes admin profile replaces coded admin site (decided 2026-06-26, jazz-canon-extras session)
- Growth loop: fresh JSON batch files in `data/batches/`, not append-with-flags
- Data Platforming First scaffold packaged for reuse in idea-foundry-vault

## Open Items (not blocking)
- 3 null Apple Music IDs
- 9 sessions without studio
- Vocal sub-collection (June Christy, Mel Tormé, Shelly Manne) — deferred

## Notes
- Session started: 2026-06-26
- Session name: jazz-canon-app
- UI reference material: `research/ui-reference/`
- Phase 5 plan: `docs/phase5-and-beyond.md`
- Status doc: `.docs/status.md`
