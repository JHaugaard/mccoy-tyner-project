# Cool Jazz / West Coast Jazz — Candidate Records (Round 2)

Growth push toward ~100. 15 candidates, the deeper cool/West Coast bench the POC run flagged as gaps: the Tristano/Konitz cerebral wing, the Los Angeles / Lighthouse scene, and the arranged-cool large-ensemble side. Phase 1 (Judge) then full Phase 2 (Gather) per `docs/personnel-contract.md`.

**Excludes honored:** the 15 albums in `data/dispatch-ledger.json` — including the 5 cool records already collected (*Birth of the Cool*, *Time Out*, *Gerry Mulligan Quartet*, *Chet Baker Sings*, *Art Pepper Meets the Rhythm Section*). None re-surfaced here. **Cull-notes:** no prior verdicts to calibrate against (Segment A had zero culls). **`year` = recording year** (last documented session, per the *Birth of the Cool* / *Chet Baker Sings* precedent in the prior run); differing release years noted in each record's `notes`. `include` is `null` on every record.

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — *Subconscious-Lee* | Encyclopedia | https://en.wikipedia.org/wiki/Subconscious-Lee | Session→track mapping, personnel, tracklist |
| S2 | Wikipedia — *Lennie Tristano* (album) | Encyclopedia | https://en.wikipedia.org/wiki/Lennie_Tristano_(album) | Studio vs live personnel, tracks, dates |
| S3 | Wikipedia — *West Coast Jazz* (Stan Getz album) | Encyclopedia | https://en.wikipedia.org/wiki/West_Coast_Jazz_(Stan_Getz_album) | Personnel, dates, studio, original tracklist |
| S4 | Wikipedia — *Shorty Rogers and His Giants* | Encyclopedia | https://en.wikipedia.org/wiki/Shorty_Rogers_and_His_Giants | Per-session personnel, tracks, producer |
| S5 | Wikipedia — *My Fair Lady* (Shelly Manne album) | Encyclopedia | https://en.wikipedia.org/wiki/My_Fair_Lady_(Shelly_Manne_album) | Trio personnel, date, production, tracks |
| S6 | Wikipedia — *The Jimmy Giuffre 3* | Encyclopedia | https://en.wikipedia.org/wiki/The_Jimmy_Giuffre_3 | Personnel, tracks, composers |
| S7 | JazzDisco.org — Contemporary Records catalog (3500/7500) | Discography | https://www.jazzdisco.org/contemporary-records/catalog-3500-7500-series/ | Lighthouse Vol. 1 per-track piano/conga, date, personnel |
| S8 | Wikipedia — *Lee Konitz Plays with the Gerry Mulligan Quartet* | Encyclopedia | https://en.wikipedia.org/wiki/Lee_Konitz_Plays_with_the_Gerry_Mulligan_Quartet | Per-session personnel, dates, tracks |
| S9 | Wikipedia — *Django* (Modern Jazz Quartet album) | Encyclopedia | https://en.wikipedia.org/wiki/Django_(Modern_Jazz_Quartet_album) | Personnel, three session dates, producers, engineer |
| S10 | Wikipedia — *Art Pepper + Eleven – Modern Jazz Classics* | Encyclopedia | https://en.wikipedia.org/wiki/Art_Pepper_%2B_Eleven_%E2%80%93_Modern_Jazz_Classics | Per-track session dates, tracklist, personnel |
| S11 | Wikipedia — *Jazz at Oberlin* | Encyclopedia | https://en.wikipedia.org/wiki/Jazz_at_Oberlin | Quartet personnel, date, location, tracks |
| S12 | Wikipedia — *The Poll Winners* | Encyclopedia | https://en.wikipedia.org/wiki/The_Poll_Winners | Trio personnel, dates, producer, tracks |
| S13 | Wikipedia — *New Bottle Old Wine* | Encyclopedia | https://en.wikipedia.org/wiki/New_Bottle_Old_Wine | Large-ensemble personnel by track, dates, producer |
| S14 | Wikipedia — *Chet Baker & Crew* | Encyclopedia | https://en.wikipedia.org/wiki/Chet_Baker_%26_Crew | Personnel, dates, tracks, producer |
| S15 | Wikipedia — *Chico Hamilton Quintet featuring Buddy Collette* | Encyclopedia | https://en.wikipedia.org/wiki/Chico_Hamilton_Quintet_featuring_Buddy_Collette | Studio/live personnel, tracks, dates |
| S16 | iTunes Search API (Apple Music) | API | https://itunes.apple.com/search | `collectionId` lookups (Layer 5) |
| S17 | Web search corpus (AllMusic / Discogs / RateYourMusic / Fresh Sound / Internet Archive snippets) | Aggregated search results | — | Cool/West-Coast genre classification; Giuffre Dec 1956 session dates; Art Pepper +Eleven per-session sax/brass rotation; Lighthouse Vol. 1 personnel cross-check |

---

## 2. Candidate Records

```json
{
  "id": "lee-konitz-subconscious-lee-1950",
  "artist": "Lee Konitz",
  "album": "Subconscious-Lee",
  "year": 1950,
  "label": "Prestige",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S1", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S1]: Konitz/Tristano-school sides recorded 1949-1950 (four NYC sessions) and gathered as the Prestige LP Subconscious-Lee; documents Warne Marsh, Billy Bauer, Lennie Tristano, Sal Mosca. obs[S17]: classified as Cool Jazz across collector/critic databases. inf: the foundational document of the Tristano 'cool/cerebral' wing the prior run named as an untouched gap; Konitz's 'Subconscious-Lee' and 'Sound-Lee' are touchstones of the lineless, contrapuntal cool aesthetic.",
  "priority": "strong",
  "overlap_risk": "The Tristano school sits at the proto-cool edge; some of Tristano's work (free 'Intuition') edges toward the avant-garde, but every track here swings with structure.",
  "scope_flag": "Earliest material (Jan 1949) brushes the bebop starting line, but the lineless, vibrato-light cool conception places it firmly post-bebop in spirit.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1949-01-11", "1949-06-28", "1949-09-27", "1950-04-07"],
    "multi_session": true,
    "studio": null,
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-11", "1949-06-28", "1949-09-27", "1950-04-07"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader." },
      { "name": "Warne Marsh", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Marshmallow", "Fishin' Around", "Tautology", "Sound-Lee"], "session_dates": ["1949-06-28", "1949-09-27"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Tracks 6-9 (June 28 and Sept 27 1949 sessions)." },
      { "name": "Billy Bauer", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["Progression", "Tautology", "Retrospection", "Subconscious-Lee", "Judy", "Rebecca", "You Go to My Head", "Ice Cream Konitz", "Palo Alto"], "session_dates": ["1949-01-11", "1950-04-07"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Tracks 1-5 and 10-13." },
      { "name": "Lennie Tristano", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Progression", "Tautology", "Retrospection", "Subconscious-Lee", "Judy"], "session_dates": ["1949-01-11"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Jan 11 1949 session (tracks 1-5)." },
      { "name": "Sal Mosca", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Marshmallow", "Fishin' Around", "Tautology", "Sound-Lee", "Rebecca", "You Go to My Head", "Ice Cream Konitz", "Palo Alto"], "session_dates": ["1949-06-28", "1949-09-27", "1950-04-07"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Tracks 6-13." },
      { "name": "Arnold Fishkin", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1949-01-11", "1949-06-28", "1949-09-27", "1950-04-07"], "epistemic": "obs", "sources": ["S1"], "name_variants": ["Arnold Fishkind"], "notes": "Bass on all four sessions." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Progression", "Tautology", "Subconscious-Lee"], "session_dates": ["1949-01-11"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Drums on tracks 1, 2, 4 only; tracks 3 and 5 of the Jan 1949 session have no drummer listed." },
      { "name": "Denzil Best", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Marshmallow", "Fishin' Around"], "session_dates": ["1949-06-28"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Tracks 6, 7." },
      { "name": "Jeff Morton", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Tautology", "Sound-Lee", "Rebecca", "You Go to My Head", "Ice Cream Konitz", "Palo Alto"], "session_dates": ["1949-09-27", "1950-04-07"], "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Tracks 8-13." }
    ],
    "tracks": [
      { "title": "Progression", "track_number": 1, "side": "A", "duration": "3:00", "session_date": "1949-01-11", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Lennie Tristano", "Arnold Fishkin", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Tautology", "track_number": 2, "side": "A", "duration": "2:45", "session_date": "1949-01-11", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Lennie Tristano", "Arnold Fishkin", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Retrospection", "track_number": 3, "side": "A", "duration": "3:09", "session_date": "1949-01-11", "composers": ["Lennie Tristano"], "personnel": ["Lee Konitz", "Billy Bauer", "Lennie Tristano", "Arnold Fishkin"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Subconscious-Lee", "track_number": 4, "side": "A", "duration": "2:49", "session_date": "1949-01-11", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Lennie Tristano", "Arnold Fishkin", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Judy", "track_number": 5, "side": "A", "duration": "2:56", "session_date": "1949-01-11", "composers": ["Lennie Tristano"], "personnel": ["Lee Konitz", "Billy Bauer", "Lennie Tristano", "Arnold Fishkin"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Marshmallow", "track_number": 6, "side": "A", "duration": "2:55", "session_date": "1949-06-28", "composers": ["Warne Marsh"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Arnold Fishkin", "Denzil Best"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Fishin' Around", "track_number": 7, "side": "B", "duration": "3:47", "session_date": "1949-06-28", "composers": ["Warne Marsh"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Arnold Fishkin", "Denzil Best"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Tautology", "track_number": 8, "side": "B", "duration": "2:56", "session_date": "1949-09-27", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Sound-Lee", "track_number": 9, "side": "B", "duration": "4:08", "session_date": "1949-09-27", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Warne Marsh", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Rebecca", "track_number": 10, "side": "B", "duration": "3:05", "session_date": "1950-04-07", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "You Go to My Head", "track_number": 11, "side": "B", "duration": "2:38", "session_date": "1950-04-07", "composers": ["J. Fred Coots", "Haven Gillespie"], "personnel": ["Lee Konitz", "Billy Bauer", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Ice Cream Konitz", "track_number": 12, "side": "B", "duration": "2:45", "session_date": "1950-04-07", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Palo Alto", "track_number": 13, "side": "B", "duration": "2:31", "session_date": "1950-04-07", "composers": ["Lee Konitz"], "personnel": ["Lee Konitz", "Billy Bauer", "Sal Mosca", "Arnold Fishkin", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "cover_art": [],
    "notes": "Compilation LP (Prestige PRLP 7004, released 1955) drawing on four New York sessions: 1949-01-11 (tracks 1-5), 1949-06-28 (6-7), 1949-09-27 (8-9), 1950-04-07 (10-13). Several of these sides first appeared as 78s on New Jazz/Prestige under Konitz's name. Specific studio not documented in S1; producer Bob Weinstock (Prestige) is plausible but unstated, so production fields are null/unk. Per-track personnel reconstructed from S1's explicit session→track and per-musician mappings; tracks 3 and 5 list no drummer. No clean original-album match in the iTunes catalog (only later reissues/comps), so apple_album_id is null."
  }
}
```

