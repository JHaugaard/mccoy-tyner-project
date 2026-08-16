# Personnel Record Contract

**Version:** 1.1 · 2026-08-16
**Status:** Single source of truth for the `personnel_record` block.

> **v1.1 — `recording_sites`.** The flat `"studio"` string cannot express an
> album recorded in two places, and cannot carry the precision the Studios map
> needs. A per-session `recording_sites` array is now the authoritative record
> of where an album was made; `"studio"` stays as a derived convenience. See
> **Recording sites** below. This closes `docs/follow-ups.md` #7.

This document defines the personnel/session/track data that the **style specialists**
(`jazz-hard-bop-researcher`, `jazz-cool-jazz-researcher`, `jazz-modal-jazz-researcher`) gather in their
one-pass run, and that the dormant `jazz-personnel-researcher` produces if the seam is ever reopened.
The specialists read this file at dispatch (the same way they read `docs/genre-definitions.md` for scope).

The block is **cleanly separable by design** — it is the *seam*. To split personnel back into a separate
agent later, lift `personnel_record` out of the specialist record and hand the `{id, artist, album, year,
label}` stub to the personnel agent; nothing else changes.

> This is deep, source-grounded extraction, not summarizing: every musician, every instrument, every
> production credit traces to a named source. Where sources conflict or data is absent, say so precisely
> rather than guessing. The data platform can upgrade confidence with better sources later; it cannot
> manufacture credibility that was never there.

---

## Sources (priority order, per album)

Stop when you have complete, reliable data; go deeper when top sources conflict or are incomplete. Source
IDs are local to the specialist's single source map (shared with the canon-list sources — one map per file).

1. **AllMusic album page** — open the full **Credits tab**, not just the overview. Usually the most complete single source for this era.
2. **Wikipedia album article** — "Personnel" section, or the track listing when it includes per-track credits; often cites liner notes.
3. **Tom Lord's Jazz Discography** (`lordisco.com`) — session-level authority: exact dates, studio, personnel per session. Strongest for Blue Note, Prestige, Impulse!.
4. **JazzDiscography.com** — personnel database, strong on Blue Note and the hard bop era.
5. **Discogs** — track metadata (side, number, duration), sometimes personnel; also a UPC/barcode cross-reference (useful for resolving Apple Music IDs later).
6. **Label discographies** — Blue Note, Prestige, Impulse!, Columbia, Verve, ECM official archives. Most authoritative for production credits.
7. **Liner notes (digitized)** — Google Books, archive.org, label reissue pages. The primary source — when found, they supersede all others; cite them directly.
8. **Artist sessionographies** — dedicated discography pages for the primary artist often list personnel per session date.

Minimum 3 sources per album is the target; one source per record is acceptable when it provides complete, reliable data.

---

## Five Layers

Build up from the base. Capture each layer when sources make it available; never skip to a deeper layer
without securing the one above.

**Layer 1 — Core ensemble + production credits (always required).** Every musician on most or all tracks, with instrument (`scope: "all-tracks"`). Producer, engineer, recording dates, and `recording_sites` (see **Recording sites** — required, one entry per session, `unk` is an acceptable answer). No record is complete without this.

**Layer 2 — Session contributors.** Musicians on some but not all tracks (`scope: "selected-tracks"`, tracks listed). This is what separates a "Freddie Freeloader" piano credit (Wynton Kelly) from a "Kind of Blue" piano credit (Bill Evans).

**Layer 3 — Track-level assignments.** When liner notes, AllMusic, or a sessionography lists personnel per track, populate the `tracks` array. Do not infer — only record what sources state. `track_assignments_complete: true` only when every musician has confirmed assignments.

**Layer 4 — Per-session recording dates.** For multi-session albums, which tracks belong to each date (`recording_dates` block-level, `session_date` per track). Enables downstream timeline queries.

**Layer 5 — Album-art + Apple Music references (optional, opportunistic).** While on AllMusic/Wikipedia/Discogs/MusicBrainz pages, capture the MusicBrainz release-group MBID and cover-art URL(s) into `cover_art`. For Apple Music, query the **free iTunes Search/Lookup API** (`https://itunes.apple.com/search?term=ARTIST+ALBUM&entity=album` — no token, no cost) and record the album's `collectionId` into `apple_album_id` when you find a confident match. You are **recording references, not downloading anything** — a later ingest step fetches files, and a later serving step builds previews/links/player. Lowest priority — never let it slow personnel work; empty/null is fine.

