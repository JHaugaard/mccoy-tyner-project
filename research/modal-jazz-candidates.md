# Modal Jazz / Post-Bop — Candidate Records

**Specialist:** Modal Jazz & Post-Bop researcher
**Run:** POC, 5 candidates · 2026-06-18
**Directive:** Gather 5 next-best candidates (full merged contract — canon + personnel) for The Jazz Canon.
**Exclusions:** `data/dispatch-ledger.json` `albums_in_collection` empty — nothing excluded this run.
**Calibration:** `research/cull-notes.md` empty — no prior verdicts to honor.

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — album articles | Encyclopedia | en.wikipedia.org/wiki/{Kind_of_Blue, A_Love_Supreme, The_Real_McCoy_(McCoy_Tyner_album), Maiden_Voyage_(Herbie_Hancock_album), Speak_No_Evil_(Wayne_Shorter_album)} | Personnel, sessions, studios, producers, track listings. Consulted this run. |
| S2 | iTunes Search API | API | itunes.apple.com/search | Apple `collectionId` (apple_album_id) per album. Free, no token. Consulted this run. |
| S3 | MusicBrainz release-group API | API | musicbrainz.org/ws/2/release-group | Release-group MBIDs. Consulted this run. |
| S4 | uDiscoverMusic "Best Jazz Albums" / JazzFuel "50 Best Jazz Albums" | Web list | udiscovermusic.com/stories/50-greatest-jazz-albums-ever / jazzfuel.com/best-jazz-albums | Canon-status grounding for 4 of 5 (The Real McCoy not named in this aggregate). Consulted via web search this run. |
| S5 | Cover Art Archive | Image archive | coverartarchive.org/release-group/{MBID}/front | Front-cover reference URLs derived from S3 MBIDs; existence not individually verified (epistemic inf). |

Note: AllMusic album pages were targeted for star-rating grounding but returned HTTP 403 to automated fetch this run; not cited. Penguin Guide not directly consulted this run — not cited.

---

## 2. Candidate Records

```json
{
  "id": "miles-davis-kind-of-blue-1959",
  "artist": "Miles Davis",
  "album": "Kind of Blue",
  "year": 1959,
  "label": "Columbia",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S4]: cited as the head of virtually any greatest-jazz-albums list and the best-selling jazz album in history. obs[S1]: the foundational modal-jazz statement, two-session 1959 Columbia recording. inf: anchor album of the modal genre per project genre-definitions; non-negotiable canon.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-03-02", "1959-04-22"],
    "multi_session": true,
    "studio": "Columbia 30th Street Studio, New York",
    "producer": "Irving Townsend",
    "engineer": "Fred Plaut",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Cannonball Adderley", "instrument": "alto saxophone", "scope": "selected-tracks",
        "tracks": ["So What", "Freddie Freeloader", "All Blues", "Flamenco Sketches"],
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"],
        "name_variants": ["Julian \"Cannonball\" Adderley"], "notes": "Absent on \"Blue in Green\"." },
      { "name": "Bill Evans", "instrument": "piano", "scope": "selected-tracks",
        "tracks": ["So What", "Blue in Green", "All Blues", "Flamenco Sketches"],
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Piano on all tracks except \"Freddie Freeloader\"." },
      { "name": "Wynton Kelly", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Freddie Freeloader"],
        "session_dates": ["1959-03-02"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Piano on \"Freddie Freeloader\" only." },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Cobb", "instrument": "drums", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1959-03-02", "1959-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "So What", "track_number": 1, "side": "A", "duration": "9:22", "session_date": "1959-03-02",
        "composers": ["Miles Davis"],
        "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Freddie Freeloader", "track_number": 2, "side": "A", "duration": "9:46", "session_date": "1959-03-02",
        "composers": ["Miles Davis"],
        "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Blue in Green", "track_number": 3, "side": "A", "duration": "5:27", "session_date": "1959-03-02",
        "composers": ["Miles Davis", "Bill Evans"],
        "personnel": ["Miles Davis", "John Coltrane", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "All Blues", "track_number": 4, "side": "B", "duration": "11:33", "session_date": "1959-04-22",
        "composers": ["Miles Davis"],
        "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Flamenco Sketches", "track_number": 5, "side": "B", "duration": "9:26", "session_date": "1959-04-22",
        "composers": ["Miles Davis", "Bill Evans"],
        "personnel": ["Miles Davis", "John Coltrane", "Cannonball Adderley", "Bill Evans", "Paul Chambers", "Jimmy Cobb"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "8e8a594f-2175-38c7-a871-abb68ec363e7",
    "apple_album_id": "268443092",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive",
        "url": "https://coverartarchive.org/release-group/8e8a594f-2175-38c7-a871-abb68ec363e7/front",
        "is_original_cover": true, "epistemic": "inf", "notes": "URL derived from S3 MBID; image existence not individually verified." }
    ],
    "notes": "Two sessions. March 2, 1959: tracks 1-3. April 22, 1959: tracks 4-5. Fred Plaut engineered but was uncredited on the original liner notes (S1)."
  }
}
```