```json
{
  "id": "lennie-tristano-lennie-tristano-1955",
  "artist": "Lennie Tristano",
  "album": "Lennie Tristano",
  "year": 1955,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S2", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S2]: the pianist's landmark self-titled Atlantic album — overdubbed studio sides ('Line Up', 'Requiem', 'Turkish Mambo', 'East Thirty-Second') plus a June 1955 live quartet set with Lee Konitz. obs[S17]: filed as Cool Jazz in critical databases. inf: the central statement of the Tristano cerebral school the POC run flagged as a gap; 'Line Up' (a single-line improvisation over a bass-and-drums overdub) is a defining cool experiment.",
  "priority": "must_have",
  "overlap_risk": "Tristano's tape-speed and overdubbing experiments pull toward the avant-garde edge of cool; the playing nonetheless swings with structure throughout.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1954-01-01/1955-06-11", "1955-06-11"],
    "multi_session": true,
    "studio": "Lennie Tristano's home studio, New York (studio tracks); The Sing-Song Room, Confucius Restaurant, New York (live tracks)",
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Lennie Tristano", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Leader. Studio tracks 2-3 are solo, overdubbed/multitracked piano." },
      { "name": "Peter Ind", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Line Up", "East Thirty-Second"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Studio tracks 1 and 4; overdubbed onto Tristano's piano." },
      { "name": "Jeff Morton", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Line Up", "East Thirty-Second"], "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Studio tracks 1 and 4." },
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["These Foolish Things", "You Go to My Head", "If I Had You", "I Don't Stand a Ghost of a Chance With You", "All the Things You Are"], "session_dates": ["1955-06-11"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Live tracks 5-9." },
      { "name": "Gene Ramey", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["These Foolish Things", "You Go to My Head", "If I Had You", "I Don't Stand a Ghost of a Chance With You", "All the Things You Are"], "session_dates": ["1955-06-11"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Live tracks 5-9." },
      { "name": "Art Taylor", "instrument": "drums", "scope": "selected-tracks", "tracks": ["These Foolish Things", "You Go to My Head", "If I Had You", "I Don't Stand a Ghost of a Chance With You", "All the Things You Are"], "session_dates": ["1955-06-11"], "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Live tracks 5-9." }
    ],
    "tracks": [
      { "title": "Line Up", "track_number": 1, "side": "A", "duration": "3:34", "session_date": null, "composers": ["Lennie Tristano"], "personnel": ["Lennie Tristano", "Peter Ind", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Requiem", "track_number": 2, "side": "A", "duration": "4:53", "session_date": null, "composers": ["Lennie Tristano"], "personnel": ["Lennie Tristano"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Turkish Mambo", "track_number": 3, "side": "A", "duration": "3:41", "session_date": null, "composers": ["Lennie Tristano"], "personnel": ["Lennie Tristano"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "East Thirty-Second", "track_number": 4, "side": "A", "duration": "4:33", "session_date": null, "composers": ["Lennie Tristano"], "personnel": ["Lennie Tristano", "Peter Ind", "Jeff Morton"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "These Foolish Things", "track_number": 5, "side": "B", "duration": "5:46", "session_date": "1955-06-11", "composers": ["Jack Strachey", "Holt Marvell", "Harry Link"], "personnel": ["Lennie Tristano", "Lee Konitz", "Gene Ramey", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "You Go to My Head", "track_number": 6, "side": "B", "duration": "5:20", "session_date": "1955-06-11", "composers": ["J. Fred Coots", "Haven Gillespie"], "personnel": ["Lennie Tristano", "Lee Konitz", "Gene Ramey", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "If I Had You", "track_number": 7, "side": "B", "duration": "6:29", "session_date": "1955-06-11", "composers": ["Jimmy Campbell", "Reg Connelly", "Ted Shapiro"], "personnel": ["Lennie Tristano", "Lee Konitz", "Gene Ramey", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "I Don't Stand a Ghost of a Chance With You", "track_number": 8, "side": "B", "duration": "6:07", "session_date": "1955-06-11", "composers": ["Bing Crosby", "Ned Washington", "Victor Young"], "personnel": ["Lennie Tristano", "Lee Konitz", "Gene Ramey", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "All the Things You Are", "track_number": 9, "side": "B", "duration": "6:11", "session_date": "1955-06-11", "composers": ["Jerome Kern", "Oscar Hammerstein II"], "personnel": ["Lennie Tristano", "Lee Konitz", "Gene Ramey", "Art Taylor"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "cover_art": [],
    "notes": "Atlantic 1224, released 1956. Side A: studio tracks recorded at Tristano's home studio 1954-55 (exact dates not documented; tracks 2-3 are solo overdubbed piano, 1 and 4 add Ind/Morton via overdub). Side B: live quartet recorded 1955-06-11 at the Sing-Song Room, Confucius Restaurant, NYC. No producer credited in S2; production fields null/unk. No confident original-album iTunes match isolated (catalog dominated by comps), so apple_album_id null."
  }
}
```

```json
{
  "id": "stan-getz-west-coast-jazz-1955",
  "artist": "Stan Getz",
  "album": "West Coast Jazz",
  "year": 1955,
  "label": "Norgran",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S3", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S3]: Getz quintet date cut in Hollywood Aug 1955 with Conte Candoli, Lou Levy, Leroy Vinnegar, and Shelly Manne, produced by Norman Granz for Norgran. obs[S17]: catalogued as Cool Jazz. inf: a high-energy cool blowing date pairing Getz's signature light-toned tenor with a West Coast rhythm section; one of his strongest mid-50s small-group statements.",
  "priority": "strong",
  "overlap_risk": "Getz is an East Coast/Tristano-adjacent cool figure recording with West Coast players — a hinge between the two scenes.",
  "scope_flag": "The album title is a documented in-joke (Getz was not part of the West Coast school); west-coast tag reflects the recording locale and the Candoli/Levy/Vinnegar/Manne personnel, not Getz's own affiliation.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-08-10/1955-08-19"],
    "multi_session": true,
    "studio": "Radio Recorders, Hollywood, California",
    "producer": "Norman Granz",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Stan Getz", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Leader." },
      { "name": "Conte Candoli", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "S3 lists Candoli on tracks 1-7 of the expanded numbering; present on all six original-LP tracks." },
      { "name": "Lou Levy", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Leroy Vinnegar", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "East of the Sun (and West of the Moon)", "track_number": 1, "side": "A", "duration": "6:17", "session_date": null, "composers": ["Brooks Bowman"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Four", "track_number": 2, "side": "A", "duration": "7:32", "session_date": null, "composers": ["Miles Davis"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Suddenly It's Spring", "track_number": 3, "side": "A", "duration": "6:56", "session_date": null, "composers": ["Johnny Burke", "Jimmy Van Heusen"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "A Night in Tunisia", "track_number": 4, "side": "B", "duration": "6:09", "session_date": null, "composers": ["Dizzy Gillespie", "Frank Paparelli"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Summertime", "track_number": 5, "side": "B", "duration": "6:04", "session_date": null, "composers": ["George Gershwin", "Ira Gershwin", "DuBose Heyward"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "S-H-I-N-E", "track_number": 6, "side": "B", "duration": "8:53", "session_date": null, "composers": ["Lew Brown", "Ford Dabney", "Cecil Mack"], "personnel": ["Stan Getz", "Conte Candoli", "Lou Levy", "Leroy Vinnegar", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443133429",
    "cover_art": [],
    "notes": "Norgran MG N-1032; recorded at Radio Recorders, Hollywood, over sessions dated Aug 10-19 1955 (S3 does not split tracks to individual dates). Cover by David Stone Martin. Only the six original-LP tracks recorded here; the 1999 Verve CD added eight bonus tracks, excluded. apple_album_id from S16 (iTunes)."
  }
}
```

