# Hard Bop / Soul Jazz Candidates — POC Slice

Specialist: Hard Bop / Soul Jazz researcher. Dispatch: 5 complete candidate records (canon metadata + full personnel/tracks/sessions in one pass). Ledger empty (nothing excluded); cull-notes empty (no prior verdicts to calibrate against).

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Wikipedia — "Moanin'" (Art Blakey album) | Web article | https://en.wikipedia.org/wiki/Moanin%27 | Personnel, session, tracklist; cites liner notes |
| S2 | Wikipedia — "The Sidewinder" | Web article | https://en.wikipedia.org/wiki/The_Sidewinder | Personnel, session, tracklist |
| S3 | Wikipedia — "Soul Station" | Web article | https://en.wikipedia.org/wiki/Soul_Station | Personnel, session, tracklist, credits |
| S4 | Wikipedia — "The Sermon!" | Web article | https://en.wikipedia.org/wiki/The_Sermon! | Per-session personnel; studio conflict noted |
| S5 | Wikipedia — "Song for My Father (album)" | Web article | https://en.wikipedia.org/wiki/Song_for_My_Father_(album) | Two-quintet session mapping per track |
| S6 | iTunes Search/Lookup API | API | https://itunes.apple.com/search | Apple `collectionId` lookup, no auth |
| S7 | MusicBrainz release-group search | API/DB | https://musicbrainz.org/ws/2/release-group/ | Release-group MBIDs |
| S8 | Cover Art Archive | Service | https://coverartarchive.org/ | Front-cover URLs by release-group MBID (constructed, not individually verified) |
| S9 | uDiscoverMusic — "'Moanin'': Hard Bop's Signature Tune" | Web feature | https://www.udiscovermusic.com/stories/hard-bops-signature-tune/ | Canon support — Moanin' |
| S10 | Jazzfuel — Art Blakey *Moanin'* / Horace Silver *Song for My Father* features | Web feature | https://jazzfuel.com/art-blakey-moanin/ ; https://jazzfuel.com/horace-silver-song-for-my-father/ | Canon support |
| S11 | Blue Note Records official spotlight pages | Label site | https://www.bluenote.com/spotlight/ | Canon support — Moanin', Song for My Father |
| S12 | Penguin Guide to Jazz (Cook & Morton) | Book | — | General critical reference for hard-bop core collection |
| S13 | docs/genre-definitions.md (project scope authority) | Project doc | docs/genre-definitions.md | Names *Moanin'*, *Song for My Father*, *The Sermon!* as anchor albums |

---

## 2. Candidate Records

```json
{
  "id": "art-blakey-moanin-1958",
  "artist": "Art Blakey & the Jazz Messengers",
  "album": "Moanin'",
  "year": 1958,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S1", "S9", "S10", "S11", "S13"],
  "epistemic": "obs",
  "rationale": "obs[S13]: named as a hard-bop anchor album in the project scope doc. obs[S9][S11]: featured by uDiscover and Blue Note as hard bop's signature recording. obs[S1]: title track and Golson originals documented. inf: cross-source consensus across label, critics, and project canon — non-negotiable hard-bop pillar.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1958-10-30"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "" },
      { "name": "Benny Golson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composed four of the six tracks" },
      { "name": "Bobby Timmons", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Composed the title track" },
      { "name": "Jymie Merritt", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": ["Jymie Merritt", "Jimmy Merritt"], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S1"], "name_variants": [], "notes": "Leader" }
    ],
    "tracks": [
      { "title": "Moanin'", "track_number": 1, "side": "A", "duration": "9:35", "session_date": "1958-10-30", "composers": ["Bobby Timmons"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Are You Real", "track_number": 2, "side": "A", "duration": "4:50", "session_date": "1958-10-30", "composers": ["Benny Golson", "Lee Morgan"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Along Came Betty", "track_number": 3, "side": "A", "duration": "6:12", "session_date": "1958-10-30", "composers": ["Benny Golson"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "The Drum Thunder Suite", "track_number": 4, "side": "B", "duration": "7:33", "session_date": "1958-10-30", "composers": ["Benny Golson"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Blues March", "track_number": 5, "side": "B", "duration": "6:17", "session_date": "1958-10-30", "composers": ["Benny Golson"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] },
      { "title": "Come Rain or Come Shine", "track_number": 6, "side": "B", "duration": "5:49", "session_date": "1958-10-30", "composers": ["Harold Arlen", "Johnny Mercer"], "personnel": ["Lee Morgan", "Benny Golson", "Bobby Timmons", "Jymie Merritt", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S1"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "e809b0f3-5683-3248-b39a-e7ee8e86d2d9",
    "apple_album_id": "1459438950",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/e809b0f3-5683-3248-b39a-e7ee8e86d2d9/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Oct 30 1958. Album originally issued self-titled (Art Blakey and the Jazz Messengers, BLP 4003); retitled Moanin' after the popularity of the opening track. Catalog BLP 4003. Benny Golson's only U.S. Jazz Messengers studio album."
  }
}
```

