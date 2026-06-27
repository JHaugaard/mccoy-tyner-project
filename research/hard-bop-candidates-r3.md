# Hard Bop / Soul Jazz Candidates — Round 3 (final push toward 100)

Dispatch: 15 genuinely-new hard-bop/soul-jazz candidate records, full personnel/session/track data in one pass.
Recording year locked as `year`; release year noted where it differs. `include: null` on every record.
Generated 2026-06-23. None of these 15 appears in the 60-album exclusion list (15 collected + 45 pending).

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Penguin Guide to Jazz (Cook & Morton) | Book | — | Core critical reference for canon standing; ratings cited from established critical record (not page-fetched this run → `inf`). |
| S2 | AllMusic | Website | allmusic.com | Editor ratings / genre standing; cited from established critical record this run (not page-fetched → `inf`). |
| S3 | Wikipedia album articles | Website | en.wikipedia.org (per-album) | Personnel, recording dates, studio, production credits, track listings. Cites original liner notes. Primary `obs` source for all personnel facts. |
| S4 | iTunes Search/Lookup API | API | itunes.apple.com/search | Apple Music `collectionId` (→ `apple_album_id`). Queried live this run. |
| S5 | Personnel Record Contract — Van Gelder inference rule | Project doc | docs/personnel-contract.md | Basis for `inf` engineer = Rudy Van Gelder on undocumented Blue Note / Van Gelder Studio sessions. |

Note on Layer 5: MusicBrainz web service (musicbrainz.org/ws/2) returned a certificate-verification error on every attempt this run, so `musicbrainz_release_group_mbid` is `null` and `cover_art` is `[]` for all 15 — not fabricated. Apple IDs (S4) were captured successfully for all 15.

---

## 2. Candidate Records

```json
{
  "id": "john-coltrane-blue-train-1957",
  "artist": "John Coltrane",
  "album": "Blue Train",
  "year": 1957,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the September 15, 1957 sextet date, full personnel and tracks; Coltrane's only Blue Note session as leader. inf[S1][S2]: long-established Penguin core-collection / AllMusic 5-star pillar of the hard-bop canon. A foundational hard-bop statement absent from the collection and pending lists.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-09-15"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Coltrane", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Curtis Fuller", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Kenny Drew", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Blue Train", "track_number": 1, "side": "A", "duration": "10:43", "session_date": "1957-09-15", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Lee Morgan", "Curtis Fuller", "Kenny Drew", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Moment's Notice", "track_number": 2, "side": "A", "duration": "9:10", "session_date": "1957-09-15", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Lee Morgan", "Curtis Fuller", "Kenny Drew", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Locomotion", "track_number": 3, "side": "B", "duration": "7:14", "session_date": "1957-09-15", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Lee Morgan", "Curtis Fuller", "Kenny Drew", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "I'm Old Fashioned", "track_number": 4, "side": "B", "duration": "7:58", "session_date": "1957-09-15", "composers": ["Johnny Mercer", "Jerome Kern"], "personnel": ["John Coltrane", "Lee Morgan", "Curtis Fuller", "Kenny Drew", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Lazy Bird", "track_number": 5, "side": "B", "duration": "7:00", "session_date": "1957-09-15", "composers": ["John Coltrane"], "personnel": ["John Coltrane", "Lee Morgan", "Curtis Fuller", "Kenny Drew", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1468202477",
    "cover_art": [],
    "notes": "Single session. Released January 1958. Per-track personnel marked inf: sources confirm a fixed sextet across the date but do not break out personnel per title (uniform participation inferred). Apple ID 1468202477 = original 'Blue Train'."
  }
}
```

```json
{
  "id": "sonny-rollins-way-out-west-1957",
  "artist": "Sonny Rollins",
  "album": "Way Out West",
  "year": 1957,
  "label": "Contemporary",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the March 7, 1957 pianoless-trio date with Ray Brown and Shelly Manne. inf[S1][S2]: established Penguin core-collection / AllMusic top-tier Rollins date. A pillar of the saxophone-trio idiom not in the collection (Saxophone Colossus is excluded; this is a distinct, equally canonical Rollins record).",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "Pianoless trio recorded in Los Angeles; still swings with structure, firmly post-bop and pre-fusion — in scope.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-03-07"],
    "multi_session": false,
    "studio": "Contemporary Records studio, Los Angeles",
    "producer": "Lester Koenig",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Sonny Rollins", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Ray Brown", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "I'm an Old Cowhand (From the Rio Grande)", "track_number": 1, "side": "A", "duration": "5:42", "session_date": "1957-03-07", "composers": ["Johnny Mercer"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Solitude", "track_number": 2, "side": "A", "duration": "7:52", "session_date": "1957-03-07", "composers": ["Duke Ellington", "Eddie DeLange", "Irving Mills"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Come, Gone", "track_number": 3, "side": "A", "duration": "7:53", "session_date": "1957-03-07", "composers": ["Sonny Rollins"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Wagon Wheels", "track_number": 4, "side": "B", "duration": "10:11", "session_date": "1957-03-07", "composers": ["Peter DeRose", "Billy Hill"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "There Is No Greater Love", "track_number": 5, "side": "B", "duration": "5:17", "session_date": "1957-03-07", "composers": ["Isham Jones", "Marty Symes"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Way Out West", "track_number": 6, "side": "B", "duration": "6:30", "session_date": "1957-03-07", "composers": ["Sonny Rollins"], "personnel": ["Sonny Rollins", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1440789922",
    "cover_art": [],
    "notes": "Single trio session — all three musicians on every track, so track_assignments_complete is true. Engineer not credited by S3; Contemporary dates of this era were typically engineered by Roy DuNann (inf, not asserted). CD reissues add three alternate takes (excluded here as reissue-only)."
  }
}
```

