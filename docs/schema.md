# Data Model & Schema — Phase 3

**Version:** 1.0
**Date:** 2026-06-10
**Status:** Design complete. Schema is *applied* at Phase 4 (`CREATE SCHEMA _jazzcanon`), not now.
**Companions:** `data/schema.sql` (DDL) · `data/seed.json` (worked example) · `data/data-platform-handoff.json` (machine-readable handoff)

---

## 1. Purpose & altitude

This document maps the two research-capture contracts —
[`research/candidate-schema.md`](../research/candidate-schema.md) (Phase 1 canon) and
[`research/personnel-schema.md`](../research/personnel-schema.md) (Phase 2 personnel) — onto a
**relational query contract** in Postgres. It is designed **contract-first**: no Phase 1–2 data
exists yet, so the research schemas *are* the data shape. The job here is to decide how those JSON
records become tables, relationships, and constraints that serve the project's exploration goals.

The schema is the authoritative vocabulary. Every consumer — the web app, an agent, a CLI, a future
RAG pipeline — speaks this language.

---

## 2. Design principles

1. **Source-grounded, epistemic-first.** Every fact-bearing row carries an `epistemic` label
   (`obs`/`inf`/`unk`) and links to its source(s). This is the project's spine, not metadata to
   discard — the app *renders* "inferred" vs "directly sourced." Provenance is enforced by FK, not
   convention.
2. **People are one entity.** Performers, leaders, producers, engineers, and composers are all
   `person` rows. Without this, "Engineer → Sessions → Albums" and "Wayne Shorter compositions across
   the canon" are impossible. This is the single most important normalization decision in Phase 3.
3. **Identity is resolved, not assumed.** The research data identifies musicians by name string +
   variants. Phase 4 ingest runs a **person identity-resolution pass** that collapses "Bill Evans" /
   "William John Evans" into one `person` with a stable id. This step does not exist in the research
   data; the schema provides the structures for it (`person`, `person_name_variant`).
4. **Two query engines, one store.** Relational/recursive SQL answers the network questions
   (six-degrees, sideman co-occurrence, timelines). pgvector answers similarity/discovery. Both live
   in the same schema. See §8.
5. **Normalize freely — the corpus is tiny.** ~100 albums × ~10 tracks × ~6 musicians ≈ 1,000 tracks,
   ~6,000 performances, ~300–400 people. Generous normalization costs nothing and buys clean queries.
6. **Soft curation, hard facts.** Canon membership (`canon_status`) is editorial and mutable; album
   facts (personnel, sessions) are source-grounded. Keep the two conceptually separate even though
   both ride on `album`.

---

## 3. Namespace & target

- **Schema:** `_jazzcanon` (decided 2026-06-10; created at Phase 4, see naming note in `conventions.md`).
- **Instance:** shared Postgres 16, `vps8-core` `127.0.0.1:5433`.
- **Extensions:** `vector` (pgvector 0.8.2, already installed), `pg_cron` (available).
- **Roles (Phase 4):** `_jazzcanon_role` (read/write app), `_jazzcanon_ro` (read-only for app/agents).
- All objects live in `_jazzcanon`; nothing in `public`.

---

## 4. Entity map (ERD, text form)

