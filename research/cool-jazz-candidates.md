# Cool Jazz / West Coast Jazz — Candidate Records

POC run, 5 candidates. Specialist: Cool Jazz / West Coast slice. Selection (Phase 1) then full personnel pass (Phase 2) per `docs/personnel-contract.md`. Ledger empty (nothing excluded); cull-notes empty (no prior verdicts to calibrate against). `include` is `null` on every record — John decides at the gate.

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — *Birth of the Cool* | Encyclopedia | https://en.wikipedia.org/wiki/Birth_of_the_Cool | Per-session lineups, dates, studio, composers |
| S2 | Wikipedia — *Time Out* (album) | Encyclopedia | https://en.wikipedia.org/wiki/Time_Out_(album) | Personnel, dates, production, track durations |
| S3 | Wikipedia — *Chet Baker Sings* | Encyclopedia | https://en.wikipedia.org/wiki/Chet_Baker_Sings | Session personnel (incl. conflicts), tracks, production |
| S4 | Wikipedia — *Art Pepper Meets the Rhythm Section* | Encyclopedia | https://en.wikipedia.org/wiki/Art_Pepper_Meets_the_Rhythm_Section | Personnel, date, studio, composers |
| S5 | It's A Raggy Waltz — "Gerry Mulligan Quartet (Pacific Jazz PJLP-1)" | Blog (collector) | https://raggywaltz.com/2017/12/11/gerry-mulligan-quartet-gerry-mulligan-pacific-jazz-pjlp-1/ | PJLP-1 partial tracklist, personnel, Oct 1952 dates |
| S6 | Wikipedia — "Cool jazz" | Encyclopedia | https://en.wikipedia.org/wiki/Cool_jazz | Canon overview; names key albums/figures |
| S7 | iTunes Search API (Apple Music) | API | https://itunes.apple.com/search | Apple Music `collectionId` lookups |
| S8 | Library of Congress, Gerry Mulligan Collection + Stuart Nicholson essay | Archive / essay | https://www.loc.gov/collections/gerry-mulligan/ ; https://stuartnicholson.uk/ | 1952–53 pianoless-quartet history, personnel rotation |

---

## 2. Candidate Records

