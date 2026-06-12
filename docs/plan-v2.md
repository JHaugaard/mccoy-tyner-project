# The Jazz Canon — Phased Plan v2

**Project (external):** The Jazz Canon · `jazzcanon.com` (domain registered; Cloudflare for **DNS only** — not a hosting/stack decision)
**Project (codename):** `mccoy-tyner` — the working repo name; stays as long as John likes
**DB namespace:** `_jazzcanon`
**Directory:** `~/dev/active/mccoy-tyner/`
**Approach:** Deliberate, measured, no one-shotting. Research-first; prove the pipeline small before scaling.
**Orchestration:** Platform-agnostic — names *roles*, not products. (Proceeding in Claude Code.)

> **v2 supersedes plan-v1.md (v1.4).** v1 is retained as history. The two structural changes in v2 are
> (1) the framing pivot — **"Starting with 100"** instead of **"Paring to 100"** — and (2) the **merge** —
> the domain specialist gathers personnel in the same pass, so old Phase 1 (canon) and Phase 2
> (personnel) collapse into one gathering pass. Everything else from v1.4 is carried forward intact.

---

## The v2 thesis (what changed and why)

**From jewel box to growing collection.** v1 framed the work as *paring* a large pool down to a coveted
~100 — agents competing for scarce slots, heavy culling, judgment-dominant. v2 reframes: the corpus is an
**expansive collection that grows organically**, and "the canon" becomes a *curated lens over* the
collection rather than a hard cap. Growth is a feature, not scope creep. The ~100 is now a **starting
target**, not a ceiling. The style range is unchanged for this pass (Cool / Hard Bop / Modal; post-bebop,
pre-Fusion; no Free Jazz); future **domain-specialist agents** (fusion, electronic, niches) are **banked**
for later, not built now.

**One pass, gather everything (the merge).** Because the agents are no longer gatekeepers fighting over
slots, there's no reason to split "find the album" from "find its personnel." When a specialist is
neck-deep in an album it already has the sources loaded — gathering personnel, tracks, dates, and
locations right then **reuses context you've already paid for**. The separate personnel agent re-discovers
each album from scratch; the merged agent does not. So the specialist now does the **full record** in one
pass. *(Decision rationale: 2026-06-12. The seam stays open — see below.)*

**Keep the seam.** The schema keeps personnel a **cleanly separable concern** (its own block, its own
epistemic labels) so the split can be re-adopted later at near-zero cost. Two futures justify splitting:
(a) the POC shows the merged agent gets **sloppy on personnel** because canon-judgment eats its attention
— split with evidence, not speculation; (b) the project ever goes **programmatic/API-billed at scale**,
where routing rote extraction to a cheaper model becomes a real lever. Neither is true today.

**Cost reframe.** These dispatches run inside John's Max **subscription** interactive pool, which he has
never dented. The marginal dollar cost of a 30-album POC is **$0**, whichever model. Therefore model
choice is made on **quality and speed, never cost** (see Model Strategy).

---

## Foundation Decisions (carried from v1.4, still locked)

- **Storage:** Shared Postgres 16 on `vps8-core` (native, `127.0.0.1:5433`). Project owns a **schema**
  (`_jazzcanon`), not a database. `DROP SCHEMA … CASCADE` is the kill switch. pgvector 0.8.2 + pg_cron
  installed. Schema *created* at the platform-build phase; JSON drafts are the source of truth until then.
- **Two-engine semantic search:** (1) **pgvector** over composed per-album / per-musician search documents
  for similarity & discovery; (2) **relational/recursive SQL** for networks (six-degrees, sideman
  co-occurrence, timelines). A build step exports a **static bundle** (JSON + precomputed neighbors) so the
  app needs no live backend; only free-text NL search would need one.
- **Built to outlive the first canon:** albums belong to named **collections** (the canon = seed collection
  `core-canon`); **styles are rows, not enums**; the year CHECK is wide. Adding albums / artists / styles /
  whole new canons is an **ingest run, never a migration** (schema v1.1, `docs/schema.md` §5.2b). *This is
  the structural feature that makes "Starting with 100" free.*
- **Agents are first-class:** project agents live in `~/.claude/agents/` as named, self-contained,
  model-scoped Claude Agents. Briefs in `research/agent-briefs/` retained as design history.
