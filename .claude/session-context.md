# Session Context

## Session Name
mccoy-build

## Current Focus
Build McCoy — the Hermes agent profile — from `docs/mccoy-agent-spec.md`
(v0.3 draft → **v1.0 BUILT**). Fable 5 session, launched via
`docs/fable-build-prompt.md`, indexed as "mccoy-build".

## What This Session Did (2026-07-15)

### Database (spec §10 3b–3c)
- `site_status` lookup (text-code PK: found/reviewed/approved/live/retired) +
  `album.site_status` (100 included albums backfilled → `live`), `edit_log`
  (append-only), `_jazzcanon_app` role (SELECT/INSERT/UPDATE, **no DELETE** —
  never-delete is structural). `scripts/migrate-3b-site-status.sql` +
  `run-migrate-3b.sh`; grants verified live (DELETE + edit_log UPDATE denied).
- `export.sh` now enforces the publication gate in all 4 query sites — it was
  previously **unfiltered** (first staged candidate would have leaked to the
  site). Verified content-identical output for the current 100.
- Citation backfill: `scripts/citation-backfill.py` (Sonnet subagent).

### Hermes (spec §10 3d–3f)
- **mccoy profile**: SOUL.md constitution (Fable-authored), Kimi K2.7-Code lead,
  delegation lane (web+file children), `canon-council` MoA preset (DeepSeek +
  Gemini refs via Nous; GPT-5.6 Terra aggregator via Codex OAuth — verified).
- **JUDGE lane** = `~/.hermes/scripts/canon-council.py` (agent-invocable; no
  in-agent MoA tool exists in v0.18.2; refs argue both cases — per-ref roles
  unsupported). Verified e2e: real ballot on a next-batch candidate, 60s.
- **Drip**: cron job `canon-drip` in the DEFAULT profile scheduler (always-on;
  zero new footprint) with per-job Kimi override; 06:00, telegram,
  `--script canon-drip-precheck.py` (dedup list + backlog cap as code; both
  branches verified). Drip gathers INLINE; delegation is for interactive
  missions. Next fire: 2026-07-16 06:00.
- **Staging** = deterministic `scripts/stage-candidate.py` (Sonnet subagent),
  adapted from ingest.py: candidate/found only, dedup + window guards.

### Repo config (John steers by editing markdown)
`config/canon-rubric.md` (scope window/gates in frontmatter + judgment prose),
`config/edit-contract.md`, `config/gather-mission.md`, `docs/mccoy-runbook.md`,
`scripts/canon-search.py` (semantic search, nomic via vps4 tunnel — verified).

## Key Decisions
Round-3 build decisions **#13–#22** appended to spec §11 (the spec remains the
source of truth). Notables: preset lives in mccoy profile config only
(canon-council.py pins HERMES_HOME); Hermes v0.18.2 always backgrounds
top-level delegations (fine interactively, breaks -z probes only);
McCoy executes John's explicit per-album status verdicts (decision John's,
typing McCoy's); `subagent_auto_approve` stays false (moot for web+file
children).

## Late-session completions
- Citation backfill EXECUTED: 191 sources, 393 citations, 100/100 albums,
  idempotent (2nd run creates 0). Held item 1 closed.
- Full pipeline validated live: Shorty Rogers and His Giants (1953) staged as
  the first real candidate (dossier + real council ballot → stage-candidate.py
  → candidate/found, tier consensus_core, must_have; edit_log row; backlog
  1/10; export still exactly 100 — the publication gate holds).
- ship.sh now flips approved→live after verified deploy (audited).

## Open Items / Next
- John reviews the staged Shorty Rogers candidate (first item in the queue);
  first drip fires 2026-07-16 06:00 → Telegram.
- First interactive mission (John: `mccoy` chat → "run a gather mission…")
  is the natural full-pipeline smoke test; all mechanics verified piecewise.
- First drip fires 2026-07-16 06:00 → Telegram.
- Deferred: per-line citation backfill (memory reminder); `_jazzcanon_ro`
  password rotation (carried from last session).
- DONE late in session: approved→live flip wired into ship.sh (audited via
  edit_log; SQL dry-run verified).

## Session Status
Completed: 2026-07-15 (evening)
Servers cleaned: none added this session — nothing to clean up
Honcho curation: 5 durable facts written to session `mccoy-build` (McCoy
shipped v1.0; executes-but-never-initiates verdict boundary + no-DELETE
pattern; drip-gathers-inline architecture refinement; Hermes v0.18.2
delegation-backgrounds gotcha; open loop: Shorty Rogers verdict + first drip
2026-07-16 + commits pending). Rejected: field-level decision list (spec is
source of truth), one-off Q&A noise.
