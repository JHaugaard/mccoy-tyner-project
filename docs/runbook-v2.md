# Runbook v2 — The Jazz Canon, End to End

**Version:** 2.0 · 2026-06-12
**Purpose:** The executable form of `plan-v2.md` (v2.0). Each segment dispatches with a single prompt;
John's gates are **hard stops** — the run halts and resumes only on his decision.

> **Supersedes runbook.md (v1.0)**, retained as history.
>
> **✅ Live as of 2026-06-12.** The specialist agents are updated to the merged one-pass role (Step 2), the
> Apple Music pivot is adopted, and the schema carries `apple_album_id` (Step 3). **Segment A runs now.**
> Segments C–D apply the schema at Phase 4 and stay gated on John's go. The only setup left is the empty
> ledger + cull-notes (step A0), created on first use. The Master Prompts below are a *convenience* —
> slow, gate-by-gate iteration is the chosen mode, not one-shot automation.

**Agents (in `~/.claude/agents/`):** `jazz-hard-bop-researcher`, `jazz-cool-jazz-researcher`,
`jazz-modal-jazz-researcher` (the three specialists — **merged one-pass gatherers**: canon + personnel),
`jazz-canon-orchestrator` (now a **recurring gardener**), `jazz-personnel-researcher`
(**retained dormant — the seam**; dispatched only if the POC gate reopens the split).

---

## Preconditions (verify before any dispatch)

- [ ] Working directory: `~/dev/active/mccoy-tyner/`
- [x] Specialist agents updated to merged role (Step 2, 2026-06-12) — **done**
- [ ] `docs/genre-definitions.md` present (scope authority, passed to specialists)
- [ ] `data/dispatch-ledger.json` exists (initialize empty on first run) and `research/cull-notes.md` exists
- [ ] Clean git state or a deliberate branch — research outputs are git-tracked

---

## Segment A — Phase 1–2: One-Pass Gathering (POC)

The first real run. Goal: **30 complete records** (canon + personnel in one pass), and a **debugged
pipeline**. This is the kink-finder, not the full canon.

### A0. Initialize the ledger (first run only, mechanical)
Create `data/dispatch-ledger.json` with empty `albums_in_collection` and `dispatches`. Create an empty
`research/cull-notes.md` with a one-line header. Haiku-grade.

### A1. Dispatch the three specialists — 10 albums each (parallel, single message, three Agent calls)

Each prompt invokes the merged contract + ledger/cull-notes awareness (built into the agents).

| Agent | Dispatch prompt |
|-------|----------------|
| `jazz-hard-bop-researcher` | "Gather **10** complete candidate records for The Jazz Canon — canon metadata **and** full personnel/tracks/sessions/dates/locations in one pass, per your output contract. Read `docs/genre-definitions.md` (scope), `data/dispatch-ledger.json` (exclude everything already listed), and `research/cull-notes.md` (calibrate to John's past verdicts) first. Output: `research/hard-bop-candidates.md`. Capture album-art + Apple/iTunes + MusicBrainz reference IDs where available." |
| `jazz-cool-jazz-researcher` | same, 10 records → `research/cool-jazz-candidates.md` |
| `jazz-modal-jazz-researcher` | same, 10 records → `research/modal-jazz-candidates.md` |

**Model A/B — Opus 4.8 vs Fable 5 (free window, before 2026-06-22).** Best run **standalone, first**, to
settle the model before the full POC. **No-bleed protocol:** keep `dispatch-ledger.json` and `cull-notes.md`
**empty for both runs** (identical inputs); dispatch the **modal** specialist **twice in parallel**, same
prompt and count, the *only* difference being `model: opus` vs `model: fable`; write to **distinct,
neutrally-named** paths (`research/modal-run-1.md` / `research/modal-run-2.md`) so neither sees the other
and you can judge **blind**. Do **not** update the ledger until after you compare and pick. Then run the
full 3-style POC on the winner. Compare the two runs on judgment quality, source grounding, personnel
depth/accuracy, and scope discipline before un-blinding.

**Validate before proceeding:** each file has a source map (≥4 sources); JSON blocks parse; every record
carries the **full merged contract** (canon fields **and** a personnel block with `obs/inf/unk` labels);
`include: null`; no album already in the ledger; priority distribution honest (not all `must_have`).

### A2. (Optional) Gardener pass
Only if useful at 30 albums — likely skip for the POC, run once the collection is larger. When run:
`jazz-canon-orchestrator` reads the three files + ledger and emits tier observations + gap/overlap notes
(it never sets `include`).

### A3. 🛑 GATE — John reviews the POC
John reviews the 30 records (and the Fable-vs-Opus pair). For each: accept / cull. He:
1. promotes accepted records in `data/canon-draft.json` (`include: true`);
2. **updates `data/dispatch-ledger.json`** — adds accepted albums to `albums_in_collection`, logs the
   dispatch row (agent, date, requested, accepted, model);
3. **appends `research/cull-notes.md`** — one line + reason per culled pick.

**This gate also decides the merge:** personnel clean from the merged pass → stay merged. Personnel sloppy
→ reopen the seam (Segment B-split below). Decide with the evidence in front of you.

---

## Segment B — Scaled / Repeat Dispatch (after POC validated)

The growth loop. Repeat as often as wanted; each run is one **dispatch spec**.

### B1. Spec the dispatch
Choose: **style** (which specialist) · **count** · **model** · output path. `exclude` is **automatic** —
the agent reads the current ledger. Optionally target a gap the gardener flagged.

