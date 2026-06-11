# McCoy Tyner Project — Phased Plan v1

**Project:** Canonical Jazz Albums (Cool Jazz → Hard Bop → Modal Jazz)  
**Directory:** `~/dev/active/mccoy-tyner/`  
**Approach:** Deliberate, no one-shotting. Research-first, data model emerges from findings.  
**Orchestration:** Platform-agnostic by design — the plan names *roles*, not products. A planning/architecture agent shapes the work; an implementation harness builds it. (Currently proceeding in Claude Code; harness is not load-bearing in the plan.)  
**Research Tool:** *research-compiler* skill for source-grounded compilation

---

## Foundation Decisions (locked 2026-06-10)

Settled during the data-platforming session, before any agent launched or album selected:

- **Storage target:** Shared Postgres 16 on `vps8-core` (native, `127.0.0.1:5433`). The project gets
  its own **schema** — not its own database, not mixed into existing tables. `DROP SCHEMA ... CASCADE`
  is the clean kill switch. Third-party apps (Honcho, memory_persistence) own databases; John's
  projects own schemas (the `_foundry` pattern). pgvector 0.8.2 and pg_cron already installed.
- **Namespace:** `_jazzcanon` — **decided 2026-06-10** (John's call). The schema is *created* at
  Phase 4 (`CREATE SCHEMA`); nothing was bound through Phase 3, so choosing the name now cost nothing.
  The *product* name remains open — `mccoy-tyner` stays the working codename for as long as John likes.
- **Data lifecycle:** JSON draft files through Phase 1–2; relational schema designed in Phase 3;
  schema *applied* in Phase 4. Postgres is authoritative store **and** semantic-search lab.
- **Semantic search (two engines):** (1) **pgvector** over composed per-album / per-musician "search
  documents" for similarity & discovery; (2) **relational/recursive** for networks (six-degrees,
  sideman co-occurrence, timelines) — graph traversal, not embeddings. The ~100-album corpus is tiny,
  so a build step can export a static bundle (JSON + precomputed neighbors) for a simple static app;
  only free-text NL search needs a live backend (decide at Phase 4).
- **Built to outlive the first canon** *(locked 2026-06-11)*: the ~100-album canon is a
  well-researched, well-architected **proof of concept**, not the ceiling. Albums belong to named
  **collections** (the canon = seed collection `core-canon`); styles are rows, not enums; the year
  CHECK is wide. Adding albums, artists, styles, or whole new canons is an ingest run, never a
  migration. (Schema v1.1, `docs/schema.md` §5.2b.)
- **Agents are first-class** *(locked 2026-06-11)*: all project agents live in `~/.claude/agents/`
  as named, self-contained, model-scoped Claude Agents usable outside this project —
  `jazz-hard-bop-researcher` (Opus), `jazz-cool-jazz-researcher` (Opus), `jazz-modal-jazz-researcher`
  (Opus), `jazz-canon-orchestrator` (Opus), `jazz-personnel-researcher` (Sonnet, ×10 parallel).
  Each carries its full output contract inline and takes dispatch parameters (output path, targets);
  the briefs in `research/agent-briefs/` are retained as design history. Model posture: Opus where
  research judgment concentrates; Sonnet for high-volume extraction; Haiku only for mechanical
  validation/merge steps.
- **Serving posture (staged)** *(locked 2026-06-11)*: the schema's views/functions ARE the API
  contract. Layer 1: static export (default — app needs no backend). Layer 2: **PostgREST read-only**
  over `_jazzcanon` views via `_jazzcanon_ro` when a live consumer appears (single binary, zero
  code). Layer 3 (banked): an **MCP server** wrapping the same views, so Claude/agents query the
  canon directly. Every layer speaks the same vocabulary.

---

## Phase 0: Infrastructure & Conventions

**Goal:** Establish working patterns before research begins.

- [ ] Create project folder structure (`research/`, `data/`, `app/`, `docs/`)
- [ ] Decide data format (JSON? SQLite? Markdown?) — defer final choice until Phase 1 reveals data shape
- [ ] Establish naming conventions (kebab-case, consistent with vault)
- [ ] Set up version control (git init, .gitignore for .env, Apple Music references, etc.)
- [ ] Document the "research compile" workflow for this project

**Deliverable:** `docs/conventions.md` + working directory structure

