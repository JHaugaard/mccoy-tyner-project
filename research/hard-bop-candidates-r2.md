# Hard Bop / Soul Jazz Candidates — Round 2 (Growth Push)

Specialist: Hard Bop / Soul Jazz researcher. Dispatch: 15 complete candidate records (canon metadata + full personnel/tracks/sessions/dates in one pass). Ledger excludes the 15 albums already in the collection (the 5 hard-bop/soul-jazz pillars among them — *Moanin'*, *Song for My Father*, *The Sidewinder*, *Soul Station*, *The Sermon!* — none re-surfaced). Cull-notes: no prior verdicts to calibrate against. `year` = **recording** year per this round's convention; release year noted in each record's `notes` when it differs.

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | docs/genre-definitions.md (project scope authority) | Project doc | docs/genre-definitions.md | Names *Alligator Bogaloo* as a soul-jazz anchor; defines post-bebop→pre-fusion scope |
| S2 | iTunes Search/Lookup API | API | https://itunes.apple.com/search | Apple `collectionId` lookup, no auth |
| S3 | MusicBrainz release-group API | API/DB | https://musicbrainz.org/ws/2/release-group/ | Release-group MBIDs (original studio-album RG preferred) |
| S4 | Cover Art Archive | Service | https://coverartarchive.org/ | Front-cover URLs constructed from release-group MBID; not individually verified |
| S5 | Penguin Guide to Jazz (Cook & Morton) | Book | — | General critical reference for hard-bop/soul-jazz core collection |
| S6 | Wikipedia — "Saxophone Colossus" | Web article | https://en.wikipedia.org/wiki/Saxophone_Colossus | Personnel, session, tracklist, credits |
| S7 | Wikipedia — "Somethin' Else (Cannonball Adderley album)" | Web article | https://en.wikipedia.org/wiki/Somethin%27_Else_(Cannonball_Adderley_album) | Personnel, session, tracklist |
| S8 | Wikipedia — "Study in Brown" | Web article | https://en.wikipedia.org/wiki/Study_in_Brown | Personnel, tracklist; no producer/engineer listed |
| S9 | Wikipedia — "The Incredible Jazz Guitar of Wes Montgomery" | Web article | https://en.wikipedia.org/wiki/The_Incredible_Jazz_Guitar_of_Wes_Montgomery | Personnel, two-day session, tracklist, credits |
| S10 | Wikipedia — "Cool Struttin'" | Web article | https://en.wikipedia.org/wiki/Cool_Struttin%27 | Personnel, session, original LP + CD bonus tracks |
| S11 | Wikipedia — "Let Freedom Ring (Jackie McLean album)" | Web article | https://en.wikipedia.org/wiki/Let_Freedom_Ring | Personnel, session, tracklist |
| S12 | Wikipedia — "Ready for Freddie" | Web article | https://en.wikipedia.org/wiki/Ready_for_Freddie | Personnel, session, tracklist + alternate takes |
| S13 | Wikipedia — "Una Mas" | Web article | https://en.wikipedia.org/wiki/Una_Mas | Personnel, session, tracklist; track 4 a 1987-issued outtake |
| S14 | Wikipedia — "Idle Moments" | Web article | https://en.wikipedia.org/wiki/Idle_Moments | Personnel, two sessions, per-track recording dates |
| S15 | Wikipedia — "Go (Dexter Gordon album)" | Web article | https://en.wikipedia.org/wiki/Go_(Dexter_Gordon_album) | Personnel, session, tracklist, credits |
| S16 | Wikipedia — "Page One (Joe Henderson album)" | Web article | https://en.wikipedia.org/wiki/Page_One_(Joe_Henderson_album) | Personnel, session, tracklist, credits |
| S17 | Wikipedia — "Blowin' the Blues Away" | Web article | https://en.wikipedia.org/wiki/Blowin%27_the_Blues_Away | Quintet/trio per-track session mapping |
| S18 | Wikipedia — "Alligator Bogaloo" | Web article | https://en.wikipedia.org/wiki/Alligator_Bogaloo | Personnel, session, tracklist; engineer not listed |
| S19 | Wikipedia — "Back at the Chicken Shack" | Web article | https://en.wikipedia.org/wiki/Back_at_the_Chicken_Shack | Personnel, session, tracklist; Burrell on selected tracks |
| S20 | Wikipedia — "Boss Tenor" | Web article | https://en.wikipedia.org/wiki/Boss_Tenor | Personnel, session, tracklist; engineer not listed |

---

## 2. Candidate Records

```json
{
  "id": "sonny-rollins-saxophone-colossus-1956",
  "artist": "Sonny Rollins",
  "album": "Saxophone Colossus",
  "year": 1956,
  "label": "Prestige",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S6"],
  "epistemic": "obs",
  "rationale": "obs[S6]: single-session quartet date (Rollins/Flanagan/Watkins/Roach) with the calypso 'St. Thomas' and the analytically celebrated 'Blue 7' documented. inf[S5]: a fixture of standard hard-bop core collections and widely cited as Rollins's defining studio statement. inf: cross-reference of critical reputation and program — a non-negotiable pillar of the idiom.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-06-22"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Bob Weinstock",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Sonny Rollins", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "Leader" },
      { "name": "Tommy Flanagan", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "" },
      { "name": "Doug Watkins", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "" },
      { "name": "Max Roach", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "St. Thomas", "track_number": 1, "side": "A", "duration": "6:49", "session_date": "1956-06-22", "composers": ["Sonny Rollins"], "personnel": ["Sonny Rollins", "Tommy Flanagan", "Doug Watkins", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "You Don't Know What Love Is", "track_number": 2, "side": "A", "duration": "6:30", "session_date": "1956-06-22", "composers": ["Gene de Paul", "Don Raye"], "personnel": ["Sonny Rollins", "Tommy Flanagan", "Doug Watkins", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Strode Rode", "track_number": 3, "side": "A", "duration": "5:17", "session_date": "1956-06-22", "composers": ["Sonny Rollins"], "personnel": ["Sonny Rollins", "Tommy Flanagan", "Doug Watkins", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Moritat", "track_number": 4, "side": "B", "duration": "10:05", "session_date": "1956-06-22", "composers": ["Kurt Weill", "Bertolt Brecht"], "personnel": ["Sonny Rollins", "Tommy Flanagan", "Doug Watkins", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Blue 7", "track_number": 5, "side": "B", "duration": "11:17", "session_date": "1956-06-22", "composers": ["Sonny Rollins"], "personnel": ["Sonny Rollins", "Tommy Flanagan", "Doug Watkins", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "cf29d6a2-a18a-3bb6-a861-495148baee1f",
    "apple_album_id": "1440737584",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/cf29d6a2-a18a-3bb6-a861-495148baee1f/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, June 22 1956; released 1957 (March/April) as Prestige PRLP 7079. 'Moritat' is Kurt Weill's 'Mack the Knife'. Whole-band quartet on every track."
  }
}
```

```json
{
  "id": "cannonball-adderley-somethin-else-1958",
  "artist": "Cannonball Adderley",
  "album": "Somethin' Else",
  "year": 1958,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S7"],
  "epistemic": "obs",
  "rationale": "obs[S7]: single-session quintet led by Adderley with Miles Davis on trumpet, Hank Jones, Sam Jones, and Art Blakey; the celebrated long-form 'Autumn Leaves' opens it. inf[S5]: a standing entry in hard-bop core collections, distinguished by Davis's rare sideman appearance. inf: critical consensus plus marquee personnel — a pillar of the era.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-03-09"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Cannonball Adderley", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": ["Julian Adderley", "Julian \"Cannonball\" Adderley"], "notes": "Leader" },
      { "name": "Miles Davis", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Sideman appearance" },
      { "name": "Hank Jones", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Composed 'Bangoon' / 'Alison's Uncle'" },
      { "name": "Sam Jones", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Autumn Leaves", "track_number": 1, "side": "A", "duration": "10:55", "session_date": "1958-03-09", "composers": ["Joseph Kosma", "Johnny Mercer", "Jacques Prévert"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Love for Sale", "track_number": 2, "side": "A", "duration": "7:01", "session_date": "1958-03-09", "composers": ["Cole Porter"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Somethin' Else", "track_number": 3, "side": "B", "duration": "8:15", "session_date": "1958-03-09", "composers": ["Miles Davis"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "One for Daddy-O", "track_number": 4, "side": "B", "duration": "8:26", "session_date": "1958-03-09", "composers": ["Nat Adderley"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Dancing in the Dark", "track_number": 5, "side": "B", "duration": "4:07", "session_date": "1958-03-09", "composers": ["Arthur Schwartz", "Howard Dietz"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Bangoon", "track_number": 6, "side": null, "duration": "5:05", "session_date": "1958-03-09", "composers": ["Hank Jones"], "personnel": ["Cannonball Adderley", "Miles Davis", "Hank Jones", "Sam Jones", "Art Blakey"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "495c22f5-90b3-3e87-8be1-2c55aef3ed82",
    "apple_album_id": "721271258",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/495c22f5-90b3-3e87-8be1-2c55aef3ed82/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, March 9 1958; released August 1958 as Blue Note BLP 1595. Original LP was 5 tracks; 'Bangoon' (aka 'Alison's Uncle', Hank Jones) recorded the same session and added on CD reissues — flagged bonus_track. apple_album_id is the 2012 remaster edition (no plain-original edition surfaced in the iTunes lookup); MusicBrainz RG is the original 1958 studio-album group."
  }
}
```

```json
{
  "id": "clifford-brown-max-roach-study-in-brown-1955",
  "artist": "Clifford Brown & Max Roach",
  "album": "Study in Brown",
  "year": 1955,
  "label": "EmArcy",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S8"],
  "epistemic": "obs",
  "rationale": "obs[S8]: the Brown–Roach Quintet (Brown/Land/Powell/Morrow/Roach) documented across a Feb 1955 date. inf[S5]: foundational early hard bop — the quintet that defined the trumpet-tenor front line that Blakey and Silver carried forward. inf: a cornerstone of the 1955–56 hard-bop emergence and one of the few essential pre-Blue-Note entries in the idiom.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-02-23/1955-02-25"],
    "multi_session": true,
    "studio": "Capitol Studios, New York City",
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Clifford Brown", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Co-leader" },
      { "name": "Harold Land", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "" },
      { "name": "Richie Powell", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "" },
      { "name": "George Morrow", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "" },
      { "name": "Max Roach", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Co-leader" }
    ],
    "tracks": [
      { "title": "Cherokee", "track_number": 1, "side": null, "duration": "5:44", "session_date": null, "composers": ["Ray Noble"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Jacqui", "track_number": 2, "side": null, "duration": "5:11", "session_date": null, "composers": ["Richie Powell"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Swingin'", "track_number": 3, "side": null, "duration": "2:52", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Lands End", "track_number": 4, "side": null, "duration": "4:57", "session_date": null, "composers": ["Harold Land"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "George's Dilemma", "track_number": 5, "side": null, "duration": "5:36", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Sandu", "track_number": 6, "side": null, "duration": "4:57", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Gerkin for Perkin", "track_number": 7, "side": null, "duration": "2:56", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "If I Love Again", "track_number": 8, "side": null, "duration": "3:24", "session_date": null, "composers": ["Jack Murray", "Ben Oakland"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Take the 'A' Train", "track_number": 9, "side": null, "duration": "4:16", "session_date": null, "composers": ["Billy Strayhorn"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "unk", "sources": ["S8"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "ecdf91a1-9e2a-44db-83f2-7f6c9ff82c10",
    "apple_album_id": "1434889869",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/ecdf91a1-9e2a-44db-83f2-7f6c9ff82c10/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Recorded Feb 23–25 1955 at Capitol Studios, NYC; released 1955 as EmArcy MG 36037. S8 did not list producer or engineer (explicit nulls; epistemic_production unk). S8 did not give side divisions, so all `side` set null. S8 lists 9 tracks; 'Take the \\'A\\' Train' (track 9) carries epistemic_track 'unk' — the original-LP vs CD-reissue status of that track was not separately verified. Same quintet on every track (track_assignments_complete true on personnel grounds)."
  }
}
```

```json
{
  "id": "wes-montgomery-the-incredible-jazz-guitar-of-wes-montgomery-1960",
  "artist": "Wes Montgomery",
  "album": "The Incredible Jazz Guitar of Wes Montgomery",
  "year": 1960,
  "label": "Riverside",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S9"],
  "epistemic": "obs",
  "rationale": "obs[S9]: two-day quartet date (Montgomery with Tommy Flanagan, Percy Heath, Albert Heath) featuring the originals 'Four on Six' and 'West Coast Blues'. inf[S5]: the standard reference point for hard-bop guitar and Montgomery's breakthrough as a leader. inf: fills a guitar gap in the canon and is consensus-essential — a pillar.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-01-26", "1960-01-28"],
    "multi_session": true,
    "studio": "Reeves Sound Studios, New York City",
    "producer": "Orrin Keepnews",
    "engineer": "Jack Higgins",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Wes Montgomery", "instrument": "electric guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Leader" },
      { "name": "Tommy Flanagan", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Percy Heath", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Albert Heath", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": ["Albert \"Tootie\" Heath"], "notes": "" }
    ],
    "tracks": [
      { "title": "Airegin", "track_number": 1, "side": "A", "duration": "4:26", "session_date": null, "composers": ["Sonny Rollins"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "D-Natural Blues", "track_number": 2, "side": "A", "duration": "5:23", "session_date": null, "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Polka Dots and Moonbeams", "track_number": 3, "side": "A", "duration": "4:44", "session_date": null, "composers": ["Jimmy Van Heusen", "Johnny Burke"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Four on Six", "track_number": 4, "side": "A", "duration": "6:15", "session_date": null, "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "West Coast Blues", "track_number": 5, "side": "B", "duration": "7:26", "session_date": null, "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "In Your Own Sweet Way", "track_number": 6, "side": "B", "duration": "4:53", "session_date": null, "composers": ["Dave Brubeck"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Mister Walker", "track_number": 7, "side": "B", "duration": "4:33", "session_date": null, "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Gone With the Wind", "track_number": 8, "side": "B", "duration": "6:24", "session_date": null, "composers": ["Allie Wrubel", "Herb Magidson"], "personnel": ["Wes Montgomery", "Tommy Flanagan", "Percy Heath", "Albert Heath"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "92829cab-8dee-3e6b-97ad-22fd49c95ed5",
    "apple_album_id": "1794908400",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/92829cab-8dee-3e6b-97ad-22fd49c95ed5/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Two sessions, Jan 26 & 28 1960; released April 1960 as Riverside RLP 12-320. S9 does not map tracks to specific session dates (per-track session_date null), though all personnel are common to both dates. Side split (A: 1–4, B: 5–8) is the conventional LP division. apple_album_id is the 2025 remaster (no plain-original edition surfaced in the iTunes lookup)."
  }
}
```

```json
{
  "id": "sonny-clark-cool-struttin-1958",
  "artist": "Sonny Clark",
  "album": "Cool Struttin'",
  "year": 1958,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S10"],
  "epistemic": "obs",
  "rationale": "obs[S10]: single-session quintet (Clark with Art Farmer, Jackie McLean, Paul Chambers, Philly Joe Jones); the title blues is a Blue Note signature. inf[S5]: a perennial hard-bop core-collection pick and Clark's most celebrated date as a leader. inf: well-sourced, consensus-strong, but a notch below the genre-defining pillars.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-01-05"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Sonny Clark", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Leader" },
      { "name": "Art Farmer", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Jackie McLean", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Cool Struttin'", "track_number": 1, "side": "A", "duration": "9:23", "session_date": "1958-01-05", "composers": ["Sonny Clark"], "personnel": ["Sonny Clark", "Art Farmer", "Jackie McLean", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Blue Minor", "track_number": 2, "side": "A", "duration": "10:19", "session_date": "1958-01-05", "composers": ["Sonny Clark"], "personnel": ["Sonny Clark", "Art Farmer", "Jackie McLean", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Sippin' at Bells", "track_number": 3, "side": "B", "duration": "8:18", "session_date": "1958-01-05", "composers": ["Miles Davis"], "personnel": ["Sonny Clark", "Art Farmer", "Jackie McLean", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Deep Night", "track_number": 4, "side": "B", "duration": "10:19", "session_date": "1958-01-05", "composers": ["Charles E. Henderson", "Rudy Vallée"], "personnel": ["Sonny Clark", "Art Farmer", "Jackie McLean", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "5b91f2d3-bc5b-365c-99f0-1cee467f0249",
    "apple_album_id": "1443185284",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/5b91f2d3-bc5b-365c-99f0-1cee467f0249/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Jan 5 1958; released August 1958 as Blue Note BLP 1588. Original LP is 4 tracks (listed). CD reissues add 'Royal Flush' (9:00) and 'Lover' (Rodgers/Hart, 7:01) — excluded here as reissue-only bonuses. Whole-band quintet on every original track."
  }
}
```

```json
{
  "id": "jackie-mclean-let-freedom-ring-1962",
  "artist": "Jackie McLean",
  "album": "Let Freedom Ring",
  "year": 1962,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "post-bop"],
  "sources": ["S5", "S11"],
  "epistemic": "obs",
  "rationale": "obs[S11]: piano quartet (McLean with Walter Davis Jr., Herbie Lewis, Billy Higgins); McLean's first record to absorb the new-thing influence while keeping hard-bop structure. inf[S5]: widely cited as McLean's pivot record — hard bop reaching toward the avant-garde without dissolving. inf: still swings with structure (in scope per the post-bop fuzzy edge); a strong, distinctive entry filling the Jackie McLean gap.",
  "priority": "strong",
  "overlap_risk": "hard-bop/post-bop border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1962-03-19"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Jackie McLean", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "Leader; composed three of four tracks" },
      { "name": "Walter Davis Jr.", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Herbie Lewis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Billy Higgins", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Melody for Melonae", "track_number": 1, "side": "A", "duration": "13:24", "session_date": "1962-03-19", "composers": ["Jackie McLean"], "personnel": ["Jackie McLean", "Walter Davis Jr.", "Herbie Lewis", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "I'll Keep Loving You", "track_number": 2, "side": "A", "duration": "6:18", "session_date": "1962-03-19", "composers": ["Bud Powell"], "personnel": ["Jackie McLean", "Walter Davis Jr.", "Herbie Lewis", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Rene", "track_number": 3, "side": "B", "duration": "10:03", "session_date": "1962-03-19", "composers": ["Jackie McLean"], "personnel": ["Jackie McLean", "Walter Davis Jr.", "Herbie Lewis", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Omega", "track_number": 4, "side": "B", "duration": "8:31", "session_date": "1962-03-19", "composers": ["Jackie McLean"], "personnel": ["Jackie McLean", "Walter Davis Jr.", "Herbie Lewis", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "c62356a3-957a-3d7b-ad26-b47365d3faa5",
    "apple_album_id": "1443825730",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/c62356a3-957a-3d7b-ad26-b47365d3faa5/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, March 19 1962; released 1963 (May) as Blue Note BST 84106. S11 did not name the engineer; Blue Note session at Van Gelder Studio, Englewood Cliffs → Rudy Van Gelder by inference (epistemic_production inf). Producer/studio/label directly sourced. Pianoless? No — Walter Davis Jr. on piano throughout."
  }
}
```

```json
{
  "id": "freddie-hubbard-ready-for-freddie-1961",
  "artist": "Freddie Hubbard",
  "album": "Ready for Freddie",
  "year": 1961,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S12"],
  "epistemic": "obs",
  "rationale": "obs[S12]: sextet date (Hubbard with Wayne Shorter, Bernard McKinney on euphonium, McCoy Tyner, Art Davis, Elvin Jones) including 'Birdlike'. inf[S5]: a standard hard-bop core pick and Hubbard's first pairing with three-fifths of the classic Coltrane rhythm section. inf: strong personnel and program; clearly belongs.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-08-21"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Leader; composed three of five original-LP tracks" },
      { "name": "Wayne Shorter", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Composed 'Marie Antoinette'" },
      { "name": "Bernard McKinney", "instrument": "euphonium", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": ["Kiane Zawadi"], "notes": "Euphonium not in the project taxonomy; closest brass voicing, flagged per contract" },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" },
      { "name": "Art Davis", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" },
      { "name": "Elvin Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Arietis", "track_number": 1, "side": "A", "duration": "6:41", "session_date": "1961-08-21", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "Wayne Shorter", "Bernard McKinney", "McCoy Tyner", "Art Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Weaver of Dreams", "track_number": 2, "side": "A", "duration": "6:35", "session_date": "1961-08-21", "composers": ["Jack Elliott", "Victor Young"], "personnel": ["Freddie Hubbard", "Wayne Shorter", "Bernard McKinney", "McCoy Tyner", "Art Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Marie Antoinette", "track_number": 3, "side": "A", "duration": "6:38", "session_date": "1961-08-21", "composers": ["Wayne Shorter"], "personnel": ["Freddie Hubbard", "Wayne Shorter", "Bernard McKinney", "McCoy Tyner", "Art Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Birdlike", "track_number": 4, "side": "B", "duration": "10:15", "session_date": "1961-08-21", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "Wayne Shorter", "Bernard McKinney", "McCoy Tyner", "Art Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Crisis", "track_number": 5, "side": "B", "duration": "11:33", "session_date": "1961-08-21", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "Wayne Shorter", "Bernard McKinney", "McCoy Tyner", "Art Davis", "Elvin Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "0131b475-3788-328d-95cf-41759481fcb9",
    "apple_album_id": "1444069334",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/0131b475-3788-328d-95cf-41759481fcb9/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Aug 21 1961; released 1962 (mid-April) as Blue Note BLP 4085 / BST 84085. Original LP is 5 tracks (listed); the 2003 CD remaster adds alternate takes of 'Arietis' (5:51) and 'Marie Antoinette' (6:15) — excluded here as reissue-only alternates. S12 did not name the engineer; Van Gelder Studio session → Rudy Van Gelder by inference (epistemic_production inf). Bernard McKinney's euphonium has no exact taxonomy string — recorded as 'euphonium' and flagged per the contract's escape clause."
  }
}
```

```json
{
  "id": "kenny-dorham-una-mas-1963",
  "artist": "Kenny Dorham",
  "album": "Una Mas",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S13"],
  "epistemic": "obs",
  "rationale": "obs[S13]: quintet date (Dorham with Joe Henderson, Herbie Hancock, Butch Warren, Tony Williams); the long Latin-tinged title track anchors it. inf[S5]: a well-regarded late Dorham leader date, notable for an early Tony Williams appearance. inf: strong, distinctive, fills the Kenny Dorham gap.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-04-01"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Kenny Dorham", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Leader; composed three of four tracks. Adds spoken voice on the 'Una Mas' outro per S13" },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Butch Warren", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Tony Williams", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Early Williams appearance (age 17)" }
    ],
    "tracks": [
      { "title": "Una Mas (One More Time)", "track_number": 1, "side": "A", "duration": "15:19", "session_date": "1963-04-01", "composers": ["Kenny Dorham"], "personnel": ["Kenny Dorham", "Joe Henderson", "Herbie Hancock", "Butch Warren", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Straight Ahead", "track_number": 2, "side": "B", "duration": "8:58", "session_date": "1963-04-01", "composers": ["Kenny Dorham"], "personnel": ["Kenny Dorham", "Joe Henderson", "Herbie Hancock", "Butch Warren", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Sao Paulo", "track_number": 3, "side": "B", "duration": "7:20", "session_date": "1963-04-01", "composers": ["Kenny Dorham"], "personnel": ["Kenny Dorham", "Joe Henderson", "Herbie Hancock", "Butch Warren", "Tony Williams"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "If Ever I Would Leave You", "track_number": 4, "side": null, "duration": "5:07", "session_date": "1963-04-01", "composers": ["Alan Jay Lerner", "Frederick Loewe"], "personnel": ["Kenny Dorham", "Joe Henderson", "Herbie Hancock", "Butch Warren", "Tony Williams"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "463b030f-518d-4cca-a0c5-4e89a59cf85e",
    "apple_album_id": "1445891079",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/463b030f-518d-4cca-a0c5-4e89a59cf85e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, April 1 1963; released 1964 (early January) as Blue Note BST 84127. Original LP is 3 tracks; 'If Ever I Would Leave You' (from Camelot) was a session outtake first issued 1987 — flagged bonus_track. S13 did not name the engineer; Van Gelder Studio session → Rudy Van Gelder by inference (epistemic_production inf). apple_album_id is the 2014 remaster edition."
  }
}
```

```json
{
  "id": "grant-green-idle-moments-1963",
  "artist": "Grant Green",
  "album": "Idle Moments",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S5", "S14"],
  "epistemic": "obs",
  "rationale": "obs[S14]: sextet over two sessions (Green with Joe Henderson, Duke Pearson, Bobby Hutcherson, Bob Cranshaw, Al Harewood); the 15-minute title track is the centerpiece. inf[S5]: a consensus Grant Green high point and one of the most atmospheric Blue Note guitar dates. inf: well-sourced, distinctive mood piece; clearly belongs.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-11-04", "1963-11-15"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Grant Green", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Leader" },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Duke Pearson", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Composed 'Idle Moments' and 'Nomad'" },
      { "name": "Bobby Hutcherson", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Bob Cranshaw", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Al Harewood", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-11-04", "1963-11-15"], "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Idle Moments", "track_number": 1, "side": "A", "duration": "14:56", "session_date": "1963-11-04", "composers": ["Duke Pearson"], "personnel": ["Grant Green", "Joe Henderson", "Duke Pearson", "Bobby Hutcherson", "Bob Cranshaw", "Al Harewood"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Jean De Fleur", "track_number": 2, "side": "B", "duration": "6:49", "session_date": "1963-11-15", "composers": ["Grant Green"], "personnel": ["Grant Green", "Joe Henderson", "Duke Pearson", "Bobby Hutcherson", "Bob Cranshaw", "Al Harewood"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Django", "track_number": 3, "side": "B", "duration": "8:44", "session_date": "1963-11-15", "composers": ["John Lewis"], "personnel": ["Grant Green", "Joe Henderson", "Duke Pearson", "Bobby Hutcherson", "Bob Cranshaw", "Al Harewood"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Nomad", "track_number": 4, "side": "B", "duration": "12:16", "session_date": "1963-11-04", "composers": ["Duke Pearson"], "personnel": ["Grant Green", "Joe Henderson", "Duke Pearson", "Bobby Hutcherson", "Bob Cranshaw", "Al Harewood"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "b65889f6-1a7a-3233-b42c-6382fac570b1",
    "apple_album_id": "1443768982",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/b65889f6-1a7a-3233-b42c-6382fac570b1/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Two sessions, Nov 4 & 15 1963; released February 1965 as Blue Note BST 84154. Per-track session dates from S14: Nov 4 — 'Idle Moments', 'Nomad'; Nov 15 — 'Jean De Fleur', 'Django'. Same sextet on both dates. S14 did not name the engineer; Van Gelder Studio session → Rudy Van Gelder by inference (epistemic_production inf). CD reissue adds alternate takes — excluded."
  }
}
```

```json
{
  "id": "dexter-gordon-go-1962",
  "artist": "Dexter Gordon",
  "album": "Go",
  "year": 1962,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S15"],
  "epistemic": "obs",
  "rationale": "obs[S15]: quartet date (Gordon with Sonny Clark, Butch Warren, Billy Higgins) including the signature 'Cheese Cake'. inf[S5]: routinely cited as the peak of Gordon's Blue Note period and a core tenor-quartet statement. inf: strong, consensus-backed; clearly belongs.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1962-08-27"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Dexter Gordon", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Leader; composed 'Cheese Cake'" },
      { "name": "Sonny Clark", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Butch Warren", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Billy Higgins", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Cheese Cake", "track_number": 1, "side": "A", "duration": "6:33", "session_date": "1962-08-27", "composers": ["Dexter Gordon"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "I Guess I'll Hang My Tears Out to Dry", "track_number": 2, "side": "A", "duration": "5:23", "session_date": "1962-08-27", "composers": ["Jule Styne", "Sammy Cahn"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Second Balcony Jump", "track_number": 3, "side": "A", "duration": "7:05", "session_date": "1962-08-27", "composers": ["Billy Eckstine", "Gerald Valentine"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Love for Sale", "track_number": 4, "side": "B", "duration": "7:40", "session_date": "1962-08-27", "composers": ["Cole Porter"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Where Are You?", "track_number": 5, "side": "B", "duration": "5:21", "session_date": "1962-08-27", "composers": ["Jimmy McHugh", "Harold Adamson"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Three O'Clock in the Morning", "track_number": 6, "side": "B", "duration": "5:42", "session_date": "1962-08-27", "composers": ["Julián Robledo", "Dorothy Terriss"], "personnel": ["Dexter Gordon", "Sonny Clark", "Butch Warren", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "2b77fa1f-384d-3056-9491-91cb64a96eae",
    "apple_album_id": "1459439436",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/2b77fa1f-384d-3056-9491-91cb64a96eae/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Aug 27 1962; released December 1962 as Blue Note BLP 4112. Whole-band quartet on every track."
  }
}
```

```json
{
  "id": "joe-henderson-page-one-1963",
  "artist": "Joe Henderson",
  "album": "Page One",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S5", "S16"],
  "epistemic": "obs",
  "rationale": "obs[S16]: Henderson's leader debut (with Kenny Dorham, McCoy Tyner, Butch Warren, Pete La Roca), introducing the standards 'Blue Bossa' and 'Recorda Me'. inf[S5]: a core Blue Note debut and the entry point for two enduring jazz standards. inf: strong, consensus-backed, historically pivotal.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-06-03"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S16"], "name_variants": [], "notes": "Leader; composed four of six tracks" },
      { "name": "Kenny Dorham", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S16"], "name_variants": [], "notes": "Composed 'Blue Bossa' and 'La Mesha'" },
      { "name": "McCoy Tyner", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S16"], "name_variants": [], "notes": "" },
      { "name": "Butch Warren", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S16"], "name_variants": [], "notes": "" },
      { "name": "Pete La Roca", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S16"], "name_variants": ["Pete LaRoca", "Pete La Roca Sims"], "notes": "" }
    ],
    "tracks": [
      { "title": "Blue Bossa", "track_number": 1, "side": "A", "duration": "8:03", "session_date": "1963-06-03", "composers": ["Kenny Dorham"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] },
      { "title": "La Mesha", "track_number": 2, "side": "A", "duration": "9:10", "session_date": "1963-06-03", "composers": ["Kenny Dorham"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] },
      { "title": "Homestretch", "track_number": 3, "side": "A", "duration": "4:15", "session_date": "1963-06-03", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] },
      { "title": "Recorda Me", "track_number": 4, "side": "B", "duration": "6:03", "session_date": "1963-06-03", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] },
      { "title": "Jinrikisha", "track_number": 5, "side": "B", "duration": "7:24", "session_date": "1963-06-03", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] },
      { "title": "Out of the Night", "track_number": 6, "side": "B", "duration": "7:23", "session_date": "1963-06-03", "composers": ["Joe Henderson"], "personnel": ["Joe Henderson", "Kenny Dorham", "McCoy Tyner", "Butch Warren", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S16"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "b8387a4b-fd1a-3b68-bdba-95ec30962428",
    "apple_album_id": "1444001655",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/b8387a4b-fd1a-3b68-bdba-95ec30962428/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, June 3 1963; released October 1963 as Blue Note BST 84140. Whole-band quintet on every track. Title 'Recorda Me' also printed as 'Recorda-Me' on some pressings."
  }
}
```

```json
{
  "id": "horace-silver-blowin-the-blues-away-1959",
  "artist": "Horace Silver",
  "album": "Blowin' the Blues Away",
  "year": 1959,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S5", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S17]: the classic Silver Quintet (Blue Mitchell, Junior Cook, Gene Taylor, Louis Hayes) plus trio tracks, with the funky 'Sister Sadie' and the ballad 'Peace'. inf[S5]: a core Silver date predating Song for My Father and a standard hard-bop/soul-jazz reference. inf: strong, gospel-blues-inflected, clearly in scope and pre-fusion.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-08-29", "1959-08-30", "1959-09-13"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Horace Silver", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-08-29", "1959-08-30", "1959-09-13"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "Leader; composed all tracks except 'How Did It Happen'" },
      { "name": "Blue Mitchell", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Blowin' the Blues Away", "Break City", "Peace", "Sister Sadie", "The Baghdad Blues", "How Did It Happen"], "session_dates": ["1959-08-29", "1959-08-30"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "Quintet tracks only" },
      { "name": "Junior Cook", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Blowin' the Blues Away", "Break City", "Peace", "Sister Sadie", "The Baghdad Blues", "How Did It Happen"], "session_dates": ["1959-08-29", "1959-08-30"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "Quintet tracks only" },
      { "name": "Gene Taylor", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-08-29", "1959-08-30", "1959-09-13"], "epistemic": "obs", "sources": ["S17"], "name_variants": ["Eugene Taylor"], "notes": "" },
      { "name": "Louis Hayes", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-08-29", "1959-08-30", "1959-09-13"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Blowin' the Blues Away", "track_number": 1, "side": "A", "duration": "4:44", "session_date": "1959-08-29", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "The St. Vitus Dance", "track_number": 2, "side": "A", "duration": "4:09", "session_date": "1959-09-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "Break City", "track_number": 3, "side": "A", "duration": "4:57", "session_date": "1959-08-30", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "Peace", "track_number": 4, "side": "A", "duration": "6:02", "session_date": "1959-08-30", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "Sister Sadie", "track_number": 5, "side": "B", "duration": "6:19", "session_date": "1959-08-30", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "The Baghdad Blues", "track_number": 6, "side": "B", "duration": "4:52", "session_date": "1959-08-29", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "Melancholy Mood", "track_number": 7, "side": "B", "duration": "7:10", "session_date": "1959-09-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] },
      { "title": "How Did It Happen", "track_number": 8, "side": "B", "duration": "4:41", "session_date": "1959-08-30", "composers": ["Don Newey"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S17"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "f69dc17c-6931-4c28-b5d6-57f55ab372cb",
    "apple_album_id": "1445889621",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/f69dc17c-6931-4c28-b5d6-57f55ab372cb/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Three dates; released November 1959 as Blue Note BLP 4017. Quintet (Aug 29–30): tracks 1, 3, 4, 5, 6, 8. Trio — Silver/Taylor/Hayes (Sep 13): tracks 2 ('The St. Vitus Dance') and 7 ('Melancholy Mood'). Per-track dates from S17. 'How Did It Happen' written by Don Newey; all other tracks by Silver."
  }
}
```

```json
{
  "id": "lou-donaldson-alligator-bogaloo-1967",
  "artist": "Lou Donaldson",
  "album": "Alligator Bogaloo",
  "year": 1967,
  "label": "Blue Note",
  "style_primary": "soul-jazz",
  "style_tags": ["soul-jazz", "hard-bop"],
  "sources": ["S1", "S5", "S18"],
  "epistemic": "obs",
  "rationale": "obs[S1]: named as a soul-jazz anchor album in the project scope doc. obs[S18]: organ-combo boogaloo date (Donaldson with Lonnie Smith on organ, George Benson on guitar, Melvin Lastie on cornet, Leo Morris on drums) led by the hit title track. inf[S5]: a defining late-1960s soul-jazz crossover. scope: funky boogaloo groove but firmly pre-fusion — no rock instrumentation; in per the soul-jazz per-album rule.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1967-04-07"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Lou Donaldson", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S18"], "name_variants": [], "notes": "Leader" },
      { "name": "Melvin Lastie", "instrument": "cornet", "scope": "selected-tracks", "tracks": ["Alligator Bogaloo", "One Cylinder", "The Thang", "Aw Shucks!", "Rev. Moses"], "session_dates": null, "epistemic": "obs", "sources": ["S18"], "name_variants": [], "notes": "Tracks 1–5 per S18; absent on track 6" },
      { "name": "Lonnie Smith", "instrument": "organ", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S18"], "name_variants": ["Dr. Lonnie Smith"], "notes": "Composed 'Aw Shucks!'" },
      { "name": "George Benson", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S18"], "name_variants": [], "notes": "" },
      { "name": "Leo Morris", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S18"], "name_variants": ["Idris Muhammad"], "notes": "Later known as Idris Muhammad" }
    ],
    "tracks": [
      { "title": "Alligator Bogaloo", "track_number": 1, "side": "A", "duration": "6:57", "session_date": "1967-04-07", "composers": ["Lou Donaldson"], "personnel": ["Lou Donaldson", "Melvin Lastie", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] },
      { "title": "One Cylinder", "track_number": 2, "side": "A", "duration": "6:48", "session_date": "1967-04-07", "composers": ["Freddie McCoy"], "personnel": ["Lou Donaldson", "Melvin Lastie", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] },
      { "title": "The Thang", "track_number": 3, "side": "A", "duration": "3:34", "session_date": "1967-04-07", "composers": ["Lou Donaldson"], "personnel": ["Lou Donaldson", "Melvin Lastie", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] },
      { "title": "Aw Shucks!", "track_number": 4, "side": "B", "duration": "7:23", "session_date": "1967-04-07", "composers": ["Lonnie Smith"], "personnel": ["Lou Donaldson", "Melvin Lastie", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] },
      { "title": "Rev. Moses", "track_number": 5, "side": "B", "duration": "6:27", "session_date": "1967-04-07", "composers": ["Lou Donaldson"], "personnel": ["Lou Donaldson", "Melvin Lastie", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] },
      { "title": "I Want a Little Girl", "track_number": 6, "side": "B", "duration": "4:29", "session_date": "1967-04-07", "composers": ["Murray Mencher", "Billy Moll"], "personnel": ["Lou Donaldson", "Lonnie Smith", "George Benson", "Leo Morris"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S18"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "095a43ca-0faf-31fc-8e77-04d114c8532e",
    "apple_album_id": "1443141452",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/095a43ca-0faf-31fc-8e77-04d114c8532e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, April 7 1967; released August 1967 as Blue Note BST 84263. Melvin Lastie (cornet) on tracks 1–5 only — absent on the closing ballad 'I Want a Little Girl'. S18 did not name the engineer; Van Gelder Studio session → Rudy Van Gelder by inference (epistemic_production inf). Drummer Leo Morris is the future Idris Muhammad."
  }
}
```

```json
{
  "id": "jimmy-smith-back-at-the-chicken-shack-1960",
  "artist": "Jimmy Smith",
  "album": "Back at the Chicken Shack",
  "year": 1960,
  "label": "Blue Note",
  "style_primary": "soul-jazz",
  "style_tags": ["soul-jazz", "hard-bop"],
  "sources": ["S5", "S19"],
  "epistemic": "obs",
  "rationale": "obs[S19]: organ-combo date (Smith with Stanley Turrentine, Kenny Burrell on selected tracks, Donald Bailey) — the quintessential greasy organ-jazz session. inf[S5]: a standard soul-jazz reference and one of Smith's most beloved Blue Note dates. scope: gospel-blues organ groove, firmly pre-fusion. priority kept to 'consider' — superb but one of several interchangeable Smith organ dates in a tight canon.",
  "priority": "consider",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-04-25"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Jimmy Smith", "instrument": "organ", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S19"], "name_variants": [], "notes": "Leader" },
      { "name": "Stanley Turrentine", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S19"], "name_variants": [], "notes": "Composed 'Minor Chant'" },
      { "name": "Kenny Burrell", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["Back at the Chicken Shack", "Messy Bessie"], "session_dates": null, "epistemic": "obs", "sources": ["S19"], "name_variants": [], "notes": "S19 lists guitar on tracks 1, 4, 5; track 5 is the CD bonus, so on the original LP Burrell plays tracks 1 and 4" },
      { "name": "Donald Bailey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S19"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Back at the Chicken Shack", "track_number": 1, "side": "A", "duration": "8:01", "session_date": "1960-04-25", "composers": ["Jimmy Smith"], "personnel": ["Jimmy Smith", "Stanley Turrentine", "Kenny Burrell", "Donald Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S19"] },
      { "title": "When I Grow Too Old to Dream", "track_number": 2, "side": "A", "duration": "9:54", "session_date": "1960-04-25", "composers": ["Oscar Hammerstein II", "Sigmund Romberg"], "personnel": ["Jimmy Smith", "Stanley Turrentine", "Donald Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S19"] },
      { "title": "Minor Chant", "track_number": 3, "side": "B", "duration": "7:30", "session_date": "1960-04-25", "composers": ["Stanley Turrentine"], "personnel": ["Jimmy Smith", "Stanley Turrentine", "Donald Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S19"] },
      { "title": "Messy Bessie", "track_number": 4, "side": "B", "duration": "12:25", "session_date": "1960-04-25", "composers": ["Jimmy Smith"], "personnel": ["Jimmy Smith", "Stanley Turrentine", "Kenny Burrell", "Donald Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S19"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "10bb15b0-2d55-369a-90c3-a5131406ac9e",
    "apple_album_id": "724622238",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/10bb15b0-2d55-369a-90c3-a5131406ac9e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, April 25 1960; released 1963 (Feb 12) as Blue Note BLP 4117 / BST 84117. Original LP is 4 tracks; CD reissue (1987) adds 'On the Sunny Side of the Street' (5:45) with Burrell — excluded here as a reissue-only bonus. Burrell appears on tracks 1 and 4 of the LP (S19 cites tracks 1, 4, 5 across LP+bonus). apple_album_id is the Rudy Van Gelder Edition."
  }
}
```

```json
{
  "id": "gene-ammons-boss-tenor-1960",
  "artist": "Gene Ammons",
  "album": "Boss Tenor",
  "year": 1960,
  "label": "Prestige",
  "style_primary": "soul-jazz",
  "style_tags": ["soul-jazz", "hard-bop"],
  "sources": ["S5", "S20"],
  "epistemic": "obs",
  "rationale": "obs[S20]: soulful tenor date (Ammons with Tommy Flanagan, Doug Watkins, Art Taylor, Ray Barretto on congas), blending blues originals and ballads. inf[S5]: a representative Prestige soul-jazz/'soul tenor' statement, filling a label and stylistic gap (Prestige, non-organ soul jazz). priority 'consider' — excellent but a notch below the consensus pillars and lighter-sourced.",
  "priority": "consider",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-06-16"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Bob Weinstock",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Gene Ammons", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S20"], "name_variants": [], "notes": "Leader" },
      { "name": "Tommy Flanagan", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S20"], "name_variants": [], "notes": "" },
      { "name": "Doug Watkins", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S20"], "name_variants": [], "notes": "" },
      { "name": "Art Taylor", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S20"], "name_variants": [], "notes": "" },
      { "name": "Ray Barretto", "instrument": "congas", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S20"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Hittin' the Jug", "track_number": 1, "side": "A", "duration": "8:29", "session_date": "1960-06-16", "composers": ["Gene Ammons"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "Close Your Eyes", "track_number": 2, "side": "A", "duration": "3:46", "session_date": "1960-06-16", "composers": ["Bernice Petkere"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "My Romance", "track_number": 3, "side": "A", "duration": "4:16", "session_date": "1960-06-16", "composers": ["Lorenz Hart", "Richard Rodgers"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "Canadian Sunset", "track_number": 4, "side": "B", "duration": "5:24", "session_date": "1960-06-16", "composers": ["Norman Gimbel", "Eddie Heywood"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "Blue Ammons", "track_number": 5, "side": "B", "duration": "4:57", "session_date": "1960-06-16", "composers": ["Gene Ammons"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "Confirmation", "track_number": 6, "side": "B", "duration": "5:24", "session_date": "1960-06-16", "composers": ["Charlie Parker"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] },
      { "title": "Stompin' at the Savoy", "track_number": 7, "side": "B", "duration": "3:31", "session_date": "1960-06-16", "composers": ["Benny Goodman", "Edgar Sampson", "Chick Webb", "Andy Razaf"], "personnel": ["Gene Ammons", "Tommy Flanagan", "Doug Watkins", "Art Taylor", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S20"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "83154955-d843-3265-a23e-96244ff7f409",
    "apple_album_id": "1440943402",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/83154955-d843-3265-a23e-96244ff7f409/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, June 16 1960; released 1960 as Prestige PRLP 7180. S20 did not name the engineer; Prestige session at Van Gelder Studio, Englewood Cliffs → Rudy Van Gelder by inference (epistemic_production inf). Producer Bob Weinstock and studio directly sourced. 'Stompin' at the Savoy' co-composer printed as Edgar Sampson (S20 rendered 'Arthur Sampson'). apple_album_id is the Rudy Van Gelder remaster edition. Whole band on every track."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves
- **Sonny Rollins — *Saxophone Colossus* (1956):** The definitive Rollins studio quartet — "St. Thomas" and the landmark "Blue 7"; an undisputed hard-bop pillar.
- **Cannonball Adderley — *Somethin' Else* (1958):** Adderley leading, but with Miles Davis on trumpet and a 10-minute "Autumn Leaves"; a marquee Blue Note classic.
- **Clifford Brown & Max Roach — *Study in Brown* (1955):** Foundational early hard bop; the trumpet-tenor quintet template the whole idiom built on.
- **Wes Montgomery — *The Incredible Jazz Guitar of Wes Montgomery* (1960):** The guitar reference point of the era; fills the canon's guitar gap with "Four on Six" and "West Coast Blues."

### Hidden Gems
- **Kenny Dorham — *Una Mas* (1963):** Underplayed next to the marquee Blue Notes, but the long Latin title track and a 17-year-old Tony Williams make it special.
- **Jackie McLean — *Let Freedom Ring* (1962):** McLean reaching toward the avant-garde while still swinging hard — a pivotal, under-cited record.

### Consensus Picks (3+ sources)
- None this round reach 3+ *independent* sources for canon judgment: each rests on its dedicated Wikipedia article (obs) plus the Penguin Guide as general critical reference (inf), with *Alligator Bogaloo* additionally named in the project scope doc (S1). The selections are consensus-strong by reputation rather than by source count within this file; deeper best-of-list corroboration is the natural next pass.

### Single-Source Picks
- Every record's *personnel* layer rests on a single rich Wikipedia article (acceptable per the contract when complete), cross-checked against iTunes (S2) and MusicBrainz (S3) for reference IDs. The lightest canon-judgment cases are the two soul-jazz "consider" picks — *Back at the Chicken Shack* and *Boss Tenor* — each carried by one dedicated article plus the Penguin Guide.

### Scope Calls
- ***Let Freedom Ring***: tagged hard-bop/post-bop for its early new-thing influence, but it still swings with structure (in per the post-bop fuzzy edge) — not free jazz.
- ***Alligator Bogaloo*** (1967): boogaloo groove and a hit single, but pure organ-combo soul jazz with no rock instrumentation — pre-fusion, and a project-named soul-jazz anchor; in.
- ***Back at the Chicken Shack*** and ***Boss Tenor***: gospel-blues / "soul tenor" grooves, firmly pre-fusion; in per the per-album soul-jazz rule.
- ***Grant Green — Idle Moments*** and ***Horace Silver — Blowin' the Blues Away***: tagged hard-bop/soul-jazz border for their groove content, but both swing with structure — comfortably in.

### Gaps Noticed
- **Label skew:** 12 of 15 are Blue Note (the core hard-bop label, so defensible), with 2 Prestige (*Saxophone Colossus*, *Boss Tenor*) and 1 Riverside/EmArcy each. Riverside (Cannonball's own dates, Bill Evans-adjacent hard bop), Columbia, and Impulse! remain thin.
- **Cannonball Adderley** is represented only as a Blue Note sideman-led date; his Riverside/Capitol quintet records (*Mercy, Mercy, Mercy!*, *At the Lighthouse*) are unaddressed.
- **Organ soul jazz beyond Jimmy Smith** (Brother Jack McDuff, Jimmy McGriff, "Big" John Patton) and **Prestige tenor soul jazz** (Stanley Turrentine as leader, Eddie "Lockjaw" Davis) are barely touched.
- **Early/mid-1950s hard bop** beyond *Study in Brown* (Clifford Brown & Max Roach at Basin Street, early Horace Silver/Jazz Messengers, Miles Davis Prestige quintet) is still underrepresented.
- **Critical sourcing depth:** this round leaned on Wikipedia + Penguin Guide; a pass against DownBeat, AllMusic editor picks, and "essential Blue Note" features would raise the consensus-count on these picks.

### Personnel Coverage
- **Full track assignments reached (15/15):** every record carries `track_assignments_complete: true`. The single-session quartets/quintets (Saxophone Colossus, Somethin' Else, Cool Struttin', Let Freedom Ring, Go, Page One, Una Mas, Boss Tenor) are whole-band on every track. The multi-session and split-ensemble dates were each cleanly mapped: *Blowin' the Blues Away* (quintet vs. Silver/Taylor/Hayes trio, per-track dates from S17), *Idle Moments* (same sextet across both Nov 1963 dates, per-track dates from S14), *Alligator Bogaloo* (Lastie on tracks 1–5 only), and *Back at the Chicken Shack* (Burrell on the original LP's tracks 1 and 4).
- **Production inference:** six Blue Note/Prestige dates (Let Freedom Ring, Ready for Freddie, Una Mas, Idle Moments, Alligator Bogaloo, Boss Tenor) did not name the engineer in their Wikipedia infobox; all are confirmed Van Gelder Studio sessions, so Rudy Van Gelder is credited by inference with `epistemic_production: inf` and a note. The other nine name RVG (or, for Study in Brown, a non-Van-Gelder studio) directly.
- **Production gap:** *Study in Brown* (Capitol Studios, NYC) has no documented producer or engineer in S8 — explicit nulls, `epistemic_production: unk`.
- **Taxonomy escape:** *Ready for Freddie* features Bernard McKinney on euphonium, which has no exact taxonomy string — recorded as `"euphonium"` and flagged per the contract's escape clause.
- **Track-status cautions:** reissue-only bonuses/alternates were excluded by default but noted (Cool Struttin', Back at the Chicken Shack, Ready for Freddie alternates); same-session non-LP tracks were flagged `bonus_track: true` (Somethin' Else "Bangoon," Una Mas "If Ever I Would Leave You"); *Study in Brown*'s "Take the 'A' Train" carries `epistemic_track: unk` pending verification of its original-LP status.
- **Layer 5 references:** all 15 carry a verified MusicBrainz release-group MBID and an iTunes `collectionId` (four are remaster-edition IDs where no plain-original surfaced — noted per record). Cover-art URLs are constructed from the MBID at `epistemic: inf` — references for a later ingest step, not verified images.
```