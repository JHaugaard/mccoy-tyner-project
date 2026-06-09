# McCoy Tyner Project — Phased Plan v1

**Project:** Canonical Jazz Albums (Cool Jazz → Hard Bop → Modal Jazz)  
**Directory:** `~/dev/active/mccoy-tyner/`  
**Approach:** Deliberate, no one-shotting. Research-first, data model emerges from findings.  
**Orchestration:** Hermes (research, planning, architecture) → Coding model (TBD — chosen at Phase 4) for implementation and agent orchestration  
**Research Tool:** *research-compiler* skill for source-grounded compilation

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

4. **John's evaluative sort** — John listens, reads, applies taste at the margins.
   - No quotas per phase
   - No hard category boundaries
   - Post-bebop, pre-Fusion, no Free Jazz

**Deliverables:**
- `research/source-<name>-compile.md` (per source)
- `research/canon-synthesis.md` (merged analysis)
- `data/canon-draft.json` (structured album list, ~100 entries)

**Parallel opportunities:** Multiple source compiles can run simultaneously via:
- Hermes `delegate_task` subagents (up to 3 concurrent)
- Coding model agent swarm (if available and configured at Phase 4)
- Hermes `researcher` profile for background compiles

**Gate:** John reviews canon-draft.json, confirms or adjusts the ~100.

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

## Phase 3: Data Model & Schema Design

**Goal:** Lock the data structure before building the app.

**Approach:**
1. Review Phase 1–2 data shapes
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

**Deliverables:**
- `docs/schema.md`
- `data/schema.sql` (if SQL)
- `data/seed.json` (validated, canonical)

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

1. Should we ingest final data into Postgres (for query flexibility) or keep as JSON (for simplicity)?
2. Should the app be public-facing or private (vps2 only)?
3. Do we want Apple Music / Spotify embeds?
4. Timeline visualization — static or interactive?

---

*Plan version: 1.1*  
*Updated: 2026-06-09*  
*Changes from v1.0: Phase 3 (Personnel by Track) folded into Phase 2 (single deep research pass). Phases 4–7 renumbered to 3–6. Phase 3 schema note and timeline query use case added.*  
*Next step: Phase 1 dispatch — three specialist agents ready in `research/agent-briefs/`*