```json
{
  "id": "shorty-rogers-and-his-giants-1953",
  "artist": "Shorty Rogers",
  "album": "Shorty Rogers and His Giants",
  "year": 1953,
  "label": "RCA Victor",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S4", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S4]: Rogers nonet/octet sides for RCA Victor (Jan 1953) plus a 1954 quartet session, with Art Pepper, Jimmy Giuffre, Hampton Hawes, Shelly Manne. obs[S17]: a canonical West Coast Jazz title. inf: one of the founding documents of the arranged, contrapuntal Los Angeles sound the prior run named as a gap; Rogers's charts and the Lighthouse-circle personnel define the West Coast nonet template.",
  "priority": "must_have",
  "overlap_risk": "Shares the core Lighthouse/Contemporary personnel pool (Manne, Giuffre, Pepper, Hawes) with several other candidates here.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-01-12", "1953-01-15", "1954-10-10"],
    "multi_session": true,
    "studio": "RCA Studios, Hollywood, California",
    "producer": "Jack Lewis",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Shorty Rogers", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Leader and arranger." },
      { "name": "Milt Bernhart", "instrument": "trombone", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks (1-4, 7-10)." },
      { "name": "John Graas", "instrument": "French horn", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks." },
      { "name": "Gene Englund", "instrument": "tuba", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks. 'tuba' is outside the contract taxonomy; recorded as the most specific term per source." },
      { "name": "Art Pepper", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks." },
      { "name": "Jimmy Giuffre", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "inf", "sources": ["S4"], "name_variants": [], "notes": "S4 lists Giuffre without a track restriction; placed on the octet tracks by inference (he composed 'The Pesky Serpent' and 'Indian Club'). Also arranged for the date." },
      { "name": "Hampton Hawes", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks (1-4, 7-10)." },
      { "name": "Pete Jolly", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Joycycle", "The Lady Is a Tramp", "The Goof and I", "My Little Suede Shoes"], "session_dates": ["1954-10-10"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Quartet tracks (5, 6, 11, 12)." },
      { "name": "Curtis Counce", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Morpo", "Bunny", "Powder Puff", "Mambo del Crow", "The Pesky Serpent", "Diablo's Dance", "Pirouette", "Indian Club"], "session_dates": ["1953-01-12", "1953-01-15"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Octet tracks." },
      { "name": "Joe Mondragon", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Joycycle", "The Lady Is a Tramp", "The Goof and I", "My Little Suede Shoes"], "session_dates": ["1954-10-10"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Quartet tracks." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-01-12", "1953-01-15", "1954-10-10"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Drums on all sessions." }
    ],
    "tracks": [
      { "title": "Morpo", "track_number": 1, "side": "A", "duration": "3:27", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Bunny", "track_number": 2, "side": "A", "duration": "3:25", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Powder Puff", "track_number": 3, "side": "A", "duration": "2:49", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Mambo del Crow", "track_number": 4, "side": "A", "duration": "3:02", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Joycycle", "track_number": 5, "side": "A", "duration": "2:39", "session_date": "1954-10-10", "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Pete Jolly", "Joe Mondragon", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "The Lady Is a Tramp", "track_number": 6, "side": "A", "duration": "2:17", "session_date": "1954-10-10", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Shorty Rogers", "Pete Jolly", "Joe Mondragon", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "The Pesky Serpent", "track_number": 7, "side": "B", "duration": "2:38", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Diablo's Dance", "track_number": 8, "side": "B", "duration": "3:17", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Pirouette", "track_number": 9, "side": "B", "duration": "3:10", "session_date": null, "composers": ["Shorty Rogers"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Indian Club", "track_number": 10, "side": "B", "duration": "2:35", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Shorty Rogers", "Milt Bernhart", "John Graas", "Gene Englund", "Art Pepper", "Jimmy Giuffre", "Hampton Hawes", "Curtis Counce", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "The Goof and I", "track_number": 11, "side": "B", "duration": "2:53", "session_date": "1954-10-10", "composers": ["Al Cohn"], "personnel": ["Shorty Rogers", "Pete Jolly", "Joe Mondragon", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "My Little Suede Shoes", "track_number": 12, "side": "B", "duration": "2:46", "session_date": "1954-10-10", "composers": ["Charlie Parker"], "personnel": ["Shorty Rogers", "Pete Jolly", "Joe Mondragon", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1652403010",
    "cover_art": [],
    "notes": "Originally the 10-inch LP RCA Victor LPM-3137 (1953, octet tracks from the Jan 12 & 15 1953 sessions). The 12-inch LPM-1195 (1956) added the four 1954-10-10 quartet tracks (5, 6, 11, 12); this record documents that expanded 12-track sequence. year=1953 reflects the album's identity and the bulk of its material; the 1954 quartet session and 1956 12-inch reissue are noted. track_assignments_complete is false because Giuffre's exact track coverage is an inference (S4 lists him without a restriction). 'tuba' (Gene Englund) is outside the contract taxonomy. apple_album_id from S16."
  }
}
```

```json
{
  "id": "shelly-manne-my-fair-lady-1956",
  "artist": "Shelly Manne",
  "album": "My Fair Lady",
  "year": 1956,
  "label": "Contemporary",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S5", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S5]: the Shelly Manne / André Previn / Leroy Vinnegar trio's jazz reworking of the Lerner & Loewe musical, cut in one Aug 1956 LA session for Contemporary (Koenig/DuNann). obs[S17]: filed as West Coast / Cool Jazz. inf: a landmark and enormous commercial success that proved the 'jazz interpretation of a Broadway score' format and is among the defining West Coast trio records.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-08-17"],
    "multi_session": false,
    "studio": "Contemporary Records, Los Angeles",
    "producer": "Lester Koenig",
    "engineer": "Roy DuNann",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1956-08-17"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "Leader." },
      { "name": "André Previn", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1956-08-17"], "epistemic": "obs", "sources": ["S5"], "name_variants": ["Andre Previn"], "notes": "" },
      { "name": "Leroy Vinnegar", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1956-08-17"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Get Me to the Church on Time", "track_number": 1, "side": "A", "duration": "4:11", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "On the Street Where You Live", "track_number": 2, "side": "A", "duration": "5:37", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "I've Grown Accustomed to Her Face", "track_number": 3, "side": "A", "duration": "3:21", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Wouldn't It Be Loverly", "track_number": 4, "side": "A", "duration": "5:31", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Ascot Gavotte", "track_number": 5, "side": "B", "duration": "4:17", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Show Me", "track_number": 6, "side": "B", "duration": "3:40", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "With a Little Bit of Luck", "track_number": 7, "side": "B", "duration": "6:01", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "I Could Have Danced All Night", "track_number": 8, "side": "B", "duration": "3:00", "session_date": "1956-08-17", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Shelly Manne", "André Previn", "Leroy Vinnegar"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1532292530",
    "cover_art": [],
    "notes": "Full title: 'Modern Jazz Performances of Songs from My Fair Lady' (Contemporary C 3527). Single session 1956-08-17, constant trio. All compositions by Frederick Loewe with lyrics by Alan Jay Lerner. apple_album_id from S16 (the 1956-08-17 original release; a 2023 remaster and a 1957-dated reissue also exist in the catalog)."
  }
}
```

```json
{
  "id": "jimmy-giuffre-the-jimmy-giuffre-3-1956",
  "artist": "Jimmy Giuffre",
  "album": "The Jimmy Giuffre 3",
  "year": 1956,
  "label": "Atlantic",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S6", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S6]: the drummerless trio of Giuffre (clarinet/tenor/baritone), Jim Hall (guitar), and Ralph Peña (bass) for Atlantic, home of 'The Train and the River'. obs[S17]: recorded in Los Angeles Dec 3-4 1956; a touchstone of folk-inflected chamber cool. inf: the defining statement of Giuffre's pastoral, contrapuntal 'blues-folk' cool — a key piece the POC run flagged as missing.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "Quietly experimental drummerless chamber jazz, but unmistakably cool and pre-fusion in spirit.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-12-03", "1956-12-04"],
    "multi_session": true,
    "studio": "Los Angeles",
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Jimmy Giuffre", "instrument": "clarinet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "Leader. Doubles tenor saxophone and baritone saxophone across the album; primary reed varies by track." },
      { "name": "Jim Hall", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": [], "notes": "" },
      { "name": "Ralph Peña", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S6"], "name_variants": ["Ralph Pena"], "notes": "" }
    ],
    "tracks": [
      { "title": "Gotta Dance", "track_number": 1, "side": "A", "duration": "2:29", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Two Kinds of Blues", "track_number": 2, "side": "A", "duration": "5:10", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "The Song Is You", "track_number": 3, "side": "A", "duration": "3:52", "session_date": null, "composers": ["Jerome Kern", "Oscar Hammerstein II"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Crazy She Calls Me", "track_number": 4, "side": "A", "duration": "5:14", "session_date": null, "composers": ["Bob Russell", "Carl Sigman"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Voodoo", "track_number": 5, "side": "A", "duration": "2:48", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "My All", "track_number": 6, "side": "B", "duration": "4:09", "session_date": null, "composers": ["Jimmy Giuffre", "Bob Russell"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "That's the Way It Is", "track_number": 7, "side": "B", "duration": "3:45", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "Crawdad Suite", "track_number": 8, "side": "B", "duration": "7:10", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] },
      { "title": "The Train and the River", "track_number": 9, "side": "B", "duration": "3:31", "session_date": null, "composers": ["Jimmy Giuffre"], "personnel": ["Jimmy Giuffre", "Jim Hall", "Ralph Peña"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S6"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "50268852",
    "cover_art": [],
    "notes": "Atlantic 1254; recorded in Los Angeles Dec 3-4 1956 (dates per S17), released 1957. All originals by Giuffre except tracks 3, 4 and the co-written track 6. S6 does not credit a producer/engineer (Nesuhi Ertegun produced most Atlantic jazz of this period but is unconfirmed here), so production fields are null/unk. Constant drummerless trio; Giuffre's per-track reed (clarinet vs tenor vs baritone) is not broken out in S6. apple_album_id from S16 (catalog lists 11 tracks — includes later additions to the original 9)."
  }
}
```