```json
{
  "id": "miles-davis-birth-of-the-cool-1950",
  "artist": "Miles Davis",
  "album": "Birth of the Cool",
  "year": 1950,
  "label": "Capitol",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S1", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: Wikipedia's Cool jazz article names this the landmark recording of the style, compiled from the 1949-50 nonet sessions. obs[S1]: documented across three dated sessions with Mulligan, Konitz, and Gil Evans arrangements. inf: the founding document of cool jazz and the project's named anchor album per docs/genre-definitions.md.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1949-01-21", "1949-04-22", "1950-03-09"],
    "multi_session": true,
    "studio": "WOR Studios, New York City",
    "producer": "Pete Rugolo",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-21", "1949-04-22", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Bandleader." },
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-21", "1949-04-22", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Gerry Mulligan", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-21", "1949-04-22", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Also arranger on several tracks." },
      { "name": "Bill Barber", "instrument": "tuba", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-21", "1949-04-22", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Instrument 'tuba' is outside the contract taxonomy; recorded as the most specific term per source." },
      { "name": "Kai Winding", "instrument": "trombone", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-01-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Jan 21 1949 session only." },
      { "name": "Junior Collins", "instrument": "French horn", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-01-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Al Haig", "instrument": "piano", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-01-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Joe Shulman", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-01-21"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Max Roach", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-01-21", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Jan 21 1949 and Mar 9 1950 sessions." },
      { "name": "J.J. Johnson", "instrument": "trombone", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-04-22", "1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": ["J. J. Johnson"], "notes": "" },
      { "name": "Sandy Siegelstein", "instrument": "French horn", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "John Lewis", "instrument": "piano", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Also arranger on 'Move', 'Budo', 'Rouge'. Some discographies also place Lewis on the Mar 9 1950 session; cited source (S1) does not list a pianist for that date." },
      { "name": "Nelson Boyd", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Kenny Clarke", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1949-04-22"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Gunther Schuller", "instrument": "French horn", "scope": "selected-tracks", "tracks": null, "session_dates": ["1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Al McKibbon", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Kenny Hagood", "instrument": "vocals", "scope": "selected-tracks", "tracks": ["Darn That Dream"], "session_dates": ["1950-03-09"], "epistemic": "obs", "sources": ["S1"], "name_variants": ["Kenny Haygood"], "notes": "Vocal on 'Darn That Dream' (added to 1972 reissues)." }
    ],
    "tracks": [
      { "title": "Move", "track_number": 1, "side": "A", "duration": null, "session_date": "1949-01-21", "composers": ["Denzil Best"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Jeru", "track_number": 2, "side": "A", "duration": null, "session_date": "1949-01-21", "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Moon Dreams", "track_number": 3, "side": "A", "duration": null, "session_date": null, "composers": ["Chummy MacGregor", "Johnny Mercer"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Venus de Milo", "track_number": 4, "side": "A", "duration": null, "session_date": "1949-04-22", "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Budo", "track_number": 5, "side": "A", "duration": null, "session_date": "1949-01-21", "composers": ["Miles Davis", "Bud Powell"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Deception", "track_number": 6, "side": "A", "duration": null, "session_date": "1950-03-09", "composers": ["George Shearing", "Miles Davis"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Godchild", "track_number": 7, "side": "B", "duration": null, "session_date": "1949-01-21", "composers": ["George Wallington"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Boplicity", "track_number": 8, "side": "B", "duration": null, "session_date": "1949-04-22", "composers": ["Miles Davis", "Gil Evans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Rocker", "track_number": 9, "side": "B", "duration": null, "session_date": "1950-03-09", "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Israel", "track_number": 10, "side": "B", "duration": null, "session_date": "1949-04-22", "composers": ["John Carisi"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Rouge", "track_number": 11, "side": "B", "duration": null, "session_date": "1949-04-22", "composers": ["John Lewis"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Darn That Dream", "track_number": 12, "side": "B", "duration": null, "session_date": "1950-03-09", "composers": ["Eddie DeLange", "Jimmy Van Heusen"], "personnel": ["Kenny Hagood"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440951879",
    "cover_art": [],
    "notes": "Compiled in 1957 (Capitol T-762) from three nonet sessions: 1949-01-21, 1949-04-22, 1950-03-09. 'Boplicity' originally credited to the pseudonym 'Cleo Henry' (Davis/Evans). 'Darn That Dream' added to 1972 reissues. Gil Evans arranged 'Moon Dreams' and 'Boplicity'. Per-track session dates beyond the documented session lineups are reconstructed from standard discography; treat exact track-to-session mapping as best-available, not fully source-confirmed. 'tuba' falls outside the contract taxonomy."
  }
}
```

```json
{
  "id": "dave-brubeck-quartet-time-out-1959",
  "artist": "The Dave Brubeck Quartet",
  "album": "Time Out",
  "year": 1959,
  "label": "Columbia",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S2", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: Wikipedia's Cool jazz article names Time Out (1959) among the style's landmark recordings (reached No. 2 on the Billboard pop chart). obs[S2]: classic Brubeck/Desmond quartet album built on unconventional time signatures (5/4, 9/8). inf: a cornerstone cool-jazz record despite its 1959 date.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "Recorded 1959, just past the ~1949-1958 cool-jazz window in docs/genre-definitions.md; its arranged, classically-informed character is squarely cool/third-stream, so kept in scope. Flagged for John's review.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-06-25", "1959-07-01", "1959-08-18"],
    "multi_session": true,
    "studio": "Columbia 30th Street Studio, New York City",
    "producer": "Teo Macero",
    "engineer": "Fred Plaut",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Dave Brubeck", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Bandleader." },
      { "name": "Paul Desmond", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Composer of 'Take Five'." },
      { "name": "Eugene Wright", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Joe Morello", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Blue Rondo à la Turk", "track_number": 1, "side": "A", "duration": "6:44", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Strange Meadow Lark", "track_number": 2, "side": "A", "duration": "7:22", "session_date": null, "composers": ["Dave Brubeck", "Iola Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Take Five", "track_number": 3, "side": "A", "duration": "5:24", "session_date": null, "composers": ["Paul Desmond"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Three to Get Ready", "track_number": 4, "side": "B", "duration": "5:24", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Kathy's Waltz", "track_number": 5, "side": "B", "duration": "4:48", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Everybody's Jumpin'", "track_number": 6, "side": "B", "duration": "4:23", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Pick Up Sticks", "track_number": 7, "side": "B", "duration": "4:16", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Dave Brubeck", "Paul Desmond", "Eugene Wright", "Joe Morello"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "193085545",
    "cover_art": [],
    "notes": "Three sessions (1959-06-25, 1959-07-01, 1959-08-18); cited source does not map individual tracks to specific dates. Cover art by S. Neil Fujita. Track personnel are the constant quartet, hence track_assignments_complete true; per-track session_date left null (Layer 4 unconfirmed)."
  }
}
```