```json
{
  "id": "clifford-brown-clifford-brown-and-max-roach-1954",
  "artist": "Clifford Brown & Max Roach",
  "album": "Clifford Brown and Max Roach",
  "year": 1954,
  "label": "EmArcy",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the quintet (Brown/Land/Powell/Morrow/Roach) and the August 1954 / February 1955 Hollywood sessions, including 'Joy Spring' and 'Daahoud'. inf[S1][S2]: established Penguin core-collection / AllMusic landmark — the definitive Brown–Roach quintet statement and a hard-bop cornerstone. Distinct from the excluded 'Study in Brown'.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-08-02/1954-08-06", "1955-02-24/1955-02-25"],
    "multi_session": true,
    "studio": "Capitol Studios, Hollywood",
    "producer": "Bob Shad",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Clifford Brown", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Harold Land", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Richie Powell", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "George Morrow", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Max Roach", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Delilah", "track_number": 1, "side": "A", "duration": "8:03", "session_date": null, "composers": ["Victor Young"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Parisian Thoroughfare", "track_number": 2, "side": "A", "duration": "7:16", "session_date": null, "composers": ["Bud Powell"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "The Blues Walk", "track_number": 3, "side": "A", "duration": "6:53", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Daahoud", "track_number": 4, "side": "B", "duration": "4:01", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Joy Spring", "track_number": 5, "side": "B", "duration": "6:48", "session_date": null, "composers": ["Clifford Brown"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Jordu", "track_number": 6, "side": "B", "duration": "4:00", "session_date": null, "composers": ["Duke Jordan"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "What Am I Here For?", "track_number": 7, "side": "B", "duration": "3:04", "session_date": "1955-02-24/1955-02-25", "composers": ["Duke Ellington"], "personnel": ["Clifford Brown", "Harold Land", "Richie Powell", "George Morrow", "Max Roach"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1868798541",
    "cover_art": [],
    "notes": "year=1954 (core August 1954 sessions). The 12-inch LP (MG-36036, 1955) added 'What Am I Here For?' from the February 1955 date — assigned the 1955 session_date (inf). S3 gives aggregate session ranges, not per-title dates, so per-track session attribution beyond track 7 is left null and track_assignments_complete is false."
  }
}
```

```json
{
  "id": "art-blakey-a-night-at-birdland-vol-1-1954",
  "artist": "Art Blakey Quintet",
  "album": "A Night at Birdland, Vol. 1",
  "year": 1954,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the February 21, 1954 live Birdland date with Clifford Brown, Lou Donaldson, Horace Silver, Curley Russell and Blakey. inf[S1][S2]: widely cited as one of the foundational live recordings of the emerging hard-bop style and a Penguin/AllMusic-acknowledged landmark. Pre-Jazz Messengers Blakey, distinct from the excluded 'Moanin''.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "Recorded 1954 — at the leading edge of hard bop; the Test Question (swings with structure, post-bebop) is clearly met.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-02-21"],
    "multi_session": false,
    "studio": "Birdland (live), New York City",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Clifford Brown", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Lou Donaldson", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Horace Silver", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Curley Russell", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Announcement by Pee Wee Marquette", "track_number": 1, "side": null, "duration": "0:58", "session_date": "1954-02-21", "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Split Kick", "track_number": 2, "side": null, "duration": "8:44", "session_date": "1954-02-21", "composers": ["Horace Silver"], "personnel": ["Clifford Brown", "Lou Donaldson", "Horace Silver", "Curley Russell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Once in a While", "track_number": 3, "side": null, "duration": "5:18", "session_date": "1954-02-21", "composers": ["Bud Green", "Michael Edwards"], "personnel": ["Clifford Brown", "Lou Donaldson", "Horace Silver", "Curley Russell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Quicksilver", "track_number": 4, "side": null, "duration": "6:58", "session_date": "1954-02-21", "composers": ["Horace Silver"], "personnel": ["Clifford Brown", "Lou Donaldson", "Horace Silver", "Curley Russell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "A Night in Tunisia", "track_number": 5, "side": null, "duration": "9:20", "session_date": "1954-02-21", "composers": ["Dizzy Gillespie", "Frank Paparelli"], "personnel": ["Clifford Brown", "Lou Donaldson", "Horace Silver", "Curley Russell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Mayreh", "track_number": 6, "side": null, "duration": "6:19", "session_date": "1954-02-21", "composers": ["Horace Silver"], "personnel": ["Clifford Brown", "Lou Donaldson", "Horace Silver", "Curley Russell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443211091",
    "cover_art": [],
    "notes": "Live single-night recording; released August 1956 as Vol. 1. Track 1 is Pee Wee Marquette's spoken introduction (no musical personnel). Sides not meaningfully distinguished for the live LP (set to null). Per-track personnel inferred uniform across the set."
  }
}
```

