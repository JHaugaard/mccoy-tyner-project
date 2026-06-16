# Session Context

## Current Focus

Hardening the jazz canon build from plan to runnable, then setting up a model A/B. This session (2026-06-12 → 2026-06-16) took the project from "Phase 3 done" to "Segment A live," adopted Apple Music, and stood up a clean-room Kimi Code twin for a Claude-vs-Kimi comparison. Still no albums dispatched — but everything is now ready to run.

## Key Decisions (this session)

- **Plan/Runbook v2** written (`docs/plan-v2.md`, `docs/runbook-v2.md`); v1 retained as history. Two structural shifts: the **"Starting with 100"** pivot (collection grows organically; canon is a curated lens) and **the merge** (style specialists now gather canon judgment AND personnel in one two-phase pass).
- **Agent updates** (Steps 1–3): name scrub to "the jazz canon project" (kept McCoy-Tyner-the-musician refs); model defaults are floors, overridable up per dispatch; hardwired counts replaced by a **dispatch directive** (count and/or focus); personnel contract extracted to **`docs/personnel-contract.md`** (single source of truth, read at dispatch); record gains a nested `personnel_record` block = the **seam** for a future split; specialists read a dispatch-ledger (exclude) + cull-notes (calibrate); orchestrator reframed as a recurring gardener.
- **Apple Music, not Spotify** — Spotify killed previews; Apple still serves them and gives John full playback as a subscriber. Schema bumped to **v1.2** (`apple_album_id` on album, optional `apple_track_id` on track). Capture is free via the iTunes Search API in the data phase; paid MusicKit player deferred to serving. John now has an Apple Developer account + MusicKit access; `.env.example`/`.env.local` carry the Apple block; `*.p8` gitignored.
- **Merge-seam confirmed** needs no migration — personnel already lives in dedicated tables independent of canon-judgment columns.
- **Model A/B pivot** — Fable 5 suspended worldwide (2026-06-12, US export-control directive), killing the Opus-vs-Fable plan. Replaced with a **Claude Code vs Kimi Code** comparison: clean-room twin repo `~/dev/active/mccoy-tyner-kc/` (own git, own DB namespace `_jazzcanonkc`, solution-design deliberately withheld to avoid the "transcription trap"; `docs/runbook-kernel.md` gives Kimi gated starter prompts that make it design its own).
- **Runbook-v2 cleaned** of the dead Fable A/B (POC now runs on Opus 4.8).

## Notes

- Execution mode: **slow, gated iteration** — not one-shot automation (John's explicit choice).
- **Nothing committed to git** in either repo this whole session — John's standing call.
- Memory files written this session: `move-to-v2`, `execution-mode-slow-iterate`, `kimi-ab-twin` (+ the research-platform-template vision saved to Honcho as peer=john).

## Session Status
Completed: 2026-06-16
Servers cleaned: none added this session
Honcho curation: 1 consolidated user-fact written (Apple Developer account + Claude-vs-Kimi A/B); template vision already saved earlier in session
