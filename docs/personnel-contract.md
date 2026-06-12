# Personnel Record Contract

**Version:** 1.0 · 2026-06-12
**Status:** Single source of truth for the `personnel_record` block.

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

**Layer 1 — Core ensemble + production credits (always required).** Every musician on most or all tracks, with instrument (`scope: "all-tracks"`). Producer, engineer, studio, recording dates. No record is complete without this.

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

**Block-level rules:** `recording_dates` are ISO dates; use a range string `"1959-03-02/1959-03-15"` when only a range is documented; `[]` if unknown. `studio`/`producer`/`engineer` are `null` if unknown — explicit null, never a missing field. `tracks: []` when track-level data is unavailable — never invent assignments. `musicbrainz_release_group_mbid` and `apple_album_id` (the iTunes `collectionId`) only if readily found — do not guess; `null` otherwise. `notes` holds session distribution, name conflicts, doubles — anything unstructured.

**Personnel entry rules:** `name` is the canonical, most-cited form ("McCoy Tyner", not "Tyner, McCoy"), consistent across the whole run. `instrument` is exactly one string from the taxonomy below. `scope` is `all-tracks` / `selected-tracks` (list the tracks) / `unknown`. `tracks` and `session_dates` are `null` when not applicable/distinguished. `name_variants` records other forms found in sources.

**Track entry rules:** `title` as printed on the original release; `track_number` sequential across sides; `side` is `"A"`–`"D"` or `null` (CD); `personnel` names must exactly match the block's `personnel` names; `bonus_track`/`alternate_take` flag reissue additions and alternates.

**Cover-art entry rules:** `role` front/back/liner/disc/alternate/other; `source` cover-art-archive/itunes/discogs/wikimedia/other (prefer Cover Art Archive); `is_original_cover` true/false/null; `epistemic` obs (unambiguously this release) / inf (matched by title+artist+year, pressing uncertain) / unk. Never fabricate a URL.

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