```json
{
  "id": "horace-silver-horace-silver-and-the-jazz-messengers-1954",
  "artist": "Horace Silver",
  "album": "Horace Silver and the Jazz Messengers",
  "year": 1954,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the November 13, 1954 and February 6, 1955 sessions, the Silver/Dorham/Mobley/Watkins/Blakey quintet, and per-track recording dates including 'The Preacher' and 'Doodlin''. inf[S1][S2]: frequently cited as the record that codified the hard-bop template — gospel/blues phrasing over bop structure. A genesis document of the genre.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-11-13", "1955-02-06"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Horace Silver", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-11-13", "1955-02-06"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Kenny Dorham", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-11-13", "1955-02-06"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Hank Mobley", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-11-13", "1955-02-06"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Doug Watkins", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-11-13", "1955-02-06"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-11-13", "1955-02-06"], "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Room 608", "track_number": 1, "side": "A", "duration": "5:22", "session_date": "1954-11-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Creepin' In", "track_number": 2, "side": "A", "duration": "7:26", "session_date": "1954-11-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Stop Time", "track_number": 3, "side": "A", "duration": "4:07", "session_date": "1954-11-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "To Whom It May Concern", "track_number": 4, "side": "A", "duration": "5:11", "session_date": "1955-02-06", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Hippy", "track_number": 5, "side": "B", "duration": "5:23", "session_date": "1955-02-06", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "The Preacher", "track_number": 6, "side": "B", "duration": "4:18", "session_date": "1955-02-06", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Hankerin'", "track_number": 7, "side": "B", "duration": "5:18", "session_date": "1955-02-06", "composers": ["Hank Mobley"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Doodlin'", "track_number": 8, "side": "B", "duration": "6:45", "session_date": "1954-11-13", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Kenny Dorham", "Hank Mobley", "Doug Watkins", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444052680",
    "cover_art": [],
    "notes": "year=1954 (first session). Released October 1956 (BLP 1518). Same quintet on both dates; S3 gives per-track recording dates (obs), so session distribution is fully resolved and track_assignments_complete is true. Nov 13, 1954: tracks 1,2,3,8. Feb 6, 1955: tracks 4,5,6,7."
  }
}
```

```json
{
  "id": "lee-morgan-the-cooker-1957",
  "artist": "Lee Morgan",
  "album": "The Cooker",
  "year": 1957,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the September 29, 1957 quintet with Pepper Adams, Bobby Timmons, Paul Chambers and Philly Joe Jones. inf[S1][S2]: a well-regarded hot Blue Note Morgan date (the muscular 'A Night in Tunisia' is a standout). Distinct from the excluded 'The Sidewinder'.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-09-29"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Pepper Adams", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Bobby Timmons", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "A Night in Tunisia", "track_number": 1, "side": "A", "duration": "9:24", "session_date": "1957-09-29", "composers": ["Dizzy Gillespie", "Frank Paparelli"], "personnel": ["Lee Morgan", "Pepper Adams", "Bobby Timmons", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Heavy Dipper", "track_number": 2, "side": "A", "duration": "7:05", "session_date": "1957-09-29", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Pepper Adams", "Bobby Timmons", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Just One of Those Things", "track_number": 3, "side": "B", "duration": "7:18", "session_date": "1957-09-29", "composers": ["Cole Porter"], "personnel": ["Lee Morgan", "Pepper Adams", "Bobby Timmons", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Lover Man", "track_number": 4, "side": "B", "duration": "6:50", "session_date": "1957-09-29", "composers": ["Jimmy Davis", "Roger Ramirez", "Jimmy Sherman"], "personnel": ["Lee Morgan", "Pepper Adams", "Bobby Timmons", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "New-Ma", "track_number": 5, "side": "B", "duration": "8:14", "session_date": "1957-09-29", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Pepper Adams", "Bobby Timmons", "Paul Chambers", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443237724",
    "cover_art": [],
    "notes": "Single session; released January 1958 (BLP 1578). CD reissue adds an alternate take of 'Just One of Those Things' (excluded here). Per-track personnel inferred uniform across the date."
  }
}
```

```json
{
  "id": "hank-mobley-roll-call-1960",
  "artist": "Hank Mobley",
  "album": "Roll Call",
  "year": 1960,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the November 13, 1960 date with Freddie Hubbard, Wynton Kelly, Paul Chambers and Art Blakey. inf[S1][S2]: a strong Mobley Blue Note date from his peak period, the immediate follow-up to the excluded 'Soul Station' with the same rhythm core plus Hubbard.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-11-13"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Hank Mobley", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Wynton Kelly", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Roll Call", "track_number": 1, "side": "A", "duration": "10:33", "session_date": "1960-11-13", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "My Groove Your Move", "track_number": 2, "side": "A", "duration": "6:07", "session_date": "1960-11-13", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Take Your Pick", "track_number": 3, "side": "A", "duration": "5:27", "session_date": "1960-11-13", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "A Baptist Beat", "track_number": 4, "side": "B", "duration": "8:54", "session_date": "1960-11-13", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "The More I See You", "track_number": 5, "side": "B", "duration": "6:47", "session_date": "1960-11-13", "composers": ["Harry Warren", "Mack Gordon"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "The Breakdown", "track_number": 6, "side": "B", "duration": "4:57", "session_date": "1960-11-13", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Freddie Hubbard", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "724670579",
    "cover_art": [],
    "notes": "Single session; released mid-1961 (BST 84058). Engineer = Rudy Van Gelder by inference (Blue Note date at Van Gelder Studio; S3 did not list the engineer), per docs/personnel-contract.md Van Gelder rule → epistemic_production inf. CD reissue adds an alternate of 'A Baptist Beat' (excluded). Apple ID is the Rudy Van Gelder Edition reissue (collectionId 724670579)."
  }
}
```