### B2. Dispatch (parallel where multiple styles run at once)
Same merged prompt as A1, with the new count and the (now larger) ledger. Validate as in A1.

### B3. 🛑 GATE — John reviews, then **ledger + cull-notes update** (as A3 steps 1–3)
The agents get better each round because they read the growing ledger (what's done) and cull-notes (what
John rejected and why). No retraining — feedback-driven calibration.

### B-split (only if A3 reopened the seam) **[the dormant seam]**
If merged personnel quality failed: specialists return to **canon-only** gathering; re-activate
`jazz-personnel-researcher` in batches of ~10 over accepted albums (the v1 flow). The schema already
supports this — no migration. Document the reason in `research/cull-notes.md` so the decision is traceable.

---

## Segment C — Phase 3: Schema (locked; two pending changes)

Design locked (schema v1.1): `docs/schema.md`, `data/schema.sql`, `data/seed.json`,
`data/data-platform-handoff.json`. **Before ingest, apply John's step-3 changes:**
1. add `apple_album_id` (album) + optional `apple_track_id` (track);
2. confirm the personnel block is cleanly separable (merge-seam check).
Then verify `schema.sql` parses (load into a scratch schema and drop). If Phase 1–2 data surfaced any
other contract gap, **STOP and surface to John** — do not patch silently.

---

## Segment D — Phase 4: Platform Build

> App stack/UX choices remain John's. This segment is the **data-platform build**, fully specified.

### D1. Apply the schema
On vps8 (`127.0.0.1:5433`): `CREATE SCHEMA _jazzcanon;` + run `data/schema.sql`; create
`_jazzcanon_role` / `_jazzcanon_ro` (passwords from vault, `jazzcanon_*` secrets, per
`database-conventions.md`).

### D2. Ingest pipeline (idempotent, in order)
1. **Validate** `canon-draft.json` (`include:true`) against the contracts.
2. **Identity-resolve persons** — cluster name variants → `person` + `person_name_variant`;
   **borderline merges go to John** (mini-gate, batched).
3. **Load** albums, sessions, tracks, performances, production credits, citations.
4. **Seed collection** — `collection(slug='core-canon')` + membership for every included album.
5. **Album art** — resolve MBIDs (honor Phase 1–2 refs; else MusicBrainz, ≤1 req/s) → fetch Cover Art
   Archive → iTunes/Apple → `data/album-art/` + `album_art` rows + `manifest.json`.
6. **Apple Music IDs** — load captured `apple_album_id`s (preview / link / player targets for the serving phase).
7. **Search documents** — populate `album.search_document` / `person.search_document` from the
   `v_*_search_source` views.
8. **Embed** — `nomic-embed-text` via Ollama (vps4) → vector columns → HNSW indexes.
9. **Static export** — JSON bundle + precomputed album×album neighbors + art → `app/data/`.

**Validate:** row counts reconcile with draft JSON; `fn_degrees_between` returns sane results on a known
pair; `v_album_card` renders the full canon; every album has ≥1 citation.

### D3. Serving layer (staged — only on demand)
- **Default: nothing to do** — the static bundle is the app's data source.
- **PostgREST (when a live consumer appears):** single binary on vps8, `db-schemas = "_jazzcanon"`,
  `db-anon-role = "_jazzcanon_ro"` — read-only REST over the views, zero code.
- **MCP server (banked):** wraps the same views + `fn_degrees_between` + vector search for agent-facing
  access (this is the **research interface** for John's "dig in and write" goal). Build per `mcp-building`.

### D4. 🛑 GATE — John reviews the loaded platform
His queries run; epistemic labels render; canon browseable via `v_album_card`. Phase 5 (app) starts here
with its own UX gate.

---

## Master prompts

**Model A/B (optional, run first — settles Opus vs Fable):**
> Run the Model A/B from `docs/runbook-v2.md` Segment A: with `dispatch-ledger.json` and `cull-notes.md`
> empty, dispatch the **modal** specialist twice in parallel — identical prompt and count of 10, one on
> `model: opus`, one on `model: fable` — writing to `research/modal-run-1.md` and `research/modal-run-2.md`.
> Do not touch the ledger. Stop and show me both, labeled only run-1 / run-2, for a blind compare.

**Segment A (POC):**
> Run Segment A of `docs/runbook-v2.md`: initialize the ledger + cull-notes if needed, dispatch the three
> specialists (10 records each, merged contract) on [chosen model], validate all outputs, and stop at the
> A3 gate with a per-style summary and anything needing my attention.

**Segment B (one dispatch):**
> Run a Segment B dispatch of `docs/runbook-v2.md`: [style], [count] records, model [x]. Exclude is the
> current ledger. Validate and stop at the B3 gate.

**Segment D (platform build):**
> Run Segment D of `docs/runbook-v2.md`: apply schema, ingest `canon-draft.json`, batch borderline person
> merges to me, build art/search/embeddings/static export, stop at the D4 gate.

---

## Failure handling

- Specialist returns malformed records → re-dispatch **that specialist only**, citing the validation
  failure; leave the others.
- Specialist re-surfaces a ledger album → drop that record, note it; the ledger exclude is the contract.
- Merged personnel quality poor at A3 → **reopen the seam** (Segment B-split), don't force the merge.
- Ingest validation failure → fix the draft JSON (human-editable source of truth), re-run; loader is
  idempotent.
- Any schema gap surfaced by real data → **STOP, surface to John** (step-3 territory), no silent patches.