```json
{
  "id": "howard-rumsey-sunday-jazz-a-la-lighthouse-vol-1-1953",
  "artist": "Howard Rumsey's Lighthouse All-Stars",
  "album": "Sunday Jazz a la Lighthouse, Vol. 1",
  "year": 1953,
  "label": "Contemporary",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S7", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S7]: live Lighthouse All-Stars date recorded at The Lighthouse, Hermosa Beach, Feb 21 1953 (Contemporary C3501), with Maynard Ferguson, Shorty Rogers, Milt Bernhart, Bob Cooper, Jimmy Giuffre, Frank Patchen/Hampton Hawes, Howard Rumsey, Shelly Manne. obs[S17]: catalogued as West Coast Jazz. inf: the document of the Lighthouse club scene — the literal home base of West Coast jazz the prior run named as a gap.",
  "priority": "consider",
  "overlap_risk": "Shares the West Coast personnel pool (Rogers, Giuffre, Manne, Cooper) with other candidates; value here is as the live scene document rather than a tightly-arranged studio statement.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-02-21"],
    "multi_session": false,
    "studio": "The Lighthouse, Hermosa Beach, California (live)",
    "producer": "Lester Koenig",
    "engineer": null,
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Howard Rumsey", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Leader." },
      { "name": "Maynard Ferguson", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Shorty Rogers", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Milt Bernhart", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Bob Cooper", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Giuffre", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Frank Patchen", "instrument": "piano", "scope": "selected-tracks", "tracks": ["Four Others", "Creme De Menthe", "Viva Zapata!", "Bernie's Tune", "Solitaire"], "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Piano on tracks 1, 3-6 per S7." },
      { "name": "Hampton Hawes", "instrument": "piano", "scope": "selected-tracks", "tracks": ["All The Things You Are", "Morgan Davis", "La Soncailli"], "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Piano on tracks 2, 7, 8 per S7." },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "" },
      { "name": "Carlos Vidal", "instrument": "congas", "scope": "selected-tracks", "tracks": ["Viva Zapata!"], "session_dates": ["1953-02-21"], "epistemic": "obs", "sources": ["S7"], "name_variants": [], "notes": "Conga drums on track 4 ('Viva Zapata!') only." }
    ],
    "tracks": [
      { "title": "Four Others", "track_number": 1, "side": "A", "duration": null, "session_date": "1953-02-21", "composers": [], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Frank Patchen", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "All The Things You Are", "track_number": 2, "side": "A", "duration": null, "session_date": "1953-02-21", "composers": ["Jerome Kern", "Oscar Hammerstein II"], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Hampton Hawes", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Creme De Menthe", "track_number": 3, "side": "A", "duration": null, "session_date": "1953-02-21", "composers": [], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Frank Patchen", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Viva Zapata!", "track_number": 4, "side": "A", "duration": null, "session_date": "1953-02-21", "composers": ["Shorty Rogers"], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Frank Patchen", "Shelly Manne", "Carlos Vidal"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Bernie's Tune", "track_number": 5, "side": "B", "duration": null, "session_date": "1953-02-21", "composers": ["Bernie Miller"], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Frank Patchen", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Solitaire", "track_number": 6, "side": "B", "duration": null, "session_date": "1953-02-21", "composers": [], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Frank Patchen", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "Morgan Davis", "track_number": 7, "side": "B", "duration": null, "session_date": "1953-02-21", "composers": [], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Hampton Hawes", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] },
      { "title": "La Soncailli", "track_number": 8, "side": "B", "duration": null, "session_date": "1953-02-21", "composers": [], "personnel": ["Howard Rumsey", "Maynard Ferguson", "Shorty Rogers", "Milt Bernhart", "Bob Cooper", "Jimmy Giuffre", "Hampton Hawes", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S7"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1769227404",
    "cover_art": [],
    "notes": "Contemporary C3501, recorded live at The Lighthouse, Hermosa Beach, 1953-02-21; reissued OJC-151 (1984). Track titles and per-track piano/conga assignments per S7 (JazzDisco). Durations and most composer credits not given by S7; 'Bernie's Tune' (Bernie Miller) and 'All the Things You Are' (Kern/Hammerstein) and 'Viva Zapata!' (Rogers) are standard attributions. Producer Lester Koenig inferred as Contemporary's founder/producer (epistemic_production inf). The horn front line plays as an ensemble across all tracks; only piano (Patchen/Hawes) and conga (Vidal, track 4) rotate. apple_album_id from S16."
  }
}
```

```json
{
  "id": "lee-konitz-plays-with-the-gerry-mulligan-quartet-1953",
  "artist": "Lee Konitz",
  "album": "Lee Konitz Plays with the Gerry Mulligan Quartet",
  "year": 1953,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S8", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S8]: Lee Konitz guesting with the pianoless Gerry Mulligan Quartet (Mulligan, Chet Baker) across three Jan-Feb 1953 LA sessions for Pacific Jazz, produced by Richard Bock. obs[S17]: a canonical West Coast cool date (also issued as 'Konitz Meets Mulligan'). inf: a summit of the two leading cool-school voices — Konitz's Tristano-line alto over Mulligan's drummerless contrapuntal quartet.",
  "priority": "strong",
  "overlap_risk": "Closely related to the collected 'Gerry Mulligan Quartet' (same pianoless quartet, same producer, overlapping repertoire like 'Bernie's Tune'); the distinguishing element is Konitz's presence.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-01-23", "1953-01-30", "1953-02-01"],
    "multi_session": true,
    "studio": "The Haig, Hollywood (live, 1953-01-23); unidentified Los Angeles studio (1953-01-30); Phil Turetsky's home studio, Los Angeles (1953-02-01)",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Lee Konitz", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-01-23", "1953-01-30", "1953-02-01"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Featured soloist (leader on the reissue billing)." },
      { "name": "Gerry Mulligan", "instrument": "baritone saxophone", "scope": "selected-tracks", "tracks": ["Too Marvelous for Words", "Lover Man", "I'll Remember April", "These Foolish Things", "All the Things You Are", "Bernie's Tune"], "session_dates": ["1953-01-23"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Tracks 1-6 only (the Jan 23 Haig session)." },
      { "name": "Chet Baker", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Too Marvelous for Words", "Lover Man", "I'll Remember April", "These Foolish Things", "All the Things You Are", "Bernie's Tune"], "session_dates": ["1953-01-23"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Tracks 1-6 only." },
      { "name": "Carson Smith", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Too Marvelous for Words", "Lover Man", "I'll Remember April", "These Foolish Things", "All the Things You Are", "Bernie's Tune", "Almost Like Being in Love", "Sextet", "Broadway"], "session_dates": ["1953-01-23", "1953-01-30"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Tracks 1-9." },
      { "name": "Joe Mondragon", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["I Can't Believe That You're in Love with Me", "Oh, Lady Be Good!"], "session_dates": ["1953-02-01"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Tracks 10-12 (Feb 1 session, including the 'Oh, Lady Be Good!' alternate)." },
      { "name": "Larry Bunker", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-01-23", "1953-01-30", "1953-02-01"], "epistemic": "obs", "sources": ["S8"], "name_variants": [], "notes": "Drums across all three sessions." }
    ],
    "tracks": [
      { "title": "Too Marvelous for Words", "track_number": 1, "side": "A", "duration": "3:36", "session_date": "1953-01-23", "composers": ["Richard A. Whiting", "Johnny Mercer"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Lover Man", "track_number": 2, "side": "A", "duration": "3:01", "session_date": "1953-01-23", "composers": ["Jimmy Davis", "Roger Ramirez", "Jimmy Sherman"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "I'll Remember April", "track_number": 3, "side": "A", "duration": "4:08", "session_date": "1953-01-23", "composers": ["Gene de Paul", "Patricia Johnston", "Don Raye"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "These Foolish Things", "track_number": 4, "side": "A", "duration": "3:15", "session_date": "1953-01-23", "composers": ["Jack Strachey", "Holt Marvell", "Harry Link"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "All the Things You Are", "track_number": 5, "side": "A", "duration": "3:55", "session_date": "1953-01-23", "composers": ["Jerome Kern", "Oscar Hammerstein II"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Bernie's Tune", "track_number": 6, "side": "A", "duration": "3:32", "session_date": "1953-01-23", "composers": ["Bernie Miller", "Jerry Leiber", "Mike Stoller"], "personnel": ["Lee Konitz", "Gerry Mulligan", "Chet Baker", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Almost Like Being in Love", "track_number": 7, "side": "B", "duration": "2:50", "session_date": "1953-01-30", "composers": ["Frederick Loewe", "Alan Jay Lerner"], "personnel": ["Lee Konitz", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Sextet", "track_number": 8, "side": "B", "duration": "2:59", "session_date": "1953-01-30", "composers": ["Gerry Mulligan"], "personnel": ["Lee Konitz", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Broadway", "track_number": 9, "side": "B", "duration": "2:54", "session_date": "1953-01-30", "composers": ["Bill Bird", "Teddy McRae", "Henri Woode"], "personnel": ["Lee Konitz", "Carson Smith", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "I Can't Believe That You're in Love with Me", "track_number": 10, "side": "B", "duration": "3:05", "session_date": "1953-02-01", "composers": ["Jimmy McHugh", "Clarence Gaskill"], "personnel": ["Lee Konitz", "Joe Mondragon", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Oh, Lady Be Good!", "track_number": 11, "side": "B", "duration": "2:38", "session_date": "1953-02-01", "composers": ["George Gershwin", "Ira Gershwin"], "personnel": ["Lee Konitz", "Joe Mondragon", "Larry Bunker"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S8"] },
      { "title": "Oh, Lady Be Good!", "track_number": 12, "side": "B", "duration": "1:52", "session_date": "1953-02-01", "composers": ["George Gershwin", "Ira Gershwin"], "personnel": ["Lee Konitz", "Joe Mondragon", "Larry Bunker"], "bonus_track": false, "alternate_take": true, "epistemic_track": "obs", "sources": ["S8"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "cover_art": [],
    "notes": "Pacific Jazz (later World Pacific) original 1953 release; widely reissued as 'Konitz Meets Mulligan'. Three sessions: Jan 23 1953 (full quartet + Konitz, live at The Haig, tracks 1-6), Jan 30 1953 (Konitz with bass/drums only, tracks 7-9), Feb 1 1953 (Konitz with Mondragon/Bunker, tracks 10-12). Mulligan and Baker appear only on tracks 1-6. Track 12 is an alternate take of 'Oh, Lady Be Good!'. No confident original-album iTunes match isolated, so apple_album_id null."
  }
}
```

