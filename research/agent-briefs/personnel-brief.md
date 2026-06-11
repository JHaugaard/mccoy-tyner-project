# Personnel Research Agent Brief

## Your Role

You are a personnel research agent for the McCoy Tyner jazz canon project. Your task: for each album in your assigned list, extract complete personnel and production data and write it to your output file.

This is deep, source-grounded research. You are not summarizing — you are extracting structured facts. Every musician, every instrument, every production credit should trace back to a named source. Where sources conflict or data is absent, say so precisely rather than guessing.

Your output feeds directly into the project data platform. Musician names and instrument labels must be consistent across all agents in this phase — the platform will use your records to build a canonical musician and session database. Inconsistent naming creates data problems downstream.

---

## Your Album List

[POPULATED AT DISPATCH — album IDs and titles from data/canon-draft.json]

You have approximately 10 albums. Work through them in the order given.

---

## Output File

Write to: `research/personnel-batch-[NN].md`  
(NN will be provided at dispatch, e.g., `personnel-batch-01.md`)

Structure — in this order:
1. Source map table at the top (one map covering all your albums)
2. One JSON block per album
3. Summary notes section at the end

Follow `research/personnel-schema.md` exactly for all field names, types, values, and instrument strings. The schema is the contract.

---

## Sources (in priority order)

Work through these for each album. Stop when you have complete, reliable data. If top sources conflict or are incomplete, go deeper.

1. **AllMusic album page** — search `allmusic.com [Album Title] [Artist]`  
   Open the full "Credits" tab, not just the overview. AllMusic personnel sections are usually the most complete single source for this era.

2. **Wikipedia album article** — search `[Album Title] [Artist] Wikipedia`  
   The "Personnel" section, or the track listing when it includes per-track credits. Wikipedia jazz album articles are often well-maintained and cite liner notes.

3. **Tom Lord's Jazz Discography** — `lordisco.com`  
   Session-level data: exact recording dates, studio, personnel per session. Most authoritative for Blue Note, Prestige, and Impulse! recordings.

4. **JazzDiscography.com** — personnel database, particularly strong on Blue Note and hard bop era.

5. **Discogs** — `discogs.com`  
   Track listing (side, track number, duration), sometimes personnel. Use for track metadata when AllMusic/Wikipedia are incomplete.

6. **Recording label discographies** — Blue Note, Prestige, Impulse!, Columbia, Verve, ECM official archives or authorized discography pages. Most authoritative for production credits (engineer, studio, producer) specific to that label.

7. **Liner notes (digitized)** — search `[Album Title] liner notes` on Google Books, archive.org, or the label's official reissue documentation. Liner notes are the primary source — when you find them, they supersede all others. Cite them directly.

8. **Artist discographies** — dedicated sessionography or discography pages for the primary artist (e.g., "Miles Davis Discography," "John Coltrane Discography") often list personnel per session date.

---

## Research Approach

Build up from the base layers for each album. Capture each layer when sources make it available — do not skip to a deeper layer without first securing the layer above it.

**Layer 1 — Core ensemble + production credits (always required)**  
Every musician who played on most or all tracks, with instrument. Producer, engineer, studio, recording dates. This is the minimum — no album record is complete without it.  
Use `scope: "all-tracks"` for core band members.

**Layer 2 — Session contributors (capture when sources identify them)**  
Musicians who played on some but not all tracks. List their tracks in the `tracks` field.  
Use `scope: "selected-tracks"`.  
This is what separates a "Freddie Freeloader" piano credit (Wynton Kelly) from a "Kind of Blue" piano credit (Bill Evans).

**Layer 3 — Track-level assignments (capture when sources provide them)**  
When liner notes, AllMusic, or a sessionography lists personnel per track, populate the `tracks` array.  
Do not infer track assignments — only record what sources state explicitly.  
Set `track_assignments_complete: true` only when every musician has confirmed track assignments.

**Layer 4 — Per-session recording dates (capture when available)**  
For multi-session albums, which tracks were recorded on which date. This data enables downstream queries like "which sessions did this musician play across the whole canon" — the timeline view.  
Record session dates in `recording_dates` (album level) and in `session_date` per track when sources provide it.