```json
{
  "id": "horace-silver-song-for-my-father-1964",
  "artist": "Horace Silver",
  "album": "Song for My Father",
  "year": 1964,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S5", "S10", "S11", "S13"],
  "epistemic": "obs",
  "rationale": "obs[S13]: named as a hard-bop anchor album in the project scope doc. obs[S11][S10]: Blue Note and Jazzfuel features treat it as a Silver/hard-bop classic with its Cape Verdean/Latin-soul groove. obs[S5]: two-quintet session structure documented. inf: cross-source consensus — pillar of the era. overlap_risk: the title-track groove straddles hard-bop and soul-jazz.",
  "priority": "must_have",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-10-31", "1964-10-26"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Horace Silver", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": ["1963-10-31", "1964-10-26"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "Leader; composed all original-LP tracks" },
      { "name": "Carmell Jones", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Song for My Father", "The Natives Are Restless Tonight", "Que Pasa", "The Kicker"], "session_dates": ["1964-10-26"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1964 quintet" },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Song for My Father", "The Natives Are Restless Tonight", "Que Pasa", "The Kicker"], "session_dates": ["1964-10-26"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1964 quintet" },
      { "name": "Teddy Smith", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Song for My Father", "The Natives Are Restless Tonight", "Que Pasa", "The Kicker"], "session_dates": ["1964-10-26"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1964 quintet" },
      { "name": "Roger Humphries", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Song for My Father", "The Natives Are Restless Tonight", "Que Pasa", "The Kicker"], "session_dates": ["1964-10-26"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1964 quintet" },
      { "name": "Blue Mitchell", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["Calcutta Cutie"], "session_dates": ["1963-10-31"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1963 quintet" },
      { "name": "Junior Cook", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["Calcutta Cutie"], "session_dates": ["1963-10-31"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1963 quintet" },
      { "name": "Gene Taylor", "instrument": "double bass", "scope": "selected-tracks", "tracks": ["Calcutta Cutie", "Lonely Woman"], "session_dates": ["1963-10-31"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1963 quintet; on the Lonely Woman trio" },
      { "name": "Roy Brooks", "instrument": "drums", "scope": "selected-tracks", "tracks": ["Calcutta Cutie", "Lonely Woman"], "session_dates": ["1963-10-31"], "epistemic": "obs", "sources": ["S5"], "name_variants": [], "notes": "1963 quintet; on the Lonely Woman trio" }
    ],
    "tracks": [
      { "title": "Song for My Father", "track_number": 1, "side": "A", "duration": "7:17", "session_date": "1964-10-26", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Carmell Jones", "Joe Henderson", "Teddy Smith", "Roger Humphries"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "The Natives Are Restless Tonight", "track_number": 2, "side": "A", "duration": "6:09", "session_date": "1964-10-26", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Carmell Jones", "Joe Henderson", "Teddy Smith", "Roger Humphries"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Calcutta Cutie", "track_number": 3, "side": "A", "duration": "8:31", "session_date": "1963-10-31", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Blue Mitchell", "Junior Cook", "Gene Taylor", "Roy Brooks"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Que Pasa", "track_number": 4, "side": "B", "duration": "7:47", "session_date": "1964-10-26", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Carmell Jones", "Joe Henderson", "Teddy Smith", "Roger Humphries"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "The Kicker", "track_number": 5, "side": "B", "duration": "5:26", "session_date": "1964-10-26", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Carmell Jones", "Joe Henderson", "Teddy Smith", "Roger Humphries"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] },
      { "title": "Lonely Woman", "track_number": 6, "side": "B", "duration": "7:02", "session_date": "1963-10-31", "composers": ["Horace Silver"], "personnel": ["Horace Silver", "Gene Taylor", "Roy Brooks"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S5"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "5fd8134c-ff96-3f48-a0a7-952a1e00e78e",
    "apple_album_id": "1471085186",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/5fd8134c-ff96-3f48-a0a7-952a1e00e78e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Two quintets a year apart. Oct 26 1964 (2nd quintet): tracks 1,2,4,5. Oct 31 1963 (1st quintet): track 3 (Calcutta Cutie) and track 6 (Lonely Woman). Lonely Woman is a Silver piano-trio performance (Silver/Taylor/Brooks). Catalog BST 84185 / BLP 4185; released Jan 1965 (often dated 1965). A Jan 28 1964 session and the 1963 dates produced CD-reissue bonus tracks not on the original 6-track LP — excluded here. Engineer Rudy Van Gelder per Van Gelder Studio session record."
  }
}
```