```json
{
  "id": "modern-jazz-quartet-django-1955",
  "artist": "The Modern Jazz Quartet",
  "album": "Django",
  "year": 1955,
  "label": "Prestige",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S9", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S9]: the MJQ (Milt Jackson, John Lewis, Percy Heath, Kenny Clarke) across three sessions 1953-55 for Prestige, Van Gelder-engineered, including the title elegy 'Django'. obs[S17]: filed as Cool Jazz. inf: the quartet's defining early statement and a cornerstone of the chamber/cool wing — Lewis's classically-poised compositions over a swinging bop rhythm core.",
  "priority": "must_have",
  "overlap_risk": "The MJQ straddles cool and third-stream; Kenny Clarke's presence and the Van Gelder/Prestige setting give it a hard-bop-adjacent rhythmic core.",
  "scope_flag": "Third-stream-leaning chamber jazz, but swings with structure throughout and sits squarely in the cool tradition.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-06-25", "1954-12-23", "1955-01-09"],
    "multi_session": true,
    "studio": "New York City (1953-06-25); Van Gelder Studio, Hackensack, New Jersey (1954-12-23 and 1955-01-09)",
    "producer": "Bob Weinstock",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Milt Jackson", "instrument": "vibraphone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-06-25", "1954-12-23", "1955-01-09"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "John Lewis", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-06-25", "1954-12-23", "1955-01-09"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Musical director; composer of most originals." },
      { "name": "Percy Heath", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-06-25", "1954-12-23", "1955-01-09"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "" },
      { "name": "Kenny Clarke", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-06-25", "1954-12-23", "1955-01-09"], "epistemic": "obs", "sources": ["S9"], "name_variants": [], "notes": "Original MJQ drummer (left in 1955; Connie Kay succeeded him after these sessions)." }
    ],
    "tracks": [
      { "title": "Django", "track_number": 1, "side": "A", "duration": "7:03", "session_date": null, "composers": ["John Lewis"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "One Bass Hit", "track_number": 2, "side": "A", "duration": "2:59", "session_date": null, "composers": ["Dizzy Gillespie"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "La Ronde Suite", "track_number": 3, "side": "A", "duration": "9:38", "session_date": null, "composers": ["John Lewis"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "The Queen's Fancy", "track_number": 4, "side": "B", "duration": "3:12", "session_date": null, "composers": ["John Lewis"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Delaunay's Dilemma", "track_number": 5, "side": "B", "duration": "4:01", "session_date": null, "composers": ["John Lewis"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Autumn in New York", "track_number": 6, "side": "B", "duration": "3:40", "session_date": null, "composers": ["Vernon Duke"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "But Not for Me", "track_number": 7, "side": "B", "duration": "3:44", "session_date": null, "composers": ["George Gershwin", "Ira Gershwin"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] },
      { "title": "Milano", "track_number": 8, "side": "B", "duration": "4:23", "session_date": null, "composers": ["John Lewis"], "personnel": ["Milt Jackson", "John Lewis", "Percy Heath", "Kenny Clarke"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S9"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": null,
    "cover_art": [],
    "notes": "Prestige PRLP 7057, compiled and released 1956 from three sessions: 1953-06-25 (NYC), 1954-12-23 and 1955-01-09 (Van Gelder, Hackensack). year=1955 reflects the latest session (per the Birth-of-the-Cool last-session precedent); release 1956. S9 does not map individual tracks to sessions, so per-track session_date is null; the constant quartet means track personnel are complete. Producers per S9: Ira Gitler (tracks 4-7) and Bob Weinstock (tracks 1-3, 8) — Weinstock recorded as primary producer with the split noted here. iTunes catalog returned only a later single for 'Django', so apple_album_id null."
  }
}
```

```json
{
  "id": "art-pepper-art-pepper-plus-eleven-1959",
  "artist": "Art Pepper",
  "album": "Art Pepper + Eleven – Modern Jazz Classics",
  "year": 1959,
  "label": "Contemporary",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S10", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S10]: Art Pepper fronting an eleven-piece ensemble in Marty Paich's arrangements of bop/cool standards, three Contemporary sessions in 1959. obs[S17]: filed as West Coast / Cool Jazz. inf: the definitive 'arranged West Coast' statement — Paich's tightly-voiced charts (the 'Dek-tette' sound) with Pepper as featured soloist; a different animal from the collected 'Meets the Rhythm Section'.",
  "priority": "strong",
  "overlap_risk": "Second Art Pepper leader date in the canon (alongside the collected 'Meets the Rhythm Section'); distinct in being a large-ensemble arranged record rather than a quartet blowing date.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1959-03-14", "1959-03-28", "1959-05-12"],
    "multi_session": true,
    "studio": "Contemporary Records studio, Los Angeles",
    "producer": "Lester Koenig",
    "engineer": "Roy DuNann",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Art Pepper", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Leader and featured soloist. Doubles tenor saxophone and clarinet (clarinet feature on 'Anthropology')." },
      { "name": "Jack Sheldon", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Pete Candoli", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Opus De Funk", "'Round Midnight", "Walkin' Shoes", "Airegin"], "session_dates": ["1959-03-14"], "epistemic": "obs", "sources": ["S10", "S17"], "name_variants": [], "notes": "March 14 session tracks (3, 4, 8, 10)." },
      { "name": "Al Porcino", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Move", "Groovin' High", "Four Brothers", "Shawnuff", "Bernie's Tune", "Anthropology", "Walkin'", "Donna Lee"], "session_dates": ["1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10", "S17"], "name_variants": [], "notes": "March 28 and May 12 session tracks." },
      { "name": "Dick Nash", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Bob Enevoldsen", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "Plays valve trombone; also doubles tenor saxophone in the section." },
      { "name": "Vincent DeRosa", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Herb Geller", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Opus De Funk", "'Round Midnight", "Walkin' Shoes", "Airegin"], "session_dates": ["1959-03-14"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "March 14 session (tracks 3, 4, 8, 10) per S17 per-session sax rotation." },
      { "name": "Bud Shank", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Groovin' High", "Shawnuff", "Anthropology", "Donna Lee"], "session_dates": ["1959-03-28"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "March 28 session (tracks 2, 6, 9, 12) per S17." },
      { "name": "Charlie Kennedy", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["Move", "Four Brothers", "Bernie's Tune", "Walkin'"], "session_dates": ["1959-05-12"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "May 12 session (tracks 1, 5, 7, 11) per S17." },
      { "name": "Bill Perkins", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Groovin' High", "Opus De Funk", "'Round Midnight", "Shawnuff", "Walkin' Shoes", "Anthropology", "Airegin", "Donna Lee"], "session_dates": ["1959-03-14", "1959-03-28"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "March 14 and March 28 sessions per S17." },
      { "name": "Richie Kamuca", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Move", "Four Brothers", "Bernie's Tune", "Walkin'"], "session_dates": ["1959-05-12"], "epistemic": "obs", "sources": ["S17"], "name_variants": [], "notes": "May 12 session per S17." },
      { "name": "Med Flory", "instrument": "baritone saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Russ Freeman", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Joe Mondragon", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" },
      { "name": "Mel Lewis", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1959-03-14", "1959-03-28", "1959-05-12"], "epistemic": "obs", "sources": ["S10"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Move", "track_number": 1, "side": "A", "duration": "3:26", "session_date": "1959-05-12", "composers": ["Denzil Best"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Groovin' High", "track_number": 2, "side": "A", "duration": "3:22", "session_date": "1959-03-28", "composers": ["Dizzy Gillespie"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Opus De Funk", "track_number": 3, "side": "A", "duration": "3:13", "session_date": "1959-03-14", "composers": ["Horace Silver"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "'Round Midnight", "track_number": 4, "side": "A", "duration": "3:32", "session_date": "1959-03-14", "composers": ["Thelonious Monk", "Cootie Williams", "Bernie Hanighen"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Four Brothers", "track_number": 5, "side": "A", "duration": "2:57", "session_date": "1959-05-12", "composers": ["Jimmy Giuffre"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Shawnuff", "track_number": 6, "side": "A", "duration": "2:58", "session_date": "1959-03-28", "composers": ["Charlie Parker", "Dizzy Gillespie"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Bernie's Tune", "track_number": 7, "side": "B", "duration": "2:41", "session_date": "1959-05-12", "composers": ["Bernie Miller"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Walkin' Shoes", "track_number": 8, "side": "B", "duration": "3:31", "session_date": "1959-03-14", "composers": ["Gerry Mulligan"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Anthropology", "track_number": 9, "side": "B", "duration": "3:19", "session_date": "1959-03-28", "composers": ["Charlie Parker", "Dizzy Gillespie"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Airegin", "track_number": 10, "side": "B", "duration": "3:01", "session_date": "1959-03-14", "composers": ["Sonny Rollins"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Walkin'", "track_number": 11, "side": "B", "duration": "5:15", "session_date": "1959-05-12", "composers": ["Richard Carpenter"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] },
      { "title": "Donna Lee", "track_number": 12, "side": "B", "duration": "3:23", "session_date": "1959-03-28", "composers": ["Charlie Parker"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S10"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443544593",
    "cover_art": [],
    "notes": "Contemporary M 3568 / S 7568; recorded over three 1959 sessions and released 1960. Session→track mapping (per S10): March 14 = tracks 3, 4, 8, 10; March 28 = 2, 6, 9, 12; May 12 = 1, 5, 7, 11. Marty Paich arranged and conducted all tracks (not listed as an instrumentalist). The saxophone and second-trumpet chairs rotated by session (per S17): Pepper/Sheldon/Nash/Enevoldsen/DeRosa/Flory plus rhythm (Freeman/Mondragon/Mel Lewis) are constant; Geller/Perkins (Mar 14), Shank/Perkins (Mar 28), Kennedy/Kamuca (May 12) and Candoli (Mar 14)/Porcino (Mar 28 & May 12) rotate. Track-level personnel arrays left empty because the per-track ensemble follows the session rotation rather than per-name confirmation, so track_assignments_complete is false. Producer Lester Koenig and engineer Roy DuNann inferred as Contemporary's standard team (not explicit in S10). apple_album_id from S16."
  }
}
```