- **Serving posture (staged):** the schema's views/functions ARE the API contract. L1 static export
  (default) → L2 **PostgREST read-only** over `_jazzcanon` views when a live consumer appears → L3 **MCP
  server** (banked) wrapping the same views for agent/Claude access. Every layer speaks one vocabulary.

### New locks (2026-06-12)

- **Framing:** "Starting with 100" — collection grows organically; canon is a curated lens. *Locked.*
- **Merge:** domain specialist gathers the full record (canon + personnel) in one pass; seam kept in
  schema for a future split. *Locked.*
- **POC-first:** first real dispatch is a **10-album proof-of-concept per specialist** (3 × 10 = 30),
  to debug the whole pipeline at small blast radius. *Locked.*
- **Dispatch ledger:** a single "what exists" manifest the agents read before running and John updates
  after accepting picks — prevents cross-dispatch duplication; the spine of repeat dispatch and agent
  self-awareness. *Locked (build at Phase 1 kickoff).*
- **Music posture: Apple Music** (decided 2026-06-12 — John is an Apple Music subscriber; supersedes the
  earlier Spotify lean). Capture an **`apple_album_id` as data** now (free iTunes `collectionId`); player
  deferred to serving. Two serving doors: **free iTunes Search API** (30-sec previews + artwork + Apple
  Music links, no auth, $0) for the public site; paid **MusicKit** ($99/yr Apple Developer Program — John
  is enrolling) for the embedded player + full-length playback for Apple Music subscribers, incl. John.
  *Locked.*
- **Model posture:** quality/speed not cost; Fable 5 where its edge is real, with a free-window A/B test
  vs. Opus 4.8 before 2026-06-22. *Locked (see Model Strategy).*

---

## The Dispatch Model (new — the heart of v2)

This is the loop that makes a *growing* collection cheap and good. Four parts:

### 1. The dispatch ledger — `data/dispatch-ledger.json`
A running manifest of **what the collection already contains** and **what has already been dispatched**.
Every specialist reads it **before** a run and treats listed albums as already-claimed (don't re-surface
*Kind of Blue*). John updates it **after** he accepts picks from a dispatch. Minimal shape:

```json
{
  "albums_in_collection": [{ "id": "...", "artist": "...", "title": "...", "year": 1959, "style": "modal" }],
  "dispatches": [
    { "id": "d01", "agent": "modal", "date": "2026-06-13", "requested": 10, "accepted": 8, "model": "fable-5" }
  ],
  "last_updated": "2026-06-13"
}
```

It is the agent's **memory of what it has accomplished** (point #3 of John's 2026-06-12 list) and the
guard against duplication across any number of future dispatches.