If a source gives you Layer 3/4/5 data "for free" while you're there, take it. This is a single deep pass — no second pass is planned.

---

## The `personnel_record` block (JSON shape)

Nested inside each specialist candidate record. The parent record already carries `id`, `artist`,
`album`, `year`, `label` — so the block does **not** repeat them (no `album_id`; the parent `id` is the key).

```json
"personnel_record": {
  "recording_dates": ["1959-03-02", "1959-04-22"],
  "multi_session": true,
  "studio": "Columbia 30th Street Studio, New York",
  "recording_sites": [
    { "session_date": "1959-03-02", "site_raw": "Columbia 30th Street Studio, New York City",
      "site_slug": "cbs-30th-street-studio", "site_new": null,
      "epistemic": "obs", "source": "S3" },
    { "session_date": "1959-04-22", "site_raw": "Columbia 30th Street Studio, New York City",
      "site_slug": "cbs-30th-street-studio", "site_new": null,
      "epistemic": "obs", "source": "S3" }
  ],
  "producer": "Irving Townsend",
  "engineer": "Fred Plaut",
  "epistemic_production": "obs",
  "personnel": [
    { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null,
      "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "" },
    { "name": "Bill Evans", "instrument": "piano", "scope": "selected-tracks",
      "tracks": ["So What", "Blue in Green", "Flamenco Sketches"],
      "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S5"],
      "name_variants": [], "notes": "" }
  ],
  "tracks": [
    { "title": "So What", "track_number": 1, "side": "A", "duration": "9:22",
      "session_date": "1959-03-02", "composers": ["Miles Davis"],
      "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
      "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] }
  ],
  "track_assignments_complete": false,
  "musicbrainz_release_group_mbid": "f5093c06-23e3-404f-aeaa-40f72885ee3a",
  "apple_album_id": "1469577723",
  "cover_art": [
    { "role": "front", "source": "cover-art-archive",
      "url": "https://coverartarchive.org/release-group/f5093c06-23e3-404f-aeaa-40f72885ee3a/front",
      "is_original_cover": true, "epistemic": "obs", "notes": "" }
  ],
  "notes": "Two sessions. March 2: tracks 1–3. April 22: tracks 4–5."
}
```

**Block-level rules:** `recording_dates` are ISO dates; use a range string `"1959-03-02/1959-03-15"` when only a range is documented; `[]` if unknown. `producer`/`engineer` are `null` if unknown — explicit null, never a missing field. `studio` is now a **derived convenience** — the first entry's `site_raw`, kept so older tooling and eyeballing still work. It is not authoritative and nothing reads it into the database; **`recording_sites` is the record of where the album was made.** `tracks: []` when track-level data is unavailable — never invent assignments. `musicbrainz_release_group_mbid` and `apple_album_id` (the iTunes `collectionId`) only if readily found — do not guess; `null` otherwise. `notes` holds session distribution, name conflicts, doubles — anything unstructured.

**Personnel entry rules:** `name` is the canonical, most-cited form ("McCoy Tyner", not "Tyner, McCoy"), consistent across the whole run. `instrument` is exactly one string from the taxonomy below. `scope` is `all-tracks` / `selected-tracks` (list the tracks) / `unknown`. `tracks` and `session_dates` are `null` when not applicable/distinguished. `name_variants` records other forms found in sources.

**Track entry rules:** `title` as printed on the original release; `track_number` sequential across sides; `side` is `"A"`–`"D"` or `null` (CD); `personnel` names must exactly match the block's `personnel` names; `bonus_track`/`alternate_take` flag reissue additions and alternates.

**Cover-art entry rules:** `role` front/back/liner/disc/alternate/other; `source` cover-art-archive/itunes/discogs/wikimedia/other (prefer Cover Art Archive); `is_original_cover` true/false/null; `epistemic` obs (unambiguously this release) / inf (matched by title+artist+year, pressing uncertain) / unk. Never fabricate a URL.

---

## Recording sites