```json
{
  "id": "john-coltrane-a-love-supreme-1964",
  "artist": "John Coltrane",
  "album": "A Love Supreme",
  "year": 1964,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S4]: described as a high point in Coltrane's discography and a milestone in jazz history. obs[S1]: recorded December 9, 1964 by the classic quartet; explicitly in scope per genre-definitions (A Love Supreme named as firmly in). inf: peak of the classic-quartet modal tradition, pre-Ascension; non-negotiable canon.",
  "priority": "must_have",
  "overlap_risk": "spiritual-jazz framing in some sources, but structure and swing keep it in modal scope",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-12-09"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Bob Thiele",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Leader. Also chants the \"a love supreme\" vocal on \"Acknowledgement\" (vocals not a separate taxonomy entry here; noted)." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Garrison", "instrument": "double bass", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Also plays gong and timpani (not in taxonomy)." },
      { "name": "Archie Shepp", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": null,
        "session_dates": ["1964-12-10"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Sextet alternate takes recorded Dec 10, 1964; appear on deluxe/expanded reissues only, not the original LP." },
      { "name": "Art Davis", "instrument": "double bass", "scope": "selected-tracks", "tracks": null,
        "session_dates": ["1964-12-10"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Second bassist on Dec 10, 1964 alternate session; reissue-only." }
    ],
    "tracks": [
      { "title": "Part 1: Acknowledgement", "track_number": 1, "side": "A", "duration": "7:47", "session_date": "1964-12-09",
        "composers": ["John Coltrane"],
        "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part 2: Resolution", "track_number": 2, "side": "A", "duration": "7:22", "session_date": "1964-12-09",
        "composers": ["John Coltrane"],
        "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part 3: Pursuance", "track_number": 3, "side": "B", "duration": null, "session_date": "1964-12-09",
        "composers": ["John Coltrane"],
        "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part 4: Psalm", "track_number": 4, "side": "B", "duration": null, "session_date": "1964-12-09",
        "composers": ["John Coltrane"],
        "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "77cf47ba-58cd-3f3d-a5f9-79bf89860421",
    "apple_album_id": "1440713018",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive",
        "url": "https://coverartarchive.org/release-group/77cf47ba-58cd-3f3d-a5f9-79bf89860421/front",
        "is_original_cover": true, "epistemic": "inf", "notes": "URL derived from S3 MBID; image existence not individually verified." }
    ],
    "notes": "Single session Dec 9, 1964. Side two (Parts 3-4) is presented as a continuous 17:53 on the original LP per S1; individual Pursuance/Psalm durations not given by source, recorded as null. Archie Shepp / Art Davis sextet alternates from Dec 10 appear on deluxe reissues only."
  }
}
```

```json
{
  "id": "mccoy-tyner-the-real-mccoy-1967",
  "artist": "McCoy Tyner",
  "album": "The Real McCoy",
  "year": 1967,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S3", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S1]: Tyner's first Blue Note leader date post-Coltrane, recorded April 21, 1967 with Joe Henderson, Ron Carter, Elvin Jones; all-original modal program. inf: the project's namesake artist and a landmark of post-quartet modal jazz; widely treated as essential McCoy Tyner (not surfaced in the S4 aggregate, so canon status held at inf rather than obs).",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1967-04-21"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1967-04-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all five tracks." },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1967-04-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1967-04-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1967-04-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Passion Dance", "track_number": 1, "side": null, "duration": "8:47", "session_date": "1967-04-21",
        "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Joe Henderson", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Contemplation", "track_number": 2, "side": null, "duration": "9:12", "session_date": "1967-04-21",
        "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Joe Henderson", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Four by Five", "track_number": 3, "side": null, "duration": "6:37", "session_date": "1967-04-21",
        "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Joe Henderson", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Search for Peace", "track_number": 4, "side": null, "duration": "6:32", "session_date": "1967-04-21",
        "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Joe Henderson", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Blues on the Corner", "track_number": 5, "side": null, "duration": "5:58", "session_date": "1967-04-21",
        "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Joe Henderson", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "637892d3-1941-3905-9795-76564a7e4413",
    "apple_album_id": "721273864",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive",
        "url": "https://coverartarchive.org/release-group/637892d3-1941-3905-9795-76564a7e4413/front",
        "is_original_cover": true, "epistemic": "inf", "notes": "URL derived from S3 MBID; image existence not individually verified." }
    ],
    "notes": "Single session April 21, 1967 (Blue Note BST 84264). Engineer not stated by S1; recorded at Van Gelder Studio for Blue Note in 1967 -> Rudy Van Gelder inferred per personnel-contract Van Gelder rule (epistemic inf). Original-LP side split not stated by source; track sides recorded as null."
  }
}
```