### 2. The learning loop — `research/cull-notes.md`
When John declines or culls a pick, he appends a one-line **verdict with reason** ("too bebop", "edges
into fusion", "comp/reissue, prefer original"). Specialists read this file before running and **calibrate**
to John's taste. This is learning-by-feedback — no model training, no infrastructure — and directly
answers "can the agents get better along the way?" (point #4): *the model* doesn't learn, but *the agent*
does, through the ledger (what's done) + cull-notes (what John rejected and why).

### 3. Dispatch spec — how a run is planned
Each dispatch is parameterized: **style** · **count** · **exclude = current ledger** · **model** ·
**output path**. A dispatch is "spec a run, send it, review, accept into ledger, append cull-notes." That
repeatable unit is how the collection grows past 100 without re-planning from scratch.

### 4. The Orchestrator becomes a gardener
Under the pivot the Canon Orchestrator is **no longer a one-time gatekeeper**. It becomes a **recurring
gardener**: run it periodically over the accumulated collection to surface tier shifts, newly-contested
calls, gaps, and overlaps. Scope (style boundaries) becomes a **per-agent property**, so adding a future
fusion agent doesn't disturb the existing three.

---

## Phases

> Phase numbers are kept aligned to v1 for continuity. The visible change: **old Phase 1 + Phase 2 are
> merged** into a single one-pass gathering phase (now "Phase 1–2"). Schema stays Phase 3 (done), platform
> Phase 4, app 5, deploy 6.

### Phase 0 — Infrastructure & Conventions  *(complete)*
Folder structure, naming conventions, git, the research-compile workflow. Deliverable `docs/conventions.md`.

### Phase 1–2 — One-Pass Gathering (canon **and** personnel, merged)
**Goal:** For each album a specialist judges to have merit, produce the **complete record in one pass** —
canon metadata *and* personnel/tracks/sessions/dates/locations — source-grounded, epistemically labeled.

**The merge in practice.** The domain specialist no longer hands off to a personnel agent. While
researching an album it gathers, in the same record:
- canon metadata (title, artist, year, label, style, why-it-belongs);
- core ensemble + production credits (engineer, producer, studio, recording dates);
- session contributors (`scope: selected-tracks`) and track-level assignments where sources allow;
- per-session dates/locations for multi-session albums;
- album-art + Apple/iTunes + MusicBrainz **reference IDs** (captured; files/links resolved at Phase 4).

**Proof-of-concept first (the kink-finder).** Before any scaled run, each of the three specialists does a
**10-album POC** (3 × 10 = 30). Purpose is to debug the *contract end to end* — agent → candidate JSON →
schema validation → John's review → ledger update — while the blast radius is 30 rows, not 100. No slot
competition: agents gather what has merit, not what wins a fight.

**Fable 5 A/B (free window, closes 2026-06-22).** Run one POC dispatch on **Fable 5** and the same on
**Opus 4.8**; compare candidate lists and personnel quality side by side. Costs nothing in the free window
and produces real evidence for whether Fable 5 is worth paying for after 2026-06-23.

**Deliverables:**
- `research/{hard-bop,cool-jazz,modal-jazz}-candidates.md` (merged records, per specialist)
- `data/dispatch-ledger.json` (initialized this phase) · `research/cull-notes.md`
- `data/canon-draft.json` (accepted records; `include` set as John promotes them)

**Gate:** John reviews each POC batch; accepts into the ledger; appends cull-notes. **The POC gate is also
the decision point on the merge:** if personnel quality is clean from the merged pass, stay merged; if the
agent is sloppy on personnel, open the seam (split a personnel agent back out) — *with evidence*.

**Pending (your step 2):** the three specialist agents must be **updated to the merged role** (absorb the
personnel contract; read ledger + cull-notes before running; emit the full record). `jazz-personnel-researcher`
is **retained but dormant** — the seam — not deleted.

### Phase 3 — Data Model & Schema  *(complete; two pending changes flagged)*
Locked: `docs/schema.md` (v1.1), `data/schema.sql`, `data/seed.json`, `data/data-platform-handoff.json`.
**Pending changes (your step 3, after agents):**
1. **Apple Music ID column** — `apple_album_id` (album), optional `apple_track_id` (track), mirroring the
   album-art MBID pattern. Captured in Phase 1–2 (free iTunes Search `collectionId`); column added before ingest.
2. **Merge-seam confirmation** — verify the personnel block in the contract is cleanly separable so a
   future split needs no migration. (Likely already true; verify, don't assume.)

### Phase 4 — Platform Build & App Architecture
Apply `_jazzcanon`; ingest validated JSON; identity-resolve persons (**borderline merges go to John**);
seed `core-canon`; fetch album art (Cover Art Archive → iTunes/Apple); build search
documents; embed (Ollama, vps4); export static bundle. App stack/UX choices remain John's, decided here.
*Hosting candidates open (vps2 / Fly.io / Cloudflare Pages) — a later, explicit discussion; the static
bundle runs identically on all three, so the DB does not constrain the host.*

### Phase 5 — App Implementation
Build the interactive exploration app against the static bundle (and, if/when present, the live layer).
Browse albums; album → tracks → personnel; musician → albums → tracks; search; timelines; "six degrees".

### Phase 6 — Deployment & Wrap
Deploy to the chosen host; document maintenance; bank future extensions (deep-link players, more
collections, graph viz). Live URL, `docs/maintenance.md`, `README.md`.

---

## Model Strategy (Fable 5 / Opus 4.8 / Sonnet)

- **Fable 5** (released 2026-06-09; 1M context; top agentic/vision; **$10/M in, $50/M out = 2× Opus 4.8**;
  **free on subscription through 2026-06-22**, credits after 2026-06-23). Edge is real in exactly two
  spots: the **front-line gathering agents** (judgment-heavy canon calls) and **Phase 4 ingest /
  identity-resolution** (large context, fiddly reasoning). Wasted on schema edits, runbook prose,
  mechanical merges.
- **Opus 4.8** — the default strong model for agents and judgment work; the A/B baseline against Fable 5.
- **Sonnet** — high-volume rote extraction *if/when the seam reopens*; mechanical transforms.
- **Decision rule:** on John's subscription the dollar delta is $0, so **choose by quality and speed**.
  The A/B in the free window produces the evidence for any post-June-22 spend.

---

## Music / Apple Music posture

**Apple all the way** (decided 2026-06-12 — John is an Apple Music subscriber; supersedes the earlier
Spotify lean). Apple beats Spotify here on both goals: Spotify killed its 30-second previews (Nov 2024),
Apple still serves them — and via Apple, John gets **full-length playback in his own research tool** as a
subscriber. Two doors:
- **Free (iTunes Search/Lookup API, no token, $0):** Apple Music links, cover artwork, and 30-second
  `previewUrl` clips. Powers the public site's "click to hear it" with no visitor login.
- **Paid (MusicKit, $99/yr Apple Developer Program):** embedded web player + full-length playback for
  Apple Music subscribers (incl. John), and previews without visitor auth. Needs a signed developer token
  (John is enrolling in the Developer Program).
- **Now (data):** capture an `apple_album_id` (free iTunes `collectionId`) + MusicBrainz MBIDs as fields.
  No player, no OAuth, no spend in the data phase.
- **Later (serving):** free iTunes previews for the public site; the MusicKit player only if/when
  full in-page playback is wanted. Deferred.

---

## Mission-creep guardrails (Claude's standing job, per John 2026-06-12 #5)

The line, stated so it can be enforced:
- **On the efficiency side (do now):** the dispatch ledger, the learning loop, the merged one-pass agent,
  the 10-album POC, the Fable 5 free-window A/B. These make the core loop cheaper and better.
- **On the creep side (defer):** a live Apple Music / MusicKit player, future domain agents (fusion/electronic), a
  two-agent personnel pipeline built *before* evidence demands it, hosting/stack commitments. Capture data
  and keep seams open; don't build serving features inside a data phase.
- **Standing test:** *does this make the next dispatch cheaper or the records better right now?* If not,
  it's banked, not built. Claude flags creep when it sees it.

---

## Cross-Cutting Concerns (carried forward)

- **Epistemic discipline:** every record carries `obs / inf / unk` labels + source citations; John reviews
  before anything becomes canonical.
- **Data integrity:** source URLs preserved per claim; JSON drafts are the human-editable source of truth
  and are git-tracked.
- **Multi-agent opportunities:** three specialists run in parallel; Phase 4 ingest is one-shot-able.

---

## Open Questions

1. ~~Postgres vs JSON?~~ Resolved — Postgres `_jazzcanon` authoritative + static export for the app.
2. Public-facing vs. private? (Gates cover-art display rights and any public Apple Music linking.)
3. ~~Streaming embeds?~~ Resolved — **Apple Music** (decided 2026-06-12). Free iTunes previews on the
   public site; paid MusicKit player deferred to serving; `apple_album_id` captured as data now.
4. Timeline visualization — static or interactive? (Phase 5)
5. ~~NL search live backend?~~ Posture set — staged serving; NL search rides whichever live layer exists.
6. Embeddings local to `_jazzcanon` or also pushed to `_foundry` for cross-project RAG? (Phase 4)
7. Hosting/stack — vps2 / Fly.io / Cloudflare Pages — **explicit later discussion**; not constrained by DB.
8. Fable 5 worth paying for post-June-22? — answered by the Phase 1–2 A/B evidence.

---

## Pending next steps (John's measured sequence, 2026-06-12)

1. **Now:** John reviews this plan-v2 and runbook-v2. *(this step)*
2. **Then:** update the three specialist agents to the **merged role** (+ ledger/cull-notes awareness);
   retain `jazz-personnel-researcher` dormant as the seam.
3. **Then:** schema changes — Apple Music ID column + merge-seam confirmation.
4. **Then:** run the 10-album POC (with the Fable 5 / Opus A/B) before 2026-06-22 if possible.

---

*Plan version: 2.0 · 2026-06-12*
*Supersedes plan-v1.md (v1.4), retained as history.*
*Changes from v1.4: framing pivot to "Starting with 100" (collection grows; canon is a curated lens);
the merge (specialist gathers personnel in one pass; old Phases 1+2 collapse; seam kept for a future
split); POC-first 10-album dispatch; dispatch-ledger + cull-notes learning loop; Orchestrator reframed as
recurring gardener; Fable 5 model strategy + free-window A/B; Apple-Music-as-data posture (free iTunes previews; paid MusicKit player deferred);
mission-creep guardrails made explicit; external name "The Jazz Canon" / jazzcanon.com (DNS only).*
