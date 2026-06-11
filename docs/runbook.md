# Runbook — Phases 1→4, End to End

**Version:** 1.0 · 2026-06-11
**Purpose:** The executable form of `plan-v1.md` (v1.4). Each phase segment can be dispatched with a
single prompt; John's gates are **hard stops** — the run halts there and resumes only on his decision.
A "one-shot" run = paste the master prompt below; the harness executes everything up to the next gate,
then waits.

**Agents:** all first-class, in `~/.claude/agents/` — `jazz-hard-bop-researcher` (Opus),
`jazz-cool-jazz-researcher` (Opus), `jazz-modal-jazz-researcher` (Opus), `jazz-canon-orchestrator`
(Opus), `jazz-personnel-researcher` (Sonnet). Each is self-contained; dispatch prompts only pass
parameters.

---

## Preconditions (verify before any dispatch)

- [ ] Working directory: `~/dev/active/mccoy-tyner/`
- [ ] The five agent files exist in `~/.claude/agents/` (names above)
- [ ] `docs/genre-definitions.md` present (scope authority, passed to specialists)
- [ ] Clean git state or a deliberate branch — research outputs are git-tracked

---

## Segment A — Phase 1: Canon Assembly

### A1. Dispatch the three specialists (parallel — single message, three Agent calls)

| Agent | Dispatch prompt |
|-------|----------------|
| `jazz-hard-bop-researcher` | "Compile your candidate list for the McCoy Tyner jazz canon project. Output: `research/hard-bop-candidates.md`. Target 40–60. Scope authority: read `docs/genre-definitions.md` first." |
| `jazz-cool-jazz-researcher` | "Compile your candidate list for the McCoy Tyner jazz canon project. Output: `research/cool-jazz-candidates.md`. Target 30–50. Scope authority: read `docs/genre-definitions.md` first." |
| `jazz-modal-jazz-researcher` | "Compile your candidate list for the McCoy Tyner jazz canon project. Output: `research/modal-jazz-candidates.md`. Target 50–70. Scope authority: read `docs/genre-definitions.md` first." |

**Validate before proceeding:** each file has a source map (≥4 sources), JSON blocks parse, every
record has `include: null`, priority distribution is honest (not all `must_have`).

### A2. Dispatch the Orchestrator (after all three complete)

`jazz-canon-orchestrator`: "Merge the three specialist files (`research/hard-bop-candidates.md`,
`research/cool-jazz-candidates.md`, `research/modal-jazz-candidates.md`) into the decision ballot.
Outputs: `data/canon-ballot.json` + `research/canon-synthesis.md`. Scope authority:
`docs/genre-definitions.md`. Target canon size ~100. Derive specialist rebuttals from their synthesis
notes (single-agent mode) and label them as derived."

**Validate:** every ballot album traces to a specialist record (no inventions); `include` is `null`
throughout; tier counts table present in the synthesis.

### A3. 🛑 GATE — John rules on the ballot