```json
{
  "id": "dave-brubeck-jazz-at-oberlin-1953",
  "artist": "The Dave Brubeck Quartet",
  "album": "Jazz at Oberlin",
  "year": 1953,
  "label": "Fantasy",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S11", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S11]: the Brubeck/Desmond quartet (with Ron Crotty, Lloyd Davis) recorded live at Finney Chapel, Oberlin College, March 2 1953 for Fantasy. obs[S17]: a canonical Cool / West Coast live album. inf: a landmark early-Brubeck concert document — the quartet's interplay on extended standards is among the most celebrated cool live records, predating the collected 'Time Out' by six years.",
  "priority": "strong",
  "overlap_risk": "Second Dave Brubeck Quartet album in the canon (alongside the collected 'Time Out'); distinct as an early live concert rather than the studio odd-meter project.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1953-03-02"],
    "multi_session": false,
    "studio": "Finney Chapel, Oberlin College, Oberlin, Ohio (live)",
    "producer": null,
    "engineer": null,
    "epistemic_production": "unk",
    "personnel": [
      { "name": "Dave Brubeck", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-03-02"], "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "Leader." },
      { "name": "Paul Desmond", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-03-02"], "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Ron Crotty", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-03-02"], "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" },
      { "name": "Lloyd Davis", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1953-03-02"], "epistemic": "obs", "sources": ["S11"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "These Foolish Things (Remind Me of You)", "track_number": 1, "side": "A", "duration": "6:25", "session_date": "1953-03-02", "composers": ["Holt Marvell", "Jack Strachey", "Harry Link"], "personnel": ["Dave Brubeck", "Paul Desmond", "Ron Crotty", "Lloyd Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Perdido", "track_number": 2, "side": "A", "duration": "8:03", "session_date": "1953-03-02", "composers": ["Juan Tizol", "Hans Lengsfelder", "Ervin Drake"], "personnel": ["Dave Brubeck", "Paul Desmond", "Ron Crotty", "Lloyd Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "Stardust", "track_number": 3, "side": "A", "duration": "6:32", "session_date": "1953-03-02", "composers": ["Hoagy Carmichael", "Mitchell Parish"], "personnel": ["Dave Brubeck", "Paul Desmond", "Ron Crotty", "Lloyd Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "The Way You Look Tonight", "track_number": 4, "side": "B", "duration": "7:43", "session_date": "1953-03-02", "composers": ["Jerome Kern", "Dorothy Fields"], "personnel": ["Dave Brubeck", "Paul Desmond", "Ron Crotty", "Lloyd Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] },
      { "title": "How High the Moon", "track_number": 5, "side": "B", "duration": "9:04", "session_date": "1953-03-02", "composers": ["Nancy Hamilton", "Morgan Lewis"], "personnel": ["Dave Brubeck", "Paul Desmond", "Ron Crotty", "Lloyd Davis"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S11"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1442860850",
    "cover_art": [],
    "notes": "Fantasy F 3245; recorded live at Finney Chapel, Oberlin College, 1953-03-02. The original 10-inch LP omitted 'How High the Moon' and reordered the rest; the 12-inch (documented here) carries all five tracks. No producer/engineer named in S11; production fields null/unk. apple_album_id from S16 (OJC remaster)."
  }
}
```

```json
{
  "id": "barney-kessel-the-poll-winners-1957",
  "artist": "Barney Kessel",
  "album": "The Poll Winners",
  "year": 1957,
  "label": "Contemporary",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S12", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S12]: the trio of Barney Kessel (guitar), Ray Brown (bass), and Shelly Manne (drums) — all then-current jazz-poll winners — recorded for Contemporary March 1957 (Lester Koenig). obs[S17]: filed as West Coast / Cool Jazz. inf: a benchmark West Coast guitar-trio date; light-swinging, conversational, and a model for the chamber-trio format.",
  "priority": "consider",
  "overlap_risk": "Light, standards-driven trio jazz that some might file as mainstream/swing rather than core cool; the West Coast personnel and Contemporary aesthetic keep it in style.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-03-18", "1957-03-19"],
    "multi_session": true,
    "studio": "Contemporary Records studio, Los Angeles, California",
    "producer": "Lester Koenig",
    "engineer": "Roy DuNann",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Barney Kessel", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-03-18", "1957-03-19"], "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "Leader." },
      { "name": "Ray Brown", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-03-18", "1957-03-19"], "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" },
      { "name": "Shelly Manne", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-03-18", "1957-03-19"], "epistemic": "obs", "sources": ["S12"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Jordu", "track_number": 1, "side": "A", "duration": "3:27", "session_date": null, "composers": ["Duke Jordan"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Satin Doll", "track_number": 2, "side": "A", "duration": "6:30", "session_date": null, "composers": ["Duke Ellington", "Billy Strayhorn", "Johnny Mercer"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "It Could Happen to You", "track_number": 3, "side": "A", "duration": "4:23", "session_date": null, "composers": ["Jimmy Van Heusen", "Johnny Burke"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Mean to Me", "track_number": 4, "side": "A", "duration": "6:28", "session_date": null, "composers": ["Fred E. Ahlert", "Roy Turk"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Don't Worry 'bout Me", "track_number": 5, "side": "A", "duration": "4:34", "session_date": null, "composers": ["Rube Bloom", "Ted Koehler"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "On Green Dolphin Street", "track_number": 6, "side": "B", "duration": "4:02", "session_date": null, "composers": ["Bronisław Kaper", "Ned Washington"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "You Go to My Head", "track_number": 7, "side": "B", "duration": "4:22", "session_date": null, "composers": ["J. Fred Coots", "Haven Gillespie"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Minor Mood", "track_number": 8, "side": "B", "duration": "3:18", "session_date": null, "composers": ["Barney Kessel"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] },
      { "title": "Nagasaki", "track_number": 9, "side": "B", "duration": "3:05", "session_date": null, "composers": ["Harry Warren", "Mort Dixon"], "personnel": ["Barney Kessel", "Ray Brown", "Shelly Manne"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S12"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443860013",
    "cover_art": [],
    "notes": "Contemporary C 3535; recorded 1957-03-18 and 03-19 (S12 does not split tracks to dates). Constant trio. Engineer Roy DuNann inferred as Contemporary's standard engineer (not explicit in S12), hence epistemic_production inf. First of a 'Poll Winners' series. apple_album_id from S16 (multiple near-identical reissues exist; the 1443860013 OJC-era release chosen)."
  }
}
```

