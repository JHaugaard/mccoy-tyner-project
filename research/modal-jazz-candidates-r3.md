# Modal Jazz / Post-Bop Candidates — Round 3

**Agent:** jazz-modal-jazz-researcher
**Dispatch:** 2026-06-23 — gather 15 genuinely-new modal/post-bop candidate records (canon + full personnel in one pass).
**Recording-year convention:** `year` = recording year; release year noted in `notes` when it differs.
**MusicBrainz status:** retried this round per dispatch instruction; the MusicBrainz WS/2 endpoint still returned TLS certificate-verification errors on every call. All `musicbrainz_release_group_mbid` are therefore `null` and all `cover_art` arrays are empty — **not fabricated**. iTunes Search API (no cert issue) supplied Apple `collectionId`s.

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | AllMusic — album pages + Modal Jazz / Post-Bop genre pages | Web | allmusic.com | Editorial canon stature; Credits cross-reference |
| S2 | Wikipedia — individual album articles | Web | en.wikipedia.org | Personnel, sessions, durations; usually cites liner notes |
| S3 | Penguin Guide to Jazz (Cook & Morton) | Book | — | Core critical reference for canon stature (ratings recalled, used for inf-level canon weight) |
| S4 | iTunes Search API | Web/API | itunes.apple.com/search | Apple `collectionId` (apple_album_id); free, no token |
| S5 | MusicBrainz WS/2 | Web/API | musicbrainz.org/ws/2 | **FAILED — TLS cert error on every call this round; MBIDs/cover-art left null** |
| S6 | Discogs | Web | discogs.com | Release/track cross-reference surfaced in searches |
| S7 | NPR Music / DownBeat critical consensus | Web | npr.org, downbeat.com | Canon-stature corroboration (surfaced in searches) |

Production-credit convention: Blue Note / Van Gelder Studio sessions with no engineer named in the source carry `"engineer": "Rudy Van Gelder"` at `epistemic_production: "inf"` per the personnel-contract RVG rule, with a note.

Instrument-taxonomy note: `tuba` and `euphonium` (Africa/Brass, Tender Moments) and `piccolo` (Africa/Brass) are not in the contract taxonomy; per the contract's fallback rule they use the most specific descriptive term and are flagged in `notes`. "alto flute" (Speak Like a Child), "wooden flute" (Expansions) recorded as `flute` with the variant in `notes`.

---

## 2. Candidate Records

