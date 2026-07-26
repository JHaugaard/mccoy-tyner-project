# Hand-off: Carry Council Rationale into the Database + Semantic Search Decision

**Date:** 2026-07-21
**From:** McCoy (Hermes profile), for Claude Code
**Status:** Approved by John in conversation; option A vs B below is his open decision
**Scope:** Schema migration + pipeline patches + backfill. Small, well-bounded.

---

## Background

Every drip dossier carries three prose fields John calls the gems of the report:

| Dossier field | Origin | Current DB destination |
|---|---|---|
| `rationale` | GATHER dossier (researcher's case) | **none** — exists only in the JSON file |
| `ballot.case_for` | canon-council ballot | `album.inclusion_rationale` ✓ |
| `ballot.case_against` | canon-council ballot | **none** — lost from the DB at staging |

`scripts/stage-candidate.py` (lines ~550-554) lifts only `tier`, `priority`, and `case_for` from the ballot. `case_against` (plus `disagreement`, `recommendation`, `confidence`) survives only in `research/candidates-archive/*.json` — durable but not queryable.

John wants all three fields in the database for later thinking/planning/writing work. Storage cost is negligible (established in conversation: all current rationale text across 111 albums is 39 kB; the album table is 288 kB total).

---

## Work item 1 — Schema migration

Add to `_jazzcanon.album`:

```sql
ALTER TABLE _jazzcanon.album
  ADD COLUMN dossier_rationale text,      -- the GATHER dossier's own rationale field
  ADD COLUMN council_case_against text;   -- ballot.case_against
```

Naming note: `inclusion_rationale` already holds `case_for`. Renaming it to `council_case_for` for symmetry is tempting but touches the export pipeline and both site repos — **do not rename**. Accept the asymmetry; document it in a column comment:

```sql
COMMENT ON COLUMN _jazzcanon.album.inclusion_rationale IS 'Canon-council ballot case_for (historical name; not renamed to avoid export churn)';
COMMENT ON COLUMN _jazzcanon.album.dossier_rationale IS 'GATHER dossier rationale — the researcher''s case before council';
COMMENT ON COLUMN _jazzcanon.album.council_case_against IS 'Canon-council ballot case_against';
```

Optional fourth column: `council_disagreement text` (ballot.disagreement, where references split). John didn't ask for it; flag it in the PR as a zero-cost add while the migration is open. `recommendation` and `confidence` are probably worth leaving in the archive — they're council-process metadata, not album-level prose. John's call if raised.

**Edit contract impact:** add `dossier_rationale` and `council_case_against` to the album whitelist in `config/edit-contract.md` (McCoy can patch that doc; it's a doc change, not code).

---

## Work item 2 — Patch `scripts/stage-candidate.py`

In the ballot-resolution block (~line 550), also lift:

```python
dossier_rationale = null(record.get("rationale"))
council_case_against = null(ballot_entry.get("case_against")) if ballot_entry else None
```

and include both in the album INSERT/UPDATE. Also carry `ballot_entry.get("disagreement")` if work item 1's optional column is taken. Keep behavior when fields are absent: NULL, no fabrication.

---

## Work item 3 — Backfill the 11 drip-staged albums

Eleven albums were staged via the drip and are now `canon_status='included'`; their full dossiers (with `rationale` and `ballot.case_against`) are in `research/candidates-archive/`:

- shorty-rogers-and-his-giants-1953
- thelonious-monk-brilliant-corners-1956
- benny-golson-the-modern-touch-1957
- miles-davis-sketches-of-spain-1960
- john-coltrane-ole-coltrane-1961
- kenny-dorham-whistle-stop-1961
- mccoy-tyner-inception-1962
- charles-mingus-the-black-saint-and-the-sinner-lady-1963
- art-blakey-the-jazz-messengers-free-for-all-1964
- wes-montgomery-smokin-at-the-half-note-1965
- horace-silver-serenade-to-a-soul-sister-1968

Write a one-shot backfill script (or SQL driven by a small Python reader) that UPDATEs each album from its archive file. Verify: row count = 11, spot-check two albums' text against the dossiers.

Note: the v1 canonical 100 have no dossiers — these columns will be NULL for them. That's correct, not a defect; they were never council-reviewed.

---

## Work item 4 — Semantic search: TWO OPTIONS (John's open decision)

Current state (`scripts/embed.py` lines 62-86): album `search_document` = title, artist, year, style, performer roster, `description`. **No rationale text is embedded today** — council prose is invisible to `canon-search.py`.

### Option A — Fold rationale into the album's search_document

Append `dossier_rationale`, `inclusion_rationale`, `council_case_against` to `parts` in `embed.py`, then `embed.py --force` to re-embed all albums (Ollama on vps4; 111 albums is a few minutes).

- Cost: ~one-line patch + re-embed run.
- Benefit: queries like "albums the council called defining statements" or "candidates with scope doubts" just work.
- Risk: **dilution.** The album embedding currently encodes *what the album is* (musical identity). Folding council prose in means "Spanish classical influences" could match Sketches of Spain via the case_against rather than the album itself. With ~360 chars of rationale vs ~200 chars of identity text per album, council prose would outweigh musical description in the vector.

### Option B — Separate searchable surface for council text

Keep album embeddings as-is (musical identity only). Embed council text separately — e.g. a `council_document` + `council_embedding` pair on album, or a thin `_jazzcanon.council_note` table (one row per reviewed album, its own search_document/embedding). `canon-search.py` gains a flag: default searches albums (identity); `--council` searches council prose.

- Cost: more pipeline work — second embedding column or table, search-tool flag, embed.py branch. Maybe a day, not a week.
- Benefit: "what the album is" and "what the council argued" stay distinct questions. Precision preserved on both. Matches how John framed the use ("later when thinking, planning, or writing") — he'd query the council record deliberately, not want it blended into album similarity.
- Risk: more surface to maintain; another derived-field pair the pipeline owns (add to the "never hand-edit" list in the edit contract).

### Recommendation (McCoy's, not settled)

Option B. The dilution in A is real and silent — you'd never see it fail, just get slightly-wrong similarity. B keeps the album vectors clean for the site's discovery purposes and gives John a purpose-built research surface. But A gets 90% of the value for near-zero effort, and if John wants it this week, A-now-B-later is legitimate.

---

## Verification checklist

- [ ] Migration applied; two (or three) new columns present, comments written
- [ ] `stage-candidate.py --dry-run` on a fresh dossier shows new fields flowing
- [ ] Backfill: 11 rows updated; spot-check 2 against archive JSON
- [ ] Edit contract whitelist updated (McCoy can do this part)
- [ ] Option chosen; embed path patched; `--force` re-embed completed without Ollama errors
- [ ] `canon-search.py` returns council-text hits (A) or `--council` flag works (B)

## Out of scope (explicitly)

- Renaming `inclusion_rationale` (see naming note)
- Exporting case_against to the public site — separate product decision for John; the site currently shows nothing of council prose
- Backfilling council data for the v1 100 (no dossiers exist)