```json
{
  "id": "gil-evans-new-bottle-old-wine-1958",
  "artist": "Gil Evans",
  "album": "New Bottle Old Wine",
  "year": 1958,
  "label": "World Pacific",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz"],
  "sources": ["S13", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S13]: Gil Evans's orchestral arrangements of jazz standards (W.C. Handy to Charlie Parker) with Cannonball Adderley as featured alto soloist, recorded NYC 1958 (George Avakian). obs[S17]: filed as Cool Jazz. inf: a cornerstone of the arranged/orchestral cool lineage that runs from Birth of the Cool through the Evans-Davis collaborations; the single-soloist-plus-orchestra concept in concentrated form.",
  "priority": "consider",
  "overlap_risk": "Large orchestral arranged jazz — adjacent to third-stream and to the Gil Evans/Miles Davis orchestral records; lighter on the small-group 'swing' some associate with core cool.",
  "scope_flag": "Big-band-scale arranged date rather than a combo; included for its direct lineage from Birth of the Cool's arranged-cool aesthetic, with the orchestral character flagged for John.",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-04-09", "1958-05-02", "1958-05-21", "1958-05-26"],
    "multi_session": true,
    "studio": "New York City",
    "producer": "George Avakian",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Gil Evans", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Arranger, conductor, and piano." },
      { "name": "Cannonball Adderley", "instrument": "alto saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": ["Julian Adderley"], "notes": "Featured soloist throughout." },
      { "name": "Johnny Coles", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Willow Tree", "Lester Leaps In", "'Round Midnight"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1-3, 5-6." },
      { "name": "Louis Mucci", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Willow Tree", "Lester Leaps In", "'Round Midnight"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1-3, 5-6." },
      { "name": "Ernie Royal", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Willow Tree", "Lester Leaps In", "'Round Midnight"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1-3, 5-6." },
      { "name": "Clyde Reasinger", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Struttin' With Some Barbeque", "Manteca!", "Bird Feathers"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 4, 7-8." },
      { "name": "Joe Bennett", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Frank Rehak", "instrument": "trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Tom Mitchell", "instrument": "bass trombone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Listed as trombone in S13; the section's lowest trombone chair." },
      { "name": "Julius Watkins", "instrument": "French horn", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Harvey Phillips", "instrument": "tuba", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Lester Leaps In", "'Round Midnight"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1, 2, 5-6. 'tuba' is outside the contract taxonomy." },
      { "name": "Bill Barber", "instrument": "tuba", "scope": "selected-tracks", "tracks": ["Willow Tree", "Struttin' With Some Barbeque", "Manteca!", "Bird Feathers"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 3, 4, 7-8. 'tuba' is outside the contract taxonomy." },
      { "name": "Jerry Sanfino", "instrument": "flute", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Lester Leaps In", "'Round Midnight"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Listed generically as 'reeds' in S13; reed-section doubler (tracks 1, 2, 5-6). Specific reed not broken out; flute recorded as a representative reed-section instrument — see notes." },
      { "name": "Phil Bodner", "instrument": "flute", "scope": "selected-tracks", "tracks": ["Willow Tree", "Struttin' With Some Barbeque", "Manteca!", "Bird Feathers"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Listed generically as 'reeds' in S13; reed-section doubler (tracks 3, 4, 7-8). Specific reed not broken out — see notes." },
      { "name": "Chuck Wayne", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "selected-tracks", "tracks": ["St. Louis Blues", "King Porter Stomp", "Struttin' With Some Barbeque", "Lester Leaps In", "'Round Midnight", "Manteca!", "Bird Feathers"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Tracks 1, 2, 4-8." },
      { "name": "Philly Joe Jones", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Willow Tree"], "session_dates": null, "epistemic": "obs", "sources": ["S13"], "name_variants": [], "notes": "Track 3 only." }
    ],
    "tracks": [
      { "title": "St. Louis Blues", "track_number": 1, "side": "A", "duration": "5:26", "session_date": null, "composers": ["W. C. Handy"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "King Porter Stomp", "track_number": 2, "side": "A", "duration": "3:19", "session_date": null, "composers": ["Jelly Roll Morton"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Willow Tree", "track_number": 3, "side": "A", "duration": "4:40", "session_date": null, "composers": ["Fats Waller", "Andy Razaf"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Struttin' With Some Barbeque", "track_number": 4, "side": "A", "duration": "4:34", "session_date": null, "composers": ["Lil Hardin Armstrong"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Lester Leaps In", "track_number": 5, "side": "B", "duration": "4:17", "session_date": null, "composers": ["Lester Young"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "'Round Midnight", "track_number": 6, "side": "B", "duration": "4:08", "session_date": null, "composers": ["Thelonious Monk"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Manteca!", "track_number": 7, "side": "B", "duration": "5:18", "session_date": null, "composers": ["Dizzy Gillespie", "Gil Fuller", "Babs Gonzales"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] },
      { "title": "Bird Feathers", "track_number": 8, "side": "B", "duration": "6:57", "session_date": null, "composers": ["Charlie Parker"], "personnel": [], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S13"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1461938778",
    "cover_art": [],
    "notes": "World Pacific WP-1246; four NYC sessions in spring 1958. S13 gives trumpet/tuba/reed/drum rotations by track-group but not full per-track lineups across the whole band, so track personnel arrays are left empty and track_assignments_complete is false. 'reeds' chairs (Sanfino, Bodner) are not broken out to a specific instrument in S13 — recorded as 'flute' as a representative reed-section instrument and flagged; treat the specific instrument as uncertain. Two musicians named 'tuba' fall outside the contract taxonomy. apple_album_id from S16."
  }
}
```

```json
{
  "id": "chet-baker-chet-baker-and-crew-1956",
  "artist": "Chet Baker",
  "album": "Chet Baker & Crew",
  "year": 1956,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S14", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S14]: Chet Baker's working quintet (Phil Urso, Bobby Timmons, Jimmy Bond, Peter Littmann) recorded live-in-studio at the Forum Theater, LA, July 1956, for Pacific Jazz (Richard Bock). obs[S17]: filed as West Coast / Cool Jazz. inf: the strongest document of Baker as an instrumental bandleader (as opposed to the collected vocal 'Chet Baker Sings') — a hard-swinging West Coast quintet date.",
  "priority": "consider",
  "overlap_risk": "Second Chet Baker entry (alongside the collected 'Chet Baker Sings'); distinct as an instrumental quintet record. Bobby Timmons's presence gives it a faint hard-bop tinge.",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1956-07-24", "1956-07-25", "1956-07-31"],
    "multi_session": true,
    "studio": "Forum Theater, Los Angeles",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Chet Baker", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Leader. Also sings on 'Line for Lyons' (track 14)." },
      { "name": "Phil Urso", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Bobby Timmons", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Jimmy Bond", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "" },
      { "name": "Peter Littmann", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": ["Peter Littman"], "notes": "" },
      { "name": "Bill Loughborough", "instrument": "percussion", "scope": "selected-tracks", "tracks": ["To Mickey's Memory", "To Mickey's Memory", "Pawnee Junction"], "session_dates": null, "epistemic": "obs", "sources": ["S14"], "name_variants": [], "notes": "Plays chromatic timpani (outside the contract taxonomy; recorded as 'percussion') on tracks 1, 9 and 12. Track 9 is the alternate take of 'To Mickey's Memory'." }
    ],
    "tracks": [
      { "title": "To Mickey's Memory", "track_number": 1, "side": "A", "duration": "5:12", "session_date": null, "composers": ["Harvey Leonard"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann", "Bill Loughborough"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Slightly Above Moderate", "track_number": 2, "side": "A", "duration": "6:59", "session_date": null, "composers": ["Bob Zieff"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Halema", "track_number": 3, "side": "A", "duration": "3:51", "session_date": null, "composers": ["Phil Urso"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Revelation", "track_number": 4, "side": "A", "duration": "3:58", "session_date": null, "composers": ["Gerry Mulligan"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Something For Liza", "track_number": 5, "side": "A", "duration": "4:05", "session_date": null, "composers": ["Al Cohn"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Lucius Lu", "track_number": 6, "side": "A", "duration": "5:34", "session_date": null, "composers": ["Phil Urso"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Worryin' the Life Out of Me", "track_number": 7, "side": "B", "duration": "2:59", "session_date": null, "composers": ["Miff Mole", "Bob Russell", "Frank Signorelli"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Medium Rock", "track_number": 8, "side": "B", "duration": "5:30", "session_date": null, "composers": ["Bob Zieff"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "To Mickey's Memory", "track_number": 9, "side": "B", "duration": "5:25", "session_date": null, "composers": ["Harvey Leonard"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann", "Bill Loughborough"], "bonus_track": true, "alternate_take": true, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Jumpin' Off a Clef", "track_number": 10, "side": "B", "duration": "4:55", "session_date": null, "composers": ["Al Haig"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Chippyin'", "track_number": 11, "side": "B", "duration": "3:20", "session_date": null, "composers": ["Harvey Leonard"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Pawnee Junction", "track_number": 12, "side": "B", "duration": "4:01", "session_date": null, "composers": ["Bill Loughborough"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann", "Bill Loughborough"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Music to Dance By", "track_number": 13, "side": "B", "duration": "4:35", "session_date": null, "composers": ["Al Cohn"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] },
      { "title": "Line for Lyons", "track_number": 14, "side": "B", "duration": "2:48", "session_date": null, "composers": ["Gerry Mulligan", "Bill Loughborough"], "personnel": ["Chet Baker", "Phil Urso", "Bobby Timmons", "Jimmy Bond", "Peter Littmann"], "bonus_track": true, "alternate_take": false, "epistemic_track": "obs", "sources": ["S14"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "716144378",
    "cover_art": [],
    "notes": "Original Pacific Jazz PJ-1224 carried the first 8-10 tracks; the listing here follows the expanded edition (S14), where tracks 9-14 are reissue/bonus additions (track 9 an alternate take of 'To Mickey's Memory'). Recorded at the Forum Theater, LA, July 24-25 & 31 1956; S14 does not split tracks to dates. Baker sings only on the bonus 'Line for Lyons'. Bill Loughborough's 'chromatic timpani' is outside the taxonomy (recorded as 'percussion'). track_assignments_complete false because the original vs bonus boundary and per-date mapping are not fully resolved in S14. apple_album_id from S16 is the 2003 expanded edition."
  }
}
```

