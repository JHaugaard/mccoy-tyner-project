# Modal Jazz / Post-Bop — Candidate Records (Round 2)

**Specialist:** Modal Jazz & Post-Bop researcher
**Run:** Growth push toward ~100, 15 candidates · 2026-06-23
**Directive:** Gather 15 complete candidate records (merged contract — canon + full personnel/tracks/sessions) for The Jazz Canon.
**Exclusions:** `data/dispatch-ledger.json` `albums_in_collection` (15 albums) — none re-surfaced. The 5 modal/post-bop titles already collected (Kind of Blue, A Love Supreme, The Real McCoy, Maiden Voyage, Speak No Evil) are deliberately avoided.
**Calibration:** `research/cull-notes.md` — no culls recorded yet; nothing to honor beyond the standing scope rules.
**Convention this round:** `year` = RECORDING year. Where release year differs, it is stated in the record's `notes`. Session dates live in the personnel block.

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — album articles | Encyclopedia | en.wikipedia.org/wiki/{E.S.P., Miles_Smiles, Nefertiti, My_Favorite_Things, Crescent, Coltrane_(1962_album), Sunday_at_the_Village_Vanguard, JuJu, Adam's_Apple, Inner_Urge, Empyrean_Isles, Sahara, Now_He_Sings_Now_He_Sobs, The_Köln_Concert, Point_of_Departure} | Primary for personnel, sessions, studios, producers, composers, track listings. Cites liner notes. |
| S2 | iTunes Search API | API | itunes.apple.com/search | Apple `collectionId` (apple_album_id) per album. Free, no token. Queried this run. |
| S3 | MusicBrainz release-group API | API | musicbrainz.org/ws/2/release-group | TARGETED but UNREACHABLE this run — repeated TLS "certificate verification error" on every call. Release-group MBIDs left `null`; Cover Art Archive URLs (which derive from the MBID) therefore left empty. Not a data source this run. |
| S4 | Jazzwise "Modal Jazz: 10 Essential Albums" + JazzFuel "50 Best Jazz Albums" | Web list | jazzwise.com/content/features/modal-jazz-10-essential-albums · jazzfuel.com/best-jazz-albums | Modal/piano canon grounding (Köln Concert, Now He Sings, modal lineage). Web search this run. |
| S5 | uDiscover "The 50 Greatest Blue Note Albums" | Web list | udiscovermusic.com/stories/the-50-greatest-blue-note-albums | Blue Note canon grounding with explicit rankings: Point of Departure #9, Empyrean Isles #33, JuJu #35. Web search this run. |
| S6 | WBGO / JazzFuel / eJazzNews — Miles Davis Second Quintet features | Web feature | wbgo.org/2023-05-25/our-top-ten-the-essential-miles-davis-albums · jazzfuel.com/miles-davis-albums | Canon grounding for E.S.P. / Miles Smiles / Nefertiti as the Second Great Quintet pillars. Web search this run. |
| S7 | BestEverAlbums + All About Jazz — essential/ranked Coltrane lists | Web list | besteveralbums.com (Coltrane chart) · allaboutjazz.com/john-coltrane-an-alternative-top-ten-albums | Canon grounding for My Favorite Things (#4 of his catalogue), Crescent, Coltrane (1962). Web search this run. |

Notes: AllMusic album pages were targeted for star-rating grounding but, as in the prior run, are not reliably fetchable by automated request; not cited. Penguin Guide not directly consulted this run; not cited. Track **durations** were not individually source-verified this pass — set `null` rather than estimated, per the no-fabrication guardrail. Personnel, composers, studios, producers, recording dates, and track titles/order are S1-grounded (`obs`); production-engineer credits for Blue Note/Impulse Van Gelder dates are inferred (`inf`) per the contract's Van Gelder rule.

---

## 2. Candidate Records

```json
{
  "id": "miles-davis-e-s-p-1965",
  "artist": "Miles Davis",
  "album": "E.S.P.",
  "year": 1965,
  "label": "Columbia",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: cited as the debut statement of the Second Great Quintet and a groundbreaking shift to a freer, longer-form style. obs[S1]: recorded Jan 20-22, 1965 in Hollywood by the Davis/Shorter/Hancock/Carter/Williams quintet; all-original program. inf: the canonical post-bop synthesis ensemble named in genre-definitions; firmly in scope.",
  "priority": "strong",
  "overlap_risk": "modal/post-bop border — modal heads with free-leaning interplay; stays structured and swinging",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1965-01-20", "1965-01-21", "1965-01-22"],
    "multi_session": true,
    "studio": "Columbia Studios, Hollywood, Los Angeles",
    "producer": "Irving Townsend",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Co-composer of \"Eighty-One\" and \"Mood\"." },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "E.S.P.", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Eighty-One", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Miles Davis", "Ron Carter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Little One", "track_number": 3, "side": "A", "duration": null, "session_date": null, "composers": ["Herbie Hancock", "Miles Davis"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "R.J.", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["Ron Carter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Agitation", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["Miles Davis"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Iris", "track_number": 6, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Mood", "track_number": 7, "side": "B", "duration": null, "session_date": null, "composers": ["Miles Davis", "Ron Carter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "203773370",
    "cover_art": [],
    "notes": "Released August 1965; recording year 1965 per convention. Three-day session Jan 20-22, 1965 at Columbia's Hollywood studio; per-track session-date splits not distinguished by S1, left null. apple_album_id is the 2022 Remaster (203773370), the only complete-program edition surfaced by iTunes. MBID null and cover_art empty — MusicBrainz unreachable (TLS error) this run. Durations not source-verified, left null."
  }
}
```

```json
{
  "id": "miles-davis-miles-smiles-1966",
  "artist": "Miles Davis",
  "album": "Miles Smiles",
  "year": 1966,
  "label": "Columbia",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: described as the Second Quintet 'fully arrived,' reaching a rhythmic and harmonic freedom beyond E.S.P.; 'hard to imagine a better post bop album.' obs[S1]: recorded Oct 24-25, 1966 at Columbia 30th Street Studio. inf: a pillar of the post-bop synthesis zone; among the strongest must-have candidates this run.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1966-10-24", "1966-10-25"],
    "multi_session": true,
    "studio": "Columbia 30th Street Studio, New York",
    "producer": "Teo Macero",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Orbits", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Circle", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Miles Davis"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Footprints", "track_number": 3, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Dolores", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Freedom Jazz Dance", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["Eddie Harris"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Ginger Bread Boy", "track_number": 6, "side": "B", "duration": null, "session_date": null, "composers": ["Jimmy Heath"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "209407331",
    "cover_art": [],
    "notes": "Recorded Oct 24-25, 1966; released early 1967. Recording year 1966 per convention. apple_album_id 209407331 (Miles Davis Quintet). Per-track session-date split not distinguished by S1, left null. MBID null / cover_art empty — MusicBrainz unreachable this run. Durations not source-verified."
  }
}
```

```json
{
  "id": "miles-davis-nefertiti-1967",
  "artist": "Miles Davis",
  "album": "Nefertiti",
  "year": 1967,
  "label": "Columbia",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: described as the peak of the Second Quintet's four-year run and the last all-acoustic Miles album, inverting the conventions of jazz performance. obs[S1]: recorded June-July 1967 at Columbia 30th Street Studio. inf: post-bop pillar; the title track famously rotates the melody without solos.",
  "priority": "strong",
  "overlap_risk": "edges toward free interplay but remains acoustic and structured — stays in scope",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1967-06-07", "1967-06-22", "1967-06-23", "1967-07-19"],
    "multi_session": true,
    "studio": "Columbia 30th Street Studio, New York",
    "producer": "Teo Macero",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composed four of the six tracks." },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composed \"Hand Jive\"." }
    ],
    "tracks": [
      { "title": "Nefertiti", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Fall", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Hand Jive", "track_number": 3, "side": "A", "duration": null, "session_date": null, "composers": ["Tony Williams"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Madness", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Riot", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["Herbie Hancock"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Pinocchio", "track_number": 6, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Miles Davis", "Wayne Shorter", "Herbie Hancock", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1664589722",
    "cover_art": [],
    "notes": "Recorded across several June-July 1967 sessions; released early 1968. Recording year 1967 per convention. Exact track-to-date assignment not fully distinguished by S1 — recording_dates lists the documented session dates; the July 19 date is held with the others and per-track session_date left null rather than mis-assigned. apple_album_id 1664589722 is the 2023 Remaster (6-track original program); a Bonus Track Version (169899671) also exists. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "john-coltrane-my-favorite-things-1960",
  "artist": "John Coltrane",
  "album": "My Favorite Things",
  "year": 1960,
  "label": "Atlantic",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S7"],
  "epistemic": "obs",
  "rationale": "obs[S7]: ranked 4th of Coltrane's catalogue on BestEverAlbums; first album to feature his soprano saxophone and a commercial breakthrough, described as a reflection of his journey into modal jazz. obs[S1]: recorded Oct 1960 at Atlantic Studios with the nascent classic quartet (Tyner, Davis, Jones). inf: a foundational modal-jazz statement; the soprano-led title track is a genre landmark.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-10-21", "1960-10-24", "1960-10-26"],
    "multi_session": true,
    "studio": "Atlantic Studios, New York",
    "producer": "Nesuhi Ertegun",
    "engineer": "Tom Dowd",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "soprano saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader. Plays soprano saxophone on \"My Favorite Things\" and \"Everytime We Say Goodbye\"; tenor saxophone on \"Summertime\" and \"But Not for Me\"." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Steve Davis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "My Favorite Things", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Richard Rodgers", "Oscar Hammerstein II"], "personnel": ["John Coltrane", "McCoy Tyner", "Steve Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Everytime We Say Goodbye", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Cole Porter"], "personnel": ["John Coltrane", "McCoy Tyner", "Steve Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Summertime", "track_number": 3, "side": "B", "duration": null, "session_date": null, "composers": ["George Gershwin", "Ira Gershwin", "DuBose Heyward"], "personnel": ["John Coltrane", "McCoy Tyner", "Steve Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "But Not for Me", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["George Gershwin", "Ira Gershwin"], "personnel": ["John Coltrane", "McCoy Tyner", "Steve Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "962193155",
    "cover_art": [],
    "notes": "Recorded Oct 21, 24, 26, 1960 at Atlantic Studios; released March 1961. Recording year 1960 per convention. Per-track session-date split not distinguished by S1, left null. Coltrane's soprano/tenor split is documented per track (see his personnel note). apple_album_id 962193155 (original Atlantic). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "john-coltrane-crescent-1964",
  "artist": "John Coltrane",
  "album": "Crescent",
  "year": 1964,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S7"],
  "epistemic": "obs",
  "rationale": "obs[S7]: a 1964 Impulse! studio album by the classic quartet of all-original Coltrane compositions, commonly regarded as his darkest and most introspective record; appears on essential-Coltrane lists. obs[S1]: recorded April-June 1964 at Van Gelder Studio with Tyner, Garrison, Jones. inf: the immediate predecessor to A Love Supreme and a peak of the classic quartet's modal language.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-04-27", "1964-06-01"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Bob Thiele",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all five tracks." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Garrison", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Crescent", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Wise One", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Bessie's Blues", "track_number": 3, "side": "B", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Lonnie's Lament", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Drum Thing", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440856835",
    "cover_art": [],
    "notes": "Recorded April 27 and June 1, 1964 at Van Gelder Studio; released 1964. Per-track session-date split not distinguished by S1, left null. apple_album_id 1440856835 (John Coltrane Quartet). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "john-coltrane-coltrane-1962",
  "artist": "John Coltrane",
  "album": "Coltrane",
  "year": 1962,
  "label": "Impulse!",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S7"],
  "epistemic": "obs",
  "rationale": "obs[S7]: the self-titled 1962 Impulse! album appears on All About Jazz's essential-Coltrane top ten. obs[S1]: recorded April-June 1962 at Van Gelder Studio by the classic quartet; opens with the modal tour-de-force \"Out of This World.\" inf: a strong second-tier classic-quartet record, lighter on canon-list consensus than Crescent, so held at strong/consider.",
  "priority": "consider",
  "overlap_risk": "standards-and-originals program touches hard bop, but the modal frame (Out of This World, Miles' Mode) keeps it in modal scope",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1962-04-11", "1962-06-19", "1962-06-20", "1962-06-29"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Bob Thiele",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader. Plays soprano saxophone on \"The Inch Worm\"." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Garrison", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Out of This World", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Harold Arlen", "Johnny Mercer"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Soul Eyes", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Mal Waldron"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Inch Worm", "track_number": 3, "side": "B", "duration": null, "session_date": null, "composers": ["Frank Loesser"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Tunji", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Miles' Mode", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["John Coltrane"], "personnel": ["John Coltrane", "McCoy Tyner", "Jimmy Garrison", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443143816",
    "cover_art": [],
    "notes": "Recorded across April 11 and June 19/20/29, 1962 at Van Gelder Studio; released 1962. Per-track session-date split not distinguished by S1, left null. \"Miles' Mode\" composer sometimes credited jointly with Eric Dolphy in some sources; S1 credits Coltrane — recorded as Coltrane, conflict noted. apple_album_id 1443143816 (John Coltrane Quartet, original 5-track). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "bill-evans-sunday-at-the-village-vanguard-1961",
  "artist": "Bill Evans",
  "album": "Sunday at the Village Vanguard",
  "year": 1961,
  "label": "Riverside",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S4]: Bill Evans is a named modal key figure; this live trio date is among the most celebrated piano-trio recordings, spotlighting bassist Scott LaFaro weeks before his death. obs[S1]: recorded live June 25, 1961 at the Village Vanguard with LaFaro and Paul Motian; producer Orrin Keepnews. inf: the interactive-trio approach is foundational modal/post-bop piano; fills the standing Bill Evans gap.",
  "priority": "must_have",
  "overlap_risk": "cool-jazz lineage in Evans's touch, but the conversational modal interplay places it here",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-06-25"],
    "multi_session": false,
    "studio": "Village Vanguard, New York (live)",
    "producer": "Orrin Keepnews",
    "engineer": "David B. Jones",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Bill Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "Scott LaFaro", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composed \"Gloria's Step\" and \"Jade Visions\"; died ten days after this date." },
      { "name": "Paul Motian", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Gloria's Step", "track_number": 1, "side": "A", "duration": null, "session_date": "1961-06-25", "composers": ["Scott LaFaro"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "My Man's Gone Now", "track_number": 2, "side": "A", "duration": null, "session_date": "1961-06-25", "composers": ["George Gershwin", "Ira Gershwin", "DuBose Heyward"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Solar", "track_number": 3, "side": "A", "duration": null, "session_date": "1961-06-25", "composers": ["Miles Davis"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Alice in Wonderland", "track_number": 4, "side": "B", "duration": null, "session_date": "1961-06-25", "composers": ["Sammy Fain", "Bob Hilliard"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "All of You", "track_number": 5, "side": "B", "duration": null, "session_date": "1961-06-25", "composers": ["Cole Porter"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Jade Visions", "track_number": 6, "side": "B", "duration": null, "session_date": "1961-06-25", "composers": ["Scott LaFaro"], "personnel": ["Bill Evans", "Scott LaFaro", "Paul Motian"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1713854971",
    "cover_art": [],
    "notes": "Recorded live in a single day, June 25, 1961, across five sets at the Village Vanguard; the companion LP Waltz for Debby draws from the same date. Original LP = 6 tracks; reissues add alternate takes (flagged when present, none included here). apple_album_id 1713854971 is the \"Live At The Village Vanguard / 1961\" 6-track edition matching the original program; a Keepnews Collection edition (1440926338) also exists. Engineer David B. Jones credited on the Riverside session. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified (live-set takes vary across editions)."
  }
}
```

```json
{
  "id": "wayne-shorter-juju-1964",
  "artist": "Wayne Shorter",
  "album": "JuJu",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S5]: ranked #35 on uDiscover's 50 Greatest Blue Note Albums; the rhythm section of Tyner, Workman and Elvin Jones 'glides like a smooth-revving racecar,' intensifying Shorter's modal tunes. obs[S1]: recorded Aug 3, 1964 at Van Gelder Studio with three-quarters of Coltrane's classic quartet. inf: Shorter's modal Blue Note peak alongside Speak No Evil; a strong canon candidate.",
  "priority": "strong",
  "overlap_risk": "post-bop tag — Shorter compositions, but the Coltrane-quartet rhythm section pushes it modal",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-08-03"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all tracks." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "JuJu", "track_number": 1, "side": "A", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Deluge", "track_number": 2, "side": "A", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "House of Jade", "track_number": 3, "side": "A", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Mahjong", "track_number": 4, "side": "B", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Yes or No", "track_number": 5, "side": "B", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Twelve More Bars to Go", "track_number": 6, "side": "B", "duration": null, "session_date": "1964-08-03", "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "McCoy Tyner", "Reggie Workman", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444117518",
    "cover_art": [],
    "notes": "Recorded Aug 3, 1964 at Van Gelder Studio; released 1965. Recording year 1964 per convention. Original LP = 6 tracks; the iTunes 1444117518 listing shows 7 tracks (an alternate take of \"Twelve More Bars to Go\" or \"Juju\" added on CD) — only the 6 original tracks recorded here. Engineer inferred Rudy Van Gelder per contract Van Gelder rule (epistemic inf). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "wayne-shorter-adams-apple-1966",
  "artist": "Wayne Shorter",
  "album": "Adam's Apple",
  "year": 1966,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S1]: recorded Feb 1966 at Van Gelder Studio with Hancock, Workman and Joe Chambers; contains the original studio recording of \"Footprints.\" inf[S5]: sits within the heavily-canonized mid-60s Shorter Blue Note run; lighter on explicit list placement than JuJu/Speak No Evil, so held at consider. inf: a durable post-bop quartet date and the home of a jazz standard.",
  "priority": "consider",
  "overlap_risk": "hard-bop and modal both present; the quartet's harmonic openness leans post-bop",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1966-02-03", "1966-02-24"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed five of six tracks." },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Joe Chambers", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Adam's Apple", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "502 Blues (Drinkin' and Drivin')", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Jimmy Rowles"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "El Gaucho", "track_number": 3, "side": "A", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Footprints", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Teru", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Chief Crazy Horse", "track_number": 6, "side": "B", "duration": null, "session_date": null, "composers": ["Wayne Shorter"], "personnel": ["Wayne Shorter", "Herbie Hancock", "Reggie Workman", "Joe Chambers"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443300056",
    "cover_art": [],
    "notes": "Recorded Feb 3 and Feb 24, 1966 at Van Gelder Studio; released 1967. Recording year 1966 per convention. Per-track session-date split not distinguished by S1, left null. This is the original studio \"Footprints,\" predating the Miles Smiles version. Engineer inferred Rudy Van Gelder per contract (epistemic inf). apple_album_id 1443300056 (original 1966, 6 tracks). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "joe-henderson-inner-urge-1964",
  "artist": "Joe Henderson",
  "album": "Inner Urge",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz", "post-bop"],
  "sources": ["S1", "S2", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S5]: cited among the greatest Blue Note albums; \"Isotope\" called one of the most angular blues themes in the jazz canon, and the record is a fan favorite of Henderson's catalogue. obs[S1]: recorded Nov 30, 1964 at Van Gelder Studio with McCoy Tyner, Bob Cranshaw and Elvin Jones — a pianoless-front-line modal quartet. inf: Henderson is a named modal key figure; this is his most modal leader date.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-11-30"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed four of five tracks." },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Bob Cranshaw", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Inner Urge", "track_number": 1, "side": "A", "duration": null, "session_date": "1964-11-30", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "McCoy Tyner", "Bob Cranshaw", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Isotope", "track_number": 2, "side": "A", "duration": null, "session_date": "1964-11-30", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "McCoy Tyner", "Bob Cranshaw", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "El Barrio", "track_number": 3, "side": "A", "duration": null, "session_date": "1964-11-30", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "McCoy Tyner", "Bob Cranshaw", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "You Know I Care", "track_number": 4, "side": "B", "duration": null, "session_date": "1964-11-30", "composers": ["Duke Pearson"], "personnel": ["Joe Henderson", "McCoy Tyner", "Bob Cranshaw", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Night and Day", "track_number": 5, "side": "B", "duration": null, "session_date": "1964-11-30", "composers": ["Cole Porter"], "personnel": ["Joe Henderson", "McCoy Tyner", "Bob Cranshaw", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "724519387",
    "cover_art": [],
    "notes": "Recorded Nov 30, 1964 at Van Gelder Studio; released 1966. Recording year 1964 per convention. Engineer inferred Rudy Van Gelder per contract (epistemic inf). apple_album_id 724519387 (Rudy Van Gelder Edition, 5-track original program). MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "herbie-hancock-empyrean-isles-1964",
  "artist": "Herbie Hancock",
  "album": "Empyrean Isles",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S5]: ranked #33 on uDiscover's 50 Greatest Blue Note Albums. obs[S1]: recorded June 17, 1964 at Van Gelder Studio by a pianoless-plus-cornet quartet (Hubbard on cornet, Carter, Williams); home of \"Cantaloupe Island.\" inf: the immediate predecessor to Maiden Voyage and a post-bop landmark in its own right.",
  "priority": "strong",
  "overlap_risk": "modal/post-bop border — \"Cantaloupe Island\" is modal, the rest leans freer post-bop",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-06-17"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all four tracks." },
      { "name": "Freddie Hubbard", "instrument": "cornet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Plays cornet on this date rather than his usual trumpet." },
      { "name": "Ron Carter", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "One Finger Snap", "track_number": 1, "side": "A", "duration": null, "session_date": "1964-06-17", "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Oliloqui Valley", "track_number": 2, "side": "A", "duration": null, "session_date": "1964-06-17", "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Cantaloupe Island", "track_number": 3, "side": "B", "duration": null, "session_date": "1964-06-17", "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Egg", "track_number": 4, "side": "B", "duration": null, "session_date": "1964-06-17", "composers": ["Herbie Hancock"], "personnel": ["Herbie Hancock", "Freddie Hubbard", "Ron Carter", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443829596",
    "cover_art": [],
    "notes": "Recorded June 17, 1964 at Van Gelder Studio; released November 1964. Engineer inferred Rudy Van Gelder per contract (epistemic inf). apple_album_id 1443829596 (original 4-track); an Expanded Edition (724298445) adds alternates. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "mccoy-tyner-sahara-1972",
  "artist": "McCoy Tyner",
  "album": "Sahara",
  "year": 1972,
  "label": "Milestone",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S1]: recorded January 1972 for Milestone with Sonny Fortune, Calvin Hill and Alphonse Mouzon; a Grammy-nominated landmark of Tyner's post-Blue-Note period, with Tyner adding koto, flute and percussion. inf[S4]: continuous with the 1960s modal tradition (the genre-definitions fuzzy-edge late-modal allowance) and the project namesake's defining 1970s statement. inf: pre-fusion, acoustic, modal in spirit.",
  "priority": "consider",
  "overlap_risk": "1970s date — verify against fusion proximity; instrumentation is acoustic and modal, not electric",
  "scope_flag": "1972 — late-modal fuzzy edge; kept as continuous with the 1960s modal tradition per genre-definitions",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1972-01-15"],
    "multi_session": false,
    "studio": null,
    "producer": "Orrin Keepnews",
    "engineer": null,
    "epistemic_production": "inf",
    "personnel": [
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all tracks. Also plays koto (not in taxonomy), flute and percussion on \"Valley of Life\" and elsewhere." },
      { "name": "Sonny Fortune", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Doubles soprano saxophone and flute." },
      { "name": "Calvin Hill", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Also plays percussion and reed flute." },
      { "name": "Alphonse Mouzon", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Also plays trumpet and percussion on the date." }
    ],
    "tracks": [
      { "title": "Ebony Queen", "track_number": 1, "side": "A", "duration": null, "session_date": "1972-01-15", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Sonny Fortune", "Calvin Hill", "Alphonse Mouzon"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "A Prayer for My Family", "track_number": 2, "side": "A", "duration": null, "session_date": "1972-01-15", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Valley of Life", "track_number": 3, "side": "A", "duration": null, "session_date": "1972-01-15", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Sonny Fortune", "Calvin Hill"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Rebirth", "track_number": 4, "side": "A", "duration": null, "session_date": "1972-01-15", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Sonny Fortune", "Calvin Hill", "Alphonse Mouzon"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Sahara", "track_number": 5, "side": "B", "duration": null, "session_date": "1972-01-15", "composers": ["McCoy Tyner"], "personnel": ["McCoy Tyner", "Sonny Fortune", "Calvin Hill", "Alphonse Mouzon"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1442370232",
    "cover_art": [],
    "notes": "Recorded January 1972 for Milestone (M-9039); released 1972. Exact session day not confirmed by S1 — recording_dates carries a placeholder mid-January date and should be tightened against Tom Lord. Studio location not stated by S1 (Milestone NYC sessions of the era), left null. \"A Prayer for My Family\" is a solo-piano interlude and \"Valley of Life\" omits drums (Tyner koto / Fortune flute / Hill) — per-track personnel reflect S1 where stated; track_assignments_complete left false because instrument doublings per track are not exhaustively source-confirmed. The title track \"Sahara\" fills LP side B. apple_album_id 1442370232. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "chick-corea-now-he-sings-now-he-sobs-1968",
  "artist": "Chick Corea",
  "album": "Now He Sings, Now He Sobs",
  "year": 1968,
  "label": "Solid State",
  "style_primary": "post-bop",
  "style_tags": ["post-bop", "modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S4]: described as the acoustic trio record that established Corea's voice before fusion arrived, in the classic piano-trio lineup with Miroslav Vitouš and Roy Haynes. obs[S1]: recorded March 1968 at A&R Studios, NYC, for Solid State. inf: a pillar of late-60s post-bop piano-trio playing, pre-fusion and firmly in scope; \"Matrix\" became a standard.",
  "priority": "strong",
  "overlap_risk": "Corea's later fusion looms, but this date is wholly acoustic and structured — clearly pre-fusion",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1968-03-14", "1968-03-19", "1968-03-27"],
    "multi_session": true,
    "studio": "A&R Studios, New York",
    "producer": "Sonny Lester",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Chick Corea", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all tracks." },
      { "name": "Miroslav Vitouš", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": ["Miroslav Vitous"], "notes": "" },
      { "name": "Roy Haynes", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Steps - What Was", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Chick Corea"], "personnel": ["Chick Corea", "Miroslav Vitouš", "Roy Haynes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Matrix", "track_number": 2, "side": "A", "duration": null, "session_date": null, "composers": ["Chick Corea"], "personnel": ["Chick Corea", "Miroslav Vitouš", "Roy Haynes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Now He Sings, Now He Sobs", "track_number": 3, "side": "B", "duration": null, "session_date": null, "composers": ["Chick Corea"], "personnel": ["Chick Corea", "Miroslav Vitouš", "Roy Haynes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Now He Beats the Drum, Now He Stops", "track_number": 4, "side": "B", "duration": null, "session_date": null, "composers": ["Chick Corea"], "personnel": ["Chick Corea", "Miroslav Vitouš", "Roy Haynes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Law of Falling and Catching Up", "track_number": 5, "side": "B", "duration": null, "session_date": null, "composers": ["Chick Corea"], "personnel": ["Chick Corea", "Miroslav Vitouš", "Roy Haynes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1458144305",
    "cover_art": [],
    "notes": "Recorded March 1968 at A&R Studios, NYC; released 1968 on Solid State (later widely reissued on Blue Note, which is why iTunes tags it Blue Note). Multiple March 1968 session dates documented; exact track-to-date split not distinguished by S1, per-track session_date left null. apple_album_id 1458144305 is the 5-track original program; an expanded 13-track edition (724790507) adds alternate takes. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "keith-jarrett-the-koln-concert-1975",
  "artist": "Keith Jarrett",
  "album": "The Köln Concert",
  "year": 1975,
  "label": "ECM",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S4]: the best-selling solo piano album in history, a fully improvised concert; named on Jazzwise modal/essential lists and explicitly cited in genre-definitions as an eligible late-modal title. obs[S1]: recorded live Jan 24, 1975 at the Cologne Opera House for ECM, produced by Manfred Eicher. inf: continuous with the modal tradition of sustained vamps and pedal-point improvisation; firmly eligible per the fuzzy-edge rule.",
  "priority": "must_have",
  "overlap_risk": "solo-piano improvisation with gospel/folk inflections; the static-vamp modal core keeps it in scope",
  "scope_flag": "1975 — late-modal fuzzy edge; explicitly named eligible in genre-definitions",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1975-01-24"],
    "multi_session": false,
    "studio": "Opera House (Opernhaus), Cologne, Germany (live)",
    "producer": "Manfred Eicher",
    "engineer": "Martin Wieland",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Keith Jarrett", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Solo, fully improvised performance." }
    ],
    "tracks": [
      { "title": "Part I", "track_number": 1, "side": "A", "duration": null, "session_date": "1975-01-24", "composers": ["Keith Jarrett"], "personnel": ["Keith Jarrett"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part II a", "track_number": 2, "side": "B", "duration": null, "session_date": "1975-01-24", "composers": ["Keith Jarrett"], "personnel": ["Keith Jarrett"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part II b", "track_number": 3, "side": "C", "duration": null, "session_date": "1975-01-24", "composers": ["Keith Jarrett"], "personnel": ["Keith Jarrett"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Part II c", "track_number": 4, "side": "D", "duration": null, "session_date": "1975-01-24", "composers": ["Keith Jarrett"], "personnel": ["Keith Jarrett"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440840566",
    "cover_art": [],
    "notes": "Recorded live Jan 24, 1975 at the Cologne Opera House; released late 1975 as a double LP on ECM. Wholly improvised — \"composers\" credited to Jarrett as the improviser. Original 2-LP sides: Part I (A), Part IIa (B), Part IIb (C), Part IIc (D); \"Part II c\" is sometimes split into IIc and an encore on later editions. apple_album_id 1440840566. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

```json
{
  "id": "andrew-hill-point-of-departure-1964",
  "artist": "Andrew Hill",
  "album": "Point of Departure",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "post-bop",
  "style_tags": ["post-bop"],
  "sources": ["S1", "S2", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S5]: ranked #9 on uDiscover's 50 Greatest Blue Note Albums; Hill described as a boundary-pusher expanding the harmonic limits of hard bop from within. obs[S1]: recorded March 21, 1964 at Van Gelder Studio with Dorham, Dolphy, Henderson, Richard Davis and Tony Williams. inf: a recognized post-bop masterpiece sitting at the structured edge of the avant-garde — surfaced as a boundary call for John.",
  "priority": "consider",
  "overlap_risk": "avant-garde proximity — Dolphy-driven and harmonically open; still composed and swinging, not free jazz",
  "scope_flag": "avant-garde-leaning post-bop — verify it reads as 'swings with structure' rather than dissolving; kept in per the post-bop controlled-experimentation allowance",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1964-03-21"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Andrew Hill", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader; composed all five tracks." },
      { "name": "Kenny Dorham", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Eric Dolphy", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Doubles flute and bass clarinet across the date." },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Richard Davis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Refuge", "track_number": 1, "side": "A", "duration": null, "session_date": "1964-03-21", "composers": ["Andrew Hill"], "personnel": ["Andrew Hill", "Kenny Dorham", "Eric Dolphy", "Joe Henderson", "Richard Davis", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "New Monastery", "track_number": 2, "side": "A", "duration": null, "session_date": "1964-03-21", "composers": ["Andrew Hill"], "personnel": ["Andrew Hill", "Kenny Dorham", "Eric Dolphy", "Joe Henderson", "Richard Davis", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Spectrum", "track_number": 3, "side": "A", "duration": null, "session_date": "1964-03-21", "composers": ["Andrew Hill"], "personnel": ["Andrew Hill", "Kenny Dorham", "Eric Dolphy", "Joe Henderson", "Richard Davis", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Flight 19", "track_number": 4, "side": "B", "duration": null, "session_date": "1964-03-21", "composers": ["Andrew Hill"], "personnel": ["Andrew Hill", "Kenny Dorham", "Eric Dolphy", "Joe Henderson", "Richard Davis", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Dedication", "track_number": 5, "side": "B", "duration": null, "session_date": "1964-03-21", "composers": ["Andrew Hill"], "personnel": ["Andrew Hill", "Kenny Dorham", "Eric Dolphy", "Joe Henderson", "Richard Davis", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444096239",
    "cover_art": [],
    "notes": "Recorded March 21, 1964 at Van Gelder Studio; released 1965. Recording year 1964 per convention. Dolphy's per-track instrument (alto sax / flute / bass clarinet) varies but is not broken out per track by S1 — primary alto saxophone with doubling noted. Engineer inferred Rudy Van Gelder per contract (epistemic inf). apple_album_id 1444096239 (original 5-track); RVG Edition (723474259) adds alternates. MBID null / cover_art empty — MusicBrainz unreachable. Durations not source-verified."
  }
}
```

---

## 3. Synthesis Notes

**Must-Haves (top picks):**
- *Miles Smiles* (Miles Davis, 1966) — the Second Great Quintet "fully arrived"; the strongest single post-bop synthesis statement available after the titles already collected.
- *My Favorite Things* (John Coltrane, 1960) — the soprano-led modal breakthrough and a named-key-figure cornerstone; closes a glaring early-classic-quartet gap.
- *Sunday at the Village Vanguard* (Bill Evans, 1961) — fills the standing Bill Evans gap with the most celebrated modal piano-trio date; spotlights Scott LaFaro days before his death.
- *The Köln Concert* (Keith Jarrett, 1975) — the best-selling solo piano record in history and the genre-definitions' own named late-modal exemplar; anchors the 1970s tail.

**Hidden Gems (under-cited but strong):**
- *Coltrane* (1962) — overshadowed by Crescent and A Love Supreme but a complete classic-quartet statement ("Out of This World," "Miles' Mode"); thinner list consensus, held at consider.
- *Adam's Apple* (Wayne Shorter, 1966) — frequently passed over for JuJu/Speak No Evil, yet it houses the original studio "Footprints"; a durable post-bop quartet date.
- *Inner Urge* (Joe Henderson, 1964) — Henderson's most modal leader date with the Tyner/Jones engine; under-listed relative to its quality.

**Consensus Picks (3+ sources):**
- Every record carries S1 (Wikipedia personnel/session) + S2 (iTunes ID) + one canon-list source (S4/S5/S6/S7). The Blue Note trio (JuJu #35, Empyrean Isles #33, Point of Departure #9) carry explicit uDiscover rankings; the three Miles titles carry concordant second-quintet feature coverage; the Coltrane titles carry ranked-list placement.

**Single-Source Picks:**
- None on the factual record — all personnel blocks are S1-grounded. *Sahara* is the lightest on canon-list grounding (named-figure/late-modal inference rather than an explicit ranked list), so its canon status is held at `inf` / consider.

**Scope Calls (boundary judgments):**
- *Point of Departure* — kept, flagged: Dolphy-driven and harmonically open, it leans avant-garde but remains composed and swinging; surfaced explicitly so John can rule on the "structure vs. dissolution" line.
- *Sahara* (1972) and *The Köln Concert* (1975) — both kept under the late-modal fuzzy-edge allowance; acoustic, pre-fusion, continuous with the 1960s modal language. Flagged by year, not down-ranked for it.
- *Nefertiti* — free-leaning interplay noted but acoustic and structured; left in scope with no flag.
- *E.S.P. / Miles Smiles / Nefertiti / Empyrean Isles / Adam's Apple* tagged `post-bop` primary for synthesis tracking; *My Favorite Things / Crescent / Coltrane / JuJu / Inner Urge / Sahara / Köln* sit `modal-jazz` primary.

**Gaps Noticed:**
- Still no *Out to Lunch* (Dolphy), *Speak Like a Child*, or *The All Seeing Eye* — the freer Blue Note post-bop wing remains a deliberate boundary question for later passes.
- McCoy Tyner's deeper Milestone run (*Enlightenment*, *Echoes of a Friend*, *Atlantis*) and his Blue Note *Tender Moments* are untouched — room for one or two more namesake records.
- ECM beyond Köln (Jarrett's *Belonging*, Garbarek) and Chick Corea beyond this trio are unexplored.
- No Coltrane *Live at the Village Vanguard* (1961) or *Ballads* yet; no Bill Evans studio trio (*Portrait in Jazz*, *Explorations*).

**Personnel Coverage:**
- Full track-level assignments (`track_assignments_complete: true`) reached on 14 of 15 — all are fixed-lineup quartets/quintets/trios (or solo) where every musician plays every track, confirmed by S1. *Sahara* is the lone `false`: its per-track instrument doublings (Tyner koto/flute, the solo "A Prayer for My Family," the drummerless "Valley of Life") are partially but not exhaustively source-confirmed, so it is held open.
- Thin spots, deliberately left as explicit nulls rather than guessed: (1) **Track durations** across all 15 — not individually source-verified this pass; the downstream ingest can pull these from Discogs/Apple. (2) **Per-track session dates** for the multi-session studio dates (E.S.P., Miles Smiles, Nefertiti, My Favorite Things, Crescent, Coltrane 1962, Adam's Apple, Now He Sings) — the date *sets* are documented but track-to-date splits were not, so per-track `session_date` is null. (3) **Engineer** inferred as Rudy Van Gelder (`inf`) for the five Blue Note dates per the contract rule; left null for the Columbia/Milestone dates where no engineer is documented. (4) **Sahara** studio location and exact session day unconfirmed (null / placeholder) — flagged for a Tom Lord tightening pass.
- **Reference IDs:** Apple `collectionId` captured for all 15 via the iTunes API (S2), with edition noted where the original program required disambiguation (remasters, RVG editions, expanded editions). **MusicBrainz release-group MBIDs and Cover Art Archive URLs are null across all 15** — the MusicBrainz API returned a TLS certificate-verification error on every attempt this run; these were deliberately not fabricated and remain a clean follow-up task once the endpoint is reachable.
</content>
</invoke>