```json
{
  "id": "jackie-mclean-bluesnik-1961",
  "artist": "Jackie McLean",
  "album": "Bluesnik",
  "year": 1961,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the January 8, 1961 blues-themed date with Freddie Hubbard, Kenny Drew, Doug Watkins and Pete La Roca. inf[S1][S2]: a focused, well-regarded McLean blues program — distinct from the excluded 'Let Freedom Ring'. Slightly lighter critical footprint, hence 'consider'.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-01-08"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Jackie McLean", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Kenny Drew", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Doug Watkins", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Pete La Roca", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Bluesnik", "track_number": 1, "side": "A", "duration": "9:36", "session_date": "1961-01-08", "composers": ["Jackie McLean"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Goin' 'Way Blues", "track_number": 2, "side": "A", "duration": "6:34", "session_date": "1961-01-08", "composers": ["Jackie McLean"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Drew's Blues", "track_number": 3, "side": "A", "duration": "5:52", "session_date": "1961-01-08", "composers": ["Kenny Drew"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Cool Green", "track_number": 4, "side": "B", "duration": "5:20", "session_date": "1961-01-08", "composers": ["Kenny Drew"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Blues Function", "track_number": 5, "side": "B", "duration": "7:19", "session_date": "1961-01-08", "composers": ["Freddie Hubbard"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Torchin'", "track_number": 6, "side": "B", "duration": "6:11", "session_date": "1961-01-08", "composers": ["Kenny Drew"], "personnel": ["Jackie McLean", "Freddie Hubbard", "Kenny Drew", "Doug Watkins", "Pete La Roca"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "715853834",
    "cover_art": [],
    "notes": "Single session; released February 1962 (BLP 4067). Engineer = Rudy Van Gelder by inference (Van Gelder Studio Blue Note date; S3 omitted engineer) per the Van Gelder rule → epistemic_production inf. CD reissue adds alternates of 'Goin' 'Way Blues' and 'Torchin'' (excluded). Apple ID is the Rudy Van Gelder Edition."
  }
}
```

```json
{
  "id": "freddie-hubbard-hub-tones-1962",
  "artist": "Freddie Hubbard",
  "album": "Hub-Tones",
  "year": 1962,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the October 10, 1962 date with James Spaulding, Herbie Hancock, Reggie Workman and Clifford Jarvis; 'Lament for Booker' memorializes Booker Little. inf[S1][S2]: a strong, slightly adventurous Hubbard Blue Note date — distinct from the excluded 'Ready for Freddie'.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1962-10-10"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "James Spaulding", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Also plays flute on the session (S3)." },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Reggie Workman", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Clifford Jarvis", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "You're My Everything", "track_number": 1, "side": "A", "duration": "6:33", "session_date": "1962-10-10", "composers": ["Mort Dixon", "Harry Warren", "Joe Young"], "personnel": ["Freddie Hubbard", "James Spaulding", "Herbie Hancock", "Reggie Workman", "Clifford Jarvis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Prophet Jennings", "track_number": 2, "side": "A", "duration": "5:31", "session_date": "1962-10-10", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "James Spaulding", "Herbie Hancock", "Reggie Workman", "Clifford Jarvis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Hub-Tones", "track_number": 3, "side": "A", "duration": "8:24", "session_date": "1962-10-10", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "James Spaulding", "Herbie Hancock", "Reggie Workman", "Clifford Jarvis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Lament for Booker", "track_number": 4, "side": "B", "duration": "9:39", "session_date": "1962-10-10", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "James Spaulding", "Herbie Hancock", "Reggie Workman", "Clifford Jarvis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "For Spee's Sake", "track_number": 5, "side": "B", "duration": "8:35", "session_date": "1962-10-10", "composers": ["Freddie Hubbard"], "personnel": ["Freddie Hubbard", "James Spaulding", "Herbie Hancock", "Reggie Workman", "Clifford Jarvis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1444188559",
    "cover_art": [],
    "notes": "Single session; released November 1963 (BLP 4115 / BST 84115). Spaulding doubles alto saxophone and flute (instrument string = alto saxophone, doubling noted). Engineer = Rudy Van Gelder by inference (Van Gelder Studio Blue Note date) per the Van Gelder rule → epistemic_production inf. CD reissue adds three alternates (excluded)."
  }
}
```

```json
{
  "id": "dexter-gordon-our-man-in-paris-1963",
  "artist": "Dexter Gordon",
  "album": "Our Man in Paris",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the May 23, 1963 Paris date with Bud Powell, Pierre Michelot and Kenny Clarke. inf[S1][S2]: a celebrated expatriate Gordon date — bebop repertoire delivered with hard-bop heft. Distinct from the excluded 'Go'.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "Repertoire is bebop standards, but the 1963 performance swings with hard-bop weight and structure — comfortably in scope.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-05-23"],
    "multi_session": false,
    "studio": "CBS Studios, Paris",
    "producer": "Francis Wolff",
    "engineer": "Claude Ermelin",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Dexter Gordon", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Bud Powell", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Pierre Michelot", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Kenny Clarke", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Scrapple from the Apple", "track_number": 1, "side": "A", "duration": "7:22", "session_date": "1963-05-23", "composers": ["Charlie Parker"], "personnel": ["Dexter Gordon", "Bud Powell", "Pierre Michelot", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Willow Weep for Me", "track_number": 2, "side": "A", "duration": "8:47", "session_date": "1963-05-23", "composers": ["Ann Ronell"], "personnel": ["Dexter Gordon", "Bud Powell", "Pierre Michelot", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Broadway", "track_number": 3, "side": "A", "duration": "6:44", "session_date": "1963-05-23", "composers": ["Bill Bird", "Teddy McRae", "Henri Woode"], "personnel": ["Dexter Gordon", "Bud Powell", "Pierre Michelot", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Stairway to the Stars", "track_number": 4, "side": "B", "duration": "6:57", "session_date": "1963-05-23", "composers": ["Matty Malneck", "Mitchell Parish", "Frank Signorelli"], "personnel": ["Dexter Gordon", "Bud Powell", "Pierre Michelot", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "A Night in Tunisia", "track_number": 5, "side": "B", "duration": "8:15", "session_date": "1963-05-23", "composers": ["Dizzy Gillespie", "Frank Paparelli"], "personnel": ["Dexter Gordon", "Bud Powell", "Pierre Michelot", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1442835524",
    "cover_art": [],
    "notes": "Single session; released December 1963 (BLP 4146). Engineer Claude Ermelin (recording); Ron McMaster did the later digital transfer. CD reissue adds two bonus tracks including 'Like Someone in Love', a Bud Powell trio feature without Gordon — excluded here; the five original LP tracks all feature the full quartet."
  }
}
```