```json
{
  "id": "chico-hamilton-quintet-featuring-buddy-collette-1955",
  "artist": "Chico Hamilton",
  "album": "Chico Hamilton Quintet featuring Buddy Collette",
  "year": 1955,
  "label": "Pacific Jazz",
  "style_primary": "cool-jazz",
  "style_tags": ["cool-jazz", "west-coast"],
  "sources": ["S15", "S16", "S17"],
  "epistemic": "obs",
  "rationale": "obs[S15]: drummer Chico Hamilton's chamber quintet — Buddy Collette (reeds/flute), Fred Katz (cello), Jim Hall (guitar), Carson Smith (bass) — across a studio and a live session in Aug 1955 for Pacific Jazz (Richard Bock). obs[S17]: filed as West Coast / Cool Jazz. inf: the debut of the era's most distinctive chamber-jazz instrumentation (cello-led, drummerless-feeling textures); a singular West Coast innovation the prior run named as a gap.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1955-08-04", "1955-08-23"],
    "multi_session": true,
    "studio": "The Strollers, Long Beach, California (live, 1955-08-04); Radio Recorders, Hollywood, California (studio, 1955-08-23)",
    "producer": "Richard Bock",
    "engineer": null,
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Chico Hamilton", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": ["1955-08-04", "1955-08-23"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Leader." },
      { "name": "Buddy Collette", "instrument": "flute", "scope": "all-tracks", "tracks": null, "session_dates": ["1955-08-04", "1955-08-23"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "Multi-reed: doubles tenor saxophone, alto saxophone, and clarinet; flute is his signature voice in this group." },
      { "name": "Fred Katz", "instrument": "cello", "scope": "all-tracks", "tracks": null, "session_dates": ["1955-08-04", "1955-08-23"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Jim Hall", "instrument": "guitar", "scope": "all-tracks", "tracks": null, "session_dates": ["1955-08-04", "1955-08-23"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" },
      { "name": "Carson Smith", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": ["1955-08-04", "1955-08-23"], "epistemic": "obs", "sources": ["S15"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "A Nice Day", "track_number": 1, "side": "A", "duration": "2:53", "session_date": "1955-08-23", "composers": ["Buddy Collette"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "My Funny Valentine", "track_number": 2, "side": "A", "duration": "4:16", "session_date": "1955-08-23", "composers": ["Richard Rodgers", "Lorenz Hart"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Blue Sands", "track_number": 3, "side": "A", "duration": "6:30", "session_date": "1955-08-23", "composers": ["Buddy Collette"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "The Sage", "track_number": 4, "side": "A", "duration": "3:34", "session_date": "1955-08-23", "composers": ["Fred Katz"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "The Morning After", "track_number": 5, "side": "A", "duration": "2:07", "session_date": "1955-08-23", "composers": ["Chico Hamilton"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "I Want to Be Happy", "track_number": 6, "side": "B", "duration": "2:10", "session_date": "1955-08-04", "composers": ["Vincent Youmans", "Irving Caesar"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Spectacular", "track_number": 7, "side": "B", "duration": "5:12", "session_date": "1955-08-04", "composers": ["Jim Hall"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Free Form", "track_number": 8, "side": "B", "duration": "5:00", "session_date": "1955-08-04", "composers": ["Chico Hamilton", "Buddy Collette", "Jim Hall", "Fred Katz", "Carson Smith"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Walking Carson Blues", "track_number": 9, "side": "B", "duration": "6:08", "session_date": "1955-08-04", "composers": ["Carson Smith"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] },
      { "title": "Buddy Boo", "track_number": 10, "side": "B", "duration": "6:16", "session_date": "1955-08-04", "composers": ["Buddy Collette"], "personnel": ["Chico Hamilton", "Buddy Collette", "Fred Katz", "Jim Hall", "Carson Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S15"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": null,
    "apple_album_id": "1443923804",
    "cover_art": [],
    "notes": "Pacific Jazz PJ-1209; the quintet's debut. Side 1 (tracks 1-5) recorded in studio at Radio Recorders 1955-08-23; Side 2 (tracks 6-10) recorded live at The Strollers, Long Beach, 1955-08-04. Constant quintet across both sessions. Collette doubles flute/clarinet/alto/tenor; flute recorded as his primary instrument per the group's signature sound. apple_album_id from S16 (catalog dates the reissue 1956). 'Free Form' is a collective-composed group improvisation."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves
- **Lennie Tristano — *Lennie Tristano* (1955):** the central document of the Tristano cerebral school the POC run flagged as a gap; "Line Up" is a defining cool experiment.
- **Shorty Rogers and His Giants (1953):** a founding document of the arranged Los Angeles nonet sound — Rogers's charts plus the full Lighthouse/Contemporary personnel pool.
- **The Jimmy Giuffre 3 (1956):** the touchstone of drummerless, folk-inflected chamber cool ("The Train and the River").
- **The Modern Jazz Quartet — *Django* (1955):** the cornerstone of the chamber/third-stream cool wing; Lewis's classically-poised writing over a swinging bop core.

### Hidden Gems
- **Chico Hamilton Quintet featuring Buddy Collette (1955):** the era's most distinctive instrumentation (cello-led, drummerless-feeling textures) — a singular West Coast innovation that is under-cited next to the big Mulligan/Brubeck names.
- **Howard Rumsey's Lighthouse All-Stars — *Sunday Jazz a la Lighthouse, Vol. 1* (1953):** the literal home-base scene document of West Coast jazz, rarely on best-of lists but historically pivotal.

### Consensus Picks (3+ sources)
- None reach three *fully independent* canon sources in this map; each pairs a detailed album page (S1-S15) with the genre-classification corpus (S17) and, where available, the iTunes reference (S16). The strongest multi-source grounding is *Shorty Rogers and His Giants*, *West Coast Jazz*, and *Art Pepper + Eleven*, each corroborated across S-album + S16 + S17.

### Single-Source Picks
- **Subconscious-Lee**, **Lennie Tristano**, and **Konitz Plays with the Gerry Mulligan Quartet** rest on a single detailed album source (S1 / S2 / S8 respectively) plus the genre corpus (S17); no iTunes corroboration was isolable for any of the three. The personnel facts in each are nonetheless source-internally complete (full session→track mappings).

### Scope Calls
- ***West Coast Jazz* (Getz):** title is a documented in-joke; tagged west-coast for its LA locale and personnel, not Getz's own affiliation.
- ***Django* (MJQ):** third-stream-leaning chamber jazz with a Van Gelder/Prestige bop rhythm core (Kenny Clarke); kept as core cool, flagged.
- ***New Bottle Old Wine* (Gil Evans):** a big-band-scale arranged date rather than a combo; included for its direct Birth-of-the-Cool lineage, with the orchestral character flagged.
- **Two-of-a-kind entries:** *Art Pepper + Eleven* (second Pepper), *Jazz at Oberlin* (second Brubeck), and *Chet Baker & Crew* (second Baker) are each genuinely distinct in format from their already-collected counterparts; overlap noted on each.
- **Earliest material:** *Subconscious-Lee*'s Jan 1949 sides brush the bebop starting line but are lineless, vibrato-light cool in conception — kept per the genre-definitions "spirit over year" rule.

### Gaps Noticed
- **No Bill Evans early date** (e.g., *New Jazz Conceptions*, 1956) — deferred as more modal-leaning and likely better handled by that specialist.
- **No Paul Desmond leader date** (*Desmond Blue*, *Two of a Mind*) and **no Bob Brookmeyer / Bud Shank / Stan Kenton** entries — the broader West Coast bench still has depth.
- **Penguin Guide and AllMusic editorial star-ratings were not directly fetched** this pass (Wikipedia album pages + an aggregated search corpus stood in for canon grounding); a follow-up that pulls those would sharpen priority calibration and could lift several `strong`/`consider` calls.
- **MusicBrainz release-group MBIDs and Cover Art Archive URLs** were not retrieved this pass (Layer 5 left null/empty per the optional discipline); a later art-ingest step can backfill from the captured Apple IDs and titles.

### Personnel Coverage
- **Full track listing + complete musician-level track assignments (`track_assignments_complete: true`):** *Subconscious-Lee*, *Lennie Tristano*, *West Coast Jazz*, *My Fair Lady*, *The Jimmy Giuffre 3*, *Sunday Jazz a la Lighthouse Vol. 1*, *Konitz Plays with the Gerry Mulligan Quartet*, *Django*, *Jazz at Oberlin*, *The Poll Winners*, *Chico Hamilton Quintet* — 11 of 15, mostly constant small groups or fully-documented session rotations.
- **Full track listing, per-track personnel left at session level (`false`):** *Shorty Rogers and His Giants* (Giuffre's exact coverage inferred), *Art Pepper + Eleven* (11-piece ensemble rotates by session; mapping documented in notes), *New Bottle Old Wine* (large orchestra, S13 gives group-level rotations only), *Chet Baker & Crew* (original-vs-bonus boundary unresolved in S14).
- **Production data:** producer confirmed for 9 of 15 (Granz, Lewis, Koenig, Bock, Weinstock, Avakian); inferred (`inf`) for *Sunday Jazz* (Koenig), *Art Pepper + Eleven* and *The Poll Winners* (Koenig/DuNann); unknown for *Subconscious-Lee*, *Lennie Tristano*, *The Jimmy Giuffre 3*, *Jazz at Oberlin*. Engineer is largely undocumented except Van Gelder (*Django*) and DuNann (*My Fair Lady*).
- **References:** Apple Music `collectionId` captured for 11 of 15 (null for *Subconscious-Lee*, *Lennie Tristano*, *Konitz/Mulligan*, *Django* — no clean original-album match, only comps/singles/reissues). Two albums carry small unresolved instrument-taxonomy flags (tuba on *Shorty Rogers* and *New Bottle Old Wine*; chromatic timpani on *Chet Baker & Crew*; unspecified 'reeds' on *New Bottle Old Wine*)."
