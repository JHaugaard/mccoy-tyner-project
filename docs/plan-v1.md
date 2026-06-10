# McCoy Tyner Project — Phased Plan v1

**Project:** Canonical Jazz Albums (Cool Jazz → Hard Bop → Modal Jazz)  
**Directory:** `~/dev/active/mccoy-tyner/`  
**Approach:** Deliberate, no one-shotting. Research-first, data model emerges from findings.  
**Orchestration:** Hermes (research, planning, architecture) → Coding model (TBD — chosen at Phase 4) for implementation and agent orchestration  
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

2. **Source strategy** —
   - AllMusic (Credits tab)
   - Wikipedia album articles (Personnel section)
   - Tom Lord's Jazz Discography (session-level authority)
   - JazzDiscography.com
   - Liner notes (digitized via Google Books, archive.org, label reissue pages)
   - Recording label discographies (Blue Note, Prestige, Impulse!, Columbia, Verve, ECM)

3. **Agent architecture** — 10 parallel agents, ~10 albums each, shared brief and schema. No style specialization needed; the task is identical per album. Instrument names and musician name forms follow a controlled vocabulary defined in `research/personnel-schema.md` so records are consistent across all agents.

**Note:** Track-level personnel (originally planned as a separate Phase 3) is captured here opportunistically in the same pass. When sources provide track assignments, they are recorded. `track_assignments_complete` flags what the data platform can trust.

**Deliverables:**
- `research/personnel-batch-NN.md` (one per agent, 10 total)
- `research/personnel-sources-compile.md` (source evaluation notes)
- `data/personnel-draft.json` (merged from agent outputs — album → personnel + tracks)

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

**Deliverables:**
- `docs/architecture.md`
- `app/` skeleton (stack-dependent)

**Gate:** John approves stack and UX approach.

---

## Phase 5: Web App — Implementation

**Goal:** Build the interactive exploration app.

**Approach:**
1. Hermes + Coding model pair programming:
   - Hermes: spec, review, test
   - Coding model: generate, iterate

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
2. Should the app be public-facing or private (vps2 only)?
3. Do we want Apple Music / Spotify embeds?
4. Timeline visualization — static or interactive?
5. Free-text NL search — worth a live backend, or stop at precomputed similarity + faceted filter? (Phase 4)
6. Embeddings local to `_jazzcanon`, or also pushed to `_foundry` for cross-project RAG? (Phase 4)
7. Final project name + DB namespace binding (Phase 4).

---

*Plan version: 1.2*  
*Updated: 2026-06-10*  
*Changes from v1.1: Added Foundation Decisions block (Postgres `_jazzcanon` schema, namespace binding deferred to Phase 4, two-engine semantic search). Added Canon Orchestrator decision-compression pass to Phase 1. Phase 3 designed contract-first (schema.md, schema.sql, seed.json, handoff produced). Resolved Open Question 1; added Qs 5–7.*  
*Changes from v1.0: Phase 3 (Personnel by Track) folded into Phase 2 (single deep research pass). Phases 4–7 renumbered to 3–6.*  
*Next step: Phase 1 dispatch — three specialist agents + Canon Orchestrator ready in `research/agent-briefs/`.*
