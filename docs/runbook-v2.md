# Runbook v2 — A Jazz Canon, End to End

**Version:** 3.0 · 2026-09-06
**Purpose:** The executable form of the canon-growth loop. Each dispatch is a single prompt; John's gates are **hard stops** — the run halts and resumes only on his decision.

> **Supersedes** the 2.0 text of this file (2026-06-12) and `runbook.md` (v1.0), both retained in git history.
> v3.0 replaces the six per-style researcher agents with one style-parameterized agent, drops the retired
> combined-markdown output, and removes the June 2026 model policy. Segments C and D (schema, platform
> build) were already executed; they are kept below for reference and not re-run.

**Agents (in `~/.claude/agents/`):**

| Agent | Role |
|-------|------|
| `jazz-style-researcher` | The one researcher. Dispatched with `style=<bebop\|cool-jazz\|hard-bop\|modal-jazz\|free-jazz\|fusion\|ecm>`; refuses to run without one. Reads `config/style-research/<style>.md` for scope, sources, gate posture, and style-specific fields. Merged one-pass gatherer: canon judgment **and** personnel in the same run. |
| `jazz-canon-orchestrator` | Recurring gardener: merges multi-style candidate sets into a tiered ballot. Never sets `include`. |
| `jazz-personnel-researcher` | Retained dormant — the seam. Dispatched only if a gate reopens the canon/personnel split. |

**Style modules (in `config/style-research/`):** `bebop.md`, `cool-jazz.md`, `hard-bop.md`, `modal-jazz.md`, `free-jazz.md`, `fusion.md`, `ecm.md`. Edit these to steer a style; the agent body never needs to change for a scope, source, or posture adjustment. The rubric (`config/canon-rubric.md`) stays authoritative over every module for the year window and the opened-gate rules.

---

## Preconditions (verify before any dispatch)

- [ ] Working directory: `~/dev/active/mccoy-tyner/`
- [ ] `config/canon-rubric.md` frontmatter is what you intend (`year_min`/`year_max`, `excluded_styles`)
- [ ] `data/dispatch-ledger.json` and `research/cull-notes.md` exist (create empty on first run)
- [ ] `docs/personnel-contract.md` present (record shape, read by the agent at dispatch)
- [ ] Clean git state or a deliberate branch — dossiers in `research/candidates-inbox/` are git-tracked

---

## Segment A — One-pass gathering

### A1. Dispatch (one Agent call per style; parallel in a single message when several styles run)

The dispatch prompt names the style and the directive. Everything else (ledger exclude, cull-note calibration, rubric, personnel contract, output path) is built into the agent and its module.

| Style | Module default count | Dispatch prompt |
|-------|----------------------|-----------------|
| `hard-bop` | 10 | `style=hard-bop — gather 10 next-best.` |
| `cool-jazz` | 10 | `style=cool-jazz — gather 10 next-best.` |
| `modal-jazz` | 10 | `style=modal-jazz — gather 10 next-best.` |
| `free-jazz` | 5 | `style=free-jazz — gather 5 gateway records.` |
| `fusion` | 6 | `style=fusion — gather 6, the Miles electric band 1969–72.` |
| `ecm` | 8 | `style=ecm — gather 8, Jarrett solo and the European Quartet.` |

Any count or focus overrides the default. A dispatch with no `style=` is refused by the agent — that is the intended behavior, not a failure to debug.

**Model:** per the global model-selection rule. Sonnet is the floor; Opus when the run is judgment-heavy (the opened gates, a contested boundary). Name the tier in the Agent call.

**Output:** one JSON dossier per album at `research/candidates-inbox/<id>.json`, per `research/candidate-schema.md`. Synthesis notes come back in the agent's reply, not as a file.

### A2. Validate before the gate

For each dossier: `scripts/check-candidate.py` passes; the source map has ≥4 entries (ECM: ≥2 non-house); every record carries `include: null`, the base fields, the module's required fields (`bridge_case` / `accessibility` for free-jazz, `bridge_case` for fusion, `continuity_case` + `catalog_number` for ecm); no album already in the ledger; the priority spread is honest (not all `must_have`).

Malformed dossier → re-dispatch **that style only**, citing the validation failure. Ledger album re-surfaced → drop that dossier and note it; the ledger exclude is the contract.

### A3. (Optional) Gardener pass

When several styles ran at once, or the inbox is large: `jazz-canon-orchestrator` reads the inbox + ledger and emits tier observations and gap/overlap notes. It never sets `include`.

### A4. 🛑 GATE — John reviews

For each dossier: accept / cull. On accept, `scripts/stage-candidate.py` ingests the dossier. John then:

1. adds accepted albums to `data/dispatch-ledger.json` `albums_in_collection` and logs the dispatch row (agent, style, date, requested, accepted, model);
2. appends `research/cull-notes.md` — one line + reason per culled pick. These lines are the agent's calibration on the next run; the module names the phrasings each style watches for.

---

## Segment B — Repeat dispatch

The growth loop. Each run is one dispatch spec: **style · count · focus · model**. Exclude is automatic (the agent reads the current ledger). Optionally target a gap the gardener flagged. Run A1 → A4 again.

**B-split (only if a gate reopens the seam).** If merged personnel quality fails at review: the researcher returns to canon-only gathering and `jazz-personnel-researcher` is re-activated in batches of ~10 over accepted albums. Document the reason in `research/cull-notes.md` so the decision is traceable.

---

## Segment C — Schema (executed; reference only)

Design locked (schema v1.1): `docs/schema.md`, `data/schema.sql`. The `year` field means **recording year** (pinned after the 2026-06-18 Kimi-twin cross-check surfaced recording-vs-release drift). Any schema gap surfaced by real data → **STOP, surface to John**; no silent patches.

## Segment D — Platform build (executed; reference only)

Schema `_jazzcanon` on vps8 Postgres (port 5433), roles per `database-conventions.md`. Ingest is `scripts/ingest.py` (idempotent), enrichment via the `scripts/` helpers (MBID/Apple lookup, cover art, geocoding, embeddings), export via `scripts/export.sh`, publish via `scripts/publish.sh` / `scripts/ship.sh`. The live collection row keeps slug `the-jazz-canon`; the product name is *A Jazz Canon* (renamed 2026-07-26 without touching the DB). The operational detail lives in `docs/data-pipeline-sop.md` and `docs/growth-runbook.md`.

---

## Master prompts

**One style:**
> Run a Segment A dispatch of `docs/runbook-v2.md`: `jazz-style-researcher` with `style=[style]`, [count] records, [focus if any], model [tier]. Validate per A2 and stop at the A4 gate with a summary and anything needing my attention.

**Several styles at once:**
> Run Segment A of `docs/runbook-v2.md` for styles [list], counts [list], model [tier], in parallel. Validate each per A2, run the gardener (A3), and stop at the A4 gate with a per-style summary.

---

## Failure handling

- No `style=` in the dispatch → the agent refuses and lists the valid values. Re-dispatch with one.
- Dossier fails `check-candidate.py` → re-dispatch that style only, citing the failure.
- Ledger album re-surfaced → drop it, note it.
- Personnel quality poor at review → B-split; don't force the merge.
- Any schema gap → **STOP, surface to John**.