```json
{
  "id": "kenny-burrell-midnight-blue-1963",
  "artist": "Kenny Burrell",
  "album": "Midnight Blue",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "soul-jazz",
  "style_tags": ["soul-jazz", "hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the January 8, 1963 date with Stanley Turrentine, Major Holley, Bill English and Ray Barretto on congas, and the per-track instrumentation. inf[S1][S2]: a widely-loved bluesy guitar/tenor date ('Chitlins con Carne') — a model soul-jazz-meets-hard-bop record. Firmly pre-fusion.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "Bluesy, groove-based with congas, but acoustic and pre-fusion — in scope per the soul-jazz per-album rule.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-01-08"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Kenny Burrell", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Stanley Turrentine", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Chitlins con Carne", "Mule", "Wavy Gravy", "Saturday Night Blues", "Kenny's Sound"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "S3: present on all tracks except 'Soul Lament', 'Midnight Blue', 'Gee, Baby, Ain't I Good to You' and 'K Twist'." },
      { "name": "Major Holley", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Chitlins con Carne", "Mule", "Midnight Blue", "Wavy Gravy", "Gee, Baby, Ain't I Good to You", "Saturday Night Blues", "Kenny's Sound", "K Twist"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": ["Major Holley Jr."], "notes": "S3: on all tracks except 'Soul Lament' (solo guitar)." },
      { "name": "Bill English", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Chitlins con Carne", "Mule", "Midnight Blue", "Wavy Gravy", "Gee, Baby, Ain't I Good to You", "Saturday Night Blues", "Kenny's Sound", "K Twist"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "S3: on all tracks except 'Soul Lament'." },
      { "name": "Ray Barretto", "instrument": "congas", "scope": "selected-tracks", "tracks": ["Chitlins con Carne", "Mule", "Midnight Blue", "Wavy Gravy", "Saturday Night Blues", "Kenny's Sound", "K Twist"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "S3: on all tracks except 'Soul Lament' and 'Gee, Baby, Ain't I Good to You'." }
    ],
    "tracks": [
      { "title": "Chitlins con Carne", "track_number": 1, "side": "A", "duration": "5:30", "session_date": "1963-01-08", "composers": ["Kenny Burrell"], "personnel": ["Kenny Burrell", "Stanley Turrentine", "Major Holley", "Bill English", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Mule", "track_number": 2, "side": "A", "duration": "6:56", "session_date": "1963-01-08", "composers": ["Kenny Burrell", "Major Holley"], "personnel": ["Kenny Burrell", "Stanley Turrentine", "Major Holley", "Bill English", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Soul Lament", "track_number": 3, "side": "A", "duration": "2:43", "session_date": "1963-01-08", "composers": ["Kenny Burrell"], "personnel": ["Kenny Burrell"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Midnight Blue", "track_number": 4, "side": "A", "duration": "4:02", "session_date": "1963-01-08", "composers": ["Kenny Burrell"], "personnel": ["Kenny Burrell", "Major Holley", "Bill English", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Wavy Gravy", "track_number": 5, "side": "B", "duration": "5:47", "session_date": "1963-01-08", "composers": ["Kenny Burrell"], "personnel": ["Kenny Burrell", "Stanley Turrentine", "Major Holley", "Bill English", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Gee, Baby, Ain't I Good to You", "track_number": 6, "side": "B", "duration": "4:25", "session_date": "1963-01-08", "composers": ["Andy Razaf", "Don Redman"], "personnel": ["Kenny Burrell", "Major Holley", "Bill English"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Saturday Night Blues", "track_number": 7, "side": "B", "duration": "6:16", "session_date": "1963-01-08", "composers": ["Kenny Burrell"], "personnel": ["Kenny Burrell", "Stanley Turrentine", "Major Holley", "Bill English", "Ray Barretto"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "724536844",
    "cover_art": [],
    "notes": "Single session; released early May 1963 (BLP 4123 / BST 84123). Per-track instrumentation explicitly documented by S3 (obs). 'Soul Lament' is solo Burrell; 'Midnight Blue' drops Turrentine; 'Gee, Baby' drops Turrentine and Barretto. Tracks 8–9 ('Kenny's Sound', 'K Twist') are CD bonus tracks — excluded from the original-LP track list above but reflected in the per-musician scope. track_assignments_complete left false because bonus-track coverage is not fully reconciled. Apple ID is the Rudy Van Gelder Edition."
  }
}
```