```json
{
  "id": "herbie-hancock-maiden-voyage-1965",
  "artist": "Herbie Hancock",
  "album": "Maiden Voyage",
  "year": 1965,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S4]: placed alongside Kind of Blue as a highlight of modal-jazz exploration, departing from Hancock's earlier hard bop. obs[S1]: recorded March 17, 1965 with Hubbard, Coleman, Carter, Williams; all-Hancock oceanic concept program. inf: bridges modal and post-bop; firmly in scope.",
  "priority": "strong",
  "overlap_risk": "post-bop / modal border — second-quintet rhythm section (Carter, Williams) pulls post-bop",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1965-03-17"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1965-03-17"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all five tracks." },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1965-03-17"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "George Coleman", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1965-03-17"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1965-03-17"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1965-03-17"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Maiden Voyage", "track_number": 1, "side": null, "duration": "7:57", "session_date": "1965-03-17",
        "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "George Coleman", "Ron Carter", "Tony Williams"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Eye of the Hurricane", "track_number": 2, "side": null, "duration": "6:01", "session_date": "1965-03-17",
        "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "George Coleman", "Ron Carter", "Tony Williams"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Little One", "track_number": 3, "side": null, "duration": "8:47", "session_date": "1965-03-17",
        "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "George Coleman", "Ron Carter", "Tony Williams"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Survival of the Fittest", "track_number": 4, "side": null, "duration": "10:03", "session_date": "1965-03-17",
        "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "George Coleman", "Ron Carter", "Tony Williams"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Dolphin Dance", "track_number": 5, "side": null, "duration": "9:16", "session_date": "1965-03-17",
        "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "George Coleman", "Ron Carter", "Tony Williams"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "c5e5e8ad-dc89-319e-8b2d-b3ff5e59fcea",
    "apple_album_id": "1476739989",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive",
        "url": "https://coverartarchive.org/release-group/c5e5e8ad-dc89-319e-8b2d-b3ff5e59fcea/front",
        "is_original_cover": true, "epistemic": "inf", "notes": "URL derived from S3 MBID; image existence not individually verified." }
    ],
    "notes": "Single session March 17, 1965 (Blue Note BLP 4195 / BST 84195). Engineer not stated by S1; Van Gelder Studio / Blue Note / 1965 -> Rudy Van Gelder inferred per contract (epistemic inf). Original-LP side split not stated by source; track sides recorded as null."
  }
}
```

```json
{
  "id": "wayne-shorter-speak-no-evil-1964",
  "artist": "Wayne Shorter",
  "album": "Speak No Evil",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S4]: regarded as one of Shorter's most important works and a quintessential Blue Note album blending hard bop, post-bop, and modal jazz. obs[S1]: recorded Dec 24, 1964, released 1966; quintet with Hubbard, Hancock, Carter, Jones. inf: synthesis-zone post-bop per genre-definitions; flagged post-bop for synthesis tracking.",
  "priority": "strong",
  "overlap_risk": "hard-bop border — sources note hard bop elements alongside post-bop/modal",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-12-24"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-24"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all six tracks." },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "selected-tracks",
        "tracks": ["Witch Hunt", "Fee-Fi-Fo-Fum", "Dance Cadaverous", "Speak No Evil", "Wild Flower"],
        "session_dates": ["1964-12-24"], "epistemic": "obs", "sources": ["S1"], "name_variants": [],
        "notes": "Absent on \"Infant Eyes\"." },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-24"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-24"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null,
        "session_dates": ["1964-12-24"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Witch Hunt", "track_number": 1, "side": "A", "duration": "8:11", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Fee-Fi-Fo-Fum", "track_number": 2, "side": "A", "duration": "5:54", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Dance Cadaverous", "track_number": 3, "side": "A", "duration": "6:45", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Speak No Evil", "track_number": 4, "side": "B", "duration": "8:23", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Infant Eyes", "track_number": 5, "side": "B", "duration": "6:54", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Wild Flower", "track_number": 6, "side": "B", "duration": "6:06", "session_date": "1964-12-24",
        "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Freddie Hubbard", "Herbie Hancock", "Ron Carter", "Elvin Jones"],
        "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "eae0c18f-f2fd-3b97-8631-3f682a2f3957",
    "apple_album_id": "723473694",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive",
        "url": "https://coverartarchive.org/release-group/eae0c18f-f2fd-3b97-8631-3f682a2f3957/front",
        "is_original_cover": true, "epistemic": "inf", "notes": "URL derived from S3 MBID; image existence not individually verified." }
    ],
    "notes": "Recorded Dec 24, 1964 (Blue Note); released June 1966. id/year uses recording year 1964 per contract. Engineer not stated by S1; Van Gelder Studio / Blue Note -> Rudy Van Gelder inferred per contract (epistemic inf). apple_album_id is the Rudy Van Gelder Edition (collectionId 723473694, 1966-06-01); a 2013 reissue (1453750007) also exists. MusicBrainz first-release-date returned 1965 in S3 for the release group; S1 gives June 1966 for the LP release."
  }
}
```

