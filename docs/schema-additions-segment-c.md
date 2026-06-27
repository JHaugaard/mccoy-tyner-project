# Schema Additions — Segment C

Gaps surfaced during reconciliation (Kimi comparison + UI reference work). None of these block Segment B or the reconciliation pass. Add in Segment C when schema is locked for Postgres ingest.

---

## 1. `catalog_number` field on album records

**What**: String field for the original release catalog number (e.g. "BLP-1522", "LP-628 (mono)", "LPM-3138")

**Why now**: Kimi captured catalog numbers for all 100 of its records via Discogs. Claude's schema doesn't have this field. The UI reference Venue Map view uses catalog numbers as a secondary browse identifier. Also useful for distinguishing pressings and resolving title ambiguity (confirmed key during twin scan — LPM-3137 vs LPM-3138 was the definitive way to separate two Shorty Rogers albums).

**Where**: Top-level field on each album record (alongside `label`, `year`). `adapt-kimi-record.py` already writes it as `catalog_number`.

**Postgres column**: `catalog_number TEXT` on the main albums table in `_jazzcanon`. Not nullable at ingest — mark as `""` if unknown.

**Immediate action**: `adapt-kimi-record.py` already populates this from Kimi records. For existing Claude records, add during Phase 4 gap-fill (single research pass, 105 albums, ~2 minutes per Discogs lookup).

---

## 2. Studio geocoordinates lookup table

**What**: A small reference table mapping studio name → latitude/longitude (and optionally city, address)

**Why now**: The UI reference Venue Map view uses studio as a browse axis. Van Gelder Studio (Hackensack, NJ) will be the supernode — dozens of Blue Note albums converge there. The canvas for the whole project is roughly 10–15 studios covering ~80% of the canon.

**Estimated studios**: Van Gelder (Hackensack + Englewood Cliffs), RVG (Rudy Van Gelder home studio), Fine Sound (NYC), Webster Hall (NYC), Columbia 30th Street (NYC), Atlantic (NYC), Reeves Sound (NYC), Radio Recorders (LA), Contemporary Records (LA), Pacific Jazz (LA), Club St. Germain (Paris), Pershing Lounge (Chicago). ~12–15 entries total.

**Postgres table**: `_jazzcanon.studio_lookup` with columns `studio_name TEXT PRIMARY KEY, city TEXT, lat NUMERIC, lon NUMERIC, notes TEXT`. This is a manually-curated lookup, not a scraped table.

**Immediate action**: None — add in Segment C after the main `studio` field is consistently populated in album records (Phase 4 gap-fill populates `studio`; then Segment C adds the lookup table and joins it).

---

## 3. Optional editorial description field

**What**: A short (1–3 sentence) editorial description per album for display in the web UI's album detail view.

**Why now**: The UI reference Album Deep Dive panel has a text description area. This is not the `rationale` field (which is canon-decision reasoning, internal). This is a public-facing human-readable note about the album's significance.

**Where**: Top-level `description TEXT` field on album records. Optional — NULL is fine at Phase 4 ingest.

**Source**: Editorial voice only (not sourced like personnel facts). Drafted per-album in the UI build phase (Phase 5). Not a gap-fill research task.

**Postgres column**: `description TEXT` — nullable.

---

## 4. Instrument string normalization

**What**: An enforced vocabulary for the `instrument` field on personnel records.

**Why now**: The UI reference Sideman Search allows filtering by instrument. This only works correctly if "double bass" ≠ "bass" ≠ "contrabass" ≠ "upright bass" — they're all the same instrument. Kimi already uses "double bass" consistently; Claude's records vary.

**Canonical list** (initial, extend as needed):
```
trumpet
cornet
flugelhorn
tenor saxophone
alto saxophone
soprano saxophone
baritone saxophone
clarinet
trombone
valve trombone
piano
electric piano
organ (hammond)
guitar
electric guitar
double bass
electric bass
drums
vibraphone
violin
flute
voice
conductor
arranger
```

**Where enforced**: At D2 ingest (the Phase 4 Postgres loader), not at the JSON draft level. The loader should reject unknown instrument strings and prompt correction.

**Immediate action**: None for Phase 3/4 draft work. Add validation to the D2 loader in Phase 4.

---

## 5. `consensus` field (immediate — not Segment C)

**What**: Tag on every record indicating which harness picked it: `"both"` | `"claude_only"` | `"kimi_only"`

**Why now**: This is part of the reconciliation itself, not a future schema addition. Adding it now, before Segment C, makes the A/B comparison legible inside the data.

**Where**: Top-level field on all records in `canon-draft.json`.

**Immediate action**: Add during Step 6 (rebuild after John's gate). `adapt-kimi-record.py` already writes `"consensus": "kimi_only"` on adapted records. For existing Claude records: script will set `"both"` for the 48 consensus albums and `"claude_only"` for the 57 unique ones.

---

## Not adding

These were considered and rejected for Segment C:

- **Kimi's `conflicts` array** (structured fact conflicts per record): Claude already handles this via epistemic labels + `notes` field. The structured conflicts array adds complexity without changing downstream behavior. Skip.
- **Kimi's `aliases` array** (name variant tracking per person): Claude handles this via `name_variants[]` on each personnel entry. Already covered.
- **Millisecond track durations**: Kimi uses `duration_seconds` (integer). Claude uses `duration` (M:SS string). M:SS is human-readable and sufficient for the web UI. No need to switch to milliseconds.