```json
{
  "id": "donald-byrd-a-new-perspective-1963",
  "artist": "Donald Byrd",
  "album": "A New Perspective",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the January 12, 1963 date with Hank Mobley, Herbie Hancock, Kenny Burrell, Butch Warren, Lex Humphries, vibraphonist/vocalist Donald Best, Duke Pearson's arrangements and an eight-voice gospel choir; 'Cristo Redentor' is the centerpiece. inf[S1][S2]: a distinctive gospel-jazz crossover. Lighter as a straight hard-bop pick, hence 'consider'.",
  "priority": "consider",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "Gospel choir and sacred-jazz mood, but acoustic and pre-fusion — in scope; the choir is an arrangement color over a hard-bop rhythm section.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-01-12"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Donald Byrd", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Hank Mobley", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Herbie Hancock", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Kenny Burrell", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Donald Best", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Also credited with vocals (part of/with the choir)." },
      { "name": "Butch Warren", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Lex Humphries", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Vocal choir (8 voices)", "instrument": "vocals", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Wordless gospel choir — two basses, two tenors, two altos, two sopranos; directed by Coleridge-Taylor Perkinson. Individual singers unnamed in S3. Most prominent on 'Cristo Redentor' and 'Chant'." }
    ],
    "tracks": [
      { "title": "Elijah", "track_number": 1, "side": "A", "duration": "9:21", "session_date": "1963-01-12", "composers": ["Donald Byrd"], "personnel": ["Donald Byrd", "Hank Mobley", "Herbie Hancock", "Kenny Burrell", "Donald Best", "Butch Warren", "Lex Humphries", "Vocal choir (8 voices)"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Beast of Burden", "track_number": 2, "side": "A", "duration": "10:07", "session_date": "1963-01-12", "composers": ["Donald Byrd"], "personnel": ["Donald Byrd", "Hank Mobley", "Herbie Hancock", "Kenny Burrell", "Donald Best", "Butch Warren", "Lex Humphries", "Vocal choir (8 voices)"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Cristo Redentor", "track_number": 3, "side": "B", "duration": "5:43", "session_date": "1963-01-12", "composers": ["Duke Pearson"], "personnel": ["Donald Byrd", "Hank Mobley", "Herbie Hancock", "Kenny Burrell", "Donald Best", "Butch Warren", "Lex Humphries", "Vocal choir (8 voices)"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "The Black Disciple", "track_number": 4, "side": "B", "duration": "8:12", "session_date": "1963-01-12", "composers": ["Donald Byrd"], "personnel": ["Donald Byrd", "Hank Mobley", "Herbie Hancock", "Kenny Burrell", "Donald Best", "Butch Warren", "Lex Humphries", "Vocal choir (8 voices)"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Chant", "track_number": 5, "side": "B", "duration": "7:31", "session_date": "1963-01-12", "composers": ["Duke Pearson"], "personnel": ["Donald Byrd", "Hank Mobley", "Herbie Hancock", "Kenny Burrell", "Donald Best", "Butch Warren", "Lex Humphries", "Vocal choir (8 voices)"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1442996026",
    "cover_art": [],
    "notes": "Single session; released February 1964 (BLP 4124 / BST 84124). Duke Pearson arranged; Coleridge-Taylor Perkinson directed the choir (neither plays an instrument so neither is a personnel-array performer). The choir is entered as a single 'vocals' group entry since individual singers are unnamed in S3 — flagged per the personnel-contract edge-case guidance. Per-track choir distribution not broken out (inf)."
  }
}
```

```json
{
  "id": "cannonball-adderley-the-cannonball-adderley-quintet-in-san-francisco-1959",
  "artist": "Cannonball Adderley",
  "album": "The Cannonball Adderley Quintet in San Francisco",
  "year": 1959,
  "label": "Riverside",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the October 18 & 20, 1959 live dates at the Jazz Workshop with Nat Adderley, Bobby Timmons, Sam Jones and Louis Hayes; Timmons's 'This Here' is the soul-jazz anthem that broke the band commercially. inf[S1][S2]: a landmark live soul-jazz/hard-bop crossover. Distinct from the excluded 'Somethin' Else'.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "Gospel-inflected 'soul' jazz but acoustic, swinging and pre-fusion — in scope.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-10-18", "1959-10-20"],
    "multi_session": true,
    "studio": "The Jazz Workshop (live), San Francisco",
    "producer": "Orrin Keepnews",
    "engineer": "Reice Hamel",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Cannonball Adderley", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": ["Julian Adderley"], "notes": "" },
      { "name": "Nat Adderley", "instrument": "cornet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Bobby Timmons", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Sam Jones", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Louis Hayes", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "This Here", "track_number": 1, "side": "A", "duration": "12:29", "session_date": null, "composers": ["Bobby Timmons"], "personnel": ["Cannonball Adderley", "Nat Adderley", "Bobby Timmons", "Sam Jones", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Spontaneous Combustion", "track_number": 2, "side": "A", "duration": "11:55", "session_date": null, "composers": ["Cannonball Adderley"], "personnel": ["Cannonball Adderley", "Nat Adderley", "Bobby Timmons", "Sam Jones", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Hi-Fly", "track_number": 3, "side": "B", "duration": "11:09", "session_date": null, "composers": ["Randy Weston"], "personnel": ["Cannonball Adderley", "Nat Adderley", "Bobby Timmons", "Sam Jones", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "You Got It!", "track_number": 4, "side": "B", "duration": "5:10", "session_date": null, "composers": ["Cannonball Adderley"], "personnel": ["Cannonball Adderley", "Nat Adderley", "Bobby Timmons", "Sam Jones", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Bohemia After Dark", "track_number": 5, "side": "B", "duration": "8:06", "session_date": null, "composers": ["Oscar Pettiford"], "personnel": ["Cannonball Adderley", "Nat Adderley", "Bobby Timmons", "Sam Jones", "Louis Hayes"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443103130",
    "cover_art": [],
    "notes": "Live across two nights (Oct 18 & 20, 1959; RLP 12-311). S3 does not map specific tracks to specific nights, so per-track session_date is null. 'Straight, No Chaser', plus alternates of 'This Here' and 'You Got It!', are later CD bonus tracks — excluded from the original-LP list above. Apple ID is the 2007 remaster (collectionId 1443103130)."
  }
}
```

