# Jazz Canon — Growth Runbook

Operational reference for everything that happens after the v1 canon is in Postgres.
Covers: adding albums, enriching records, admin tooling, automation inventory, and checklists.

**Status: Stub — tighten as each section is exercised.**

---

## 1. The Pipeline (Overview)

```
TRIGGER (foray type)
    │
    ▼
RESEARCH (agent dispatch → data/batches/YYYY-MM-DD-<label>.json)
    │
    ▼
REVIEW (John blesses the batch file)
    │
    ▼
INGEST (scripts/ingest.py → _jazzcanon on vps8-core)
    │
    ▼
ENRICH (scripts/enrich.py → MBID / Apple ID / cover art / catalog# / embeddings)
    │
    ▼
LOG (dispatch-ledger.json entry)
```

Postgres is the system of record. JSON batch files are staging artifacts — ephemeral once ingested, kept for provenance.

---

## 2. Foray Types

| Type | Example trigger | Who researches | Batch size |
|------|----------------|----------------|------------|
| **Batch add** | "15 more across all genres" | Multi-researcher agent dispatch | 5–20 albums |
| **Targeted add** | "Next best 2 Charles Lloyd albums" | Single researcher + personnel agent | 1–5 albums |
| **Manual add** | "I found Album X — add it" | Personnel researcher only (no curation) | 1 album |
| **Kimi import** | "Kimi found 2 modal jazz albums" | Kimi Code → adapter → standard schema | 1–5 albums |

---

## 3. Batch File Spec

### Location
```
data/batches/YYYY-MM-DD-<label>.json
```
Examples:
- `data/batches/2026-07-10-next-15.json`
- `data/batches/2026-07-15-charles-lloyd.json`
- `data/batches/2026-07-20-kimi-modal-r4.json`

### Format
Same schema as `data/canon-draft.json` — an array of complete album objects. Partial records are fine; NULL fields are filled during enrichment. Every album must have at minimum:

- `title`
- `artist`
- `year`
- `style` (from genre-definitions.md)
- `include: true`
- `source` (which agent or researcher produced it)

### Template stub
```json
[
  {
    "id": null,
    "title": "",
    "artist": "",
    "year": null,
    "label": "",
    "catalog_number": null,
    "style": "",
    "include": true,
    "source": "claude|kimi|manual",
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "sessions": [],
    "tracks": []
  }
]
```

<!-- TODO: Paste a complete single-album example from canon-draft.json here once this doc is exercised -->

---

## 4. Agent Dispatch Reference

### Researcher Agents (Claude Code)

| Agent | When to use | Subagent type |
|-------|-------------|---------------|
| `jazz-hard-bop-researcher` | Hard bop / soul jazz candidates (~1955–1965) | `jazz-hard-bop-researcher` |
| `jazz-cool-jazz-researcher` | Cool jazz / West Coast candidates (~1949–1958) | `jazz-cool-jazz-researcher` |
| `jazz-modal-jazz-researcher` | Modal jazz / post-bop candidates (1958–late 1970s) | `jazz-modal-jazz-researcher` |
| `jazz-personnel-researcher` | Fill personnel + session records for known albums | `jazz-personnel-researcher` |
| `jazz-canon-orchestrator` | Merge multi-researcher candidate lists → tiered ballot | `jazz-canon-orchestrator` |

### Sample Dispatch Prompts

#### Batch add — 15 across genres
```
Dispatch jazz-hard-bop-researcher, jazz-cool-jazz-researcher, and jazz-modal-jazz-researcher
in parallel. Each should find 5 strong candidates not already in the canon.
Current canon is in data/canon-draft.json. Output each list to data/batches/YYYY-MM-DD-batch-<genre>.json.
After all three complete, dispatch jazz-canon-orchestrator to merge into a tiered ballot.
```

#### Targeted add — artist-specific
```
Dispatch jazz-modal-jazz-researcher with a focused query:
"Find the next best 2 Charles Lloyd albums not already in the canon (see data/canon-draft.json).
Include full personnel. Output to data/batches/YYYY-MM-DD-charles-lloyd.json."
```

#### Manual add — single album
```
Dispatch jazz-personnel-researcher for one album:
Title: [X], Artist: [Y], Year: [Z], Label: [L]
Gather complete personnel, session dates, track list, MBID, Apple ID.
Output to data/batches/YYYY-MM-DD-<slug>.json.
```

<!-- TODO: Refine these prompts after first live foray and record what worked -->

---

## 5. Kimi Import Path

### Adapter
```bash
python3 scripts/adapt-kimi-record.py <kimi-output-file.json> <output-batch-file.json>
```

The adapter transforms Kimi's schema to the standard canon schema. Review the output diff before ingest — Kimi records may have different field names or NULL patterns.

### Wall rule (preserved from A/B experiment)
Kimi's raw artifacts in `mccoy-tyner-kc/` are read-only. Never paste Claude schema or plan into Kimi. The adapter is the integration layer; both sides stay clean.

<!-- TODO: Document any adapter edge cases discovered in first Kimi import post-v1 -->

---

## 6. Ingest

```bash
# Copy to /tmp (postgres can't traverse /home/john/)
cp data/batches/YYYY-MM-DD-<label>.json /tmp/batch.json

# Run ingest (upserts — safe to run twice)
sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/ingest.py /tmp/batch.json
```

The loader upserts on album slug — running it twice on the same file is safe. Check row counts before and after to confirm.

<!-- TODO: Update ingest.py to accept a file path argument if it doesn't already; verify upsert key -->

---

## 7. Post-Ingest Enrichment