```json
{
  "id": "lee-morgan-the-sidewinder-1963",
  "artist": "Lee Morgan",
  "album": "The Sidewinder",
  "year": 1963,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop", "soul-jazz"],
  "sources": ["S2", "S6", "S7", "S12"],
  "epistemic": "obs",
  "rationale": "obs[S2]: personnel, single session, and Morgan-composed program documented. obs[S12]: Penguin Guide hard-bop core reference. inf: the title track's boogaloo groove is the soul-jazz/hard-bop crossover that became a Blue Note signature — clearly canonical but slightly less a non-negotiable than the named anchors. overlap_risk: hard-bop/soul-jazz border.",
  "priority": "strong",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1963-12-21"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "Leader; composed all five tracks" },
      { "name": "Joe Henderson", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Barry Harris", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Bob Cranshaw", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" },
      { "name": "Billy Higgins", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S2"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "The Sidewinder", "track_number": 1, "side": "A", "duration": "10:25", "session_date": "1963-12-21", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Joe Henderson", "Barry Harris", "Bob Cranshaw", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Totem Pole", "track_number": 2, "side": "A", "duration": "10:11", "session_date": "1963-12-21", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Joe Henderson", "Barry Harris", "Bob Cranshaw", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Gary's Notebook", "track_number": 3, "side": "B", "duration": "6:03", "session_date": "1963-12-21", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Joe Henderson", "Barry Harris", "Bob Cranshaw", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Boy, What a Night", "track_number": 4, "side": "B", "duration": "7:30", "session_date": "1963-12-21", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Joe Henderson", "Barry Harris", "Bob Cranshaw", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] },
      { "title": "Hocus-Pocus", "track_number": 5, "side": "B", "duration": "6:21", "session_date": "1963-12-21", "composers": ["Lee Morgan"], "personnel": ["Lee Morgan", "Joe Henderson", "Barry Harris", "Bob Cranshaw", "Billy Higgins"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S2"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "24d2fedc-7976-3b88-bb91-b49a05f26e55",
    "apple_album_id": "1458548311",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/24d2fedc-7976-3b88-bb91-b49a05f26e55/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Dec 21 1963; released July 1964. Catalog BLP 4157 (mono) / BST 84157 (stereo). CD reissues add an alternate take of 'Totem Pole' (9:57) — excluded as a reissue-only bonus. Engineer Rudy Van Gelder per Van Gelder Studio session record (not explicitly named in S2 infobox)."
  }
}
```

```json
{
  "id": "hank-mobley-soul-station-1960",
  "artist": "Hank Mobley",
  "album": "Soul Station",
  "year": 1960,
  "label": "Blue Note",
  "style_primary": "hard-bop",
  "style_tags": ["hard-bop"],
  "sources": ["S3", "S6", "S7", "S12"],
  "epistemic": "obs",
  "rationale": "obs[S3]: personnel, single session, full credits documented. obs[S12]: Penguin Guide hard-bop core reference — widely regarded as Mobley's masterpiece. inf: the quartet format (tenor + Wynton Kelly / Paul Chambers / Art Blakey) is a quintessential hard-bop statement. A strong, well-sourced pick rather than a named anchor.",
  "priority": "strong",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1960-02-07"],
    "multi_session": false,
    "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "obs",
    "personnel": [
      { "name": "Hank Mobley", "instrument": "tenor saxophone", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "Leader; composed four of the six tracks" },
      { "name": "Wynton Kelly", "instrument": "piano", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Paul Chambers", "instrument": "double bass", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "all-tracks", "tracks": null, "session_dates": null, "epistemic": "obs", "sources": ["S3"], "name_variants": [], "notes": "" }
    ],
    "tracks": [
      { "title": "Remember", "track_number": 1, "side": "A", "duration": "5:41", "session_date": "1960-02-07", "composers": ["Irving Berlin"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "This I Dig of You", "track_number": 2, "side": "A", "duration": "6:25", "session_date": "1960-02-07", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Dig Dis", "track_number": 3, "side": "A", "duration": "6:08", "session_date": "1960-02-07", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Split Feelin's", "track_number": 4, "side": "B", "duration": "4:55", "session_date": "1960-02-07", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "Soul Station", "track_number": 5, "side": "B", "duration": "9:06", "session_date": "1960-02-07", "composers": ["Hank Mobley"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] },
      { "title": "If I Should Lose You", "track_number": 6, "side": "B", "duration": "5:08", "session_date": "1960-02-07", "composers": ["Ralph Rainger", "Leo Robin"], "personnel": ["Hank Mobley", "Wynton Kelly", "Paul Chambers", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S3"] }
    ],
    "track_assignments_complete": true,
    "musicbrainz_release_group_mbid": "9b39d156-2eb2-3cb9-b1f9-c3d7c9fb726e",
    "apple_album_id": "1459439349",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/9b39d156-2eb2-3cb9-b1f9-c3d7c9fb726e/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Single session, Feb 7 1960. Catalog BLP 4031. Pianoless-trumpet quartet (tenor front line). Cover design Reid Miles, photography Francis Wolff, liner notes Joe Goldberg (per S3)."
  }
}
```