```json
{
  "id": "gerry-mulligan-quartet-1952",
  "artist": "Gerry Mulligan Quartet",
  "album": "Gerry Mulligan Quartet",
  "year": 1952,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S5", "S6", "S8"],
  "epistemic": "obs",
  "rationale": "obs[S6]: Wikipedia's Cool jazz article cites Mulligan's pianoless quartet with Chet Baker as a defining West Coast cool development. obs[S5]: original Pacific Jazz PJLP-1 (10-inch LP), recorded Oct 1952 in Los Angeles. obs[S8]: Library of Congress / Stuart Nicholson document the August 1952 founding of the pianoless quartet that launched Mulligan, Baker, and Pacific Jazz. inf: the foundational West Coast cool small group.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "Original 10-inch LP; full track listing and complete personnel-per-track are not fully documented in available sources (see notes).",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1952-08-16", "1952-10-15", "1952-10-16"],
    "multi_session": true,
    "studio": "Phil Turetsky's home / Pacific Jazz sessions, Los Angeles",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Gerry Mulligan", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1952-08-16", "1952-10-15", "1952-10-16"], "epistemic": "obs", "sources": ["S5", "S8"], "name_variants": [], "notes": "Bandleader." },
      { "name": "Chet Baker", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1952-08-16", "1952-10-15", "1952-10-16"], "epistemic": "obs", "sources": ["S5", "S8"], "name_variants": [], "notes": "" },
      { "name": "Bob Whitlock", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1952-10-15", "1952-10-16"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "Confirmed on the Oct 15-16 1952 sessions ('Walkin' Shoes', 'Freeway')." },
      { "name": "Carson Smith", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": null, "epistemic": "unk", "sources": ["S8"], "name_variants": [], "notes": "Listed among quartet bassists across 1952-53; specific PJLP-1 tracks not confirmed." },
      { "name": "Chico Hamilton", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1952-08-16", "1952-10-15", "1952-10-16"], "epistemic": "obs", "sources": ["S5", "S8"], "name_variants": [], "notes": "Original quartet drummer." },
      { "name": "Larry Bunker", "instrument": "drums", "scope": "unknown", "tracks": null, "session_dates": null, "epistemic": "unk", "sources": ["S8"], "name_variants": [], "notes": "Drummer on some later quartet sessions; PJLP-1 involvement not confirmed." }
    ],
    "tracks": [
      { "title": "Bernie's Tune", "track_number": null, "side": null, "duration": null, "session_date": null, "composers": ["Bernie Miller"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Walkin' Shoes", "track_number": null, "side": null, "duration": null, "session_date": "1952-10-15", "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Freeway", "track_number": null, "side": null, "duration": null, "session_date": "1952-10-15", "composers": ["Chet Baker"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "cover_art": [],
    "notes": "Original Pacific Jazz PJLP-1, a 10-inch LP. Only three tracks ('Bernie's Tune', 'Walkin' Shoes', 'Freeway') are track-confirmed in cited sources; the full PJLP-1 sequence, track numbers, sides, and durations are not documented in available sources. Bassist/drummer rotation (Whitlock/Smith, Hamilton/Bunker) across the quartet's 1952-53 life is documented at the group level (S8) but not resolved per track. No clean original-album match found in the iTunes catalog (only later compilations), so apple_album_id is null. Composer of 'Bernie's Tune' (Bernie Miller) is standard attribution, not stated in S5."
  }
}
```