```
                         ┌───────────┐         ┌──────────┐
                  ┌──────│   label   │         │  style   │
                  │      └───────────┘         └────┬─────┘
                  │ FK                              │
            ┌─────▼──────────────────────────┐     │ M:N (album_style) + album.style_primary_id
            │            album               │◄────┘
            │  id (slug) PK                   │
            │  leader_person_id ──────────┐   │
            │  label_id, style_primary_id │   │
            │  canon_status, priority     │   │
            │  search_document, embedding │   │
            └──┬───────────┬──────────┬───┘   │
               │1:N        │1:N       │1:N     │
        ┌──────▼───┐  ┌────▼─────┐ ┌──▼──────────────┐
        │ session  │  │  track   │ │  performance    │   ┌──────────────┐
        │ id PK    │  │ id PK    │ │  id PK          │   │   person     │
        │ album_id │  │ album_id │ │  album_id       │   │  id PK       │
        │ studio_id│◄┐│ session_id──┐ person_id ─────┼──►│  canonical_  │
        │ producer/│ ││ ...       │ │ instrument_id ──┼─┐ │  name        │
        │ engineer │ │└──────────┘ │ scope, epistemic│ │ │  sort_name   │
        └────┬─────┘ │      ▲      └──┬───────────┬──┘ │ │  search_doc, │
             │       │      │         │M:N        │M:N │ │  embedding   │
        ┌────▼────┐  │ ┌────┴──────┐  │      ┌────▼────┐│ └──────┬───────┘
        │ studio  │  │ │performance│  │      │perf_    ││        │1:N
        └─────────┘  │ │_track     │◄─┘      │session  ││ ┌──────▼────────────┐
                     │ └───────────┘         └─────────┘│ │person_name_variant│
        ┌────────────┴──┐                               │ └───────────────────┘
        │production_     │ (person × album/session)─────┘
        │credit          │
        └────────────────┘
        ┌────────────────┐   ┌──────────┐   ┌──────────────────────────────┐
        │ track_composer │   │  source  │◄──│ citation (source × ONE-OF:    │
        │ track × person │   └──────────┘   │  album|performance|track|     │
        └────────────────┘                  │  production_credit)           │
                                            └──────────────────────────────┘
```

---

## 5. Tables

Full DDL with constraints, indexes, and comments is in [`data/schema.sql`](../data/schema.sql). Below
is the reference with rationale. All `id` columns are `uuid` (default `gen_random_uuid()`) **except**
`album.id`, which is the kebab-case slug from the canon (the join key to all research data) and
`instrument`/`style`/`label`/`source` which use small natural or serial keys as noted.

### 5.1 Reference / vocabulary tables

| Table | Key | Columns | Rationale |
|-------|-----|---------|-----------|
| `instrument` | `id serial` | `name` (unique, from the taxonomy), `family` (enum) | Controlled taxonomy from `personnel-schema.md`. Enables "all pianists", instrument facets. |
| `style` | `id serial` | `code` (unique: `hard-bop`…`post-bop`), `display_name`, `description` | Controlled vocab as a table (not enum) so a "browse by style" page and descriptions are first-class. |
| `label` | `id serial` | `name` (unique), `name_slug`, `notes` | Enables "Blue Note discography" views and a label facet. ~20 rows. |
| `studio` | `id serial` | `name`, `city`, `name_slug`, `notes` | Enables "recorded at Van Gelder" queries. |
| `source` | `id serial` | `title`, `source_type` (enum), `url`, `notes` | **Global** source registry. Replaces the per-file local `S1/S2` maps — ingest maps local IDs to global rows. |

### 5.2 `album` — one row per album

| Column | Type | Notes |
|--------|------|-------|
| `id` | `text` PK | kebab slug = canon `id` / personnel `album_id`. The spine. |
| `title` | `text NOT NULL` | from candidate `album` |
| `artist_name` | `text NOT NULL` | leader/primary as cited (display) |
| `leader_person_id` | `uuid` FK→person | resolved at ingest; nullable until resolved |
| `year` | `int` | recording year preferred |
| `label_id` | `int` FK→label | |
| `style_primary_id` | `int` FK→style NOT NULL | |
| `recording_dates_text` | `text` | free-form fallback for ranges/uncertainty |
| `multi_session` | `bool` | from personnel schema |
| `canon_status` | enum `candidate`/`included`/`excluded` | editorial; default `candidate` |
| `canon_tier` | enum `consensus_core`/`contested`/`scope_call`/`exclude_suggested` (nullable) | provenance from the Orchestrator ballot |
| `priority` | enum `must_have`/`strong`/`consider` (nullable) | agent/orchestrator confidence |
| `inclusion_rationale` | `text` | why it's in the canon (renderable) |
| `epistemic` | enum | epistemic of the *inclusion* claim |
| `notes` | `text` | |
| `search_document` | `text` | composed blob for embedding (§8) |
| `embedding` | `vector(768)` | pgvector; dimension = Phase 4 model choice |
| `created_at`/`updated_at` | `timestamptz` | |

