# Status

## Where are we?

**The Jazz Canon database is fully built and ready for an app.** Phase 4 is complete: 100 albums, 535 musicians, 627 performances in `_jazzcanon` on vps8-core — all enriched with MusicBrainz IDs, Apple Music IDs (97/100), catalog numbers, cover art, semantic embeddings, studios, and production credits. The data is clean; the Cannonball duplicate is merged; identity resolution found nothing else to fix.

**The project architecture is also settled** beyond just the data. A dedicated session (jazz-canon-extras, 2026-06-26) worked through three open design questions before Phase 5 begins:

- **Admin layer**: Not a coded admin site. A Hermes Agent profile (`jazz-canon-admin`) accessed via Telegram or the Hermes CUI — inference-powered, Claude Sonnet 4.6 doing the thinking, with write access guarded by SOUL.md guardrails. Already proven: Hermes has read access to `_jazzcanon` via `_foundry_app` and it's fast. Build happens in a Hermes session, not here.

- **Growth loop for new albums**: Settled architecture — fresh JSON batch file per foray (`data/batches/`), not a growing append-with-flags file. The pipeline is: dispatch agent → batch file → John reviews → ingest → enrich → log in dispatch-ledger. Fully documented in `docs/growth-runbook.md`.

- **Data Platforming First scaffold**: The methodology developed across this whole project has been packaged for reuse. Three files now live in `idea-foundry-vault/areas/research/scaffold/` — methodology, new-project starter, and growth-runbook template. Future research corpus projects (economists, film, etc.) start ~40% done.

`docs/plan-v2.md` has been updated to reflect all of the above: Phase 5 is now correctly split into 5A (Hermes admin, separate build) and 5B (public discovery app, this project).

## What's unresolved?

**The Phase 5B stack decision** is the only real gate before any visible app work begins. Framework, serving model (static export vs PostgREST vs both), and hosting need to be chosen. The Personnel Network force-directed graph is the hero feature and the main constraint on stack selection. See `docs/phase5-and-beyond.md` § 5A.

The minor open items — 3 null Apple IDs, 9 sessions without studio, vocal sub-collection question — are all low priority and not blocking anything.

## What's next?

Two parallel tracks you can start in any order:

**Track A — Hermes admin profile**: Open a Hermes session, create the `jazz-canon-admin` profile, wire up the Telegram channel, draft SOUL.md with write-access guardrails. This is a Hermes build, not a Claude Code session.

**Track B — Phase 5B stack decision**: Read `docs/phase5-and-beyond.md` § 5A, review `research/ui-reference/`, and make the stack call. No code — just the decision. Once it's made, the build sequence is already laid out session by session.

The growth runbook (`docs/growth-runbook.md`) is ready to use whenever you want to add the next batch of albums.
