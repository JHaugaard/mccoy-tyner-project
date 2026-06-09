# Personnel Research Schema

Every Phase 2 agent writes a single markdown file containing:
1. Source map table
2. One JSON block per album
3. Summary notes at the end

No deviations from this structure. The `album_id` in every record must match the `id` field from the Phase 1 canon exactly — it is the join key between the two datasets.

**Note on scope:** Phase 2 agents capture both album-level personnel and track-level assignments in a single pass. This replaces the originally planned separate Phase 3. When sources provide track-level detail, record it here. When they don't, the `tracks` array stays empty and `track_assignments_complete` stays `false` — no second pass is planned.

---

## Source Map (one per agent output file)

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | AllMusic — album page | Web | https://allmusic.com/album/... | Full Credits tab |
| S2 | Wikipedia — album article | Web | https://en.wikipedia.org/wiki/... | Personnel section |
| S3 | Tom Lord Jazz Discography | Web | https://www.lordisco.com | Session-level data |

Add a row for every source consulted. Minimum 3 sources per album is the target; one source per record is acceptable when that source provides complete, reliable data.

---

## Album Personnel Record

One JSON block per album, using this exact structure:

```json
{
  "album_id": "miles-davis-kind-of-blue-1959",
  "recording_dates": ["1959-03-02", "1959-04-22"],
  "multi_session": true,
  "studio": "Columbia 30th Street Studio, New York",
  "producer": "Irving Townsend",
  "engineer": "Fred Plaut",
  "label": "Columbia",
  "epistemic_production": "obs",
  "personnel": [
    {
      "name": "Miles Davis",
      "instrument": "trumpet",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S1"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Bill Evans",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": ["So What", "Blue in Green", "Flamenco Sketches"],
      "session_dates": ["1959-03-02", "1959-04-22"],
      "epistemic": "obs",
      "sources": ["S1"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Wynton Kelly",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": ["Freddie Freeloader"],
      "session_dates": ["1959-03-02"],
      "epistemic": "obs",
      "sources": ["S1"],
      "name_variants": [],
      "notes": ""
    }
  ],
  "tracks": [
    {
      "title": "So What",
      "track_number": 1,
      "side": "A",
      "duration": "9:22",
      "session_date": "1959-03-02",
      "composers": ["Miles Davis"],
      "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S1"]
    }
  ],
  "track_assignments_complete": false,
  "sources": ["S1", "S2"],
  "notes": "Two sessions. March 2: tracks 1–3. April 22: tracks 4–5. Bill Evans replaced by Wynton Kelly on Freddie Freeloader only."
}
```

### Top-Level Field Definitions

| Field | Type | Rules |
|-------|------|-------|
| `album_id` | string | Must exactly match the `id` field from the Phase 1 canon record. |
| `recording_dates` | array | ISO dates (YYYY-MM-DD) for each session. Use a range string `"1959-03-02/1959-03-15"` when only a range is documented. Empty array `[]` if entirely unknown. |
| `multi_session` | boolean | `true` if recording spanned more than one session date. |
| `studio` | string | Recording studio name and city. If multiple studios, list the primary one; note others in `notes`. `null` if unknown. |
| `producer` | string | Producer name. `null` if unknown. |
| `engineer` | string | Primary recording engineer. `null` if unknown. See edge cases for Rudy Van Gelder inference. |
| `label` | string | Original release label. Should match the Phase 1 record. |
| `epistemic_production` | string | `obs` if production credits come from liner notes or a reliable named source. `inf` if inferred (e.g., RVG at Van Gelder Studio). `unk` if uncertain or conflicted. |
| `personnel` | array | See Personnel Record below. One entry per musician. |
| `tracks` | array | Optional. See Track Record below. Use `[]` when track-level data is unavailable — never invent track assignments. |
| `track_assignments_complete` | boolean | `true` only when every musician in `personnel` has confirmed, source-grounded track assignments. `false` whenever any assignment is inferred, unknown, or the `tracks` array is empty. |
| `sources` | array | Source IDs from this file's source map covering this album overall. |
| `notes` | string | Free text. Use for: multi-session session distribution, name variant conflicts, instrument doubles, anything that doesn't fit structured fields. |

---

## Personnel Record