```json
{
  "id": "chet-baker-chet-baker-sings-1954",
  "artist": "Chet Baker",
  "album": "Chet Baker Sings",
  "year": 1954,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S3", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Pacific Jazz vocal-and-trumpet sessions (1954, expanded 1956) led by Richard Bock, the defining Chet Baker vocal statement. obs[S6]: Baker is named as a central West Coast cool figure in Wikipedia's Cool jazz overview. inf: a touchstone of the intimate, melody-forward West Coast cool aesthetic.",
  "priority": "strong",
  "overlap_risk": "Vocal-jazz crossover (the singing, not the playing, is the draw) — but instrumentally and stylistically firmly West Coast cool.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-02-15", "1956-07-23", "1956-07-30"],
    "multi_session": true,
    "studio": "Hollywood (1954); Forum Theatre, Los Angeles (1956)",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Chet Baker", "instrument": "vocals", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-02-15", "1956-07-23", "1956-07-30"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Bandleader; also plays trumpet throughout (instrument doubling). Primary role on this album is vocals." },
      { "name": "Russ Freeman", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-02-15", "1956-07-23", "1956-07-30"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Also plays celesta on some tracks." },
      { "name": "Carson Smith", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1954-02-15"], "epistemic": "unk", "sources": ["S3"], "name_variants": [], "notes": "S3 lists 'Carson Smith or Joe Mondragon' on the 1954 session; conflict unresolved." },
      { "name": "Joe Mondragon", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1954-02-15"], "epistemic": "unk", "sources": ["S3"], "name_variants": [], "notes": "Alternative to Carson Smith on the 1954 session per S3; conflict unresolved." },
      { "name": "Bob Neel", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1954-02-15"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "1954 session." },
      { "name": "Jimmy Bond", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": ["1956-07-23", "1956-07-30"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "1956 sessions." },
      { "name": "Larance Marable", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1956-07-23", "1956-07-30"], "epistemic": "unk", "sources": ["S3"], "name_variants": [], "notes": "S3 lists 'Larance Marable or Peter Littman' on the 1956 sessions; conflict unresolved." },
      { "name": "Peter Littman", "instrument": "drums", "scope": "selected-tracks", "tracks": null, "session_dates": ["1956-07-23", "1956-07-30"], "epistemic": "unk", "sources": ["S3"], "name_variants": [], "notes": "Alternative to Larance Marable on the 1956 sessions per S3; conflict unresolved." }
    ],
    "tracks": [
      { "title": "But Not for Me", "track_number": 1, "side": "A", "duration": "3:04", "session_date": "1954-02-15", "composers": ["George Gershwin", "Ira Gershwin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Time After Time", "track_number": 2, "side": "A", "duration": "2:46", "session_date": "1954-02-15", "composers": ["Jule Styne", "Sammy Cahn"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "My Funny Valentine", "track_number": 3, "side": "A", "duration": "2:21", "session_date": "1954-02-15", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "I Fall in Love Too Easily", "track_number": 4, "side": "A", "duration": "3:21", "session_date": "1954-02-15", "composers": ["Jule Styne", "Sammy Cahn"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "There Will Never Be Another You", "track_number": 5, "side": "A", "duration": "3:00", "session_date": "1954-02-15", "composers": ["Harry Warren", "Mack Gordon"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "I Get Along Without You Very Well", "track_number": 6, "side": "A", "duration": "2:59", "session_date": "1954-02-15", "composers": ["Hoagy Carmichael"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "The Thrill Is Gone", "track_number": 7, "side": "A", "duration": "2:51", "session_date": "1954-02-15", "composers": ["Ray Henderson", "Lew Brown"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Look for the Silver Lining", "track_number": 8, "side": "A", "duration": "2:39", "session_date": "1954-02-15", "composers": ["Jerome Kern", "Buddy DeSylva"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "That Old Feeling", "track_number": 9, "side": "B", "duration": "3:03", "session_date": "1956-07-23", "composers": ["Sammy Fain", "Lew Brown"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "It's Always You", "track_number": 10, "side": "B", "duration": "3:35", "session_date": "1956-07-23", "composers": ["Jimmy Van Heusen", "Johnny Burke"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Like Someone in Love", "track_number": 11, "side": "B", "duration": "2:26", "session_date": "1956-07-23", "composers": ["Jimmy Van Heusen", "Johnny Burke"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "My Ideal", "track_number": 12, "side": "B", "duration": "4:22", "session_date": "1956-07-30", "composers": ["Richard A. Whiting", "Newell Chase", "Leo Robin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "I've Never Been in Love Before", "track_number": 13, "side": "B", "duration": "4:29", "session_date": "1956-07-30", "composers": ["Frank Loesser"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "My Buddy", "track_number": 14, "side": "B", "duration": "3:19", "session_date": "1956-07-30", "composers": ["Walter Donaldson", "Gus Kahn"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440864756",
    "cover_art": [],
    "notes": "Original 1954 LP (Pacific Jazz PJLP-11) had the 8 tracks 1-8 (recorded 1954-02-15). The canonical/expanded edition (Pacific PJ-1222, 1956) adds tracks 9-14 from 1956-07-23 and 1956-07-30. Bassist on 1954 session ('Carson Smith or Joe Mondragon') and drummer on 1956 sessions ('Larance Marable or Peter Littman') are reported as alternatives by S3 — both listed with epistemic unk. Composer credits beyond what S3 lists are standard standards-attributions. Liner notes by Gerald Heard; photography by William Claxton. Side assignment A=1954 tracks / B=1956 tracks is approximate to the expanded-LP layout."
  }
}
```