John rubber-stamps `consensus_core`, rules on `contested`/`scope_call`, skims `exclude_suggested`.
Output of the gate: `data/canon-draft.json` — ballot records with `include: true/false` set, ~100
included. (Mechanical transform of John's marked-up ballot; Haiku-grade task.)

---

## Segment B — Phase 2: Personnel & Track Data

### B1. Batch assignment (mechanical)

Split `include: true` albums from `data/canon-draft.json` into 10 batches of ~10, balanced roughly by
expected research difficulty (multi-session and compilation-prone albums spread across batches).

### B2. Dispatch 10 personnel agents (parallel)

For NN = 01…10, dispatch `jazz-personnel-researcher`:
"Albums assigned: [list of `id` + artist + title from batch NN]. Output:
`research/personnel-batch-NN.md`. Album IDs must match the canon IDs exactly."

**Validate per batch:** JSON parses; every `album_id` matches the canon; every `instrument` is
taxonomy-legal; `track_assignments_complete` honest; Summary Notes present.

### B3. Merge (mechanical, Haiku-grade)

Merge the 10 batch files → `data/personnel-draft.json` (one record per album, source maps preserved
per batch with batch-prefixed IDs, e.g. `b01:S1`). Also write
`research/personnel-sources-compile.md` (source-quality roll-up from the 10 Summary Notes).

### B4. 🛑 GATE — John spot-checks 5–10 albums

Accuracy check against a source he trusts. Failures send the affected batch back with notes.

---

## Segment C — Phase 3: Schema (already complete — verification only)

Design is locked (schema v1.1, 2026-06-11): `docs/schema.md`, `data/schema.sql`, `data/seed.json`,
`data/data-platform-handoff.json`. Verify `schema.sql` parses (`psql --dry-run` equivalent: load into
a scratch schema and drop). No new work unless Phase 2 data surfaced a contract gap — if it did, STOP
and surface to John.

---

## Segment D — Phase 4: Platform Build

> Architecture/UX design choices in Phase 4 (app stack, UX) remain John's. This segment covers the
> **data platform build**, which is fully specified and one-shot-able.

### D1. Apply the schema

On vps8 (`127.0.0.1:5433`): `CREATE SCHEMA _jazzcanon;` + run `data/schema.sql`; create
`_jazzcanon_role` / `_jazzcanon_ro` (passwords from vault, `jazzcanon_*` secrets, per
`database-conventions.md`).

### D2. Ingest pipeline (idempotent, in order)

1. **Validate** `canon-draft.json` (include:true) + `personnel-draft.json` against the contracts
2. **Identity-resolve persons** — cluster names/variants → `person` + `person_name_variant`;
   **borderline merges go to John, not auto-merged** (mini-gate, batched)
3. **Load** albums, sessions, tracks, performances, production credits, citations
4. **Seed collection** — `collection(slug='core-canon')` + membership for every included album
5. **Album art** — resolve MBIDs (honor Phase 2 refs; else MusicBrainz lookup, ≤1 req/s) → fetch
   Cover Art Archive → iTunes fallback → `data/album-art/` + `album_art` rows + `manifest.json`
6. **Search documents** — populate `album.search_document` / `person.search_document` from the
   `v_*_search_source` views
7. **Embed** — `nomic-embed-text` via Ollama (vps4) → vector columns → build HNSW indexes
8. **Static export** — JSON bundle + precomputed album×album neighbors + art → `app/data/`

**Validate:** row counts reconcile with draft JSON; `fn_degrees_between` returns sane results on a
known pair; `v_album_card` renders the full canon; every album has ≥1 citation.

### D3. Serving layer (staged — only on demand)

- **Default: nothing to do.** The static bundle is the app's data source.
- **PostgREST (when a live consumer appears):** single binary on vps8, `db-schemas = "_jazzcanon"`,
  `db-anon-role = "_jazzcanon_ro"` — read-only REST over the views, zero code.
- **MCP server (banked):** wraps the same views + `fn_degrees_between` + vector search for
  agent-facing access. Build per `mcp-building` skill when wanted.

### D4. 🛑 GATE — John reviews the loaded platform

Queries he cares about run correctly; epistemic labels render; canon browseable via `v_album_card`.
Phase 5 (app) starts from here with its own UX gate.

---

## Master one-shot prompt (Segment A)

> Run Segment A of `docs/runbook.md`: dispatch the three style specialists in parallel, validate
> their outputs, then dispatch the Canon Orchestrator, validate the ballot, and stop at the A3 gate
> with a summary of tier counts and anything that needs my attention.

Segments B and D have the same shape ("Run Segment B/D of docs/runbook.md … stop at the gate").
A full-project one-shot is the three prompts in sequence, separated by John's gate decisions — the
gates are the only places the run waits.

---

## Failure handling

- A specialist returning malformed records → re-dispatch that specialist only, citing the validation
  failure; do not touch the other outputs.
- Orchestrator inventing an album (fails trace-back validation) → discard ballot, re-dispatch with
  the violation named. This is the one non-negotiable.
- Personnel batch failing spot-check → re-dispatch that batch with John's notes appended.
- Ingest validation failure → fix the draft JSON (it is the human-editable source of truth), re-run;
  the loader is idempotent.
