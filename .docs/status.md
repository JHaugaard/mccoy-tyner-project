# Status

## Where are we?

The jazz canon project is fully designed, the agents are built, and the first real run is ready to fire. Nothing has been dispatched yet — no albums gathered, no data loaded — but the blueprint is now executable, not just planned.

Concretely, since the last handoff a lot changed:

- **The plan grew up to v2.** The framing shifted from "pare down to 100" to "start with 100 and grow" — the canon is now a curated lens over a collection that can expand without rework. The plan and an executable runbook live at `docs/plan-v2.md` and `docs/runbook-v2.md`.
- **The research agents were merged.** The three style specialists (hard bop, cool jazz, modal) now do everything in one pass: pick the album AND gather its full personnel/sessions/tracks. They read a shared `docs/personnel-contract.md` for the personnel format, exclude albums already collected (a ledger), and learn from your past cull decisions (a cull-notes file). The runbook is "live" — its banner has been lifted.
- **Apple Music replaced Spotify.** You're an Apple person, Apple still serves preview clips (Spotify killed theirs), and you get full playback in your own tool as a subscriber. The schema gained an `apple_album_id` field; capture is free in the data phase via the iTunes Search API. You now have an Apple Developer account; the token-related keys have placeholders in `.env.local`.
- **A second repo was created for a model bake-off.** Because Fable 5 got pulled offline (a US export-control order), the planned Opus-vs-Fable test is dead. Instead there's now a twin repo, `~/dev/active/mccoy-tyner-kc/`, where you'll build the same project with **Kimi Code** and compare approaches. It's deliberately walled off — its own database namespace, and it does NOT contain any of this build's design, so Kimi has to think for itself.

Nothing this session is committed to git, in either repo. That's been your call throughout.

## What's unresolved?

- **Two housekeeping items you said you'd handle:** (1) `docs/plan-v2.md` still mentions the now-dead Fable A/B in a couple of spots — wants the same cleanup the runbook already got; (2) committing both repos to git when you're ready.
- **An Apple ID question to settle once you have the token:** the free iTunes `collectionId` may NOT be the same number as the Apple Music catalog album id. A 5-minute test (does the id resolve in the catalog API, or do we look up by UPC?) decides exactly what gets stored. Serving-phase, not urgent.
- **The Kimi twin still needs its own brief file** (`.claude` / a CLAUDE.md equivalent) — you said you'd set that up.
- **Smaller, parked:** public-facing product name; whether embeddings stay local to `_jazzcanon` or also feed a cross-project index.

## What's next?

If you sit down to move the **Claude build** forward: open `docs/runbook-v2.md` and run **Segment A** — it initializes the ledger and cull-notes, sends the three specialists out for 10 albums each (on Opus 4.8), and stops at your review gate with ~30 source-grounded records across three Markdown files. Nothing touches the database; it's all reviewable text.

If you'd rather kick off the **experiment**: open Kimi Code in `~/dev/active/mccoy-tyner-kc/`, read `docs/runbook-kernel.md`, and paste its **Phase 0** prompt — it asks Kimi to propose its own plan and stack, which you then review. (Resist pasting any of the Claude build's design — that's the one rule that keeps the comparison honest.)

Either path is a calm, gated first step. Both are waiting on you.
