# McCoy Tyner Project — Phased Plan v1

**Project:** Canonical Jazz Albums (Cool Jazz → Hard Bop → Modal Jazz)  
**Directory:** `~/dev/active/mccoy-tyner/`  
**Approach:** Deliberate, no one-shotting. Research-first, data model emerges from findings.  
**Orchestration:** Hermes (research, planning, architecture) → Coding model (TBD — chosen at Phase 5) for implementation and agent orchestration  
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
   - Post-be-bop, pre-Fusion, no Free Jazz

**Deliverables:**
- `research/source-<name>-compile.md` (per source)
- `research/canon-synthesis.md` (merged analysis)
- `data/canon-draft.json` (structured album list, ~100 entries)

**Parallel opportunities:** Multiple source compiles can run simultaneously via:
- Hermes `delegate_task` subagents (up to 3 concurrent)
- Coding model agent swarm (if available and configured at Phase 5)
- Hermes `researcher` profile for background compiles

**Gate:** John reviews canon-draft.json, confirms or adjusts the ~100.

---

## Phase 2: Primary Musicians & Production Personnel

**Goal:** Extract key personnel per album.

**Approach:**
1. **Primary musicians** — For each album, identify:
   - Core ensemble (e.g., Kind of Blue quintet)
   - One-track/session contributors (e.g., Jimmy Cobb on one track)
   - Instrument per musician

2. **Production personnel** — Identify:
   - Engineer (e.g., Rudy Van Gelder)
   - Producer
   - Recording studio
   - Label

3. **Source strategy** —
   - AllMusic discographies
   - Liner notes (where digitized)
   - Wikipedia album pages
   - Dedicated jazz databases (JazzDiscography, etc.)

**Deliverables:**
- `data/personnel-draft.json` (album → primary musicians + production)
- `research/personnel-sources-compile.md` (source evaluation)

**Parallel opportunities:**
- Album personnel can be extracted in batches by decade or by label
- Delegate to subagents per batch

**Gate:** John spot-checks 5–10 albums for accuracy.

---

## Phase 3: Personnel by Track

**Goal:** Track-level musician assignment.

**Approach:**
1. For each album, map which musicians played on which tracks
2. Handle edge cases:
   - Alternate takes
   - Bonus tracks
   - Compilations vs. original sessions

3. Data validation:
   - Cross-reference with sessionographies where available
   - Flag uncertain assignments

**Deliverable:**
- `data/track-personnel.json` (album → track → [musicians])

**Note:** This is the most granular and potentially most error-prone phase. May need iterative refinement.

**Gate:** John confirms data model supports the exploration he wants.

---

## Phase 4: Data Model & Schema Design

**Goal:** Lock the data structure before building the app.

**Approach:**
1. Review Phases 1–3 data shapes
2. Design schema:
   - Album entity
   - Musician entity (with instrument taxonomy)
   - Track entity
   - Production entity
   - Relationships (played_on, produced, engineered, etc.)

3. Normalize vs. denormalize decision:
   - Query pattern: Album → Track → Personnel
   - Also: Musician → Albums → Tracks
   - JSON flat files vs. SQLite vs. Postgres

4. Migration path:
   - Draft JSON → validated schema → seed data

**Deliverables:**
- `docs/schema.md`
- `data/schema.sql` (if SQL)
- `data/seed.json` (validated, canonical)

**Gate:** John reviews schema, confirms it supports exploration goals.

---

## Phase 5: Web App — Architecture & Stack

**Goal:** Design the interactive exploration layer.

**Approach:**
1. **UX design** — John describes desired interactions:
   - Browse albums (filter by year, label, personnel)
   - View album → tracks → personnel
   - View musician → albums → tracks
   - Search across all fields
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

## Phase 6: Web App — Implementation

**Goal:** Build the interactive exploration app.

**Approach:**
1. Hermes + Coding model pair programming:
   - Hermes: spec, review, test
   - Coding model: generate, iterate

2. Agent swarm opportunities (if supported by chosen coding model at Phase 5):
   - Research (list compilation; track personnel)
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

## Phase 7: Deployment & Wrap

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
- Every research compile gets epistemic labels (direct observation / inference / uncertain)
- Personnel data flagged when source-conflicted
- John reviews before any data becomes "canonical"

### Multi-Agent Opportunities

Alert John when parallel work is possible:
- Multiple source compiles (Phase 1)
- Batch personnel extraction (Phase 2)
- Component development (Phase 6)

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
3. Should the app be public-facing or private (vps2 only)?
4. Do we want Apple Music / Spotify embeds?
5. Timeline visualization — static or interactive?

---

*Plan version: 1.0*  
*Date: 2026-05-19*  
*Next step: John reviews, adjusts, approves Phase 0 start*