```json
{
  "id": "wes-montgomery-full-house-1962",
  "artist": "Wes Montgomery",
  "album": "Full House",
  "year": 1962,
  "label": "Riverside",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the June 25, 1962 live date at Tsubo (Berkeley) with Johnny Griffin and the Miles Davis rhythm section of the day — Wynton Kelly, Paul Chambers, Jimmy Cobb. inf[S1][S2]: a prized live hard-bop guitar date. Distinct from the excluded studio classic 'The Incredible Jazz Guitar of Wes Montgomery'.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1962-06-25"],
    "multi_session": false,
    "studio": "Tsubo (live), Berkeley, California",
    "producer": "Orrin Keepnews",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Wes Montgomery", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Johnny Griffin", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Lays out on the ballad feature 'I've Grown Accustomed to Her Face' (quartet without tenor) per common documentation; not broken out by S3 → not flagged at track level here." },
      { "name": "Wynton Kelly", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Cobb", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Full House", "track_number": 1, "side": "A", "duration": "9:16", "session_date": "1962-06-25", "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Johnny Griffin", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "I've Grown Accustomed to Her Face", "track_number": 2, "side": "A", "duration": "3:29", "session_date": "1962-06-25", "composers": ["Alan Jay Lerner", "Frederick Loewe"], "personnel": ["Wes Montgomery", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Blue 'N' Boogie", "track_number": 3, "side": "A", "duration": "9:38", "session_date": "1962-06-25", "composers": ["Dizzy Gillespie", "Frank Paparelli"], "personnel": ["Wes Montgomery", "Johnny Griffin", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Cariba", "track_number": 4, "side": "B", "duration": "8:28", "session_date": "1962-06-25", "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Johnny Griffin", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Come Rain or Come Shine", "track_number": 5, "side": "B", "duration": "7:21", "session_date": "1962-06-25", "composers": ["Harold Arlen", "Johnny Mercer"], "personnel": ["Wes Montgomery", "Johnny Griffin", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "S.O.S.", "track_number": 6, "side": "B", "duration": "4:49", "session_date": "1962-06-25", "composers": ["Wes Montgomery"], "personnel": ["Wes Montgomery", "Johnny Griffin", "Wynton Kelly", "Paul Chambers", "Jimmy Cobb"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1872248473",
    "cover_art": [],
    "notes": "Single live date; released November 1962 (Riverside / OJC). Original LP = the six tracks above; later reissues add alternate takes of Cariba, Come Rain or Come Shine, S.O.S., and 'Born to Be Blue' (excluded). Engineer not credited by S3 → null. 'I've Grown Accustomed to Her Face' is a Montgomery quartet feature without Griffin (widely documented; recorded as inf at track level here). Apple match (collectionId 1872248473) is a 2026 remaster reissue — the only Full House result returned by the iTunes lookup."
  }
}
```