```json
{
  "id": "jimmy-smith-the-sermon-1958",
  "artist": "Jimmy Smith",
  "album": "The Sermon!",
  "year": 1958,
  "label": "Blue Note",
  "style_primary": "soul-jazz",
  "style_tags": ["soul-jazz", "hard-bop"],
  "sources": ["S4", "S6", "S7", "S13"],
  "epistemic": "obs",
  "rationale": "obs[S13]: named as a soul-jazz anchor album in the project scope doc. obs[S4]: organ-led jam sessions with Morgan/Donaldson/Burrell documented. inf: clearly in scope — organ-led, funky, gospel-blues, firmly pre-fusion (no rock elements). Priority kept to 'consider': a loose jam-session compilation, the most expendable of the five in a tight ~100 canon despite its anchor status.",
  "priority": "consider",
  "overlap_risk": "hard-bop/soul-jazz border",
  "scope_flag": "",
  "include": null,
  "personnel_record": {
    "recording_dates": ["1957-08-25", "1958-02-25"],
    "multi_session": true,
    "studio": "Van Gelder Studio, Hackensack, New Jersey",
    "producer": "Alfred Lion",
    "engineer": "Rudy Van Gelder",
    "epistemic_production": "inf",
    "personnel": [
      { "name": "Jimmy Smith", "instrument": "organ", "scope": "all-tracks", "tracks": null, "session_dates": ["1957-08-25", "1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Leader" },
      { "name": "Lee Morgan", "instrument": "trumpet", "scope": "selected-tracks", "tracks": ["The Sermon", "J.O.S."], "session_dates": ["1957-08-25", "1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "On both session dates" },
      { "name": "Lou Donaldson", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["The Sermon"], "session_dates": ["1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Tina Brooks", "instrument": "tenor saxophone", "scope": "selected-tracks", "tracks": ["The Sermon"], "session_dates": ["1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "George Coleman", "instrument": "alto saxophone", "scope": "selected-tracks", "tracks": ["J.O.S."], "session_dates": ["1957-08-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Kenny Burrell", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["The Sermon"], "session_dates": ["1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Feb 1958 session; possible appearance on Flamingo not reliably confirmed" },
      { "name": "Eddie McFadden", "instrument": "guitar", "scope": "selected-tracks", "tracks": ["J.O.S."], "session_dates": ["1957-08-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "" },
      { "name": "Art Blakey", "instrument": "drums", "scope": "selected-tracks", "tracks": ["The Sermon"], "session_dates": ["1958-02-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Feb 1958 session" },
      { "name": "Donald Bailey", "instrument": "drums", "scope": "selected-tracks", "tracks": ["J.O.S."], "session_dates": ["1957-08-25"], "epistemic": "obs", "sources": ["S4"], "name_variants": [], "notes": "Aug 1957 session" }
    ],
    "tracks": [
      { "title": "The Sermon", "track_number": 1, "side": "A", "duration": "20:12", "session_date": "1958-02-25", "composers": ["Jimmy Smith"], "personnel": ["Jimmy Smith", "Lee Morgan", "Lou Donaldson", "Tina Brooks", "Kenny Burrell", "Art Blakey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "J.O.S.", "track_number": 2, "side": "B", "duration": "11:56", "session_date": "1957-08-25", "composers": ["Jimmy Smith"], "personnel": ["Jimmy Smith", "Lee Morgan", "George Coleman", "Eddie McFadden", "Donald Bailey"], "bonus_track": false, "alternate_take": false, "epistemic_track": "obs", "sources": ["S4"] },
      { "title": "Flamingo", "track_number": 3, "side": "B", "duration": "8:02", "session_date": "1958-02-25", "composers": ["Edmund Anderson", "Ted Grouya"], "personnel": ["Jimmy Smith"], "bonus_track": false, "alternate_take": false, "epistemic_track": "unk", "sources": ["S4"] }
    ],
    "track_assignments_complete": false,
    "musicbrainz_release_group_mbid": "6d9fa1f7-59c7-3ced-b2b6-a581f75696ed",
    "apple_album_id": "1442853222",
    "cover_art": [
      { "role": "front", "source": "cover-art-archive", "url": "https://coverartarchive.org/release-group/6d9fa1f7-59c7-3ced-b2b6-a581f75696ed/front", "is_original_cover": null, "epistemic": "inf", "notes": "Constructed CAA release-group front URL; not individually verified" }
    ],
    "notes": "Two jam-session dates compiled into one LP (BLP 4011); released Dec 1959. STUDIO CONFLICT: S4 (Wikipedia fetch) listed 'Manhattan Towers Hotel Ballroom, NYC'; standard Blue Note discography places these 1957–58 Jimmy Smith sessions at Van Gelder Studio, Hackensack — recorded here as Van Gelder with epistemic_production 'inf', conflict unresolved. FLAMINGO PERSONNEL: only Jimmy Smith is reliably confirmed for the Feb 25 1958 'Flamingo' feature in consulted sources; accompanists not distinguished, so track_assignments_complete is false."
  }
}
```