Secondary styles via `album_style(album_id, style_id, is_primary)` M:N; `style_primary_id` is the
denormalized convenience copy of the primary.

### 5.3 `person` — unified people

| Column | Type | Notes |
|--------|------|-------|
| `id` | `uuid` PK | stable internal id |
| `canonical_name` | `text NOT NULL UNIQUE` | "McCoy Tyner" |
| `sort_name` | `text` | "Tyner, McCoy" |
| `name_slug` | `text UNIQUE` | URL key |
| `notes` | `text` | |
| `search_document` | `text` | composed (name + instruments + albums + sidemen + era) |
| `embedding` | `vector(768)` | "musicians like X" |
| `created_at`/`updated_at` | `timestamptz` | |

`person_name_variant(id, person_id FK, variant_name, source_note)` — the dedup support table. Holds
`name_variants` from the personnel schema and any merge history. This is the substrate for the
identity-resolution pass (§7).

### 5.4 `session` — recording session

| Column | Type | Notes |
|--------|------|-------|
| `id` | `uuid` PK | |
| `album_id` | `text` FK→album NOT NULL, ON DELETE CASCADE | |
| `session_date` | `date` (nullable) | ISO; null when only a range/unknown |
| `session_date_text` | `text` | range/uncertainty fallback |
| `studio_id` | `int` FK→studio (nullable) | |
| `sequence` | `int` | order within album (1, 2, …) |
| `epistemic` | enum | |

Producers/engineers attach via `production_credit` (album- or session-level), not columns here — so
"engineer → sessions → albums" is one clean join.

### 5.5 `track` — one row per track per album

| Column | Type | Notes |
|--------|------|-------|
| `id` | `uuid` PK | |
| `album_id` | `text` FK→album NOT NULL, CASCADE | |
| `session_id` | `uuid` FK→session (nullable) | gives per-track date |
| `title` | `text NOT NULL` | |
| `track_number` | `int` | across all sides |
| `side` | `text` (nullable) | A/B/C/D or null (CD) |
| `duration_text` | `text` | "MM:SS" |
| `bonus_track`/`alternate_take` | `bool` | |
| `epistemic_track` | enum | |

Composers via `track_composer(track_id, person_id)` — composers are `person` rows (may have zero
performances). Enables "compositions by X across the canon".

### 5.6 Fact tables (carry epistemic + provenance)

**`performance`** — a person plays an instrument on an album.

| Column | Type | Notes |
|--------|------|-------|
| `id` | `uuid` PK | |
| `album_id` | `text` FK→album, CASCADE | |
| `person_id` | `uuid` FK→person | |
| `instrument_id` | `int` FK→instrument | |
| `scope` | enum `all-tracks`/`selected-tracks`/`unknown` | |
| `epistemic` | enum | |
| `notes` | `text` | instrument doubles, conflicts |

- `performance_track(performance_id, track_id)` — which tracks, when `scope = selected-tracks`.
  Empty for `all-tracks` (implied all).