```json
{
  "id": "tina-brooks-true-blue-1960",
  "artist": "Tina Brooks",
  "album": "True Blue",
  "year": 1960,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S2", "S3", "S4", "S5"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Wikipedia documents the June 25, 1960 date with Freddie Hubbard, Duke Jordan, Sam Jones and Art Taylor; the only album issued under Brooks's own name in his lifetime. inf[S1][S2]: a celebrated 'hidden gem' of the Blue Note catalogue, reappraised highly by critics. Under-cited relative to its quality, hence 'consider'.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-06-25"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Tina Brooks", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": ["Harold Floyd Brooks"], "notes": "" },
      { "name": "Freddie Hubbard", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Duke Jordan", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Sam Jones", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Art Taylor", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Good Old Soul", "track_number": 1, "side": "A", "duration": "8:07", "session_date": "1960-06-25", "composers": ["Tina Brooks"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Up Tight's Creek", "track_number": 2, "side": "A", "duration": "5:17", "session_date": "1960-06-25", "composers": ["Tina Brooks"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Theme for Doris", "track_number": 3, "side": "A", "duration": "5:53", "session_date": "1960-06-25", "composers": ["Tina Brooks"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "True Blue", "track_number": 4, "side": "B", "duration": "4:57", "session_date": "1960-06-25", "composers": ["Tina Brooks"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Miss Hazel", "track_number": 5, "side": "B", "duration": "5:32", "session_date": "1960-06-25", "composers": ["Tina Brooks"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] },
      { "title": "Nothing Ever Changes My Love for You", "track_number": 6, "side": "B", "duration": "7:53", "session_date": "1960-06-25", "composers": ["Jack Segal", "Marvin Fisher"], "personnel": ["Tina Brooks", "Freddie Hubbard", "Duke Jordan", "Sam Jones", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "inf", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443213355",
    "cover_art": [],
    "notes": "Single session; released December 1960 (BST 84041). Engineer = Rudy Van Gelder by inference (Van Gelder Studio Blue Note date; S3 explicitly notes no engineer credit) per the Van Gelder rule → epistemic_production inf. CD reissue adds alternates of 'True Blue' and 'Good Old Soul' (excluded). Apple ID 1443213355 = standard edition."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves
- **John Coltrane — Blue Train (1957):** Coltrane's lone Blue Note leader date and a definitive hard-bop sextet statement — a non-negotiable pillar.
- **Sonny Rollins — Way Out West (1957):** The benchmark pianoless saxophone-trio date; a second canonical Rollins record alongside the excluded Saxophone Colossus.
- **Clifford Brown & Max Roach (1954):** The definitive Brown–Roach quintet album ('Joy Spring', 'Daahoud') — a cornerstone of the style, distinct from Study in Brown.
- **Horace Silver and the Jazz Messengers (1954):** The record that codified the hard-bop template; 'The Preacher' and 'Doodlin'' are genre-founding tracks.

### Hidden Gems
- **Tina Brooks — True Blue (1960):** The only album issued under Brooks's name in his lifetime; heavily reappraised, under-cited relative to its quality.
- **Hank Mobley — Roll Call (1960):** Overshadowed by Soul Station but a peak-period Mobley date with Hubbard and the Kelly/Chambers/Blakey engine.
- **Freddie Hubbard — Hub-Tones (1962):** A slightly adventurous, less-cited Hubbard date with a young Herbie Hancock and Spaulding's flute/alto color.

### Consensus Picks (would appear across 3+ standard references)
- Blue Train, Way Out West, Clifford Brown & Max Roach, Horace Silver and the Jazz Messengers, A Night at Birdland Vol. 1, The Cannonball Adderley Quintet in San Francisco, Midnight Blue — all long-standing fixtures of Penguin/AllMusic/standard-canon coverage (cited here at `inf` for S1/S2 since those pages were not page-fetched this run; `obs` facts come from S3).

### Single-Source Picks
- None rely on a single source for personnel: every record is grounded in a dedicated Wikipedia album article (S3, which cites original liner notes) plus an iTunes identifier (S4), with S1/S2 supporting canon standing. The weakest-corroborated *canon* cases are Bluesnik and True Blue (lighter critical footprint), but both are still multi-source on the facts.

### Scope Calls
- **Way Out West** — pianoless L.A. trio; kept as hard bop because it swings with structure and is firmly pre-fusion (the Test Question, not the date/geography, governs).
- **Our Man in Paris** — bebop *repertoire* (Parker, Gillespie) but a 1963 performance with hard-bop weight; in scope.
- **Midnight Blue** — placed `soul-jazz` primary / `hard-bop` secondary: bluesy, conga-driven groove music, but acoustic and pre-fusion.
- **A New Perspective** — `hard-bop` primary / `soul-jazz` secondary: gospel choir as arrangement color over a hard-bop rhythm section; pre-fusion.
- **Cannonball Adderley in San Francisco** — `hard-bop`/`soul-jazz` border: 'This Here' is the soul-jazz anthem, but the band is an acoustic hard-bop quintet; in scope.
- **A Night at Birdland Vol. 1** and **Clifford Brown & Max Roach** — recorded 1954, at the leading edge of hard bop; kept (era is a center of gravity, not a fence, per genre-definitions draft 2).

### Gaps Noticed
- **Soul jazz / organ combos remain thin in this batch.** I deliberately leaned hard-bop-core to avoid the fusion edge and because many obvious organ picks (Jimmy Smith, Lou Donaldson, Jack McDuff, Gene Ammons) are already collected or pending. Genuinely-new organ-led candidates worth a future pass: Grant Green *Grantstand* (1961), Stanley Turrentine *That's Where It's At* (1962), Big John Patton *Along Came John* (1963), Brother Jack McDuff *The Honeydripper* (1961).
- **Prestige is under-represented** here versus Blue Note (a consequence of the exclusion list having absorbed most Prestige soul-jazz). Future Prestige-focused dispatch suggested.
- **West Coast hard bop** (Curtis Counce, Harold Land as leader) and **Chicago/hard-bop pianists** (Wynton Kelly as leader, Sonny Clark beyond Cool Struttin') are lightly covered.

### Personnel Coverage
- **Fullest records (per-track session dates resolved, `obs`):** Horace Silver and the Jazz Messengers (per-track recording dates from S3 — only album here with `track_assignments_complete: true` on a multi-session date) and Way Out West (single trio session, all-on-all → `track_assignments_complete: true`).
- **Strong per-track instrumentation (`obs`):** Midnight Blue — S3 documents exactly which musicians sit out 'Soul Lament', 'Midnight Blue' and 'Gee, Baby', enabling true selected-track scopes.
- **Standard single-session quintet dates (per-track personnel `inf`):** Blue Train, The Cooker, Roll Call, Bluesnik, Hub-Tones, Our Man in Paris, A New Perspective, True Blue — sources confirm a fixed band across the date but do not break personnel out per title, so uniform participation is inferred (`track_assignments_complete: false`).
- **Live dates with unresolved night-to-track mapping:** A Night at Birdland Vol. 1 (single night, fine) and Cannonball in San Francisco (two nights, S3 does not map tracks to nights → per-track `session_date: null`).
- **Engineer inferences (Van Gelder rule, S5):** Roll Call, Bluesnik, Hub-Tones, True Blue — Blue Note dates at Van Gelder Studio with no engineer credited by S3; engineer set to Rudy Van Gelder at `epistemic_production: "inf"`.
- **Layer 5 gap (all 15):** MusicBrainz web service was unreachable (certificate error) every attempt, so `musicbrainz_release_group_mbid` is `null` and `cover_art` is `[]` throughout — not fabricated. Apple `collectionId` (S4) was captured for all 15; note three are reissue editions (Roll Call, Bluesnik, Midnight Blue = Rudy Van Gelder Editions; Full House = 2026 remaster) where no original-pressing entry was returned.