```json
{
  "id": "john-coltrane-live-at-the-village-vanguard-1961",
  "artist": "John Coltrane",
  "album": "\"Live\" at the Village Vanguard",
  "year": 1961,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents this as the first Coltrane live album and the first record to feature the classic quartet's members. obs[S1]: AllMusic catalogs it as a landmark Impulse! release. inf[S3]: Penguin-Guide-tier canon; 'Chasin' the Trane' is a touchstone of the modal/structured-blowing tradition.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-11-01/1961-11-05"],
    "multi_session": true,
    "studio": "Village Vanguard, New York City (live)",
    "producer": "Bob Thiele",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also soprano saxophone on 'Spiritual'." },
      { "name": "Eric Dolphy", "instrument": "bass clarinet", "scope": "selected-tracks", "tracks": ["Spiritual"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Bass clarinet on 'Spiritual' only." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Spiritual", "Softly, as in a Morning Sunrise"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Side one only; absent from 'Chasin' the Trane'." },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Spiritual", "Softly, as in a Morning Sunrise"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Side one bassist." },
      { "name": "Jimmy Garrison", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Chasin' the Trane"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Side two bassist; 'Chasin' the Trane' is a sax/bass/drums trio." },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Spiritual", "track_number": 1, "side": "A", "duration": "13:47", "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Eric Dolphy", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Softly, as in a Morning Sunrise", "track_number": 2, "side": "A", "duration": "6:36", "session_date": null, "composers": ["Sigmund Romberg", "Oscar Hammerstein II"], "personnel": ["John Coltrane", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Chasin' the Trane", "track_number": 3, "side": "B", "duration": "16:08", "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443320959",
    "cover_art": [],
    "notes": "Recorded over four nights at the Village Vanguard, early Nov 1961; released Feb 1962 (Impulse! A-10). Per-track personnel from Wikipedia. Tamboura/english-horn/contrabassoon contributors (Abdul-Malik, Bushell) appear only on later complete-recordings compilations, not on this 3-track original LP. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "john-coltrane-ballads-1962",
  "artist": "John Coltrane",
  "album": "Ballads",
  "year": 1962,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the classic-quartet personnel and three-session genesis. obs[S1]: AllMusic catalogs it as one of Coltrane's most beloved Impulse! albums. inf[S3]: Penguin-Guide-tier; the lyrical counterweight to the era's intensity, classic-quartet modal interplay on standards.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-12-21", "1962-09-18", "1962-11-13"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Bob Thiele",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Garrison", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Say It (Over and Over Again)", "You Don't Know What Love Is", "Too Young to Go Steady", "All or Nothing at All", "I Wish I Knew", "What's New?", "Nancy (With the Laughing Face)"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Bass on tracks 1-6 and 8." },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["It's Easy to Remember"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Bass on track 7 only (earlier session)." },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Say It (Over and Over Again)", "track_number": 1, "side": "A", "duration": "4:18", "session_date": null, "composers": ["Jimmy McHugh", "Frank Loesser"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "You Don't Know What Love Is", "track_number": 2, "side": "A", "duration": "5:15", "session_date": null, "composers": ["Gene de Paul", "Don Raye"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Too Young to Go Steady", "track_number": 3, "side": "A", "duration": "4:23", "session_date": null, "composers": ["Jimmy McHugh", "Harold Adamson"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "All or Nothing at All", "track_number": 4, "side": "A", "duration": "3:39", "session_date": null, "composers": ["Arthur Altman", "Jack Lawrence"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "I Wish I Knew", "track_number": 5, "side": "B", "duration": "4:54", "session_date": null, "composers": ["Harry Warren", "Mack Gordon"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "What's New?", "track_number": 6, "side": "B", "duration": "3:47", "session_date": null, "composers": ["Bob Haggart", "Johnny Burke"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "It's Easy to Remember", "track_number": 7, "side": "B", "duration": "2:49", "session_date": "1961-12-21", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["John Coltrane", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Nancy (With the Laughing Face)", "track_number": 8, "side": "B", "duration": "3:10", "session_date": null, "composers": ["Jimmy Van Heusen", "Phil Silvers"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440747672",
    "cover_art": [],
    "notes": "Three sessions: 1961-12-21, 1962-09-18, 1962-11-13. Released January 1963 (Impulse! A-32). 'It's Easy to Remember' is the Reggie Workman track (earliest session); Garrison on the rest. Composer second-names added from standard credits. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "john-coltrane-africa-brass-1961",
  "artist": "John Coltrane",
  "album": "Africa/Brass",
  "year": 1961,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the large-ensemble personnel, Dolphy/Tyner arrangements, and two-session genesis. obs[S1]: AllMusic catalogs Coltrane's first Impulse! album and his most ambitious orchestral-modal statement. inf[S3]: Penguin-tier; 'Africa' extends the modal vamp approach to a brass orchestra.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-05-23", "1961-06-07"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Creed Taylor",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also soprano saxophone." },
      { "name": "Booker Little", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Core ensemble both sessions." },
      { "name": "Eric Dolphy", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also bass clarinet and flute; co-arranger." },
      { "name": "Pat Patrick", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Julius Watkins", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Bob Northern", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Robert Swisshelm", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Bill Barber", "instrument": "tuba", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Instrument 'tuba' outside contract taxonomy (descriptive term per fallback rule)." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Co-arranger; arranged 'Greensleeves'." },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Core bassist both sessions; doubled by a second bass on each track." },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "May 23 session only." },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Second bass, May 23 session." },
      { "name": "Jim Buffington", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "May 23 session only." },
      { "name": "Julian Priester", "instrument": "euphonium", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Euphonium outside taxonomy; May 23 only." },
      { "name": "Charles Greenlee", "instrument": "euphonium", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Euphonium outside taxonomy; May 23 only." },
      { "name": "Garvin Bushell", "instrument": "piccolo", "scope": "selected-tracks", "tracks": ["Greensleeves"], "session_dates": ["1961-05-23"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Piccolo/reeds; outside taxonomy; May 23 only." },
      { "name": "Britt Woodman", "instrument": "trombone", "scope": "selected-tracks", "tracks": ["Africa", "Blues Minor"], "session_dates": ["1961-06-07"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "June 7 session only." },
      { "name": "Donald Corrado", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Africa", "Blues Minor"], "session_dates": ["1961-06-07"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "June 7 session only." },
      { "name": "Carl Bowman", "instrument": "euphonium", "scope": "selected-tracks", "tracks": ["Africa", "Blues Minor"], "session_dates": ["1961-06-07"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Euphonium outside taxonomy; June 7 only." },
      { "name": "Art Davis", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Africa"], "session_dates": ["1961-06-07"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Second bass on 'Africa' (alongside Workman)." }
    ],
    "tracks": [
      { "title": "Africa", "track_number": 1, "side": "A", "duration": "16:28", "session_date": "1961-06-07", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Booker Little", "Eric Dolphy", "Pat Patrick", "Julius Watkins", "Bob Northern", "Robert Swisshelm", "Bill Barber", "McCoy Tyner", "Reggie Workman", "Elvin Jones", "Britt Woodman", "Donald Corrado", "Carl Bowman", "Art Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Greensleeves", "track_number": 2, "side": "B", "duration": "10:00", "session_date": "1961-05-23", "composers": ["Traditional"], "personnel": ["John Coltrane", "Booker Little", "Eric Dolphy", "Pat Patrick", "Julius Watkins", "Bob Northern", "Robert Swisshelm", "Bill Barber", "McCoy Tyner", "Reggie Workman", "Elvin Jones", "Freddie Hubbard", "Paul Chambers", "Jim Buffington", "Julian Priester", "Charles Greenlee", "Garvin Bushell"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Blues Minor", "track_number": 3, "side": "B", "duration": "7:22", "session_date": "1961-06-07", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Booker Little", "Eric Dolphy", "Pat Patrick", "Julius Watkins", "Bob Northern", "Robert Swisshelm", "Bill Barber", "McCoy Tyner", "Reggie Workman", "Elvin Jones", "Britt Woodman", "Donald Corrado", "Carl Bowman"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "6767697431",
    "cover_art": [],
    "notes": "Arranged by Eric Dolphy and McCoy Tyner. 'Greensleeves' = May 23 session; 'Africa' and 'Blues Minor' = June 7 session. Two basses per track. track_assignments_complete=false: exact French-horn-to-track distribution within the brass choir not fully isolatable from the source. Released Sept 1961. Instrument strings 'tuba'/'euphonium'/'piccolo' are descriptive (outside taxonomy). MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "bill-evans-portrait-in-jazz-1959",
  "artist": "Bill Evans",
  "album": "Portrait in Jazz",
  "year": 1959,
  "label": "Riverside",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "cool-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the first studio album by the Evans/LaFaro/Motian trio. obs[S1]: AllMusic catalogs it as the founding statement of the interactive piano-trio language. inf[S3]: Penguin-tier; impressionistic, modal-leaning trio interplay that reshaped jazz piano.",
  "priority": "strong",
  "overlap_risk": "Adjacent to the already-pending Sunday at the Village Vanguard / Waltz for Debby (same trio, 1961)",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-12-28"],
    "multi_session": false,
    "studio": "Reeves Sound Studios, New York City",
    "producer": "Orrin Keepnews",
    "engineer": "Jack Higgins",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Bill Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Scott LaFaro", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Paul Motian", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Come Rain or Come Shine", "track_number": 1, "side": "A", "duration": "3:24", "session_date": "1959-12-28", "composers": ["Harold Arlen", "Johnny Mercer"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Autumn Leaves", "track_number": 2, "side": "A", "duration": "6:00", "session_date": "1959-12-28", "composers": ["Joseph Kosma", "Jacques Prévert", "Johnny Mercer"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Witchcraft", "track_number": 3, "side": "A", "duration": "4:37", "session_date": "1959-12-28", "composers": ["Cy Coleman", "Carolyn Leigh"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "When I Fall in Love", "track_number": 4, "side": "A", "duration": "4:57", "session_date": "1959-12-28", "composers": ["Victor Young", "Edward Heyman"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Peri's Scope", "track_number": 5, "side": "A", "duration": "3:15", "session_date": "1959-12-28", "composers": ["Bill Evans"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "What Is This Thing Called Love?", "track_number": 6, "side": "B", "duration": "4:36", "session_date": "1959-12-28", "composers": ["Cole Porter"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Spring Is Here", "track_number": 7, "side": "B", "duration": "5:09", "session_date": "1959-12-28", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Someday My Prince Will Come", "track_number": 8, "side": "B", "duration": "4:57", "session_date": "1959-12-28", "composers": ["Frank Churchill", "Larry Morey"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Blue in Green", "track_number": 9, "side": "B", "duration": "5:25", "session_date": "1959-12-28", "composers": ["Miles Davis", "Bill Evans"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440941536",
    "cover_art": [],
    "notes": "Single session, Dec 28 1959 (Riverside RLP 12-315). 2008 CD adds alternate takes (not included here). Apple ID 1440941536 is the original-program edition. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "bill-evans-explorations-1961",
  "artist": "Bill Evans",
  "album": "Explorations",
  "year": 1961,
  "label": "Riverside",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Evans/LaFaro/Motian trio's second studio album. obs[S1]: AllMusic catalogs it as a key entry in the trio's brief, foundational run. inf[S3]: Penguin-tier; deepens the interactive-trio modal sensibility ('Nardis', 'Elsa').",
  "priority": "strong",
  "overlap_risk": "Same trio as Portrait in Jazz / Waltz for Debby",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-02-02"],
    "multi_session": false,
    "studio": "Bell Sound Studios, New York City",
    "producer": "Orrin Keepnews",
    "engineer": "Bill Stoddard",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Bill Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Scott LaFaro", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Paul Motian", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Israel", "track_number": 1, "side": "A", "duration": "6:12", "session_date": "1961-02-02", "composers": ["John Carisi"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Haunted Heart", "track_number": 2, "side": "A", "duration": "3:28", "session_date": "1961-02-02", "composers": ["Arthur Schwartz", "Howard Dietz"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Beautiful Love", "track_number": 3, "side": "A", "duration": "5:04", "session_date": "1961-02-02", "composers": ["Wayne King", "Egbert Van Alstyne", "Victor Young", "Haven Gillespie"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Elsa", "track_number": 4, "side": "A", "duration": "5:10", "session_date": "1961-02-02", "composers": ["Earl Zindars"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Nardis", "track_number": 5, "side": "B", "duration": "5:49", "session_date": "1961-02-02", "composers": ["Miles Davis"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "How Deep Is the Ocean?", "track_number": 6, "side": "B", "duration": "3:31", "session_date": "1961-02-02", "composers": ["Irving Berlin"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "I Wish I Knew", "track_number": 7, "side": "B", "duration": "4:39", "session_date": "1961-02-02", "composers": ["Harry Warren", "Mack Gordon"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Sweet and Lovely", "track_number": 8, "side": "B", "duration": "5:52", "session_date": "1961-02-02", "composers": ["Gus Arnheim", "Jules LeMare", "Harry Tobias"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440794254",
    "cover_art": [],
    "notes": "Single session, Feb 2 1961 (Riverside RLP 351). 'Beautiful Love' is Take 2 on the original. CD reissues add alternate takes (excluded). Apple ID 1440794254 = 1987 remaster of the original program. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "bill-evans-waltz-for-debby-1961",
  "artist": "Bill Evans",
  "album": "Waltz for Debby",
  "year": 1961,
  "label": "Riverside",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the June 25 1961 Village Vanguard date by the Evans/LaFaro/Motian trio (LaFaro's final recordings). obs[S1]: AllMusic catalogs it among the most celebrated live piano-trio albums. inf[S3]: Penguin-tier core-collection pillar.",
  "priority": "must_have",
  "overlap_risk": "Same date/trio as the already-pending Sunday at the Village Vanguard",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-06-25"],
    "multi_session": false,
    "studio": "Village Vanguard, New York City (live)",
    "producer": "Orrin Keepnews",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Bill Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Scott LaFaro", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "LaFaro's final recordings; he died ten days later." },
      { "name": "Paul Motian", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "My Foolish Heart", "track_number": 1, "side": "A", "duration": "4:58", "session_date": "1961-06-25", "composers": ["Victor Young", "Ned Washington"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Waltz for Debby", "track_number": 2, "side": "A", "duration": "7:00", "session_date": "1961-06-25", "composers": ["Bill Evans", "Gene Lees"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Detour Ahead", "track_number": 3, "side": "A", "duration": "7:37", "session_date": "1961-06-25", "composers": ["Lou Carter", "Herb Ellis", "Johnny Frigo"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "My Romance", "track_number": 4, "side": "B", "duration": "7:13", "session_date": "1961-06-25", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Some Other Time", "track_number": 5, "side": "B", "duration": "5:11", "session_date": "1961-06-25", "composers": ["Leonard Bernstein", "Betty Comden", "Adolph Green"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Milestones", "track_number": 6, "side": "B", "duration": "6:30", "session_date": "1961-06-25", "composers": ["Miles Davis"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440747830",
    "cover_art": [],
    "notes": "Recorded live at the Village Vanguard June 25 1961 (same date as Sunday at the Village Vanguard); released late Feb/early March 1962 (Riverside RLP 399). 'Waltz for Debby' = Take 2, 'Detour Ahead' = Take 2, 'My Romance' = Take 1 on the original LP. CD adds alternates + 'Porgy' (excluded). Engineer not named in source → null. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "wayne-shorter-night-dreamer-1964",
  "artist": "Wayne Shorter",
  "album": "Night Dreamer",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents Shorter's first Blue Note album as leader with a Coltrane-quartet-adjacent rhythm section (Tyner, Workman, Jones). obs[S1]: AllMusic catalogs it as a key early Shorter leader date. inf[S3]: Penguin-tier; modal-leaning post-bop in the Blue Note house style.",
  "priority": "strong",
  "overlap_risk": "Shares Tyner/Jones with the Coltrane quartet records this round",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-04-29"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Night Dreamer", "track_number": 1, "side": "A", "duration": "7:15", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Oriental Folk Song", "track_number": 2, "side": "A", "duration": "6:50", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Virgo", "track_number": 3, "side": "A", "duration": "7:05", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Black Nile", "track_number": 4, "side": "B", "duration": "6:25", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Charcoal Blues", "track_number": 5, "side": "B", "duration": "6:50", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Armageddon", "track_number": 6, "side": "B", "duration": "6:20", "session_date": "1964-04-29", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Lee Morgan", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1442997628",
    "cover_art": [],
    "notes": "Single session, April 29 1964 (Blue Note BLP 4173). Durations from the 1987 CD; a 'Virgo' alternate take is a CD addition (excluded from the 6-track original). All compositions by Shorter. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "wayne-shorter-the-all-seeing-eye-1965",
  "artist": "Wayne Shorter",
  "album": "The All Seeing Eye",
  "year": 1965,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop"],
  "sources": ["S1", "S2", "S4", "S7"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Oct 15 1965 septet date with Hubbard, Moncur, Spaulding, Hancock, Carter, Chambers. obs[S1]: AllMusic catalogs it as Shorter's most ambitious/abstract Blue Note program. unk[S7]: some catalogs (RYM) tag it avant-garde jazz — see scope flag.",
  "priority": "consider",
  "overlap_risk": "Shares Hancock/Carter with the Second Quintet records already collected",
  "scope_flag": "Edges toward avant-garde post-bop (compositionally outside, but themes/structure hold) — keep, but flag for John's avant-tolerance call",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1965-10-15"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also flugelhorn." },
      { "name": "Grachan Moncur III", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "James Spaulding", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Joe Chambers", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Alan Shorter", "instrument": "flugelhorn", "scope": "selected-tracks", "tracks": ["Mephistopheles"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Wayne's brother; composed and plays flugelhorn on 'Mephistopheles' only." }
    ],
    "tracks": [
      { "title": "The All Seeing Eye", "track_number": 1, "side": "A", "duration": "10:32", "session_date": "1965-10-15", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Grachan Moncur III", "James Spaulding", "Herbie Hancock", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Genesis", "track_number": 2, "side": "A", "duration": "11:44", "session_date": "1965-10-15", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Grachan Moncur III", "James Spaulding", "Herbie Hancock", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Chaos", "track_number": 3, "side": "B", "duration": "6:56", "session_date": "1965-10-15", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Grachan Moncur III", "James Spaulding", "Herbie Hancock", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Face of the Deep", "track_number": 4, "side": "B", "duration": "5:29", "session_date": "1965-10-15", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Grachan Moncur III", "James Spaulding", "Herbie Hancock", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Mephistopheles", "track_number": 5, "side": "B", "duration": "9:40", "session_date": "1965-10-15", "composers": ["Alan Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Grachan Moncur III", "James Spaulding", "Herbie Hancock", "Ron Carter", "Joe Chambers", "Alan Shorter"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443232004",
    "cover_art": [],
    "notes": "Single session, Oct 15 1965 (Blue Note BLP 4219); released Oct 1966. Engineer not named in source → RVG inferred (Van Gelder Studio) per contract, epistemic_production inf. Hubbard doubles flugelhorn. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "mccoy-tyner-expansions-1968",
  "artist": "McCoy Tyner",
  "album": "Expansions",
  "year": 1968,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Aug 23 1968 sextet (Shaw, Bartz, Shorter, Carter on cello, Lewis, Waits). obs[S1]: AllMusic frames it as Tyner's transitional modal/post-bop statement 'between advanced hard bop and the avant-garde'. inf[S3-style canon]: a strong late-Blue-Note Tyner date bridging to his Milestone modal period.",
  "priority": "consider",
  "overlap_risk": "Tyner leader date — adjacent to The Real McCoy (collected) and Sahara (pending)",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1968-08-23"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Duke Pearson",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Woody Shaw", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Gary Bartz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also wooden flute on 'Song of Happiness' (recorded as flute; variant 'wooden flute')." },
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also clarinet on 'Song of Happiness'." },
      { "name": "Ron Carter", "instrument": "cello", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Plays cello (not bass) on this date." },
      { "name": "Herbie Lewis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Freddie Waits", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Vision", "track_number": 1, "side": "A", "duration": "12:18", "session_date": "1968-08-23", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Woody Shaw", "Gary Bartz", "Wayne Shorter", "Ron Carter", "Herbie Lewis", "Freddie Waits"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Song of Happiness", "track_number": 2, "side": "A", "duration": "12:00", "session_date": "1968-08-23", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Woody Shaw", "Gary Bartz", "Wayne Shorter", "Ron Carter", "Herbie Lewis", "Freddie Waits"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Smitty's Place", "track_number": 3, "side": "B", "duration": "5:21", "session_date": "1968-08-23", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Woody Shaw", "Gary Bartz", "Wayne Shorter", "Ron Carter", "Herbie Lewis", "Freddie Waits"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Peresina", "track_number": 4, "side": "B", "duration": "10:21", "session_date": "1968-08-23", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Woody Shaw", "Gary Bartz", "Wayne Shorter", "Ron Carter", "Herbie Lewis", "Freddie Waits"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "I Thought I'd Let You Know", "track_number": 5, "side": "B", "duration": "6:25", "session_date": "1968-08-23", "composers": ["Cal Massey"], "personnel": ["McCoy Tyner", "Woody Shaw", "Gary Bartz", "Wayne Shorter", "Ron Carter", "Herbie Lewis", "Freddie Waits"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444097844",
    "cover_art": [],
    "notes": "Single session, Aug 23 1968 (Blue Note BST 84338); released 1970. Bartz doubles wooden flute and Shorter doubles clarinet on 'Song of Happiness'. Ron Carter on cello, Herbie Lewis on bass. Engineer not listed in source → RVG inferred (Van Gelder Studio), epistemic_production inf. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "mccoy-tyner-tender-moments-1967",
  "artist": "McCoy Tyner",
  "album": "Tender Moments",
  "year": 1967,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Dec 1 1967 nonet — Tyner's first big-band/large-ensemble Blue Note date — with Morgan, Priester, Northern, Johnson, Spaulding, Maupin, Lewis, Chambers. obs[S1]: AllMusic catalogs it among Tyner's Blue Note leader dates. inf: extends his modal writing to a brass-and-reed choir.",
  "priority": "consider",
  "overlap_risk": "Tyner leader date — adjacent to The Real McCoy / Expansions",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1967-12-01"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Francis Wolff",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also on the quartet track 'Lee Plus Three'." },
      { "name": "Julian Priester", "instrument": "trombone", "scope": "selected-tracks", "tracks": ["Mode to John", "Man from Tanganyika", "The High Priest", "Utopia", "All My Yesterdays"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Absent on 'Lee Plus Three'." },
      { "name": "Bob Northern", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Mode to John", "Man from Tanganyika", "The High Priest", "Utopia", "All My Yesterdays"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Absent on 'Lee Plus Three'." },
      { "name": "Howard Johnson", "instrument": "tuba", "scope": "selected-tracks", "tracks": ["Mode to John", "Man from Tanganyika", "The High Priest", "Utopia", "All My Yesterdays"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Tuba outside taxonomy (descriptive). Absent on 'Lee Plus Three'." },
      { "name": "James Spaulding", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Mode to John", "Man from Tanganyika", "The High Priest", "Utopia", "All My Yesterdays"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also flute. Absent on 'Lee Plus Three'." },
      { "name": "Bennie Maupin", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Mode to John", "Man from Tanganyika", "The High Priest", "Utopia", "All My Yesterdays"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Absent on 'Lee Plus Three'." },
      { "name": "Herbie Lewis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Joe Chambers", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Mode to John", "track_number": 1, "side": "A", "duration": "5:42", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Julian Priester", "Bob Northern", "Howard Johnson", "James Spaulding", "Bennie Maupin", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Man from Tanganyika", "track_number": 2, "side": "A", "duration": "6:54", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Julian Priester", "Bob Northern", "Howard Johnson", "James Spaulding", "Bennie Maupin", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "The High Priest", "track_number": 3, "side": "A", "duration": "6:08", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Julian Priester", "Bob Northern", "Howard Johnson", "James Spaulding", "Bennie Maupin", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Utopia", "track_number": 4, "side": "B", "duration": "7:37", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Julian Priester", "Bob Northern", "Howard Johnson", "James Spaulding", "Bennie Maupin", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "All My Yesterdays", "track_number": 5, "side": "B", "duration": "6:04", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Julian Priester", "Bob Northern", "Howard Johnson", "James Spaulding", "Bennie Maupin", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Lee Plus Three", "track_number": 6, "side": "B", "duration": "5:35", "session_date": "1967-12-01", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Lee Morgan", "Herbie Lewis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "715643790",
    "cover_art": [],
    "notes": "Single session, Dec 1 1967 (Blue Note BST 84275); released 1968. 'Lee Plus Three' is a quartet (Tyner/Morgan/Lewis/Chambers); the five horn-section players sit out. All compositions by Tyner. Howard Johnson 'tuba' outside taxonomy. Engineer not listed → RVG inferred, epistemic_production inf. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "herbie-hancock-speak-like-a-child-1968",
  "artist": "Herbie Hancock",
  "album": "Speak Like a Child",
  "year": 1968,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the March 1968 sextet with an unusual flugelhorn/bass-trombone/alto-flute front line over a Carter/Roker rhythm section. obs[S1]: AllMusic catalogs it as a key reflective post-bop Hancock leader date. inf[S3]: Penguin-tier; lush modal harmony bridging Maiden Voyage to his later work.",
  "priority": "strong",
  "overlap_risk": "Hancock leader date — adjacent to Maiden Voyage / Empyrean Isles (collected/pending)",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1968-03-06", "1968-03-09"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Duke Pearson",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Mickey Roker", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Thad Jones", "instrument": "flugelhorn", "scope": "selected-tracks", "tracks": ["Riot", "Speak Like a Child", "First Trip", "Toys", "Goodbye to Childhood"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Absent on 'The Sorcerer' (trio track)." },
      { "name": "Peter Phillips", "instrument": "bass trombone", "scope": "selected-tracks", "tracks": ["Riot", "Speak Like a Child", "First Trip", "Toys", "Goodbye to Childhood"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Absent on 'The Sorcerer'." },
      { "name": "Jerry Dodgion", "instrument": "flute", "scope": "selected-tracks", "tracks": ["Riot", "Speak Like a Child", "First Trip", "Toys", "Goodbye to Childhood"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": ["alto flute"], "notes": "Plays alto flute (recorded as flute). Absent on 'The Sorcerer'." }
    ],
    "tracks": [
      { "title": "Riot", "track_number": 1, "side": "A", "duration": "4:40", "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker", "Thad Jones", "Peter Phillips", "Jerry Dodgion"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Speak Like a Child", "track_number": 2, "side": "A", "duration": "7:50", "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker", "Thad Jones", "Peter Phillips", "Jerry Dodgion"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "First Trip", "track_number": 3, "side": "A", "duration": "6:01", "session_date": null, "composers": ["Ron Carter"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker", "Thad Jones", "Peter Phillips", "Jerry Dodgion"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Toys", "track_number": 4, "side": "B", "duration": "5:52", "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker", "Thad Jones", "Peter Phillips", "Jerry Dodgion"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Goodbye to Childhood", "track_number": 5, "side": "B", "duration": "7:06", "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker", "Thad Jones", "Peter Phillips", "Jerry Dodgion"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "The Sorcerer", "track_number": 6, "side": "B", "duration": "5:36", "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Ron Carter", "Mickey Roker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444110917",
    "cover_art": [],
    "notes": "Two sessions, March 6 and 9 1968 (Blue Note BST 84279). The three horns play on tracks 1-5; 'The Sorcerer' is a piano-trio track. Source does not split tracks by exact session date → per-track session_date null. Engineer not listed → RVG inferred (Van Gelder Studio), epistemic_production inf. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "larry-young-unity-1965",
  "artist": "Larry Young",
  "album": "Unity",
  "year": 1965,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Nov 10 1965 quartet (Young, Shaw, Henderson, Elvin Jones) and the modal Woody Shaw originals. obs[S1]: AllMusic catalogs it as the landmark that recast the Hammond organ in a Coltrane-modal idiom. inf[S3]: widely cited as the defining modal organ album — 'Coltrane on organ'.",
  "priority": "must_have",
  "overlap_risk": "Shares Elvin Jones with the Coltrane records this round; Henderson/Shaw recur",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1965-11-10"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Larry Young", "instrument": "organ", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Hammond B-3 organ." },
      { "name": "Woody Shaw", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed three of the six tunes." },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Zoltan", "track_number": 1, "side": "A", "duration": "7:41", "session_date": "1965-11-10", "composers": ["Woody Shaw"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Monk's Dream", "track_number": 2, "side": "A", "duration": "5:48", "session_date": "1965-11-10", "composers": ["Thelonious Monk"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "If", "track_number": 3, "side": "A", "duration": "6:46", "session_date": "1965-11-10", "composers": ["Joe Henderson"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "The Moontrane", "track_number": 4, "side": "B", "duration": "7:21", "session_date": "1965-11-10", "composers": ["Woody Shaw"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Softly, as in a Morning Sunrise", "track_number": 5, "side": "B", "duration": "6:24", "session_date": "1965-11-10", "composers": ["Sigmund Romberg", "Oscar Hammerstein II"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Beyond All Limits", "track_number": 6, "side": "B", "duration": "6:02", "session_date": "1965-11-10", "composers": ["Woody Shaw"], "personnel": ["Larry Young", "Woody Shaw", "Joe Henderson", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1457590359",
    "cover_art": [],
    "notes": "Single session, Nov 10 1965 (Blue Note BLP 4221); released Aug 1966. No chordal piano — Young's organ holds the harmony. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "bobby-hutcherson-dialogue-1965",
  "artist": "Bobby Hutcherson",
  "album": "Dialogue",
  "year": 1965,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the April 3 1965 sextet (Hutcherson, Rivers, Hubbard, Andrew Hill, Richard Davis, Joe Chambers) and the Hill/Chambers compositions. obs[S1]: AllMusic catalogs it as Hutcherson's debut as leader and a key modern Blue Note date. unk: leans toward the avant-garde edge of post-bop — see scope flag.",
  "priority": "consider",
  "overlap_risk": "Andrew Hill writing/playing — adjacent to the pending Point of Departure",
  "scope_flag": "Avant-leaning post-bop (Andrew Hill / Sam Rivers idiom) — still composed and structured; keep, flag for John's avant-tolerance call",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1965-04-03"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Bobby Hutcherson", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also marimba on 'Les Noirs Marchant' and 'Dialogue'." },
      { "name": "Sam Rivers", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Multi-reeds: tenor (1,6), soprano (5), bass clarinet (4,5,6), flute (2,3) per source." },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Andrew Hill", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed four of the tunes." },
      { "name": "Richard Davis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Joe Chambers", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed 'Idle While' and 'Dialogue'." }
    ],
    "tracks": [
      { "title": "Catta", "track_number": 1, "side": "A", "duration": "7:19", "session_date": "1965-04-03", "composers": ["Andrew Hill"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Idle While", "track_number": 2, "side": "A", "duration": "6:37", "session_date": "1965-04-03", "composers": ["Joe Chambers"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Les Noirs Marchant", "track_number": 3, "side": "A", "duration": "6:41", "session_date": "1965-04-03", "composers": ["Andrew Hill"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Dialogue", "track_number": 4, "side": "B", "duration": "9:59", "session_date": "1965-04-03", "composers": ["Joe Chambers"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Ghetto Lights", "track_number": 5, "side": "B", "duration": "6:16", "session_date": "1965-04-03", "composers": ["Andrew Hill"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Jasper", "track_number": 6, "side": "B", "duration": "8:29", "session_date": "1965-04-03", "composers": ["Andrew Hill"], "personnel": ["Bobby Hutcherson", "Sam Rivers", "Freddie Hubbard", "Andrew Hill", "Richard Davis", "Joe Chambers"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "723562758",
    "cover_art": [],
    "notes": "Single session, April 3 1965 (Blue Note BST 84198); released Sept 1965. 'Jasper' is a CD bonus track (flagged). Rivers switches reeds per track; Hutcherson doubles marimba on tracks 3-4. Engineer not specified in source → RVG inferred (Van Gelder Studio), epistemic_production inf. Apple ID 723562758 = RVG Edition. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "charles-lloyd-forest-flower-1966",
  "artist": "Charles Lloyd",
  "album": "Forest Flower",
  "year": 1966,
  "label": "Atlantic",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Sept 18 1966 Monterey Jazz Festival set by the Lloyd quartet with a young Keith Jarrett, Cecil McBee, and Jack DeJohnette. obs[S1]: AllMusic catalogs it as one of the best-selling jazz albums of its era and a modal crossover landmark. inf[S3]: Penguin-tier; modal post-bop that reached the rock audience without crossing into fusion.",
  "priority": "strong",
  "overlap_risk": "Early Keith Jarrett — adjacent to the pending Köln Concert (very different setting)",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1966-09-18"],
    "multi_session": false,
    "studio": "Monterey Jazz Festival, Monterey, California (live)",
    "producer": "George Avakian",
    "engineer": "Wally Heider",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Charles Lloyd", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Also flute." },
      { "name": "Keith Jarrett", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Cecil McBee", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed 'Song of Her'." },
      { "name": "Jack DeJohnette", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Forest Flower: Sunrise", "track_number": 1, "side": "A", "duration": "7:18", "session_date": "1966-09-18", "composers": ["Charles Lloyd"], "personnel": ["Charles Lloyd", "Keith Jarrett", "Cecil McBee", "Jack DeJohnette"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Forest Flower: Sunset", "track_number": 2, "side": "A", "duration": "10:37", "session_date": "1966-09-18", "composers": ["Charles Lloyd"], "personnel": ["Charles Lloyd", "Keith Jarrett", "Cecil McBee", "Jack DeJohnette"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Sorcery", "track_number": 3, "side": "B", "duration": "5:18", "session_date": "1966-09-18", "composers": ["Keith Jarrett"], "personnel": ["Charles Lloyd", "Keith Jarrett", "Cecil McBee", "Jack DeJohnette"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Song of Her", "track_number": 4, "side": "B", "duration": "5:24", "session_date": "1966-09-18", "composers": ["Cecil McBee"], "personnel": ["Charles Lloyd", "Keith Jarrett", "Cecil McBee", "Jack DeJohnette"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "East of the Sun", "track_number": 5, "side": "B", "duration": "10:40", "session_date": "1966-09-18", "composers": ["Brooks Bowman"], "personnel": ["Charles Lloyd", "Keith Jarrett", "Cecil McBee", "Jack DeJohnette"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "68186727",
    "cover_art": [],
    "notes": "Recorded live at the Monterey Jazz Festival Sept 18 1966 (Atlantic SD 1473); released Feb 1967. Lloyd doubles flute. Apple ID 68186727 carries a 1968 reissue date. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

```json
{
  "id": "joe-henderson-mode-for-joe-1966",
  "artist": "Joe Henderson",
  "album": "Mode for Joe",
  "year": 1966,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Wikipedia documents the Jan 27 1966 septet (Henderson, Morgan, Fuller, Hutcherson, Walton, Carter, Chambers) and the Walton/Henderson originals. obs[S1]: AllMusic catalogs it as one of Henderson's strongest, most modal-tinged Blue Note leader dates. inf[S3]: Penguin-tier; arranged post-bop with a modal harmonic palette.",
  "priority": "strong",
  "overlap_risk": "Henderson leader date — adjacent to the pending Inner Urge / Page One",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1966-01-27"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed 'Free Wheelin''." },
      { "name": "Curtis Fuller", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Bobby Hutcherson", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Cedar Walton", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composed 'Mode for Joe' and 'Black'." },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Joe Chambers", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "A Shade of Jade", "track_number": 1, "side": "A", "duration": "7:08", "session_date": "1966-01-27", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Mode for Joe", "track_number": 2, "side": "A", "duration": "8:00", "session_date": "1966-01-27", "composers": ["Cedar Walton"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Black", "track_number": 3, "side": "A", "duration": "6:51", "session_date": "1966-01-27", "composers": ["Cedar Walton"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Caribbean Fire Dance", "track_number": 4, "side": "B", "duration": "6:41", "session_date": "1966-01-27", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Granted", "track_number": 5, "side": "B", "duration": "7:20", "session_date": "1966-01-27", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Free Wheelin'", "track_number": 6, "side": "B", "duration": "6:39", "session_date": "1966-01-27", "composers": ["Lee Morgan"], "personnel": ["Joe Henderson", "Lee Morgan", "Curtis Fuller", "Bobby Hutcherson", "Cedar Walton", "Ron Carter", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444104530",
    "cover_art": [],
    "notes": "Single session, Jan 27 1966 (Blue Note BLP 4227); released Sept 1966. A 'Black' alternate take is a CD bonus (excluded from the 6-track original). Engineer not provided in source → RVG inferred (Van Gelder Studio), epistemic_production inf. MusicBrainz cert-failure → MBID/cover-art null."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves (true pillars)
- **Coltrane "Live" at the Village Vanguard (1961)** — the first Coltrane live album and first to capture the classic quartet's members; "Chasin' the Trane" is a foundational structured-blowing modal statement.
- **Bill Evans — Waltz for Debby (1961)** — the most celebrated live document of the Evans/LaFaro/Motian trio (LaFaro's last recordings), a core-collection piano-trio pillar.
- **Larry Young — Unity (1965)** — the defining modal organ album, recasting the Hammond B-3 in a Coltrane-quartet idiom; "The Moontrane" and "Zoltan" are standards.

### Hidden Gems (strong but under-cited relative to the pillars)
- **McCoy Tyner — Tender Moments (1967)** — Tyner's only large-ensemble Blue Note date; modal writing for a brass-and-reed nonet, rarely on best-of lists.
- **Wayne Shorter — The All Seeing Eye (1965)** — Shorter's most ambitious/abstract Blue Note program; under-cited because it sits at the avant edge.
- **Bobby Hutcherson — Dialogue (1965)** — debut as leader; an Andrew Hill / Sam Rivers writing summit that gets overshadowed by Hutcherson's later soul-jazz work.

### Consensus Picks (3+ sources / broad canon agreement)
Coltrane "Live" at the Village Vanguard, Ballads, Africa/Brass; Bill Evans Portrait in Jazz, Waltz for Debby, Explorations; Larry Young Unity; Charles Lloyd Forest Flower — all carry AllMusic + Wikipedia + Penguin-tier critical consensus (S1/S2/S3, with S7 corroboration on several).

### Single-Source Picks
None rest on a single source. Every record is anchored by Wikipedia (S2, personnel/sessions) plus AllMusic (S1, canon stature), with Apple IDs from S4. The All Seeing Eye additionally drew on S7 (search-surfaced critical/RYM tagging) for its avant-garde classification note.

### Scope Calls (boundary judgments)
- **The All Seeing Eye (1965)** — kept as post-bop despite an avant-garde tag in some catalogs (S7): the pieces are through-composed with stated themes and structure, not free improvisation. Flagged for John's avant-tolerance.
- **Dialogue (1965)** — same call: Andrew Hill/Sam Rivers idiom leans outside, but every track is a composed structure; kept, flagged.
- **Expansions / Tender Moments (1967–68)** — late-Blue-Note Tyner, post-Real-McCoy; AllMusic frames Expansions as "between advanced hard bop and the avant-garde." Comfortably in scope (modal, swinging, pre-fusion); kept at `consider`.
- **Forest Flower (1966)** — a commercial crossover that reached rock audiences, but the music is acoustic modal post-bop with no rock/funk elements; pre-fusion in spirit, firmly in.
- No date-based down-ranking applied (per genre-definitions draft 2): the 1959–1968 spread is all center-of-gravity material.

### Gaps Noticed
- **Per-session track distribution** on multi-session albums is thin in web sources: Ballads (3 sessions) and Speak Like a Child (2 sessions) could not be fully split by track without liner notes / Tom Lord (which I did not reach this round).
- **Africa/Brass** brass-choir internal assignments (which French horn on which track) are not isolatable from Wikipedia alone — Tom Lord would resolve this.
- **ECM late-modal** (Jarrett's solo/European-quartet ECM run, Garbarek) remains largely untouched and is a candidate-rich vein for a future round.
- **Pharoah Sanders in-scope dates** (e.g., the more lyrical Karma-adjacent material) were not evaluated this round.

### Personnel Coverage
- **Full track-level assignments reached (track_assignments_complete: true)** on 14 of 15: the three Bill Evans trios, both Coltrane live/quartet records (per-track personnel explicit), Night Dreamer, The All Seeing Eye, Expansions, Tender Moments, Speak Like a Child, Unity, Dialogue, Forest Flower, Mode for Joe. Durations captured for every original-LP track (last round's null-duration gap is closed).
- **Africa/Brass** is the lone `false`: full personnel and per-track session attribution captured, but the exact French-horn-to-track split within the brass choir is not source-confirmed.
- **Production credits:** producer + engineer fully confirmed (`obs`) on 7 records. Five Blue Note dates (The All Seeing Eye, Expansions, Tender Moments, Speak Like a Child, Dialogue, Mode for Joe) carry `engineer: "Rudy Van Gelder"` at `epistemic_production: "inf"` via the contract's Van Gelder Studio rule. Waltz for Debby's live engineer is unknown (`null`).
- **IDs:** Apple `collectionId` captured for all 15 (S4). All MusicBrainz MBIDs and Cover Art Archive URLs are `null` — the endpoint failed with TLS certificate errors on every attempt this round, as the dispatch anticipated; nothing fabricated.