A recording place is an **identity decision before it is a data record** — is this
the same room as one we already have? did the venue move? is this string actually
describing two places? The canon has a curated set of canonical places, each with a
`slug`, a `kind`, and a coordinate. Your job is to *match against that set*, not to
describe a venue freshly each time.

### The seven rules

**1 — One entry per session, never per album.** A source string that names two
venues describes two sessions and must be **split into two entries**. Never store a
compound string whole. This is not a style preference: a compound string staged as
one place is what produced the *Seven Steps to Heaven* failure of 2026-08-13 (raw
name `"Columbia Studios (CBS Columbia Square)"`, raw city `"Hollywood (April 16-17
sessions); Columbia 30th Street Studio, New York City (May 14 session)"`), which had
to be unpicked by hand into three sessions across two places. If your string contains
a semicolon, an "and", or a parenthetical assigning tracks or dates to different
rooms, you are looking at more than one entry.

**2 — `site_slug` comes only from the injected canonical list.** The dispatch
prompt carries the current canonical places as `slug — Name, City (kind)`. Choose
from it. **Never invent a slug, never reconstruct one from memory, never guess one
from the venue name.** A slug that is not on that list will be refused at staging,
and correctly so — the list is generated from the database at runtime and is always
current.

**3 — `site_new` only on a genuine miss, and only complete.** If the place is
truly absent from the list, fill `site_new` with **every** field:

```json
"site_new": {
  "name": "Nola Penthouse Sound Studios",
  "city": "New York, NY",
  "kind": "studio",
  "address": "111 West 57th Street (penthouse, Steinway Hall)",
  "lat": 40.76497, "lon": -73.97847,
  "location_epistemic": "obs",
  "location_source": "https://example-source.org/… | coords: OSM Nominatim: …"
}
```

`kind` is exactly one of `studio` · `club` · `hall` · `festival` · `home` · `other`.
Coordinates come from **`scripts/geocode-place.py`**, which implements the ratified
method (Wikidata/Wikipedia coordinate → OSM Nominatim on a documented address →
city centroid at 3 decimals) and emits `lat`, `lon`, `location_epistemic` and
`location_source` ready to paste. Do not hand-roll a geocoder and do not read
coordinates off a map.

A partial `site_new` is refused. This is the **completeness invariant**: an
incomplete place row breaks the site's export for the entire canon, so the pipeline
creates a place completely or not at all.

**4 — Never invent an address.** `address` is `null` when no source documents one —
that is an honest, common, and fully supported answer (12 of the current canonical
places are city-level). A null address takes a city centroid and
`location_epistemic: "inf"`. Reconstructing a plausible street number from a map, a
modern listing, or the neighbourhood is fabrication, and it is worse than the honest
city pin because the map will render it as though a source had confirmed it.

`location_epistemic` follows the database's own definition: **`obs`** = street-level
documentation cited in `location_source`; **`inf`** = city-level only. A documented
address whose coordinate is nonetheless approximate (the block was demolished, the
street renumbered) is legitimately `obs` address + `inf` epistemic — say why in
`notes`.

**5 — Unknown is a value, not an omission.** When sources genuinely do not say
where an album was recorded, the entry is:

```json
{ "session_date": null, "site_raw": null, "site_slug": null,
  "site_new": null, "epistemic": "unk", "source": null }
```

The session then carries no place, which is a supported state — 14 sessions in the
canon are placeless today. **`recording_sites` itself is required.** An absent or
empty array is a contract violation, not a way of saying "unknown": silence is
indistinguishable from an oversight, and the whole point of the epistemic labels is
that the record says what it does not know.

**6 — Conflicts are preserved, never resolved by preference.** Two sources naming
different venues for the same session ⇒ record both `site_raw` claims, set
`epistemic: "unk"`, and explain in the block's `notes`. Never pick the more likely
one silently. (Live example: one canon album carries an Atlantic-vs-Van-Gelder
conflict recorded exactly this way.)

**7 — Source hierarchy for "recorded at X".** Sequence-sensitive and slightly
different from the album-level list above:

1. **Liner notes** — primary, and supersede everything below when found.
2. **Tom Lord's Jazz Discography** — the session-level authority; strongest for
   Blue Note, Prestige, and Impulse!, and the right first stop for anything with
   multiple dates.
3. **AllMusic** Credits tab · 4. **Wikipedia** album article ·
5. **JazzDiscography.com**.