After ingest, new albums need: MBID, Apple ID, cover art, catalog number, embeddings.

**Planned: `scripts/enrich.py`** — a single wrapper that runs all four enrichment scripts in sequence for a given album slug or batch file. Until built, run manually:

```bash
# 1. MBID + Apple ID
sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/mbid-apple-lookup.py

# 2. Cover art
sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/cover-art-fetch.py

# 3. Catalog numbers
sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/catalog-lookup.py

# 4. Embeddings
sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/embed.py
```

<!-- TODO: Build scripts/enrich.py; add --slug and --batch-file flags -->

---

## 8. Dispatch Ledger

File: `data/dispatch-ledger.json`

Log every foray — what was dispatched, what came back, what was blessed, what was ingested.

```json
{
  "forays": [
    {
      "date": "YYYY-MM-DD",
      "label": "next-15",
      "type": "batch",
      "agents_dispatched": ["jazz-hard-bop-researcher", "jazz-modal-jazz-researcher"],
      "batch_file": "data/batches/YYYY-MM-DD-next-15.json",
      "albums_researched": 15,
      "albums_blessed": 12,
      "albums_ingested": 12,
      "notes": ""
    }
  ]
}
```

<!-- TODO: Automate ledger append as part of ingest script or a post-ingest hook -->

---

## 9. Hermes Admin Profile

### Purpose
Replace the coded admin front-end. Handles: CRUD, research queries, batch dispatch, ad-hoc SQL, brainstorming.

### Interface
Telegram channel (primary) or Hermes CUI.

### Profile spec (stub)
- **Model**: Claude Sonnet 4.6
- **DB access**: `_jazzcanon` on vps8-core:5433 (read initially; write after guardrails confirmed)
- **Skills**: jazz-canon-admin (to build), web search
- **System prompt / SOUL.md**: <!-- TODO: Draft once write access is enabled -->

### Guardrails (to encode in SOUL.md/AGENTS.md)
- Confirm before any INSERT, UPDATE, or DELETE
- Never execute DROP, TRUNCATE, or ALTER TABLE
- Always show the SQL before running it
- Read-only by default; write mode requires explicit session-level unlock

### Common admin queries (to wire as Hermes skills)
<!-- TODO: Enumerate once first admin session is run — capture the queries that get asked repeatedly -->

---

## 10. Automation Inventory

### Scripts (exist in `scripts/`)
| Script | Purpose |
|--------|---------|
| `ingest.py` | Upsert albums/persons/performances into `_jazzcanon` |
| `adapt-kimi-record.py` | Transform Kimi schema → standard schema |
| `mbid-apple-lookup.py` | Fetch MusicBrainz MBIDs + iTunes Apple IDs |
| `cover-art-fetch.py` | Fetch cover art (Cover Art Archive → iTunes fallback) |
| `catalog-lookup.py` | Fetch catalog numbers from MusicBrainz |
| `embed.py` | Generate nomic-embed-text embeddings for albums + persons |
| `data-quality-sweep.py` | Identity resolution + duplicate detection |
| `rebuild-canon.py` | Rebuild canon-draft.json from DB (export) |

### Scripts (planned)
| Script | Purpose |
|--------|---------|
| `enrich.py` | Wrapper: run all enrichment steps for a batch in one command |

### Claude Code Agents (exist in `~/.claude/agents/`)
| Agent | Purpose |
|-------|---------|
| `jazz-hard-bop-researcher` | Hard bop / soul jazz candidates + personnel |
| `jazz-cool-jazz-researcher` | Cool jazz / West Coast candidates + personnel |
| `jazz-modal-jazz-researcher` | Modal jazz / post-bop candidates + personnel |
| `jazz-personnel-researcher` | Personnel + session records for known albums |
| `jazz-canon-orchestrator` | Merge candidate lists → tiered ballot |

### Claude Code Skills (planned)
| Skill | Purpose |
|-------|---------|
| `jazz-add-batch` | Orchestrate full foray pipeline (dispatch → review → ingest → log) |

### Hermes Skills (planned)
| Skill | Purpose |
|-------|---------|
| `jazz-canon-admin` | Common admin operations: query, add, update, research dispatch |

---

## 11. Checklists

### Pre-Foray
- [ ] Confirm foray type (batch / targeted / manual / Kimi import)
- [ ] Check `data/dispatch-ledger.json` — is this artist/genre already in a recent foray?
- [ ] Check current canon count: `SELECT COUNT(*) FROM _jazzcanon.albums WHERE include = true`
- [ ] Name the batch file: `data/batches/YYYY-MM-DD-<label>.json`

### Post-Ingest
- [ ] Row counts match expected (albums, persons, performances)
- [ ] Run enrichment: `enrich.py` (or individual scripts until wrapper exists)
- [ ] Spot-check 2–3 new records in Postgres
- [ ] Update `data/dispatch-ledger.json`
- [ ] If any albums skipped/deferred, note reason in ledger

<!-- TODO: Add Hermes-specific checklist once admin profile is live -->

---

## 12. Open Loops

Tracked here temporarily; move to `docs/todo.md` once stable.

- [ ] Build `scripts/enrich.py` (wrap the 4 enrichment scripts)
- [ ] Verify `scripts/ingest.py` accepts a file path argument
- [ ] Draft Hermes admin profile SOUL.md/AGENTS.md
- [ ] Build Claude Code skill `jazz-add-batch`
- [ ] Build Hermes skill `jazz-canon-admin`
- [ ] Add `data/batches/` to plan-v2.md
- [ ] Run first live foray and tighten this doc against reality