---

## 3. Synthesis Notes

**Must-Haves (top picks):**
- *Kind of Blue* (Miles Davis, 1959) — the genre's anchor album and the most-cited jazz record in existence; no modal canon is coherent without it.
- *A Love Supreme* (John Coltrane, 1964) — the apex of the classic-quartet modal tradition, explicitly named in-scope by the project's own genre definitions.
- *The Real McCoy* (McCoy Tyner, 1967) — the project namesake's defining post-Coltrane modal statement; the album the whole canon is informally built around.

**Hidden Gems (under-cited but strong):**
- None this run by design — all five are heavily-cited apex titles, fitting an empty-ledger "next-best" pass that should grab the obvious foundations first. Genuine deep cuts (e.g., Tyner's *Sahara*, Henderson's *Inner Urge*) belong in later runs once the ledger fills.

**Consensus Picks (3+ sources):**
- All five carry S1+S2+S3 (and S5); four of five (*Kind of Blue*, *A Love Supreme*, *Maiden Voyage*, *Speak No Evil*) add S4 canon-list grounding. Strong multi-source agreement throughout.

**Single-Source Picks:**
- None. *The Real McCoy* is the lightest on canon-list grounding (absent from the S4 aggregate, so its canon status is held at `inf`), but its factual record is fully S1-grounded and corroborated by S2/S3/S5.

**Scope Calls (boundary judgments):**
- *Speak No Evil* flagged `style_primary: post-bop` (not modal) — sources frame it as a hard-bop/post-bop/modal synthesis; placed in the post-bop synthesis bucket for tracking.
- *Maiden Voyage* kept `modal-jazz` primary with a `post-bop` tag — modal in concept but carries the second-quintet rhythm section; noted as an overlap, not a scope risk.
- *A Love Supreme* is pre-*Ascension* (Dec 1964) and well inside the structured modal window; the 1965+ free-jazz fuzzy edge does not apply.
- No album in this run sits near the fusion or free-jazz boundary; all `scope_flag` empty.

**Gaps Noticed:**
- Late modal jazz (1970s–80s) entirely uncovered this run — McCoy Tyner's Milestone era, Keith Jarrett's ECM work, Chick Corea. The fuzzy-edge late-modal calls remain to be made in future passes.
- Bill Evans (a named key figure) not yet surfaced — *Sunday at the Village Vanguard* and the trio canon are open gaps.
- Miles Davis Second Quintet proper (*E.S.P.*, *Miles Smiles*) and Coltrane's other classic-quartet records (*Crescent*, *My Favorite Things*) not yet picked.

**Personnel Coverage:**
- Full track-level assignments (`track_assignments_complete: true`) reached on all five: *Kind of Blue* (per-track pianist/altoist splits documented by S1), *A Love Supreme*, *The Real McCoy*, *Maiden Voyage*, and *Speak No Evil* (per-track Hubbard absence on "Infant Eyes" documented).
- Thin spots: (1) *A Love Supreme* side-two durations — S1 presents Parts 3–4 as a continuous 17:53, so Pursuance/Psalm individual durations are recorded as `null` rather than guessed. (2) Original-LP side splits for *The Real McCoy* and *Maiden Voyage* were not stated by S1; track `side` set to `null` rather than inferred. (3) Engineer credit for the three Blue Note titles inferred as Rudy Van Gelder (`epistemic_production: inf`) per the contract's Van Gelder rule. (4) Cover-art URLs are derived from MusicBrainz MBIDs and marked `inf` since image existence was not individually verified this pass.
</content>
</invoke>