If a source gives you Layer 3 or 4 data "for free" while you're already there, take it. This is a single deep pass — there is no second pass planned.

**Layer 5 — Album art references (optional, opportunistic)**  
While you're on the album's AllMusic / Wikipedia / Discogs / MusicBrainz pages, capture cover-art
references into the `cover_art` array and the `musicbrainz_release_group_mbid` field — see
`research/personnel-schema.md` ("Album Art"). You are **recording URLs, not downloading images**; the
Phase 4 ingest step fetches and stores the files. Prefer the **original pressing** cover and flag
reissues. This is the lowest priority — never let it slow the personnel work, and `cover_art: []` is
fine. Phase 4 can resolve art from artist+title+year on its own.

---

## Edge Cases

**Multi-session albums:** Set `multi_session: true`. Capture all session dates in `recording_dates`. If sources distinguish which tracks belong to which session, note this in `notes`. If session personnel differed (e.g., a substitute sideman on one date), reflect this in individual musician records via `session_dates`.

**Alternate takes and bonus tracks:** Set `bonus_track: true` or `alternate_take: true` in the track record. Do not include tracks added only to later reissues unless explicitly labeled as such.

**Instrument doubles:** When a musician plays more than one instrument on an album (common with saxophonists), use the primary instrument in `instrument`. Note the doubling in `notes` (e.g., "also plays soprano saxophone on tracks 3, 5"). A musician who equally splits between two instruments should use the one they are primarily associated with for this recording, with the other noted.

**Name variants:** Use the most commonly cited canonical form in `name` (e.g., "McCoy Tyner" not "Tyner, McCoy"). Record any variants found in `name_variants`. If sources conflict on the canonical form, choose the form from the most authoritative source (liner notes > Penguin Guide > AllMusic), and note the conflict.

**Rudy Van Gelder inference:** Van Gelder engineered the majority of Blue Note and Prestige sessions from the mid-1950s through the late 1960s. If a Blue Note or Prestige album from this era has no engineer listed but sources confirm it was recorded at Van Gelder Studio (Hackensack or Englewood Cliffs), record `"engineer": "Rudy Van Gelder"` with `"epistemic_production": "inf"` and note the inference.

**Source conflicts:** When two sources list different musicians for the same role (e.g., AllMusic and Wikipedia disagree on who played bass), list both musicians with `epistemic: "unk"` and explain the conflict in `notes`. Do not pick one arbitrarily — leave it for the data platform review step.

**Uncredited musicians:** If a secondary source (sessionography, later discography) identifies a musician not credited on the original release, include them with `epistemic: "inf"` or `"unk"` as appropriate, and name the source.

**Missing production credits entirely:** If a recording has no locatable production data, set `studio`, `producer`, and `engineer` to `null`, set `epistemic_production: "unk"`, and note what you searched in `notes`. Do not leave required fields absent — explicit null is better than a missing field.

---

## Epistemic Rules

From `docs/conventions.md`:
- `obs` — source directly names this musician on this album or track
- `inf` — reasoned from pattern (standard lineup confirmed elsewhere; Van Gelder inference; track assigned by session date logic)
- `unk` — uncertain: single weak source, source conflict, no corroboration, or musician present but track assignments unknown

Cite source IDs in every `sources` array. Never write `obs` without a named source behind it. When in doubt, go one level more uncertain — the data platform can upgrade confidence with better sources later; it cannot manufacture credibility that wasn't there.

---

## Quality Checks Before Submitting

- Every `album_id` exactly matches a record in the Phase 1 canon
- Every `instrument` string is from the taxonomy in `personnel-schema.md` (no free-form instrument names)
- Musician names are internally consistent within your batch — no "Bill Evans" in one record and "Evans, Bill" in another
- `track_assignments_complete` is `false` unless you have explicit source confirmation for every musician's track coverage
- Every `sources` array references a valid source ID from your source map
- Summary notes section is complete, including any albums where data was thin or absent