### Entry fields

| field | rule |
|---|---|
| `session_date` | ISO `YYYY-MM-DD` tying the entry to its session; `null` only in the `unk` case or a genuinely undated single session |
| `site_raw` | the venue exactly as the source printed it — preserved for audit even when `site_slug` matches |
| `site_slug` | canonical slug from the injected list, or `null` |
| `site_new` | complete new-place object, or `null`. Never set alongside `site_slug` |
| `epistemic` | `obs` source names the venue for this session · `inf` reasoned (e.g. the label's house studio in that period) · `unk` conflict, single weak source, or unknown |
| `source` | source-map ID backing the claim |

### Two traps worth naming

- **Van Gelder is two places.** `van-gelder-studio-hackensack` until mid-1959,
  `van-gelder-studio-englewood-cliffs` after. Sources say only "Van Gelder Studio";
  **the session date decides**, and getting it wrong puts the pin in the wrong state.
- **Capitol is two places.** `capitol-records-studio-melrose-avenue` before the
  Capitol Tower opened in April 1956, `capitol-records-studio-capitol-tower` after.

---

## Instrument Taxonomy (exact strings — do not invent)

**Brass:** `trumpet` · `cornet` · `flugelhorn` · `trombone` · `bass trombone` · `French horn`
**Woodwinds:** `soprano saxophone` · `alto saxophone` · `tenor saxophone` · `baritone saxophone` · `clarinet` · `bass clarinet` · `flute`
**Keyboards:** `piano` · `organ` · `electric piano` · `harpsichord` · `celesta`
**Strings:** `double bass` · `electric bass` · `guitar` · `electric guitar` · `violin` · `viola` · `cello` · `harp`
**Percussion:** `drums` · `vibraphone` · `marimba` · `congas` · `bongos` · `percussion`
**Other:** `vocals`

If an instrument genuinely cannot be described by this list, use the most specific descriptive term available and flag it in `notes`.

---

## Edge Cases

- **Multi-session albums:** `multi_session: true`; all dates in `recording_dates`; per-musician `session_dates` when sources distinguish; session→track distribution in `notes`.
- **Instrument doubles:** primary instrument in `instrument`; doubling in `notes` (e.g., "also plays soprano saxophone on tracks 3, 5").
- **Name variants:** canonical form from the most authoritative source (liner notes > Penguin Guide > AllMusic); conflicts noted.
- **Rudy Van Gelder inference:** Blue Note/Prestige album, mid-1950s–late 1960s, no engineer listed, but confirmed recorded at Van Gelder Studio (Hackensack or Englewood Cliffs) → `"engineer": "Rudy Van Gelder"` with `epistemic_production: "inf"` and a note.
- **Source conflicts:** when two sources name different musicians for the same role, list both with `epistemic: "unk"` and explain in `notes`. Never pick one arbitrarily.
- **Uncredited musicians:** include when a sessionography identifies them, with `epistemic: "inf"` or `"unk"` and the source named.
- **No production data at all:** explicit nulls, `epistemic_production: "unk"`, and a note on what you searched.
- **Alternate takes / bonus tracks:** flag them; exclude reissue-only tracks unless explicitly labeled as such.

---

## Epistemic Rules

- `obs` — source directly names this musician on this album or track
- `inf` — reasoned from pattern (standard lineup confirmed elsewhere; Van Gelder inference; track assigned by session-date logic)
- `unk` — uncertain: single weak source, source conflict, no corroboration, or presence confirmed but track coverage unknown

Cite source IDs in every `sources` array. Never assert `obs` without a named source. When in doubt, go one level more uncertain.

---

## Quality Checks (before submitting)

- Every `instrument` string is from the taxonomy — no free-form names
- Musician names internally consistent within the run
- `track_assignments_complete` is `false` unless every musician's coverage is explicitly source-confirmed
- Every `sources` array references a valid source-map ID
- Production data present or explicitly null with `epistemic_production` set
- `recording_sites` is present and non-empty; one entry per session, no compound strings
- Every `site_slug` was copied from the injected canonical list, not recalled or guessed
- Every `site_new` is complete (`name`, `city`, `kind`, `lat`, `lon`, `location_epistemic`, `location_source`), with `address` null rather than invented, and coordinates from `scripts/geocode-place.py`