```json
{
  "id": "art-pepper-art-pepper-meets-the-rhythm-section-1957",
  "artist": "Art Pepper",
  "album": "Art Pepper Meets the Rhythm Section",
  "year": 1957,
  "label": "Contemporary",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S4", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S4]: West Coast altoist Art Pepper recorded with Miles Davis's then-rhythm section (Garland/Chambers/Jones) in one Los Angeles session, Jan 19 1957, on Contemporary. obs[S6]: Pepper is a central West Coast cool figure. inf: a peak West Coast cool date and a recognized Pepper masterpiece.",
  "priority": "strong",
  "overlap_risk": "The rhythm section is the Miles Davis hard-bop unit, giving the date an East Coast / hard-bop pull; Pepper's lyrical alto keeps the lead voice cool/West Coast.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-01-19"],
    "multi_session": false,
    "studio": "Contemporary Records studio, Los Angeles",
    "producer": "Lester Koenig",
    "engineer": "Roy DuNann",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Art Pepper", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-01-19"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Bandleader." },
      { "name": "Red Garland", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-01-19"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-01-19"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-01-19"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "You'd Be So Nice to Come Home To", "track_number": 1, "side": "A", "duration": "5:25", "session_date": "1957-01-19", "composers": ["Cole Porter"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Red Pepper Blues", "track_number": 2, "side": "A", "duration": "3:37", "session_date": "1957-01-19", "composers": ["Art Pepper", "Red Garland"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Imagination", "track_number": 3, "side": "A", "duration": "5:52", "session_date": "1957-01-19", "composers": ["Jimmy Van Heusen", "Johnny Burke"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Waltz Me Blues", "track_number": 4, "side": "A", "duration": "2:56", "session_date": "1957-01-19", "composers": ["Art Pepper", "Paul Chambers"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Straight Life", "track_number": 5, "side": "A", "duration": "3:59", "session_date": "1957-01-19", "composers": ["Art Pepper"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Jazz Me Blues", "track_number": 6, "side": "B", "duration": "4:47", "session_date": "1957-01-19", "composers": ["Tom Delaney"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Tin Tin Deo", "track_number": 7, "side": "B", "duration": "7:42", "session_date": "1957-01-19", "composers": ["Gil Fuller", "Chano Pozo"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Star Eyes", "track_number": 8, "side": "B", "duration": "5:12", "session_date": "1957-01-19", "composers": ["Gene de Paul", "Don Raye"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Birks' Works", "track_number": 9, "side": "B", "duration": "4:17", "session_date": "1957-01-19", "composers": ["Dizzy Gillespie"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "The Man I Love", "track_number": 10, "side": null, "duration": "6:36", "session_date": "1957-01-19", "composers": ["George Gershwin", "Ira Gershwin"], "personnel": ["Art Pepper", "Red Garland", "Paul Chambers", "Philly Joe Jones"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440780070",
    "cover_art": [],
    "notes": "Single session, 1957-01-19, Los Angeles. Constant quartet, so track personnel are complete. 'The Man I Love' is a bonus track added to the 2002 reissue. Engineer Roy DuNann inferred (standard Contemporary Records engineer for this period); not stated in S4, hence epistemic_production inf. Side split A=1-5 / B=6-9 follows the original LP; the bonus track has no original side."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves
- **Miles Davis — *Birth of the Cool* (1950):** the project's named anchor and cool jazz's founding document; non-negotiable.
- **The Dave Brubeck Quartet — *Time Out* (1959):** the most popularly recognized cool-jazz LP, built on odd meters; a cornerstone despite its 1959 date.

### Hidden Gems
- **Gerry Mulligan Quartet (1952, Pacific Jazz PJLP-1):** the pianoless quartet that launched West Coast cool and Pacific Jazz itself — historically pivotal but under-documented at the track level compared with its fame.

### Consensus Picks (3+ sources)
- None reach three independent sources in this small POC map. *Birth of the Cool* and the Mulligan Quartet each carry two-to-three corroborating sources (S1/S6 and S5/S6/S8 respectively); the rest rest on a dedicated album source plus the genre-overview source.

### Single-Source Picks
- No record relies on a single source: each pairs a detailed album source (S1–S5) with the genre-overview source (S6) or a second corroborating source (S8). The Mulligan track listing, however, is effectively single-source (S5) at the track level.

### Scope Calls
- ***Time Out* (1959)** sits just past the ~1949–1958 cool window in `docs/genre-definitions.md`; kept in for its arranged, classically-informed cool/third-stream character — flagged for John.
- ***Chet Baker Sings*** is a vocal-crossover record; retained as West Coast cool because the instrumental setting and aesthetic are squarely in style.
- ***Art Pepper Meets the Rhythm Section*** uses Miles Davis's hard-bop rhythm section (Garland/Chambers/Jones); kept as West Coast cool on the strength of Pepper's lead voice, with the hard-bop pull flagged in `overlap_risk`.

### Gaps Noticed
- No Lennie Tristano / Lee Konitz leader date, no Stan Getz, no Shorty Rogers, Shelly Manne, Jimmy Giuffre, or Howard Rumsey Lighthouse All-Stars in this POC slice — the deeper West Coast bench and the Tristano "cerebral" wing are untouched and worth a future dispatch.
- The Penguin Guide and AllMusic editorial ratings were not directly consulted in this pass (Wikipedia stood in for canon grounding); a follow-up should add those for sharper priority calibration.

### Personnel Coverage
- **Full track listing + complete track-personnel:** *Time Out* and *Art Pepper Meets the Rhythm Section* — constant quartets, every musician confirmed across all tracks (`track_assignments_complete: true`).
- **Full track listing, track-personnel not at musician level:** *Birth of the Cool* (11+1 tracks with composers, session lineups documented but per-track personnel arrays left empty) and *Chet Baker Sings* (14 tracks with session dates; two unresolved bass/drum conflicts carried as `unk`).
- **Thin:** *Gerry Mulligan Quartet (PJLP-1)* — only three tracks are track-confirmed in available sources; full 10-inch sequence, track numbers, durations, and per-track bass/drum assignments are undocumented, and no clean original-album Apple Music ID exists (only later compilations). This is the weakest personnel record of the five and the clearest candidate for a deeper discography source (Tom Lord) on a later pass.
- **References:** Apple Music `collectionId` captured for four of five (null for the Mulligan, no clean match); MusicBrainz release-group MBIDs and Cover Art Archive URLs were not retrieved this pass (left null/empty per the optional Layer 5 discipline).