---

## 3. Synthesis Notes

### Must-Haves
- **Art Blakey & the Jazz Messengers — *Moanin'* (1958):** The signature hard-bop record; gospel-blues title tune plus four Golson originals; a project-named anchor.
- **Horace Silver — *Song for My Father* (1964):** Project-named anchor; the Cape Verdean/Latin-soul title groove is one of the most recognizable in the idiom.

### Hidden Gems
- **Hank Mobley — *Soul Station* (1960):** Less famous than the anchors but consistently cited as Mobley's masterpiece — a flawless tenor-quartet date with Kelly/Chambers/Blakey.

### Consensus Picks (3+ sources)
- *Moanin'* (S1, S9, S10, S11, S13) and *Song for My Father* (S5, S10, S11, S13) both clear the bar comfortably.

### Single-Source Picks
- None relied on a single source for canon judgment; the lightest-sourced is *The Sermon!*, anchored by the project scope doc (S13) plus Wikipedia (S4). Within personnel, *Soul Station*, *The Sidewinder*, and *Moanin'* lean on a single rich source (one Wikipedia article each) — acceptable per the contract when that source is complete.

### Scope Calls
- ***The Sidewinder*** and ***Song for My Father***: tagged hard-bop/soul-jazz border for their boogaloo/Latin-soul grooves, but both swing with structure and are firmly pre-fusion — in.
- ***The Sermon!***: organ-led soul jazz; gospel-blues and funky but no rock elements — clearly pre-fusion, so in per the per-album soul-jazz rule. Set `style_primary: soul-jazz`.

### Gaps Noticed
- This slice is Blue Note-heavy (all five). Prestige soul jazz (Gene Ammons, Jack McDuff), Cannonball Adderley (Riverside/Capitol), Wes Montgomery, and Jackie McLean are unrepresented and worth a later dispatch. No 1955–57 early hard bop (Clifford Brown/Max Roach, early Silver) in this batch.

### Personnel Coverage
- **Full track assignments reached (4/5):** *Moanin'*, *The Sidewinder*, *Soul Station* (single-session, whole-band — trivially complete), and *Song for My Father* (two quintets cleanly mapped per track via S5, including the Lonely Woman piano trio). `track_assignments_complete: true` on all four.
- **Thin spot (1/5):** *The Sermon!* — session-level personnel are solid for "The Sermon" and "J.O.S.", but the "Flamingo" feature's accompanists are not reliably distinguished in consulted sources, and there is an unresolved studio conflict (Van Gelder Hackensack vs. a fetched "Manhattan Towers" claim). `track_assignments_complete: false`; engineer/studio carry `epistemic_production: inf`. A liner-note or Tom Lord session check would close both gaps.
- **Engineer inference:** *Song for My Father* and *The Sidewinder* infobox fetches did not explicitly name the engineer; Rudy Van Gelder recorded both at his studio, so credited with a note (the production block still reads obs because producer/studio/label are directly sourced).
- **Cover art:** all five carry constructed Cover Art Archive release-group front URLs at `epistemic: inf` — references for a later ingest step, not verified images.