- `performance_session(performance_id, session_id)` — which sessions, for multi-session personnel
  distinction (the personnel schema's `session_dates`).
- Unique: `(album_id, person_id, instrument_id)` — one musician+instrument per album (doubles =
  separate rows per instrument).

**`production_credit`** — a person served a non-instrumental role.

| Column | Type | Notes |
|--------|------|-------|
| `id` | `uuid` PK | |
| `album_id` | `text` FK→album, CASCADE | |
| `session_id` | `uuid` FK→session (nullable = whole album) | |
| `person_id` | `uuid` FK→person | |
| `role` | enum `producer`/`engineer`/`arranger`/`mixing`/`mastering`/`supervisor`/`other` | |
| `epistemic` | enum | RVG-at-Van-Gelder = `inf` |
| `notes` | `text` | |

### 5.7 `citation` — provenance with integrity

One table, real FKs, one CHECK — instead of four per-fact join tables:

```sql
citation (
  id            uuid PK,
  source_id     int  FK→source NOT NULL,
  album_id            text FK→album,
  performance_id      uuid FK→performance,
  track_id            uuid FK→track,
  production_credit_id uuid FK→production_credit,
  locator       text,   -- "p.124", liner notes, etc.
  CHECK (num_nonnull(album_id, performance_id, track_id, production_credit_id) = 1)
)
```

Every cited fact gets one `citation` row per source. Query "all claims backed by source X" or "what
sources support this performance" cleanly, with referential integrity the `text[]`-of-source-ids
approach can't give.

---

## 6. Enumerated types

`epistemic_label` (obs/inf/unk) · `canon_status` (candidate/included/excluded) ·
`canon_tier` (consensus_core/contested/scope_call/exclude_suggested) ·
`priority_label` (must_have/strong/consider) · `performance_scope` (all-tracks/selected-tracks/unknown) ·
`production_role` (producer/engineer/arranger/mixing/mastering/supervisor/other) ·
`instrument_family` (brass/woodwinds/keyboards/strings/percussion/other) ·
`source_type` (book/web/liner-notes/discography/other).

---

## 7. The identity-resolution pass (Phase 4 ingest — flagged, not built)

The research data has **no person IDs** — musicians are name strings with `name_variants`. Before any
"Musician → …" query works, ingest must:

1. Collect every distinct `name` and `name_variants[]` across all `personnel-draft.json` records
   (performers, leaders, producers, engineers, composers).
2. Cluster to canonical persons (exact match → variant match → fuzzy review). Borderline merges are
   surfaced for John, not auto-merged — same epistemic discipline as everything else.
3. Create `person` rows; record every surface form in `person_name_variant`.
4. Re-point `performance.person_id`, `production_credit.person_id`, `track_composer.person_id`,
   `album.leader_person_id` to the resolved ids.

This is real work the research phase does not cover. It belongs in the Phase 4 ingest script and is
called out here so it is not mistaken for free.

---

## 8. Semantic search design (the priority)

Two complementary engines, both in `_jazzcanon`.

### 8.1 pgvector — similarity & discovery

**Search documents** (generated text per row, then embedded):

- **Album** `search_document` = `title · artist · year · label · style(s) · full personnel
  "Name (instrument)" · composer list · notes`. Powers "albums like *Kind of Blue*", NL queries.
- **Person** `search_document` = `canonical_name · instruments played · albums · frequent sidemen ·
  era span · notes`. Powers "musicians like Elvin Jones".

`embedding vector(768)` columns hold the vectors. **Model decided (2026-06-10):** local
`nomic-embed-text` (768-dim) via Ollama on vps4 — free, self-hosted, working-first. The choice is
fully reversible: re-embedding the whole corpus is ~500 short documents, under a minute, pennies even
on a paid API. Swapping later = change the column dimension + re-embed. Indexed with HNSW
(`vector_cosine_ops`).

> **Decision deferred:** keep embeddings local to `_jazzcanon`, or also push album/person documents
> into `_foundry.embeddings`/`_foundry.documents` for cross-project RAG. Recommend local for a
> single-purpose tool; leave the door open. (Open Question 6 in the plan.)

### 8.2 Relational / recursive — networks

Embeddings cannot do these; SQL does:

- **Six degrees of McCoy Tyner** — recursive CTE over the `performance` co-occurrence graph
  (`fn_degrees_between(person_a, person_b)`).
- **Sideman co-occurrence** — `v_sideman_network`: person-pairs sharing ≥1 album, with weights.
- **Timeline** — `v_musician_timeline`: person × session_date × album (the Philly Joe Jones schedule).
- **Engineer → sessions → albums** — `v_engineer_sessions`.

### 8.3 Static export (resolves the deploy tension)

The corpus is small enough that a build step can precompute the album×album nearest-neighbor list and
export the whole dataset as static JSON. The app can then ship as a **static site** with full
similarity discovery and faceted/keyword search — no always-on backend. The *only* feature that needs
a live backend is free-text NL search ("type a sentence"). So: **Postgres is the authoring store and
semantic lab; a build step feeds a simple static app.** Whether to add the live NL backend is a
Phase 4 call (Open Question 5).

---

## 9. Query patterns → read contract (views)

Defined in `schema.sql`:

| Stated goal (plan) | View / function |
|--------------------|-----------------|
| Album → tracks → personnel | `v_album_detail`, `v_track_personnel` |
| Browse/filter albums (year, label, style, personnel) | `v_album_card`, `v_album_personnel` |
| Musician → albums → tracks | `v_musician_albums` |
| Musician × date timeline | `v_musician_timeline` |
| Engineer → sessions → albums | `v_engineer_sessions` |
| Six degrees | `fn_degrees_between(a, b)` (recursive CTE) |
| Sideman network / graph | `v_sideman_network` |
| Composition by X | `v_composer_works` |
| Search document source | `v_album_search_source`, `v_person_search_source` (feed embedding build) |
| "Why is this in the canon / how sure are we?" | epistemic + `citation` exposed in detail views |

Write contracts (ingest functions, embedding refresh) are Phase 4 — the data arrives via ingest of
validated JSON, not interactive inserts, so heavy write-side functions are deferred.

---

## 10. Mapping: research schemas → relational

| Research field | Lands in |
|----------------|----------|
| candidate `id` | `album.id` |
| candidate `artist`/`album`/`year` | `album.artist_name`/`title`/`year` |
| candidate `label` | `label` row + `album.label_id` |
| candidate `style_primary`/`style_tags` | `album.style_primary_id` + `album_style` |
| candidate `priority`/`epistemic`/`rationale`/`include` | `album.priority`/`epistemic`/`inclusion_rationale`/`canon_status` |
| ballot `tier` | `album.canon_tier` |
| candidate/ballot `sources` | `source` rows + `citation`(album) |
| personnel `album_id` | join key → `album.id` |
| personnel `recording_dates`/`multi_session`/`studio` | `session` rows (+ `studio`), `album.multi_session` |
| personnel `producer`/`engineer`/`epistemic_production` | `production_credit` rows |
| personnel `personnel[]` | `person` (resolved) + `performance` (+ `performance_track`/`_session`) |
| personnel `personnel[].instrument` | `instrument` row + `performance.instrument_id` |
| personnel `personnel[].name_variants` | `person_name_variant` |
| personnel `tracks[]` | `track` rows |
| personnel `tracks[].composers` | `track_composer` + `person` |
| personnel `tracks[].personnel` | `performance_track` (resolved) |
| every `sources[]` | `citation` rows |

---

## 11. Migration / ingest path (Phase 4)

```
canon-draft.json (include:true) ─┐
                                 ├─► validate ─► identity-resolve persons ─► load _jazzcanon
personnel-draft.json ────────────┘                                    │
                                                                       ├─► generate search_documents
                                                                       ├─► embed (Ollama) → vector cols
                                                                       └─► build static export (JSON + neighbors)
```

Idempotent loader keyed on `album.id` and resolved `person.id`. JSON files stay git-tracked and remain
the human-editable source; Postgres is the query/derive layer.

---

## 12. Decisions & remaining open questions

**Decided 2026-06-10 (John):**
- **Namespace** — `_jazzcanon` for all official paperwork; `mccoy-tyner` stays the codename.
- **Embedding model** — local `nomic-embed-text` (768) on vps4, working-first and reversible (§8.1).
- **Post-Bop** — Modal agent absorbs it (Option A).

**Still open (none block Phase 3):**
1. **Embeddings local vs pushed to `_foundry`** — single-purpose vs cross-project RAG. *Recommend
   local, door open.* (Phase 4)
2. **Live NL search backend** — or stop at precomputed similarity + faceted filter on a static site?
   *Recommend defer; static-first.* (Phase 4)
3. **`canon_tier`/`priority` on `album`** — keep this Phase-1 curation provenance in the album table
   (renderable "why it's here"), or drop after selection? *Recommend keep — it's cheap and tells a
   story.*
4. **Product name** — the public-facing name, distinct from the `_jazzcanon` namespace. Open.

None of these block Phase 3 — the schema is complete and internally consistent as designed.
