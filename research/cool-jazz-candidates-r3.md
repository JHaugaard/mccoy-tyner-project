# Cool Jazz / West Coast Jazz — Candidate Records (Round 3)

Final push toward 100. 15 genuinely-new cool / West Coast candidates from the deeper bench — none appear in the dispatch ledger (15 collected), the 15 pending cool/West Coast already chosen, or the 30 pending hard-bop/modal titles. Two-phase pass: Phase 1 judged against `docs/genre-definitions.md`; Phase 2 gathered full personnel/session/track data per `docs/personnel-contract.md`. `year` = **recording year** (release year noted where it differs). `include` is `null` on every record — John decides at the gate.

Apple Music `collectionId` captured on 15/15; MusicBrainz release-group MBID captured on 15/15 (Cover Art Archive front-art URLs derived from them, epistemic `inf` — endpoint is deterministic from a verified MBID but the specific pressing's image was not individually opened).

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — *Miles Ahead* (album) | Encyclopedia | https://en.wikipedia.org/wiki/Miles_Ahead_(album) | Full orchestra personnel, per-session dates, production, tracks/composers/durations |
| S2 | Wikipedia — *Focus* (Stan Getz album) | Encyclopedia | https://en.wikipedia.org/wiki/Focus_(Stan_Getz_album) | Personnel, string orchestra, dates, production, tracks |
| S3 | Wikipedia — *Lee Konitz with Warne Marsh* | Encyclopedia | https://en.wikipedia.org/wiki/Lee_Konitz_with_Warne_Marsh | Personnel incl. per-track pianist, date, studio, tracks |
| S4 | Wikipedia — *Fontessa* | Encyclopedia | https://en.wikipedia.org/wiki/Fontessa | MJQ personnel, two-session dates, producer, tracks |
| S5 | Wikipedia — *Grand Encounter* | Encyclopedia | https://en.wikipedia.org/wiki/Grand_Encounter | Personnel, date, producer, label, tracks |
| S6 | Wikipedia — *Something Cool* | Encyclopedia | https://en.wikipedia.org/wiki/Something_Cool | June Christy; arranger, partial personnel, session span, label |
| S7 | Wikipedia — *Everybody Digs Bill Evans* | Encyclopedia | https://en.wikipedia.org/wiki/Everybody_Digs_Bill_Evans | Trio personnel, date, studio, producer, tracks/composers |
| S8 | Wikipedia — *What Is There to Say?* | Encyclopedia | https://en.wikipedia.org/wiki/What_Is_There_to_Say%3F | Mulligan quartet, per-session track mapping, producer, tracks |
| S9 | Wikipedia — *Gil Evans & Ten* | Encyclopedia | https://en.wikipedia.org/wiki/Gil_Evans_%26_Ten | Personnel, per-session dates, Van Gelder studio, tracks |
| S10 | Wikipedia — *The Jimmy Giuffre Clarinet* | Encyclopedia | https://en.wikipedia.org/wiki/The_Jimmy_Giuffre_Clarinet | Per-track personnel & doubles, dates, studio, tracks |
| S11 | Wikipedia — *Contemporary Concepts* | Encyclopedia | https://en.wikipedia.org/wiki/Contemporary_Concepts | Kenton big-band personnel, arrangers, dates, tracks |
| S12 | Wikipedia — *Take Ten* | Encyclopedia | https://en.wikipedia.org/wiki/Take_Ten | Desmond/Hall personnel, per-track bassist, dates, tracks |
| S13 | Wikipedia — *The Dual Role of Bob Brookmeyer* | Encyclopedia | https://en.wikipedia.org/wiki/The_Dual_Role_of_Bob_Brookmeyer | Two-session personnel split, dates, producer, tracks |
| S14 | Wikipedia — *Martians Come Back!* | Encyclopedia | https://en.wikipedia.org/wiki/Martians_Come_Back! | Shorty Rogers selected-track personnel, five dates, tracks |
| S15 | Wikipedia — *Mel Tormé and the Marty Paich Dek-Tette* | Encyclopedia | https://en.wikipedia.org/wiki/Mel_Torm%C3%A9_and_the_Marty_Paich_Dek-Tette | Dek-Tette personnel (two sets), dates, tracks/composers |
| S16 | iTunes Search API (Apple Music) | API | https://itunes.apple.com/search | Apple Music `collectionId` lookups |
| S17 | MusicBrainz release-group API + Cover Art Archive | API | https://musicbrainz.org/ws/2/release-group/ ; https://coverartarchive.org | Release-group MBIDs; CAA front-art URLs derived |
| S18 | AllMusic (Scott Yanow reviews) | Review site | https://www.allmusic.com | Genre/canon placement (e.g., Grand Encounter "the ultimate in cool jazz") |

---

## 2. Candidate Records

```json
{
  "id": "miles-davis-miles-ahead-1957",
  "artist": "Miles Davis",
  "album": "Miles Ahead",
  "year": 1957,
  "label": "Columbia",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "third-stream"],
  "sources": ["S1", "S16", "S17", "S18"],
  "epistemic": "obs",
  "rationale": "obs[S1]: Miles Davis (flugelhorn) fronting a 19-piece orchestra arranged and conducted by Gil Evans — the first full Davis/Evans collaboration, direct heir to Birth of the Cool. obs[S18]: AllMusic frames the Davis/Evans orchestral works as cornerstones of orchestral cool/third stream. inf: a pillar of the cool lineage and the bridge between Birth of the Cool and Porgy and Bess / Sketches of Spain.",
  "priority": "must_have",
  "overlap_risk": "Third-stream / orchestral jazz border; Davis's modal turn is two years away.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-05-06", "1957-05-10", "1957-05-23", "1957-05-27", "1957-08-22"],
    "multi_session": true,
    "studio": "Columbia 30th Street Studio, New York City",
    "producer": "George Avakian",
    "engineer": "Harold Chapman",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Miles Davis", "instrument": "flugelhorn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Lead soloist; plays flugelhorn throughout. Gil Evans arranged and conducted (not an instrumentalist on the date)." },
      { "name": "Bernie Glow", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Lead trumpet." },
      { "name": "Ernie Royal", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Louis Mucci", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Taft Jordan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "John Carisi", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composer of 'Springsville'." },
      { "name": "Jimmy Cleveland", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Frank Rehak", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Joe Bennett", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tom Mitchell", "instrument": "bass trombone", "scope": "selected-tracks", "tracks": ["The Maids of Cadiz", "The Duke"], "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Listed on tracks 2-3 per source." },
      { "name": "Willie Ruff", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Tony Miranda", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Buffington", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Bill Barber", "instrument": "tuba", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "'tuba' is outside the contract taxonomy; recorded as the most specific term per source." },
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Danny Bank", "instrument": "bass clarinet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Eddie Caine", "instrument": "flute", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Doubles flute/clarinet per source." },
      { "name": "Sid Cooper", "instrument": "flute", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Doubles flute/clarinet per source." },
      { "name": "Romeo Penque", "instrument": "flute", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Doubles flute/clarinet/oboe/bass clarinet per source; primary listed as flute." },
      { "name": "Wynton Kelly", "instrument": "piano", "scope": "selected-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Source: piano 'except tracks 3, 7, 10, 12' — that numbering follows an expanded reissue, so exact track exceptions on the original 10-track LP are uncertain; scope marked selected-tracks." },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Art Taylor", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Springsville", "track_number": 1, "side": "A", "duration": "3:27", "session_date": null, "composers": ["John Carisi"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Maids of Cadiz", "track_number": 2, "side": "A", "duration": "3:53", "session_date": null, "composers": ["Léo Delibes"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Duke", "track_number": 3, "side": "A", "duration": "3:35", "session_date": null, "composers": ["Dave Brubeck"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "My Ship", "track_number": 4, "side": "A", "duration": "4:28", "session_date": null, "composers": ["Kurt Weill", "Ira Gershwin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Miles Ahead", "track_number": 5, "side": "A", "duration": "3:29", "session_date": null, "composers": ["Miles Davis", "Gil Evans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Blues for Pablo", "track_number": 6, "side": "B", "duration": "5:18", "session_date": null, "composers": ["Gil Evans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "New Rhumba", "track_number": 7, "side": "B", "duration": "4:37", "session_date": null, "composers": ["Ahmad Jamal"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Meaning of the Blues", "track_number": 8, "side": "B", "duration": "2:48", "session_date": null, "composers": ["Bobby Troup", "Leah Worth"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Lament", "track_number": 9, "side": "B", "duration": "2:14", "session_date": null, "composers": ["J.J. Johnson"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "I Don't Wanna Be Kissed (By Anyone but You)", "track_number": 10, "side": "B", "duration": "3:05", "session_date": null, "composers": ["Harold Spina", "Jack Elliott"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "cc0c7530-a135-3386-a682-0d33d14c876e",
    "apple_album_id": "200300007",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/cc0c7530-a135-3386-a682-0d33d14c876e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Released Oct 21, 1957 (Columbia CL 1041 mono). 'The Meaning of the Blues' / 'Lament' form a continuous medley on the LP. Side B is a near-continuous suite. Gil Evans arranged and conducted; Cal Lampley assistant producer. Tracks 8-9 sometimes counted as one band. Per-track session mapping (May 6/10/23/27) not distinguished by the cited source; Aug 22 was an overdub/solo-correction date."
  }
}
```

```json
{
  "id": "stan-getz-focus-1961",
  "artist": "Stan Getz",
  "album": "Focus",
  "year": 1961,
  "label": "Verve",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "third-stream"],
  "sources": ["S2", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S2]: Getz improvising over a through-composed Eddie Sauter string-orchestra suite — Wikipedia classifies it as cool jazz and third stream, and Getz himself called it a favorite. inf: the most ambitious arranged setting of cool-school tenor; continuous with the arrangement-over-improvisation values of the style.",
  "priority": "strong",
  "overlap_risk": "Third-stream / classical-crossover border.",
  "scope_flag": "Recorded 1961, past the cool window's center of gravity; its arranged, classically-scored character is squarely cool/third-stream, so kept in scope per the test question. Flagged for review.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1961-07-14", "1961-07-28"],
    "multi_session": true,
    "studio": "Webster Hall, New York City",
    "producer": "Creed Taylor",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Stan Getz", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Soloist over the string orchestra." },
      { "name": "Roy Haynes", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Steve Kuhn", "instrument": "piano", "scope": "selected-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Rhythm section; not present on all movements." },
      { "name": "John Neves", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Alan Martin", "instrument": "violin", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "One of twelve+ violinists; most string players unnamed in source." },
      { "name": "Norman Carr", "instrument": "violin", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Gerald Tarack", "instrument": "violin", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Jacob Glick", "instrument": "viola", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "One of four violists." },
      { "name": "Bruce Rogers", "instrument": "cello", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "One of two cellists; a harpist (unnamed) also present." }
    ],
    "tracks": [
      { "title": "I'm Late, I'm Late", "track_number": 1, "side": "A", "duration": "8:10", "session_date": null, "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Her", "track_number": 2, "side": "A", "duration": "6:13", "session_date": null, "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Pan", "track_number": 3, "side": "A", "duration": "3:58", "session_date": null, "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "I Remember When", "track_number": 4, "side": "A", "duration": "5:03", "session_date": null, "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Night Rider", "track_number": 5, "side": "B", "duration": "3:58", "session_date": "1961-07-28", "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Once Upon a Time", "track_number": 6, "side": "B", "duration": "4:48", "session_date": "1961-07-28", "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "A Summer Afternoon", "track_number": 7, "side": "B", "duration": "6:03", "session_date": "1961-07-28", "composers": ["Eddie Sauter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "e60ac23f-7b63-3015-8b23-cf16c6ca6725",
    "apple_album_id": "1852361609",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/e60ac23f-7b63-3015-8b23-cf16c6ca6725/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "All compositions by Eddie Sauter (composer/arranger); Hershy Kay conducted. Released late January 1962 (Verve V6-8412). July 14 1961 captured the string-orchestra parts for tracks 1-4; July 28 1961 captured Getz's parts for 1-4 and the complete tracks 5-7; further touch-ups Sept-Oct 1961. CD reissue adds two 45-rpm versions of 'I'm Late, I'm Late' and 'I Remember When' (bonus, not listed). Full string-section roster not enumerated by source."
  }
}
```

```json
{
  "id": "lee-konitz-lee-konitz-with-warne-marsh-1955",
  "artist": "Lee Konitz",
  "album": "Lee Konitz with Warne Marsh",
  "year": 1955,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S3", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S3]: the definitive recorded meeting of the two leading Tristano-school horn players, with Tristano sidemen (Sal Mosca, Billy Bauer, Ronnie Ball) — cool jazz's cerebral, contrapuntal wing. inf: distinct from the already-pending Subconscious-Lee and the Konitz/Mulligan date; a cornerstone of the Tristano lineage the dispatch called for.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-06-14"],
    "multi_session": false,
    "studio": "Coastal Studios, New York City",
    "producer": "Nesuhi Ertegun",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Warne Marsh", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Billy Bauer", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Oscar Pettiford", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Composer of 'Don't Squawk'." },
      { "name": "Kenny Clarke", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Sal Mosca", "instrument": "piano", "scope": "selected-tracks", "tracks": ["There Will Never Be Another You", "Donna Lee", "Two Not One", "Don't Squawk", "Background Music"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Piano on tracks 2, 4, 5, 6, 8." },
      { "name": "Ronnie Ball", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Ronnie's Line"], "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Piano on track 7 only; composer of 'Ronnie's Line'." }
    ],
    "tracks": [
      { "title": "Topsy", "track_number": 1, "side": "A", "duration": "5:29", "session_date": "1955-06-14", "composers": ["Edgar Battle", "Eddie Durham"], "personnel": ["Lee Konitz", "Warne Marsh", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "There Will Never Be Another You", "track_number": 2, "side": "A", "duration": "4:49", "session_date": "1955-06-14", "composers": ["Harry Warren"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "I Can't Get Started", "track_number": 3, "side": "A", "duration": "3:58", "session_date": "1955-06-14", "composers": ["Vernon Duke"], "personnel": ["Lee Konitz", "Warne Marsh", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Donna Lee", "track_number": 4, "side": "A", "duration": "6:17", "session_date": "1955-06-14", "composers": ["Charlie Parker"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Two Not One", "track_number": 5, "side": "B", "duration": "5:35", "session_date": "1955-06-14", "composers": ["Lennie Tristano"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Don't Squawk", "track_number": 6, "side": "B", "duration": "7:20", "session_date": "1955-06-14", "composers": ["Oscar Pettiford"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Ronnie's Line", "track_number": 7, "side": "B", "duration": "3:10", "session_date": "1955-06-14", "composers": ["Ronnie Ball"], "personnel": ["Lee Konitz", "Warne Marsh", "Ronnie Ball", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Background Music", "track_number": 8, "side": "B", "duration": "5:45", "session_date": "1955-06-14", "composers": ["Warne Marsh"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Billy Bauer", "Oscar Pettiford", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "bdd1200f-ab65-4a93-ad79-725409a9a1bc",
    "apple_album_id": "81873177",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/bdd1200f-ab65-4a93-ad79-725409a9a1bc/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Atlantic SD 1217, released December 1955. Single session, June 14 1955. Per-track pianist mapping from S3 (Mosca on five, Ball on one, two tracks pianoless); horns/guitar/bass/drums on all eight. track_assignments_complete left false because the pianoless-track reading is inferred from the absence of a piano credit rather than a positive per-track statement."
  }
}
```

```json
{
  "id": "modern-jazz-quartet-fontessa-1956",
  "artist": "The Modern Jazz Quartet",
  "album": "Fontessa",
  "year": 1956,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "third-stream"],
  "sources": ["S4", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S4]: the MJQ's first Atlantic LP, John Lewis's chamber-jazz aesthetic with the title suite modeled on commedia dell'arte — cool jazz's third-stream wing. inf: distinct from the already-pending Django; Fontessa is the group's most explicitly composed early statement and belongs in the cool canon.",
  "priority": "strong",
  "overlap_risk": "Third-stream / chamber-jazz border.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-01-22", "1956-02-14"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, NJ (Feb 14); New York City (Jan 22)",
    "producer": "Nesuhi Ertegun",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Lewis", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Music director; composer of 'Versailles' and 'Fontessa'." },
      { "name": "Milt Jackson", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Composer of 'Bluesology'." },
      { "name": "Percy Heath", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Connie Kay", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Versailles", "track_number": 1, "side": "A", "duration": "3:22", "session_date": null, "composers": ["John Lewis"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Angel Eyes", "track_number": 2, "side": "A", "duration": "3:48", "session_date": null, "composers": ["Earl Brent", "Matt Dennis"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Fontessa", "track_number": 3, "side": "A", "duration": "11:12", "session_date": null, "composers": ["John Lewis"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Over the Rainbow", "track_number": 4, "side": "B", "duration": "3:50", "session_date": null, "composers": ["Harold Arlen", "E.Y. Harburg"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Bluesology", "track_number": 5, "side": "B", "duration": "5:04", "session_date": null, "composers": ["Milt Jackson"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Willow Weep for Me", "track_number": 6, "side": "B", "duration": "4:47", "session_date": null, "composers": ["Ann Ronell"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Woody 'n' You", "track_number": 7, "side": "B", "duration": "4:25", "session_date": null, "composers": ["Dizzy Gillespie"], "personnel": ["John Lewis", "Milt Jackson", "Percy Heath", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "59404ca7-e67f-3adc-8123-fc03b9777f15",
    "apple_album_id": "81898862",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/59404ca7-e67f-3adc-8123-fc03b9777f15/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Atlantic 1956. Two sessions: Jan 22 1956 (NYC) and Feb 14 1956 (Van Gelder Studio, Englewood Cliffs). Source does not map tracks to sessions, so session_date is null per track and the whole quartet is credited on all tracks. Engineer not stated; the Feb 14 date was at Van Gelder but the Jan 22 NYC session was not, so no album-wide Van Gelder inference is made."
  }
}
```

```json
{
  "id": "john-lewis-grand-encounter-1956",
  "artist": "John Lewis",
  "album": "Grand Encounter: 2° East / 3° West",
  "year": 1956,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S5", "S16", "S17", "S18"],
  "epistemic": "obs",
  "rationale": "obs[S5]: John Lewis (East) meeting Bill Perkins, Jim Hall, Percy Heath and Chico Hamilton (the subtitle marks the East/West blend), on Pacific Jazz, the West Coast cool label. obs[S18]: AllMusic's Scott Yanow calls it 'the ultimate in cool jazz.' inf: a pillar of the relaxed, contrapuntal Pacific Jazz aesthetic.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-02-10"],
    "multi_session": false,
    "studio": "Los Angeles, CA",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "John Lewis", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "Composer of 'Two Degrees East - Three Degrees West'." },
      { "name": "Bill Perkins", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "West Coast contingent." },
      { "name": "Jim Hall", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "" },
      { "name": "Percy Heath", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "" },
      { "name": "Chico Hamilton", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "West Coast contingent." }
    ],
    "tracks": [
      { "title": "Love Me or Leave Me", "track_number": 1, "side": "A", "duration": "8:18", "session_date": "1956-02-10", "composers": ["Walter Donaldson", "Gus Kahn"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "I Can't Get Started", "track_number": 2, "side": "A", "duration": "3:31", "session_date": "1956-02-10", "composers": ["Vernon Duke", "Ira Gershwin"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Easy Living", "track_number": 3, "side": "A", "duration": "4:13", "session_date": "1956-02-10", "composers": ["Ralph Rainger", "Leo Robin"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Two Degrees East - Three Degrees West", "track_number": 4, "side": "B", "duration": "6:07", "session_date": "1956-02-10", "composers": ["John Lewis"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Skylark", "track_number": 5, "side": "B", "duration": "3:06", "session_date": "1956-02-10", "composers": ["Hoagy Carmichael", "Johnny Mercer"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Almost Like Being in Love", "track_number": 6, "side": "B", "duration": "9:26", "session_date": "1956-02-10", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["John Lewis", "Bill Perkins", "Jim Hall", "Percy Heath", "Chico Hamilton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "d714510c-bf94-43bd-89e4-efdf0fb2e73d",
    "apple_album_id": "1397523960",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/d714510c-bf94-43bd-89e4-efdf0fb2e73d/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Pacific Jazz PJ-1217, released November 1956. Single LA session Feb 10 1956, full quintet on every track, so track_assignments_complete is true. MusicBrainz lists the release-group first-release date as 1957 (a reissue); recording and original release were 1956."
  }
}
```

```json
{
  "id": "june-christy-something-cool-1955",
  "artist": "June Christy",
  "album": "Something Cool",
  "year": 1955,
  "label": "Capitol",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S6", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S6]: June Christy with Pete Rugolo arrangements and West Coast session players (Shelly Manne, Barney Kessel, Bud Shank named) — the title track is a touchstone of West Coast cool vocal jazz. inf: the leading 'cool school' vocal album, continuous with the Kenton/Rugolo lineage; the dispatch's call for the Kenton/cool-vocal bench.",
  "priority": "consider",
  "overlap_risk": "Vocal-pop border; arrangements are concert-jazz, not standard pop backing.",
  "scope_flag": "Vocal jazz — kept for its West Coast cool arranging pedigree (Rugolo) and personnel; flagged as a vocal-led record for review.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-08/1955-07"],
    "multi_session": true,
    "studio": null,
    "producer": "Lee Gillette",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "June Christy", "instrument": "vocals", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "Pete Rugolo arranged and conducted (not an instrumentalist on the date)." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "unknown", "tracks": null, "session_dates": null, "epistemic": "unk", "sources": ["S6"], "name_variants": [], "notes": "Named by source among the session players; specific tracks/sessions not documented." },
      { "name": "Barney Kessel", "instrument": "guitar", "scope": "unknown", "tracks": null, "session_dates": null, "epistemic": "unk", "sources": ["S6"], "name_variants": [], "notes": "Named among session players; track-level presence undocumented." },
      { "name": "Bud Shank", "instrument": "alto saxophone", "scope": "unknown", "tracks": null, "session_dates": null, "epistemic": "unk", "sources": ["S6"], "name_variants": [], "notes": "Named among the woodwind section; track-level presence undocumented." }
    ],
    "tracks": [
      { "title": "Something Cool", "track_number": 1, "side": "A", "duration": null, "session_date": null, "composers": ["Billy Barnes"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Midnight Sun", "track_number": null, "side": null, "duration": null, "session_date": null, "composers": ["Lionel Hampton", "Sonny Burke", "Johnny Mercer"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "unk", "sources": ["S6"] },
      { "title": "Lonely House", "track_number": null, "side": null, "duration": null, "session_date": null, "composers": ["Kurt Weill", "Langston Hughes"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "unk", "sources": ["S6"] },
      { "title": "I'll Take Romance", "track_number": null, "side": null, "duration": null, "session_date": null, "composers": ["Ben Oakland", "Oscar Hammerstein II"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "unk", "sources": ["S6"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "fb5bcd7c-a62d-4741-b024-35e702d861e3",
    "apple_album_id": "1440881013",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/fb5bcd7c-a62d-4741-b024-35e702d861e3/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "THIN PERSONNEL DATA. Original 10-inch Capitol H516 released Aug 2 1954; 12-inch T516 (the canonical 11-track edition) released Aug 1 1955; a 1960 stereo re-recording (ST516) exists. Recording-year set to 1955 to match the canonical 12-inch; original sessions span Aug 1953-Jul 1955. Source names only Christy, Rugolo (arranger), and a partial player list (Manne/Kessel/Shank) without per-track credits, durations, or a full tracklist; capturing AllMusic/Mosaic-level session detail would require a deeper pass. Apple ID 1440881013 is the 1954-dated jazz edition (closest to original)."
  }
}
```

```json
{
  "id": "bill-evans-everybody-digs-bill-evans-1958",
  "artist": "Bill Evans",
  "album": "Everybody Digs Bill Evans",
  "year": 1958,
  "label": "Riverside",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S7", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S7]: Evans's second album as leader, his lyrical, classically-informed touch already formed; 'Peace Piece' is a static-harmony improvisation that anticipates modal jazz. inf: the dispatch's 'early Bill Evans, cool-adjacent' target; sits on the cool/modal seam a year before Kind of Blue.",
  "priority": "strong",
  "overlap_risk": "Modal-jazz border — 'Peace Piece' is proto-modal and Evans joined Kind of Blue months later.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-12-15"],
    "multi_session": false,
    "studio": "Reeves Sound Studios, New York City",
    "producer": "Orrin Keepnews",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Bill Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "'Peace Piece' and the two 'Epilogue' fragments are solo piano." },
      { "name": "Sam Jones", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Minority", "Young and Foolish", "Night and Day", "Epilogue", "Tenderly", "What Is There to Say?", "Oleo"], "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Source: bass on tracks 1, 2, 4, 5, 7, 8 (LP numbering); absent on the solo pieces 'Lucky to Be Me' arrangement context, 'Peace Piece', and the Epilogues." },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Minority", "Young and Foolish", "Night and Day", "Epilogue", "Tenderly", "What Is There to Say?", "Oleo"], "session_dates": null, "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Same selected tracks as Sam Jones per source." }
    ],
    "tracks": [
      { "title": "Minority", "track_number": 1, "side": "A", "duration": "5:20", "session_date": "1958-12-15", "composers": ["Gigi Gryce"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Young and Foolish", "track_number": 2, "side": "A", "duration": "5:48", "session_date": "1958-12-15", "composers": ["Albert Hague", "Arnold B. Horwitt"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Lucky to Be Me", "track_number": 3, "side": "A", "duration": "3:35", "session_date": "1958-12-15", "composers": ["Leonard Bernstein", "Betty Comden", "Adolph Green"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Night and Day", "track_number": 4, "side": "A", "duration": "7:12", "session_date": "1958-12-15", "composers": ["Cole Porter"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Epilogue", "track_number": 5, "side": "A", "duration": "0:38", "session_date": "1958-12-15", "composers": ["Bill Evans"], "personnel": ["Bill Evans"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Tenderly", "track_number": 6, "side": "B", "duration": "3:29", "session_date": "1958-12-15", "composers": ["Walter Gross"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Peace Piece", "track_number": 7, "side": "B", "duration": "6:37", "session_date": "1958-12-15", "composers": ["Bill Evans"], "personnel": ["Bill Evans"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "What Is There to Say?", "track_number": 8, "side": "B", "duration": "4:49", "session_date": "1958-12-15", "composers": ["Vernon Duke", "E.Y. Harburg"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Oleo", "track_number": 9, "side": "B", "duration": "4:04", "session_date": "1958-12-15", "composers": ["Sonny Rollins"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Epilogue", "track_number": 10, "side": "B", "duration": "0:38", "session_date": "1958-12-15", "composers": ["Bill Evans"], "personnel": ["Bill Evans"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Some Other Time", "track_number": 11, "side": null, "duration": "6:09", "session_date": "1958-12-15", "composers": ["Leonard Bernstein", "Betty Comden", "Adolph Green"], "personnel": ["Bill Evans", "Sam Jones", "Philly Joe Jones"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "32830984-751a-4308-91dc-94771f882ab7",
    "apple_album_id": "1440926168",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/32830984-751a-4308-91dc-94771f882ab7/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Riverside RLP 12-291, recorded Dec 15 1958, released March 1959. The S7 'tracks 1,2,4,5,7,8' rhythm-section mapping uses the original LP numbering and excludes the two solo features 'Lucky to Be Me' and 'Peace Piece' plus the two Epilogues; 'Some Other Time' is a CD bonus. Cover liner blurbs by Miles Davis, Cannonball Adderley, and George Shearing gave the album its title. Apple ID 1440926168 is the Keepnews Collection edition (closest available to the original Riverside master)."
  }
}
```

```json
{
  "id": "gerry-mulligan-what-is-there-to-say-1959",
  "artist": "Gerry Mulligan Quartet",
  "album": "What Is There to Say?",
  "year": 1959,
  "label": "Columbia",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S8", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S8]: the classic pianoless Mulligan quartet, here with Art Farmer on trumpet — the lineal successor to the 1952-53 Mulligan/Baker quartet that defines West Coast cool. inf: distinct from the already-collected 1952 Quartet and the pending Konitz/Mulligan date; a late, polished statement of the pianoless-quartet aesthetic.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-12-17", "1958-12-23", "1959-01-15"],
    "multi_session": true,
    "studio": null,
    "producer": "Teo Macero",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Gerry Mulligan", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1958-12-17", "1958-12-23", "1959-01-15"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Leader; composer of 'Festive Minor', 'As Catch Can', 'Utter Chaos'." },
      { "name": "Art Farmer", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1958-12-17", "1958-12-23", "1959-01-15"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Composer of 'News from Blueport'." },
      { "name": "Bill Crow", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1958-12-17", "1958-12-23", "1959-01-15"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Composer of 'Blueport'." },
      { "name": "Dave Bailey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1958-12-17", "1958-12-23", "1959-01-15"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "What Is There to Say?", "track_number": 1, "side": "A", "duration": "4:03", "session_date": "1959-01-15", "composers": ["Vernon Duke", "E.Y. Harburg"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Just in Time", "track_number": 2, "side": "A", "duration": "4:11", "session_date": "1959-01-15", "composers": ["Jule Styne", "Betty Comden", "Adolph Green"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "News from Blueport", "track_number": 3, "side": "A", "duration": "5:03", "session_date": "1959-01-15", "composers": ["Art Farmer"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Festive Minor", "track_number": 4, "side": "A", "duration": "6:14", "session_date": "1959-01-15", "composers": ["Gerry Mulligan"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "As Catch Can", "track_number": 5, "side": "B", "duration": "3:54", "session_date": "1958-12-23", "composers": ["Gerry Mulligan"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "My Funny Valentine", "track_number": 6, "side": "B", "duration": "4:06", "session_date": "1958-12-23", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Blueport", "track_number": 7, "side": "B", "duration": "8:47", "session_date": "1958-12-17", "composers": ["Bill Crow"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Utter Chaos", "track_number": 8, "side": "B", "duration": "4:23", "session_date": "1958-12-23", "composers": ["Gerry Mulligan"], "personnel": ["Gerry Mulligan", "Art Farmer", "Bill Crow", "Dave Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "13644814-6a76-465d-ac4e-e670b02b0b54",
    "apple_album_id": "186288568",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/13644814-6a76-465d-ac4e-e670b02b0b54/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Columbia, released 1959. Recording-year set to 1959 (title track + half the album cut Jan 15 1959); the other four tracks were recorded Dec 17 & 23, 1958 — recording_dates capture all three. Same pianoless quartet on every track, so track_assignments_complete is true; per-track session dates from S8."
  }
}
```

```json
{
  "id": "gil-evans-gil-evans-and-ten-1957",
  "artist": "Gil Evans",
  "album": "Gil Evans & Ten",
  "year": 1957,
  "label": "Prestige",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "third-stream"],
  "sources": ["S9", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S9]: Gil Evans's debut as a leader, a tentet built on his orchestral-cool palette (Steve Lacy, Lee Konitz, Paul Chambers), recorded during the same period as the Davis collaborations. inf: distinct from the already-pending New Bottle Old Wine; this is Evans's first record under his own name and a cornerstone of arranged cool.",
  "priority": "strong",
  "overlap_risk": "Third-stream / orchestral border.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-09-06", "1957-09-27", "1957-10-10"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Hackensack, NJ",
    "producer": "Bob Weinstock",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Gil Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Leader, arranger; composer of 'Jambangle'." },
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Steve Lacy", "instrument": "soprano saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Jake Koven", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "John Carisi", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Remember"], "session_dates": ["1957-09-06"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Track 1 only." },
      { "name": "Louis Mucci", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Ella Speed", "Big Stuff", "Nobody's Heart", "Just One of Those Things", "If You Could See Me Now", "Jambangle"], "session_dates": ["1957-09-27", "1957-10-10"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Tracks 2-7." },
      { "name": "Jimmy Cleveland", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Bart Varsalona", "instrument": "bass trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Willie Ruff", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Dave Kurtzer", "instrument": "bass clarinet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Source lists bassoon; recorded here as the nearest taxonomy reed. Plays bassoon, outside the taxonomy — flagged." },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Jo Jones", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Remember"], "session_dates": ["1957-09-06"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Track 1 only." },
      { "name": "Nick Stabulas", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Ella Speed", "Big Stuff", "Nobody's Heart", "Just One of Those Things", "If You Could See Me Now", "Jambangle"], "session_dates": ["1957-09-27", "1957-10-10"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Tracks 2-7." }
    ],
    "tracks": [
      { "title": "Remember", "track_number": 1, "side": "A", "duration": "4:33", "session_date": "1957-09-06", "composers": ["Irving Berlin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Ella Speed", "track_number": 2, "side": "A", "duration": "5:50", "session_date": "1957-09-27", "composers": ["Lead Belly", "John A. Lomax"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Big Stuff", "track_number": 3, "side": "A", "duration": "4:49", "session_date": "1957-10-10", "composers": ["Leonard Bernstein"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Nobody's Heart", "track_number": 4, "side": "A", "duration": "4:25", "session_date": "1957-09-27", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Just One of Those Things", "track_number": 5, "side": "B", "duration": "4:25", "session_date": "1957-10-10", "composers": ["Cole Porter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "If You Could See Me Now", "track_number": 6, "side": "B", "duration": "4:18", "session_date": "1957-09-27", "composers": ["Tadd Dameron", "Carl Sigman"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Jambangle", "track_number": 7, "side": "B", "duration": "4:57", "session_date": "1957-10-10", "composers": ["Gil Evans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "7ae2d64b-91b7-4ec9-ac79-f43949e62c65",
    "apple_album_id": "1715961278",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/7ae2d64b-91b7-4ec9-ac79-f43949e62c65/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Prestige PRLP 7120, released early March 1958. Engineer inferred Rudy Van Gelder (Prestige session at Van Gelder Studio, Hackensack, 1957, no engineer named) per the personnel-contract Van Gelder rule; epistemic_production set to inf accordingly. Dave Kurtzer's bassoon and the trumpet/drums personnel swaps between the Sept 6 date (Carisi/Jo Jones) and the Sept 27 + Oct 10 dates (Mucci/Stabulas) per S9."
  }
}
```

```json
{
  "id": "jimmy-giuffre-the-jimmy-giuffre-clarinet-1956",
  "artist": "Jimmy Giuffre",
  "album": "The Jimmy Giuffre Clarinet",
  "year": 1956,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S10", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S10]: Giuffre's chamber-jazz reed experiments with a West Coast cast (Bud Shank, Buddy Collette, Shelly Manne, Shorty Rogers, Jimmy Rowles) recorded at Capitol Studios LA — the dispatch's call for Giuffre's other dates. inf: distinct from the already-pending Jimmy Giuffre 3; explores low-register clarinet and folk-tinged cool the trio later developed.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-03-21", "1956-03-22"],
    "multi_session": true,
    "studio": "Capitol Studios, Los Angeles, CA",
    "producer": "Nesuhi Ertegun",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Jimmy Giuffre", "instrument": "clarinet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Leader/composer; the album foregrounds his clarinet across registers." },
      { "name": "Jimmy Rowles", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Deep Purple", "Fascinating Rhythm"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Piano/celeste on tracks 2 & 7; also plays celesta." },
      { "name": "Ralph Peña", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["My Funny Valentine", "Quiet Cook", "Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Bass on tracks 4, 5, 8." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "selected-tracks", "tracks": ["The Side Pipers", "Fascinating Rhythm"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Drums on tracks 3 & 7." },
      { "name": "Stan Levey", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Quiet Cook", "Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Drums on tracks 5 & 8." },
      { "name": "Bud Shank", "instrument": "flute", "scope": "selected-tracks", "tracks": ["The Side Pipers"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Plays alto flute on track 3; 'alto flute' outside taxonomy, recorded as flute and flagged." },
      { "name": "Buddy Collette", "instrument": "clarinet", "scope": "selected-tracks", "tracks": ["The Side Pipers", "The Sheepherder"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Alto clarinet and flute on tracks 3 & 6; 'alto clarinet' outside taxonomy, recorded as clarinet and flagged." },
      { "name": "Harry Klee", "instrument": "bass clarinet", "scope": "selected-tracks", "tracks": ["The Side Pipers", "The Sheepherder"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Bass clarinet and bass flute on tracks 3 & 6." },
      { "name": "Bob Cooper", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["My Funny Valentine", "Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Tenor sax and oboe on tracks 4 & 8." },
      { "name": "Dave Pell", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["My Funny Valentine", "Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Tenor sax and English horn on tracks 4 & 8." },
      { "name": "Marty Berman", "instrument": "baritone saxophone", "scope": "selected-tracks", "tracks": ["My Funny Valentine", "Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Baritone sax and bassoon on tracks 4 & 8." },
      { "name": "Harry Edison", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Track 8 only." },
      { "name": "Shorty Rogers", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Track 8 only." },
      { "name": "Jack Sheldon", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Down Home"], "session_dates": null, "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Track 8 only." }
    ],
    "tracks": [
      { "title": "So Low", "track_number": 1, "side": "A", "duration": "2:48", "session_date": "1956-03-21", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Deep Purple", "track_number": 2, "side": "A", "duration": "4:38", "session_date": "1956-03-22", "composers": ["Peter DeRose", "Mitchell Parish"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "The Side Pipers", "track_number": 3, "side": "A", "duration": "5:07", "session_date": "1956-03-22", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "My Funny Valentine", "track_number": 4, "side": "A", "duration": "5:03", "session_date": "1956-03-21", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Quiet Cook", "track_number": 5, "side": "B", "duration": "4:18", "session_date": "1956-03-21", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "The Sheepherder", "track_number": 6, "side": "B", "duration": "5:23", "session_date": "1956-03-22", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Fascinating Rhythm", "track_number": 7, "side": "B", "duration": "4:04", "session_date": "1956-03-22", "composers": ["George Gershwin", "Ira Gershwin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Down Home", "track_number": 8, "side": "B", "duration": "5:40", "session_date": "1956-03-21", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "d7f01a94-9dfd-4147-afab-769b7ea41917",
    "apple_album_id": "310652206",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/d7f01a94-9dfd-4147-afab-769b7ea41917/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Atlantic LP 1238, 1956. Highly variable instrumentation: tracks 1, 4, 5 & 8 recorded Mar 21; tracks 2, 3, 6 & 7 recorded Mar 22 (per S10). Many players double on instruments outside the taxonomy (alto flute, alto clarinet, bass flute, oboe, English horn, bassoon, celeste) — primary taxonomy instrument captured with the double flagged in each musician's notes. Track-level personnel left to the personnel-array scope mapping rather than duplicated in each track entry."
  }
}
```

```json
{
  "id": "stan-kenton-contemporary-concepts-1955",
  "artist": "Stan Kenton",
  "album": "Contemporary Concepts",
  "year": 1955,
  "label": "Capitol",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S11", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S11]: Kenton's most swinging mid-1950s big band, almost entirely Bill Holman arrangements, with cool-school soloists (Lennie Niehaus, Charlie Mariano, Bill Perkins, Carl Fontana, Mel Lewis). inf: the Kenton 'progressive jazz' lineage the dispatch named; the Holman book pulls the band toward relaxed, contrapuntal West Coast writing rather than the bombast of earlier Kenton.",
  "priority": "consider",
  "overlap_risk": "Progressive big-band border; some Kenton edges toward bombast rather than cool.",
  "scope_flag": "Big-band 'progressive jazz' — kept for its Holman-arranged, cool-soloist character; flagged as the most big-band-leaning record in this batch.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-07-20", "1955-07-22"],
    "multi_session": true,
    "studio": "Universal Recording, Chicago, IL",
    "producer": "Bob Martin",
    "engineer": "Bill Putnam",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Stan Kenton", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "Leader/conductor; Bill Holman arranged tracks 1-6, Gerry Mulligan arranged 'Limelight'." },
      { "name": "Al Porcino", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Sam Noto", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Ed Leddy", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Bobby Clark", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Stu Williamson", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Carl Fontana", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Bob Fitzpatrick", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Kent Larsen", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Gus Chappell", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Don Kelly", "instrument": "bass trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Charlie Mariano", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Lennie Niehaus", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Bill Perkins", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "David van Kriedt", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Don Davidson", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Ralph Blaze", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Max Bennett", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Mel Lewis", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "What's New?", "track_number": 1, "side": "A", "duration": "5:43", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Stella by Starlight", "track_number": 2, "side": "A", "duration": "5:11", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "I've Got You Under My Skin", "track_number": 3, "side": "A", "duration": "5:30", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Cherokee", "track_number": 4, "side": "B", "duration": "3:06", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Stompin' at the Savoy", "track_number": 5, "side": "B", "duration": "4:36", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Yesterdays", "track_number": 6, "side": "B", "duration": "5:37", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Limelight", "track_number": 7, "side": null, "duration": "3:08", "session_date": null, "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": true, "alternate_take": false, "epistemic_track": "unk", "sources": ["S11"] },
      { "title": "Sunset Tower", "track_number": 8, "side": null, "duration": "3:11", "session_date": null, "composers": [], "personnel": [], "bonus_track": true, "alternate_take": false, "epistemic_track": "unk", "sources": ["S11"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "4e869be5-6aa3-4a5f-b98a-b941cad0da5d",
    "apple_album_id": "724725519",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/4e869be5-6aa3-4a5f-b98a-b941cad0da5d/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Capitol T 666, 1955. Recorded over two days (Jul 20 & 22 1955) at Universal Recording, Chicago. Original LP was the six Bill Holman arrangements (tracks 1-6); 'Limelight' and later 'Opus' titles appear as bonus/CD additions and are flagged bonus_track with epistemic_track unk (their original-album status is uncertain). Track composers not enumerated by S11; left empty rather than inferred. Big band credited on all tracks; per-track session split not documented."
  }
}
```

```json
{
  "id": "paul-desmond-take-ten-1963",
  "artist": "Paul Desmond",
  "album": "Take Ten",
  "year": 1963,
  "label": "RCA Victor",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S12", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S12]: Desmond's first RCA quartet album with Jim Hall, the title track a cousin of 'Take Five' — his airy alto in its most relaxed setting away from Brubeck. inf: the dispatch's Paul Desmond target; the Desmond/Hall partnership is a defining late-cool small-group sound.",
  "priority": "consider",
  "overlap_risk": "Bossa-nova content ('Black Orpheus', 'Samba de Orfeu') reflects the early-'60s Latin vogue.",
  "scope_flag": "Recorded 1963 with some bossa-tinged material; Desmond's cool alto and chamber-quartet approach keep it in scope. Flagged for review.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-06-05", "1963-06-10", "1963-06-12", "1963-06-14", "1963-06-25"],
    "multi_session": true,
    "studio": "Webster Hall, New York City",
    "producer": "George Avakian",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Paul Desmond", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Leader; composer of 'Take Ten', 'El Prince', 'Embarcadero'." },
      { "name": "Jim Hall", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" },
      { "name": "Connie Kay", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" },
      { "name": "Gene Cherico", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["El Prince", "Alone Together", "Embarcadero", "Theme from \"Black Orpheus\"", "Nancy (with the Laughing Face)", "Samba de Orfeu", "The One I Love (Belongs to Somebody Else)"], "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Bass on most tracks (2-8 plus reissue tracks 10-11 per source)." },
      { "name": "Eugene Wright", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Take Ten"], "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Bass on track 1 only." },
      { "name": "George Duvivier", "instrument": "double bass", "scope": "selected-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Bass on the source's 'track 9' (a CD-reissue track); not on the original 8-track LP." }
    ],
    "tracks": [
      { "title": "Take Ten", "track_number": 1, "side": "A", "duration": "3:11", "session_date": null, "composers": ["Paul Desmond"], "personnel": ["Paul Desmond", "Jim Hall", "Eugene Wright", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "El Prince", "track_number": 2, "side": "A", "duration": "3:38", "session_date": null, "composers": ["Paul Desmond"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Alone Together", "track_number": 3, "side": "A", "duration": "6:52", "session_date": null, "composers": ["Arthur Schwartz", "Howard Dietz"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Embarcadero", "track_number": 4, "side": "A", "duration": "4:07", "session_date": null, "composers": ["Paul Desmond"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Theme from \"Black Orpheus\"", "track_number": 5, "side": "B", "duration": "4:14", "session_date": null, "composers": ["Luiz Bonfá", "Antônio Maria"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Nancy (with the Laughing Face)", "track_number": 6, "side": "B", "duration": "6:05", "session_date": null, "composers": ["Jimmy Van Heusen", "Phil Silvers"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Samba de Orfeu", "track_number": 7, "side": "B", "duration": "4:29", "session_date": null, "composers": ["Luiz Bonfá", "Antônio Maria"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "The One I Love (Belongs to Somebody Else)", "track_number": 8, "side": "B", "duration": "5:37", "session_date": null, "composers": ["Isham Jones", "Gus Kahn"], "personnel": ["Paul Desmond", "Jim Hall", "Gene Cherico", "Connie Kay"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "8694465e-0848-33e7-8eea-dc218220db7b",
    "apple_album_id": "304783942",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/8694465e-0848-33e7-8eea-dc218220db7b/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "RCA Victor LPM 2569, 1963. Five June 1963 sessions at Webster Hall; the source does not map LP tracks to specific dates, so session_date is null per track. Bass chair rotates: Eugene Wright on 'Take Ten', Gene Cherico on the rest of the LP, George Duvivier on a CD-reissue-only track. Apple ID 304783942 is the 'Take Ten (Bonus Track Version)' — closest full-album match in the iTunes catalog; the original-master edition is not separately listed."
  }
}
```

```json
{
  "id": "bob-brookmeyer-the-dual-role-of-bob-brookmeyer-1955",
  "artist": "Bob Brookmeyer",
  "album": "The Dual Role of Bob Brookmeyer",
  "year": 1955,
  "label": "Prestige",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S13", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S13]: Brookmeyer's 'dual role' on valve trombone and piano, with cool-school sidemen (Jimmy Raney, Teddy Charles, Teddy Kotick) — the dispatch's Bob Brookmeyer target. inf: a defining showcase for the valve trombonist who anchored the Mulligan and Getz cool groups.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-01-06", "1955-06-30"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Hackensack, NJ (Jun 30 1955); New York City (Jan 6 1954)",
    "producer": "Bob Weinstock",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Bob Brookmeyer", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-01-06", "1955-06-30"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Plays valve trombone (outside taxonomy; recorded as trombone) and piano — the album's 'dual role'." },
      { "name": "Teddy Kotick", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1954-01-06", "1955-06-30"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Bass on both sessions." },
      { "name": "Jimmy Raney", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["Rocky Scotch", "Under the Lilacs", "They Say It's Wonderful", "Potrezebie"], "session_dates": ["1955-06-30"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1-4; composer of 'Potrezebie'." },
      { "name": "Mel Lewis", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Rocky Scotch", "Under the Lilacs", "They Say It's Wonderful", "Potrezebie"], "session_dates": ["1955-06-30"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1-4." },
      { "name": "Teddy Charles", "instrument": "vibraphone", "scope": "selected-tracks", "tracks": ["Revelation", "Star Eyes", "Nobody's Heart", "Loup-Garou"], "session_dates": ["1954-01-06"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 5-8; composer of 'Loup-Garou'." },
      { "name": "Ed Shaughnessy", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Revelation", "Star Eyes", "Nobody's Heart", "Loup-Garou"], "session_dates": ["1954-01-06"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 5-8." },
      { "name": "Nancy Overton", "instrument": "vocals", "scope": "selected-tracks", "tracks": ["Nobody's Heart"], "session_dates": ["1954-01-06"], "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Vocal on track 7 only." }
    ],
    "tracks": [
      { "title": "Rocky Scotch", "track_number": 1, "side": "A", "duration": "4:40", "session_date": "1955-06-30", "composers": ["Bob Brookmeyer"], "personnel": ["Bob Brookmeyer", "Jimmy Raney", "Teddy Kotick", "Mel Lewis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Under the Lilacs", "track_number": 2, "side": "A", "duration": "5:07", "session_date": "1955-06-30", "composers": ["Bob Brookmeyer"], "personnel": ["Bob Brookmeyer", "Jimmy Raney", "Teddy Kotick", "Mel Lewis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "They Say It's Wonderful", "track_number": 3, "side": "A", "duration": "5:49", "session_date": "1955-06-30", "composers": ["Irving Berlin"], "personnel": ["Bob Brookmeyer", "Jimmy Raney", "Teddy Kotick", "Mel Lewis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Potrezebie", "track_number": 4, "side": "A", "duration": "4:49", "session_date": "1955-06-30", "composers": ["Jimmy Raney"], "personnel": ["Bob Brookmeyer", "Jimmy Raney", "Teddy Kotick", "Mel Lewis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Revelation", "track_number": 5, "side": "B", "duration": "5:46", "session_date": "1954-01-06", "composers": ["Gerry Mulligan"], "personnel": ["Bob Brookmeyer", "Teddy Charles", "Teddy Kotick", "Ed Shaughnessy"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Star Eyes", "track_number": 6, "side": "B", "duration": "4:29", "session_date": "1954-01-06", "composers": ["Gene de Paul", "Don Raye"], "personnel": ["Bob Brookmeyer", "Teddy Charles", "Teddy Kotick", "Ed Shaughnessy"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Nobody's Heart", "track_number": 7, "side": "B", "duration": "4:25", "session_date": "1954-01-06", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Bob Brookmeyer", "Teddy Charles", "Teddy Kotick", "Ed Shaughnessy", "Nancy Overton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Loup-Garou", "track_number": 8, "side": "B", "duration": "4:38", "session_date": "1954-01-06", "composers": ["Teddy Charles"], "personnel": ["Bob Brookmeyer", "Teddy Charles", "Teddy Kotick", "Ed Shaughnessy"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "1bd03140-1974-4706-85a9-8b1b2702d87a",
    "apple_album_id": "1443533025",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/1bd03140-1974-4706-85a9-8b1b2702d87a/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Prestige PRLP 7066, 1956. Assembled from two sessions a year apart: tracks 5-8 from Jan 6 1954 (NYC, Teddy Charles vibes group) and tracks 1-4 from Jun 30 1955 (Van Gelder Studio, Jimmy Raney guitar group). Recording-year set to 1955 (the later, album-completing session); note both. Engineer inferred Rudy Van Gelder for the Hackensack date per the contract rule; the Jan 1954 NYC session may have a different engineer, so epistemic_production is inf. Full per-session personnel known, so track_assignments_complete is true."
  }
}
```

```json
{
  "id": "shorty-rogers-martians-come-back-1955",
  "artist": "Shorty Rogers",
  "album": "Martians Come Back!",
  "year": 1955,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S14", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S14]: Shorty Rogers leading a West Coast cast (Jimmy Giuffre, Bud Shank, Lou Levy, Shelly Manne) through his 'Martian'-themed originals on Atlantic — a sequel to the already-collected Shorty Rogers and His Giants. inf: prime Lighthouse-era West Coast small-group/octet writing; distinct from the pending Rogers title.",
  "priority": "consider",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-10-26", "1955-11-03", "1955-12-06", "1955-12-09", "1955-12-16"],
    "multi_session": true,
    "studio": "Los Angeles, CA",
    "producer": "Nesuhi Ertegun",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Shorty Rogers", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Leader; also plays flugelhorn. Doubles trumpet/flugelhorn per source." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Lou Levy", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Martians Come Back", "Astral Alley", "Lotus Bud", "Papouche", "Serenade in Sweets", "Planetarium", "Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Piano on tracks 1-3 and 5-8." },
      { "name": "Pete Jolly", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Dickie's Dream"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Piano on track 4 only." },
      { "name": "Ralph Peña", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Martians Come Back", "Astral Alley", "Lotus Bud", "Papouche", "Serenade in Sweets", "Planetarium", "Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Bass on tracks 1-3 and 5-8." },
      { "name": "Leroy Vinnegar", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Dickie's Dream"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Bass on track 4 only." },
      { "name": "Jimmy Giuffre", "instrument": "clarinet", "scope": "selected-tracks", "tracks": ["Martians Come Back", "Lotus Bud", "Papouche", "Planetarium", "Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Clarinet on tracks 1, 3, 5, 7 & 8." },
      { "name": "Bud Shank", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Dickie's Dream", "Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Alto on tracks 4 & 8." },
      { "name": "Barney Kessel", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["Dickie's Dream"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Track 4 only." },
      { "name": "Conte Candoli", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Astral Alley", "Serenade in Sweets"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Added brass on tracks 2 & 6." },
      { "name": "Pete Candoli", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Astral Alley", "Serenade in Sweets"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Tracks 2 & 6." },
      { "name": "Harry Edison", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Astral Alley", "Serenade in Sweets"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Tracks 2 & 6." },
      { "name": "Don Fagerquist", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Astral Alley", "Serenade in Sweets"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Tracks 2 & 6." },
      { "name": "Bob Enevoldsen", "instrument": "trombone", "scope": "selected-tracks", "tracks": ["Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Valve trombone (outside taxonomy; recorded as trombone) on track 8." },
      { "name": "John Graas", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Track 8 only." },
      { "name": "Paul Sarmento", "instrument": "tuba", "scope": "selected-tracks", "tracks": ["Chant of the Cosmos"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "'tuba' outside taxonomy; track 8 only." }
    ],
    "tracks": [
      { "title": "Martians Come Back", "track_number": 1, "side": "A", "duration": "6:13", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Astral Alley", "track_number": 2, "side": "A", "duration": "4:35", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Lotus Bud", "track_number": 3, "side": "A", "duration": "4:56", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Dickie's Dream", "track_number": 4, "side": "A", "duration": "5:33", "session_date": null, "composers": ["Count Basie", "Lester Young"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Papouche", "track_number": 5, "side": "B", "duration": "4:16", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Serenade in Sweets", "track_number": 6, "side": "B", "duration": "6:35", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Planetarium", "track_number": 7, "side": "B", "duration": "3:37", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Chant of the Cosmos", "track_number": 8, "side": "B", "duration": "6:15", "session_date": null, "composers": [], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "06810f81-fcb5-4d78-a7f1-4e3fe118bbea",
    "apple_album_id": "205603171",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/06810f81-fcb5-4d78-a7f1-4e3fe118bbea/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Atlantic LP 1232, released August 1956. Five LA sessions Oct-Dec 1955; S14 does not map tracks to specific dates, so session_date is null per track. Instrumentation varies by track (core quartet/quintet expanded to octet on track 8 and to a brass-heavy band on tracks 2 & 6). Only 'Dickie's Dream' has a stated composer (Basie/Young); the Rogers originals' composer credits were not given by the source and are left empty rather than inferred. 'tuba' and 'valve trombone' fall outside the taxonomy and are flagged."
  }
}
```

```json
{
  "id": "mel-torme-mel-torme-and-the-marty-paich-dek-tette-1956",
  "artist": "Mel Tormé",
  "album": "Mel Tormé and the Marty Paich Dek-Tette",
  "year": 1956,
  "label": "Bethlehem",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S15", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S15]: Mel Tormé fronting Marty Paich's ten-piece West Coast Dek-Tette (Don Fagerquist, Bob Enevoldsen, Bud Shank, Bob Cooper, Mel Lewis) — the definitive cool-vocal-with-tentet sound. inf: the dispatch's Marty Paich Dek-Tette target; pairs cleanly with the June Christy entry as the West Coast cool-vocal axis.",
  "priority": "consider",
  "overlap_risk": "Vocal-jazz border — Tormé is a singer, but the Dek-Tette arrangements are pure West Coast concert jazz.",
  "scope_flag": "Vocal-led; kept for the Paich Dek-Tette's instrumental cool pedigree. Flagged for review.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-01-16", "1956-01-17", "1956-01-18"],
    "multi_session": true,
    "studio": "Radio Recorders, Hollywood, CA",
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Mel Tormé", "instrument": "vocals", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": ["Mel Torme"], "notes": "Marty Paich arranged and conducted the Dek-Tette (not an instrumentalist on the date)." },
      { "name": "Don Fagerquist", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Pete Candoli", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Bob Enevoldsen", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Valve trombone (outside taxonomy; recorded as trombone)." },
      { "name": "Vince de Rosa", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Lulu's Back in Town", "When the Sun Comes Out", "I Love to Watch the Moonlight", "Fascinating Rhythm", "The Blues", "Carioca", "The Lady Is a Tramp", "I Like to Recognize the Tune"], "session_dates": ["1956-01-16", "1956-01-17"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "French horn on tracks 1-8; replaced by John Cave on 9-12." },
      { "name": "John Cave", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Keeping Myself for You", "Lullaby of Birdland", "When April Comes Again", "Sing for Your Supper"], "session_dates": ["1956-01-18"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "French horn on tracks 9-12." },
      { "name": "Bud Shank", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Also plays flute." },
      { "name": "Bob Cooper", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Lulu's Back in Town", "When the Sun Comes Out", "I Love to Watch the Moonlight", "Fascinating Rhythm", "The Blues", "Carioca", "The Lady Is a Tramp", "I Like to Recognize the Tune"], "session_dates": ["1956-01-16", "1956-01-17"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Tenor on tracks 1-8; replaced by Jack Montrose on 9-12." },
      { "name": "Jack Montrose", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Keeping Myself for You", "Lullaby of Birdland", "When April Comes Again", "Sing for Your Supper"], "session_dates": ["1956-01-18"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Tenor on tracks 9-12." },
      { "name": "Jack Dulong", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Albert Pollan", "instrument": "tuba", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "'tuba' outside taxonomy." },
      { "name": "Red Mitchell", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Mel Lewis", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Lulu's Back in Town", "track_number": 1, "side": "A", "duration": "3:06", "session_date": "1956-01-16", "composers": ["Al Dubin", "Harry Warren"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "When the Sun Comes Out", "track_number": 2, "side": "A", "duration": "3:20", "session_date": null, "composers": ["Harold Arlen", "Ted Koehler"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "I Love to Watch the Moonlight", "track_number": 3, "side": "A", "duration": "2:53", "session_date": null, "composers": ["Josef Myrow", "Bickley Reichner"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Fascinating Rhythm", "track_number": 4, "side": "A", "duration": "2:30", "session_date": null, "composers": ["George Gershwin", "Ira Gershwin"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "The Blues", "track_number": 5, "side": "A", "duration": "3:34", "session_date": null, "composers": ["Duke Ellington"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Carioca", "track_number": 6, "side": "A", "duration": "3:18", "session_date": null, "composers": ["Edward Eliscu", "Gus Kahn", "Vincent Youmans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "The Lady Is a Tramp", "track_number": 7, "side": "B", "duration": "2:54", "session_date": null, "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "I Like to Recognize the Tune", "track_number": 8, "side": "B", "duration": "3:16", "session_date": null, "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Keeping Myself for You", "track_number": 9, "side": "B", "duration": "3:44", "session_date": "1956-01-18", "composers": ["Sidney Clare", "Vincent Youmans"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Lullaby of Birdland", "track_number": 10, "side": "B", "duration": "4:54", "session_date": "1956-01-18", "composers": ["George Shearing", "George David Weiss"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "When April Comes Again", "track_number": 11, "side": "B", "duration": "2:59", "session_date": "1956-01-18", "composers": ["Jerry Livingston", "Doris Schaefer", "Randy Weston"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Sing for Your Supper", "track_number": 12, "side": "B", "duration": "2:23", "session_date": "1956-01-18", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "830ec95a-0870-477d-b380-2b502363bd9c",
    "apple_album_id": "785100286",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/830ec95a-0870-477d-b380-2b502363bd9c/front", "is_original_cover": null, "epistemic": "inf", "notes": "Derived from verified release-group MBID; image not individually opened." }
    ],
    "notes": "Bethlehem, 1956. Recorded at Radio Recorders, Hollywood: tracks 1-8 on Jan 16 & 17 1956, tracks 9-12 on Jan 18 1956. Personnel swap on the third date: Jack Montrose for Bob Cooper (tenor) and John Cave for Vince de Rosa (French horn). Marty Paich arranged/conducted. Production credits (producer/engineer) not stated by source — epistemic_production unk. Apple ID 785100286 is the 'Remastered 2013' Bethlehem edition. Tormé's name also appears as 'Mel Torme' (no accent) in catalog metadata."
  }
}
```

---

## 3. Synthesis Notes

**Must-Haves.** Only one true pillar surfaced in this deeper-bench batch (the obvious must-haves were collected in earlier rounds): *Miles Ahead* (1957) — Miles Davis and Gil Evans's first orchestral collaboration, the direct heir to *Birth of the Cool* and the keystone of the orchestral-cool lineage.

**Hidden Gems.** *Grand Encounter: 2° East / 3° West* (John Lewis, 1956) — AllMusic's Yanow calls it "the ultimate in cool jazz," yet it is far less circulated than the MJQ's own LPs; a perfectly documented single-session quintet (track assignments complete). *The Dual Role of Bob Brookmeyer* — an under-cited but fully-credited two-session date that showcases a defining cool-school voice. *Gil Evans & Ten* — Evans's debut as a leader, overshadowed by the Davis albums but a cornerstone of arranged cool.

**Consensus Picks (3+ sources / cross-confirmed).** Every record here is corroborated across at least a Wikipedia personnel article (S1–S15), the iTunes catalog (S16), and a MusicBrainz release group (S17); *Miles Ahead* and *Grand Encounter* additionally carry AllMusic genre/canon framing (S18). The strongest multi-source standing belongs to *Miles Ahead*, *Focus*, *Fontessa*, *Grand Encounter*, and *Everybody Digs Bill Evans*.

**Single-Source Picks.** *Something Cool* (June Christy) leans hardest on a single thin Wikipedia article — its personnel, full tracklist, and durations are not fully documented there; it is the weakest-sourced record in the batch and is marked accordingly throughout.

**Scope Calls.** *Focus* (1961) and *Take Ten* (1963) sit past the cool window's center of gravity — kept because the arranged/chamber-cool character passes the test question, flagged for review. *Take Ten*'s bossa content ('Black Orpheus', 'Samba de Orfeu') reflects the era's Latin vogue, not fusion. *Everybody Digs Bill Evans* straddles the cool/modal seam ('Peace Piece' is proto-modal) the year before *Kind of Blue* — noted as an overlap rather than a disqualifier. *Contemporary Concepts* is the most big-band-leaning entry; kept for its Holman-arranged, cool-soloist character. *Something Cool* and the *Mel Tormé Dek-Tette* are vocal-led; both kept for their West Coast concert-jazz arranging pedigree (Rugolo; Paich) and flagged as singer dates.

**Gaps Noticed.** Wikipedia personnel articles are excellent for small-group cool (clean quartet/quintet credits) but thin for (a) vocal-cool albums — *Something Cool* lacked durations, a full tracklist, and per-track players; (b) large-ensemble string rosters — *Focus* names only a handful of its twelve-plus string players; and (c) composer credits on West Coast leader-original albums (*Martians Come Back!*, *Contemporary Concepts* gave standards' titles but not composers). The Pacific Jazz / Bethlehem / Atlantic West Coast catalog would benefit from a Tom Lord or Mosaic-booklet pass to recover session-level detail the encyclopedia omits. Production credits (engineer especially) are routinely absent for the Atlantic and Pacific Jazz dates.

**Personnel Coverage.** Full, source-confirmed track-to-personnel assignment was reached on three records — *Grand Encounter*, *What Is There to Say?*, and *The Dual Role of Bob Brookmeyer* (`track_assignments_complete: true`). The small-group dates (*Lee Konitz with Warne Marsh*, *Fontessa*, *Everybody Digs Bill Evans*, *Take Ten*) have complete personnel with per-track lineups populated but are left `false` where a pianoless/solo-track reading was inferred from an absent credit rather than positively stated. The large-ensemble and West Coast multi-session dates (*Miles Ahead*, *Gil Evans & Ten*, *Contemporary Concepts*, *The Jimmy Giuffre Clarinet*, *Martians Come Back!*, *Mel Tormé Dek-Tette*) have complete personnel with selected-track scopes but unmapped session-to-track distribution, so their `tracks[].personnel` arrays are intentionally left empty (the scope mapping lives in the personnel array). *Something Cool* is the only record with genuinely thin personnel — partial player list, no per-track data, no durations — and is flagged as such. Apple Music `collectionId` captured on **15/15**; MusicBrainz release-group MBID (and a derived Cover Art Archive front URL) on **15/15** — both gaps from prior rounds closed. Instruments outside the contract taxonomy (tuba, valve trombone, alto/bass flute, alto clarinet, oboe, English horn, bassoon) were mapped to the nearest taxonomy string and flagged in each musician's `notes`.