**Gate:** John reviews and approves conventions before proceeding.

---

## Phase 1: The Canon — Compile ~100 Albums

**Goal:** Assemble a comprehensive, source-grounded list of canonical jazz albums.

**Approach:**
1. **Source sweep** — Use Research Compiler to gather "best of" lists from:
   - Penguin Guide to Jazz
   - DownBeat critics polls
   - Jazz historians (Giddins, Cook/Morton, etc.)
   - Contemporary lists (Rolling Stone, NPR, Apple Music editorial)
   - Niche/critic-specific lists (nooks and crannies)

2. **Compile per source** — Each major source gets a research-compile artifact:
   - Source map
   - Album list with metadata (title, artist, year, label)
   - Source's stated criteria
   - Limitations/bias signals

3. **Cross-source synthesis** — Merge lists, identify:
   - Consensus picks (appear on multiple lists)
   - Marginal candidates (appear once, worth evaluating)
   - Gaps (genres/periods underrepresented)

4. **Canon Orchestrator pass** *(added 2026-06-10)* — A synthesis agent reconciles the three
   specialist lists into a **decision ballot** for John. It is a *decision-compression layer*, not a
   selector: it absorbs dedup, overlap resolution, and scope arbitration, sorts every album into
   tiers (`consensus_core` / `contested` / `scope_call` / `exclude_suggested`), and drafts a
   sourced case-for/case-against on each contested album. It never sets `include` and never
   free-selects from parametric memory — every advanced album traces to a specialist's cited source.
   Spec: `research/agent-briefs/canon-orchestrator-brief.md`.

5. **John's evaluative sort** — John reviews the ballot, not the raw pool: rubber-stamps the
   `consensus_core` block, rules on the ~40 pre-argued `contested`/`scope_call` decisions.
   - No quotas per phase
   - No hard category boundaries
   - Post-bebop, pre-Fusion, no Free Jazz