| Field | Type | Rules |
|-------|------|-------|
| `name` | string | Canonical name — most commonly cited form (e.g., "McCoy Tyner", not "Tyner, McCoy"). Must be consistent with all other records in this project. |
| `instrument` | string | Exactly one string from the instrument taxonomy below. |
| `scope` | string | `"all-tracks"` — played on all or virtually all tracks. `"selected-tracks"` — played a subset; list them in `tracks`. `"unknown"` — source confirms presence but track coverage unclear. |
| `tracks` | array or null | Track titles (matching `title` values in the `tracks` array) when `scope` is `"selected-tracks"`. `null` when `scope` is `"all-tracks"` or `"unknown"`. |
| `session_dates` | array or null | Session dates this musician is confirmed to have played, when `multi_session` is `true` and sources distinguish personnel by session. `null` when not distinguished. |
| `epistemic` | string | `obs` / `inf` / `unk` — see Epistemic Rules below. |
| `sources` | array | Source IDs supporting this musician's presence on this album. |
| `name_variants` | array | Other forms of name found in sources (e.g., `["William John Evans"]`). Empty array if none found. |
| `notes` | string | Source conflicts, instrument doubles, unusual circumstances. Empty string if nothing notable. |

---

## Track Record (optional)

Populate the `tracks` array when sources explicitly provide track-level detail. Do not infer or reconstruct track assignments — only record what sources state. An empty `tracks` array with `track_assignments_complete: false` is the correct state when data isn't available.

| Field | Type | Rules |
|-------|------|-------|
| `title` | string | Track title as printed on original release. |
| `track_number` | integer | Sequential number counting across all sides. |
| `side` | string or null | `"A"`, `"B"`, `"C"`, `"D"` for vinyl. `null` for CD-only releases. |
| `duration` | string or null | `"MM:SS"` format. `null` if not available. |
| `session_date` | string or null | ISO date for this specific track's recording session. `null` if not distinguishable from album-level dates. |
| `composers` | array | Composer(s) as credited on the original release. |
| `personnel` | array | Musician names playing on this track. Each name must match a `name` value in the top-level `personnel` array exactly. |
| `bonus_track` | boolean | `true` if not on the original release (reissue additions, etc.). |
| `alternate_take` | boolean | `true` if this is an alternate take of an existing title. |
| `epistemic_track` | string | `obs` / `inf` / `unk` for the track-level personnel specifically. |
| `sources` | array | Source IDs for this track's data. |

---

## Instrument Taxonomy

Use these exact strings in the `instrument` field. Do not invent new strings.

**Brass:** `trumpet` · `cornet` · `flugelhorn` · `trombone` · `bass trombone` · `French horn`

**Woodwinds:** `soprano saxophone` · `alto saxophone` · `tenor saxophone` · `baritone saxophone` · `clarinet` · `bass clarinet` · `flute`

**Keyboards:** `piano` · `organ` · `electric piano` · `harpsichord` · `celesta`

**Strings:** `double bass` · `electric bass` · `guitar` · `electric guitar` · `violin` · `viola` · `cello` · `harp`

**Percussion:** `drums` · `vibraphone` · `marimba` · `congas` · `bongos` · `percussion`

**Other:** `vocals`

If an instrument genuinely cannot be described by this list, use the most specific descriptive term available and flag it in `notes`. The data platform will normalize these edge cases.

---

## Summary Notes

After all album records, append this section:

```markdown
## Summary Notes

### Incomplete Records
Albums where personnel data was missing, conflicted, or ambiguous. What was found vs. what remains uncertain, and why.

### Track Assignment Coverage
How many of your albums have `track_assignments_complete: true`? List any where the `tracks` array is entirely empty.

### Name Variant Conflicts
Musician names that appear differently across sources. State the canonical form chosen and why.

### Source Quality Notes
Which sources were most reliable for your batch? Any sources unavailable, paywalled, or that produced conflicting data?

### Unusual Findings
Uncredited musicians identified through secondary sources, session anomalies, anything the data platform should know about.
```

---

## Epistemic Rules

- `obs` — source directly names this musician on this album or track
- `inf` — reasoned from pattern (e.g., standard band lineup confirmed elsewhere; Van Gelder inference at Blue Note; track assigned by session date logic)
- `unk` — uncertain: single weak source, source conflict, or no corroboration

Cite source IDs in every `sources` array. Never assert `obs` without a named source. When in doubt, go one level more uncertain — the data platform can upgrade confidence; it cannot manufacture it.