**Deliverables:**
- `research/{hard-bop,cool-jazz,modal-jazz}-candidates.md` (per specialist)
- `data/canon-ballot.json` (Orchestrator output — tiered, pre-argued, `include: null`)
- `research/canon-synthesis.md` (human-readable companion to the ballot)
- `data/canon-draft.json` (John's selection — `include` set, ~100 entries)

**Parallel opportunities:** Three specialist compiles run simultaneously; the Orchestrator runs
after them as a bounded Workflow (compile → surface contested → specialist rebuttal → assemble
ballot). Live Agent Teams are CLI-only/VS-Code-unreliable — use a deterministic Workflow.

**Agents (first-class, 2026-06-11):** `jazz-hard-bop-researcher`, `jazz-cool-jazz-researcher`,
`jazz-modal-jazz-researcher` (all Opus), `jazz-canon-orchestrator` (Opus) — in `~/.claude/agents/`,
self-contained, dispatch-parameterized. Dispatch sequence: `docs/runbook.md`.

**Gate:** John reviews the ballot, confirms or adjusts the ~100.

---

## Phase 2: Personnel & Track Data

**Goal:** Extract full personnel, production credits, and track-level assignments per album in a single deep research pass.

**Approach:**
1. **Four-layer extraction** — For each album, build up from the base:
   - Layer 1: Core ensemble (instruments, `scope: all-tracks`) + production credits (engineer, producer, studio, recording dates)
   - Layer 2: Session contributors — musicians appearing on some but not all tracks (`scope: selected-tracks`)
   - Layer 3: Track-level assignments — when liner notes or sessionographies list personnel per track
   - Layer 4: Per-session recording dates — for multi-session albums, which tracks belong to each date
   - Layer 5 *(optional, added 2026-06-10)*: Album-art references — MusicBrainz release-group MBID + cover-art URL(s), captured opportunistically. Agents record URLs only; the image files are fetched and stored at Phase 4. `cover_art: []` is fine.

2. **Source strategy** —
   - AllMusic (Credits tab)
   - Wikipedia album articles (Personnel section)
   - Tom Lord's Jazz Discography (session-level authority)
   - JazzDiscography.com
   - Liner notes (digitized via Google Books, archive.org, label reissue pages)
   - Recording label discographies (Blue Note, Prestige, Impulse!, Columbia, Verve, ECM)

3. **Agent architecture** — 10 parallel dispatches of `jazz-personnel-researcher` (first-class agent, Sonnet), ~10 albums each. No style specialization needed; the task is identical per album. Instrument names and musician name forms follow the controlled vocabulary carried inline in the agent (mirrors `research/personnel-schema.md`) so records are consistent across all dispatches.

**Note:** Track-level personnel (originally planned as a separate Phase 3) is captured here opportunistically in the same pass. When sources provide track assignments, they are recorded. `track_assignments_complete` flags what the data platform can trust.

**Deliverables:**
- `research/personnel-batch-NN.md` (one per agent, 10 total)
- `research/personnel-sources-compile.md` (source evaluation notes)
- `data/personnel-draft.json` (merged from agent outputs — album → personnel + tracks + cover-art refs)

**Parallel opportunities:**
- All 10 agents run concurrently; each works independently with no cross-album dependencies
- Batching strategy: ~10 albums per agent, assigned at dispatch from `data/canon-draft.json`

**Gate:** John spot-checks 5–10 albums for accuracy before data platform work begins.

---

## Phase 3: Data Model & Schema Design  *(designed 2026-06-10 — contract-first)*

**Goal:** Lock the data structure before building the app.

**Note:** Designed *ahead of* Phase 1–2 data (none compiled yet). The two research schemas
(`candidate-schema.md`, `personnel-schema.md`) ARE the data shape; Phase 3 maps them to a relational
contract. See `docs/schema.md` for the full design, `data/schema.sql` for DDL, `data/seed.json` for a
worked example, and `data/data-platform-handoff.json` for the machine-readable implementation handoff.

**Approach:**
1. Map the two research schemas → relational entities (done)
2. Design schema:
   - Album entity
   - Musician entity (with instrument taxonomy)
   - Track entity
   - Production entity (session, studio, engineer, producer)
   - Album-art entity (cover images: files on disk, path + metadata + provenance in DB)
   - Relationships (played_on, produced, engineered, recorded_at, etc.)

3. Normalize vs. denormalize decision:
   - Query patterns: Album → Track → Personnel; Musician → Albums → Tracks; Engineer → Sessions → Albums
   - Timeline queries: Musician × Date (e.g., Philly Joe Jones recording schedule across the canon)
   - JSON flat files vs. SQLite vs. Postgres

4. Migration path:
   - Draft JSON → validated schema → seed data

**Deliverables:** *(produced 2026-06-10)*
- `docs/schema.md` ✓ — relational design doc (entities, ERD, query patterns, semantic-search design)
- `data/schema.sql` ✓ — DDL + views + functions for `_jazzcanon` (apply at Phase 4)
- `data/seed.json` ✓ — worked example (Kind of Blue) validating the shape
- `data/data-platform-handoff.json` ✓ — machine-readable handoff for implementation

**Gate:** John reviews schema, confirms it supports exploration goals.

---

## Phase 4: Web App — Architecture & Stack

**Goal:** Design the interactive exploration layer.

**Approach:**
1. **UX design** — John describes desired interactions:
   - Browse albums (filter by year, label, personnel)
   - View album → tracks → personnel
   - View musician → albums → tracks
   - Search across all fields
   - Timeline view: musician activity across the canon
2. **Stack selection** — Options to evaluate:
   - Static site (11ty, Astro) + client-side JS
   - Lightweight framework (Flask, FastAPI) + templates
   - Full SPA (React/Vue/Svelte) + API
   - Database-backed vs. static JSON
3. **Data-load & build pipeline (design)** — ingest validated JSON → `_jazzcanon` → identity-resolve
   persons → seed `core-canon` collection → **fetch + store album art** (Cover Art Archive → iTunes
   fallback, into `data/album-art/`) → generate search documents → embed (Ollama) → export static
   bundle (JSON + neighbors + art).
4. **Serving layer (decided 2026-06-11, staged)** — static export is the app's data source.
   When a live consumer appears: PostgREST read-only over the `_jazzcanon` views (`_jazzcanon_ro`
   role, single binary, config-only). Banked: an MCP server over the same views as the agent-facing
   interface. The views are the contract; no bespoke API code is planned.

**Deliverables:**
- `docs/architecture.md`
- `app/` skeleton (stack-dependent)

**Gate:** John approves stack and UX approach.

---

## Phase 5: Web App — Implementation

**Goal:** Build the interactive exploration app.

**Approach:**
1. Pair-programming loop (platform-agnostic):
   - Planning/spec agent: spec, review, test
   - Implementation harness: generate, iterate

2. Agent swarm opportunities (if supported by chosen coding model at Phase 4):
   - Parallel component development
   - Separate agents for frontend, backend, data ingestion

3. Testing:
   - Data integrity checks
   - UI/UX validation
   - Performance with ~100 albums × ~10 tracks × ~6 musicians

**Deliverables:**
- Working web app in `app/`
- `docs/deployment.md`

**Gate:** John uses the app, confirms it meets the "fun, cool, informative" bar.

---

## Phase 6: Deployment & Wrap

**Goal:** Make the app accessible.

**Approach:**
1. Deploy to vps2 (lightweight app hosting) or static host
2. Document maintenance procedures
3. Consider future extensions:
   - More albums/phases
   - Audio embeds (Apple Music links?)
   - Timeline visualization
   - "Six degrees of McCoy Tyner" graph

**Deliverables:**
- Live app URL
- `docs/maintenance.md`
- `README.md` for the project

---

## Cross-Cutting Concerns

### Epistemic Discipline
- Every research compile gets epistemic labels (obs / inf / unk)
- Personnel data flagged when source-conflicted
- John reviews before any data becomes "canonical"

### Multi-Agent Opportunities

Alert John when parallel work is possible:
- Multiple source compiles (Phase 1)
- Batch personnel extraction (Phase 2) — 10 concurrent agents
- Component development (Phase 5)

### Data Integrity
- Source URLs preserved for every claim
- Versioned data files (git-tracked)

### John's Learning Goals
- Experience chosen coding model as implementation partner
- Build first web app with these characteristics
- Deepen jazz knowledge (listening + reading)

---

## Open Questions (for future planning)

1. ~~Postgres vs JSON?~~ **Resolved 2026-06-10:** Postgres `_jazzcanon` is authoritative + semantic
   lab; a build step can export static JSON for the app. Best of both.
2. Should the app be public-facing or private (vps2 only)? (Also gates album-cover display: personal/private use is clearly fine; public reuse of cover art is a rights question.)
3. Do we want Apple Music / Spotify embeds?
4. Timeline visualization — static or interactive?
5. ~~Free-text NL search — worth a live backend?~~ **Posture set 2026-06-11:** staged serving —
   static-first; PostgREST read-only when a live consumer appears; MCP server banked. NL search rides
   whichever live layer exists; it never blocks the static app. (Final call still confirmable at Phase 4.)
6. Embeddings local to `_jazzcanon`, or also pushed to `_foundry` for cross-project RAG? (Phase 4)
7. Public-facing product name (DB namespace `_jazzcanon` decided 2026-06-10; codename `mccoy-tyner` stays).

---

*Plan version: 1.4*  
*Updated: 2026-06-11*  
*Changes from v1.3: Built-for-the-future block added (collections in schema v1.1, wide year CHECK —
the canon is a robust PoC, growth is ingest not migration). All five agents promoted to first-class,
model-scoped Claude Agents in `~/.claude/agents/` (briefs retained as design history). Staged serving
posture decided (static → PostgREST read-only → MCP, views as the single contract). End-to-end
Phase 1→4 dispatch runbook added (`docs/runbook.md`). Open Question 5 resolved as posture.*  
*Changes from v1.2: Album art added — Phase 2 captures cover-art refs (MBID + URLs) opportunistically; Phase 4 fetches/stores files (Cover Art Archive → iTunes), `album_art` table + MBID columns added to the schema. Plan made platform-agnostic (removed Hermes/coding-model-specific orchestration language — names roles, not products). Namespace decision (`_jazzcanon`) reflected in Open Questions.*  
*Changes from v1.1: Added Foundation Decisions block (Postgres `_jazzcanon` schema, two-engine semantic search). Added Canon Orchestrator decision-compression pass to Phase 1. Phase 3 designed contract-first. Resolved Open Question 1; added Qs 5–7.*  
*Changes from v1.0: Phase 3 (Personnel by Track) folded into Phase 2 (single deep research pass). Phases 4–7 renumbered to 3–6.*  
*Next step: Phase 1 dispatch — three specialist agents + Canon Orchestrator ready in `research/agent-briefs/`.*
