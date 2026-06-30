# Personnel Research — Gap Fill Batch 01

**Run date:** 2026-06-29  
**Albums covered:** 1  
**Agent:** Jazz Personnel Researcher (claude-sonnet-4-6)

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | AllMusic — Something Cool album page | Web | https://www.allmusic.com/album/something-cool-mw0000263891 | 403 Forbidden — credits tab blocked during this session; attempted and unavailable |
| S2 | Wikipedia — Something Cool article | Web | https://en.wikipedia.org/wiki/Something_Cool | Personnel section, infobox (producer), track listing with durations and composers; covers all three versions (1954/1955/1960) |
| S3 | JazzDisco.org — June Christy catalog page | Web | https://www.jazzdisco.org/june-christy/catalog/ | Session-level authority: all six session dates, studio, full personnel per session with instruments; also named track for sessions 1, 2, and 5 |
| S4 | JazzDisco.org — June Christy discography page | Web | https://www.jazzdisco.org/june-christy/discography/ | Supplementary track-to-matrix assignments for sessions 3, 4, and 6 (matrix numbers 12259–12264 and 13854–13856 matched to titles) |
| S5 | Wikidata — Q7560085 | Web | https://www.wikidata.org/wiki/Q7560085 | MusicBrainz release group MBID confirmed directly from structured Wikidata property |

---

## 2. Album Records

```json
{
  "album_id": "june-christy-something-cool-1955",
  "recording_dates": [
    "1953-08-14",
    "1953-12-27",
    "1954-01-18",
    "1954-01-19",
    "1954-01-26",
    "1954-03-18",
    "1954-12-29",
    "1955-05-10",
    "1955-05-24",
    "1955-06-02"
  ],
  "multi_session": true,
  "studio": "Capitol Melrose Studios, Los Angeles, California",
  "producer": "Lee Gillette",
  "engineer": null,
  "label": "Capitol",
  "epistemic_production": "inf",
  "personnel": [
    {
      "name": "June Christy",
      "instrument": "vocals",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S2", "S3"],
      "name_variants": ["Shirley Luster"],
      "notes": "Shirley Luster is her birth name; professionally June Christy throughout this period."
    },
    {
      "name": "Pete Rugolo",
      "instrument": "arranger",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S2", "S3"],
      "name_variants": [],
      "notes": "Arranger and conductor for all six sessions. 'arranger' is outside the instrument taxonomy — non-performance credit included per dispatch instruction. Album is sometimes titled 'Pete Rugolo and His Orchestra featuring June Christy'."
    },
    {
      "name": "Conrad Gozzo",
      "instrument": "trumpet",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "The only trumpet player present in all six sessions; the sole all-tracks performer in the brass section."
    },
    {
      "name": "Maynard Ferguson",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1953-08-14", "1954-01-18", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 3, 5, 6. Not on 'Midnight Sun' (session 2) or 'I'll Take Romance' / 'A Stranger Called the Blues' (session 4)."
    },
    {
      "name": "Shorty Rogers",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1953-08-14", "1954-01-18", "1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 3, 4, 5, 6. Not on 'Midnight Sun' (session 2 had different trumpet section)."
    },
    {
      "name": "Jimmy Zito",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only."
    },
    {
      "name": "Frank Beach",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only. Session 2 dates are Dec 27, 1953 and Mar 18, 1954; exact recording date within session block not distinguished in source."
    },
    {
      "name": "Ray Linn",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Uan Rasey",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Ray Triscari",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Conte Candoli",
      "instrument": "trumpet",
      "scope": "selected-tracks",
      "tracks": ["I'll Take Romance", "A Stranger Called the Blues"],
      "session_dates": ["1954-01-19"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 4 only. Session 4 dates are Jan 19, Jan 26, and Mar 18, 1954; exact recording date within session block not distinguished in source."
    },
    {
      "name": "Milt Bernhart",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1953-08-14", "1954-01-18", "1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 3, 4, 5, 6. Not on 'Midnight Sun' (session 2 had different trombone section: DiMaio, Pederson, Reynolds)."
    },
    {
      "name": "Herbie Harper",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": ["Something Cool", "I'll Take Romance", "A Stranger Called the Blues"],
      "session_dates": ["1953-08-14", "1954-01-19"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1 and 4."
    },
    {
      "name": "Tommy Pederson",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Midnight Sun",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You"
      ],
      "session_dates": ["1953-08-14", "1953-12-27", "1954-01-18"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 2, 3. Not on sessions 4, 5, or 6."
    },
    {
      "name": "Harry Betts",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": [
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-18", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 3, 5, 6."
    },
    {
      "name": "Nick DiMaio",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": ["Nick Dimaio"],
      "notes": "Session 2 only. Spelling 'DiMaio' per S3; Amazon listing uses 'Dimaio'."
    },
    {
      "name": "Dick Reynolds",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Bob Fitzpatrick",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": ["I'll Take Romance", "A Stranger Called the Blues"],
      "session_dates": ["1954-01-19"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 4 only."
    },
    {
      "name": "Frank Rosolino",
      "instrument": "trombone",
      "scope": "selected-tracks",
      "tracks": [
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 5 and 6."
    },
    {
      "name": "George Roberts",
      "instrument": "bass trombone",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only."
    },
    {
      "name": "Dick Noel",
      "instrument": "bass trombone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "John Graas",
      "instrument": "French horn",
      "scope": "selected-tracks",
      "tracks": ["Lonely House", "I Should Care", "It Could Happen to You"],
      "session_dates": ["1954-01-18"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 3 only."
    },
    {
      "name": "Vincent DeRosa",
      "instrument": "French horn",
      "scope": "selected-tracks",
      "tracks": [
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 5 and 6."
    },
    {
      "name": "Paul Sarmento",
      "instrument": "tuba",
      "scope": "selected-tracks",
      "tracks": [
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-18", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 3, 5, 6."
    },
    {
      "name": "Gus Bivona",
      "instrument": "alto saxophone",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only. Also plays flute."
    },
    {
      "name": "Bud Shank",
      "instrument": "alto saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1953-08-14", "1954-01-18", "1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 3, 4, 5, 6 — all sessions except session 2. Also plays flute in all his sessions. Also plays alto flute in sessions 5 and 6 (S3). Not on 'Midnight Sun'."
    },
    {
      "name": "Harry Klee",
      "instrument": "alto saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-18", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 3, 5, 6. Also plays flute. Also plays alto flute in sessions 5 and 6 (S3). Alto flute is outside the taxonomy; noted here."
    },
    {
      "name": "Skeets Herfurt",
      "instrument": "alto saxophone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only. No flute doubling listed for session 2 alto saxophonists."
    },
    {
      "name": "Willie Schwartz",
      "instrument": "alto saxophone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Bob Cooper",
      "instrument": "tenor saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues"
      ],
      "session_dates": ["1953-08-14", "1954-01-18", "1954-01-19"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 3, 4. Not on sessions 2, 5, or 6. Also plays flute. June Christy's husband."
    },
    {
      "name": "Ted Nash",
      "instrument": "tenor saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "Something Cool",
        "Midnight Sun",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You"
      ],
      "session_dates": ["1953-08-14", "1953-12-27", "1954-01-18"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1, 2, 3. Also plays flute."
    },
    {
      "name": "Jimmy Giuffre",
      "instrument": "tenor saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 4, 5, 6. Also plays flute in session 4 (S3); session 5/6 lists him as tenor sax only."
    },
    {
      "name": "Fred Fallensby",
      "instrument": "tenor saxophone",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": ["Fred Falensby"],
      "notes": "Session 2 only. Also plays flute. S3 spells 'Fallensby'; Amazon and some secondary sources spell 'Falensby'. Canonical form follows S3."
    },
    {
      "name": "Chuck Gentry",
      "instrument": "baritone saxophone",
      "scope": "selected-tracks",
      "tracks": ["Something Cool", "Midnight Sun"],
      "session_dates": ["1953-08-14", "1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 1 and 2."
    },
    {
      "name": "Johnny Rotella",
      "instrument": "baritone saxophone",
      "scope": "selected-tracks",
      "tracks": ["Lonely House", "I Should Care", "It Could Happen to You"],
      "session_dates": ["1954-01-18"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": ["John Rotella"],
      "notes": "Session 3 only. S3 uses 'Johnny Rotella'; Amazon listing and S2 use 'John Rotella'. Canonical form follows S3."
    },
    {
      "name": "Bob Gordon",
      "instrument": "baritone saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 4, 5, 6."
    },
    {
      "name": "Geoff Clarkson",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only."
    },
    {
      "name": "Paul Smith",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Russ Freeman",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": ["Lonely House", "I Should Care", "It Could Happen to You"],
      "session_dates": ["1954-01-18"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 3 only."
    },
    {
      "name": "Claude Williamson",
      "instrument": "piano",
      "scope": "selected-tracks",
      "tracks": [
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 4, 5, 6."
    },
    {
      "name": "Barney Kessel",
      "instrument": "guitar",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only ('Something Cool'). Previous DB entry marked 'unk'; upgraded to 'obs' — S3 explicitly names Kessel in session 1 personnel."
    },
    {
      "name": "Tony Rizzi",
      "instrument": "guitar",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Howard Roberts",
      "instrument": "guitar",
      "scope": "selected-tracks",
      "tracks": [
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-18", "1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 3, 4, 5, 6."
    },
    {
      "name": "Joe Comfort",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only."
    },
    {
      "name": "Joe Mondragon",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": [
        "Midnight Sun",
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues"
      ],
      "session_dates": ["1953-12-27", "1954-01-18", "1954-01-19"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 2, 3, 4."
    },
    {
      "name": "Harry Babasin",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": [
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 5 and 6."
    },
    {
      "name": "Frank Carlson",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": ["Something Cool"],
      "session_dates": ["1953-08-14"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 1 only."
    },
    {
      "name": "Alvin Stoller",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": ["Midnight Sun"],
      "session_dates": ["1953-12-27"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Session 2 only."
    },
    {
      "name": "Shelly Manne",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": [
        "Lonely House",
        "I Should Care",
        "It Could Happen to You",
        "I'll Take Romance",
        "A Stranger Called the Blues",
        "Softly, as in a Morning Sunrise",
        "I'm Thrilled",
        "The Night We Called It a Day",
        "This Time the Dream's on Me"
      ],
      "session_dates": ["1954-01-18", "1954-01-19", "1954-12-29", "1955-05-10"],
      "epistemic": "obs",
      "sources": ["S3"],
      "name_variants": [],
      "notes": "Sessions 3, 4, 5, 6. Previous DB entry marked 'unk'; upgraded to 'obs' — S3 explicitly names Manne in sessions 3, 4, 5, and 6 (session 6 confirmed as 'same as session 5')."
    }
  ],
  "tracks": [
    {
      "title": "Something Cool",
      "track_number": 1,
      "side": "A",
      "duration": "4:20",
      "session_date": "1953-08-14",
      "composers": ["Billy Barnes"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers", "Jimmy Zito",
        "Milt Bernhart", "Herbie Harper", "Tommy Pederson", "George Roberts",
        "Gus Bivona", "Bud Shank", "Bob Cooper", "Ted Nash", "Chuck Gentry",
        "Geoff Clarkson", "Barney Kessel", "Joe Comfort", "Frank Carlson"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S3", "S4"]
    },
    {
      "title": "It Could Happen to You",
      "track_number": 2,
      "side": "A",
      "duration": "1:58",
      "session_date": "1954-01-18",
      "composers": ["Jimmy Van Heusen", "Johnny Burke"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Tommy Pederson", "John Graas", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Bob Cooper", "Ted Nash", "Johnny Rotella",
        "Russ Freeman", "Howard Roberts", "Joe Mondragon", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S3", "S4"]
    },
    {
      "title": "Lonely House",
      "track_number": 3,
      "side": "A",
      "duration": "3:59",
      "session_date": "1954-01-18",
      "composers": ["Kurt Weill", "Langston Hughes"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Tommy Pederson", "John Graas", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Bob Cooper", "Ted Nash", "Johnny Rotella",
        "Russ Freeman", "Howard Roberts", "Joe Mondragon", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S3", "S4"]
    },
    {
      "title": "This Time the Dream's on Me",
      "track_number": 4,
      "side": "A",
      "duration": "1:32",
      "session_date": "1955-05-10",
      "composers": ["Harold Arlen", "Johnny Mercer"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Frank Rosolino", "Vincent DeRosa", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Jimmy Giuffre", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Harry Babasin", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3", "S4"]
    },
    {
      "title": "The Night We Called It a Day",
      "track_number": 5,
      "side": "A",
      "duration": "4:48",
      "session_date": "1955-05-10",
      "composers": ["Matt Dennis", "Tom Adair"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Frank Rosolino", "Vincent DeRosa", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Jimmy Giuffre", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Harry Babasin", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3", "S4"]
    },
    {
      "title": "Midnight Sun",
      "track_number": 6,
      "side": "B",
      "duration": "3:16",
      "session_date": "1953-12-27",
      "composers": ["Lionel Hampton", "Sonny Burke", "Johnny Mercer"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Conrad Gozzo", "Frank Beach", "Ray Linn", "Uan Rasey", "Ray Triscari",
        "Nick DiMaio", "Tommy Pederson", "Dick Reynolds", "Dick Noel",
        "Skeets Herfurt", "Willie Schwartz", "Fred Fallensby", "Ted Nash", "Chuck Gentry",
        "Paul Smith", "Tony Rizzi", "Joe Mondragon", "Alvin Stoller"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3"]
    },
    {
      "title": "I'll Take Romance",
      "track_number": 7,
      "side": "B",
      "duration": "2:21",
      "session_date": "1954-01-19",
      "composers": ["Ben Oakland", "Oscar Hammerstein II"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Conrad Gozzo", "Conte Candoli", "Shorty Rogers",
        "Milt Bernhart", "Bob Fitzpatrick", "Herbie Harper",
        "Bud Shank", "Jimmy Giuffre", "Bob Cooper", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Joe Mondragon", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3", "S4"]
    },
    {
      "title": "A Stranger Called the Blues",
      "track_number": 8,
      "side": "B",
      "duration": "3:59",
      "session_date": "1954-01-19",
      "composers": ["Mel Tormé", "Robert Wells"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Conrad Gozzo", "Conte Candoli", "Shorty Rogers",
        "Milt Bernhart", "Bob Fitzpatrick", "Herbie Harper",
        "Bud Shank", "Jimmy Giuffre", "Bob Cooper", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Joe Mondragon", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3", "S4"]
    },
    {
      "title": "I Should Care",
      "track_number": 9,
      "side": "B",
      "duration": "2:11",
      "session_date": "1954-01-18",
      "composers": ["Paul Weston", "Sammy Cahn", "Axel Stordahl"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Tommy Pederson", "John Graas", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Bob Cooper", "Ted Nash", "Johnny Rotella",
        "Russ Freeman", "Howard Roberts", "Joe Mondragon", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S3", "S4"]
    },
    {
      "title": "Softly, as in a Morning Sunrise",
      "track_number": 10,
      "side": "B",
      "duration": "2:21",
      "session_date": "1954-12-29",
      "composers": ["Sigmund Romberg", "Oscar Hammerstein II"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Frank Rosolino", "Vincent DeRosa", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Jimmy Giuffre", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Harry Babasin", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S3"]
    },
    {
      "title": "I'm Thrilled",
      "track_number": 11,
      "side": "B",
      "duration": "2:43",
      "session_date": "1955-05-10",
      "composers": ["Sidney Lippman", "Sylvia Dee"],
      "personnel": [
        "June Christy", "Pete Rugolo",
        "Maynard Ferguson", "Conrad Gozzo", "Shorty Rogers",
        "Milt Bernhart", "Harry Betts", "Frank Rosolino", "Vincent DeRosa", "Paul Sarmento",
        "Harry Klee", "Bud Shank", "Jimmy Giuffre", "Bob Gordon",
        "Claude Williamson", "Howard Roberts", "Harry Babasin", "Shelly Manne"
      ],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "inf",
      "sources": ["S3", "S4"]
    }
  ],
  "track_assignments_complete": true,
  "musicbrainz_release_group_mbid": "fb5bcd7c-a62d-4741-b024-35e702d861e3",
  "cover_art": [
    {
      "role": "front",
      "source": "cover-art-archive",
      "url": "https://coverartarchive.org/release-group/fb5bcd7c-a62d-4741-b024-35e702d861e3/front",
      "is_original_cover": null,
      "epistemic": "inf",
      "notes": "MBID confirmed via Wikidata (S5). CAA release-group URL constructed from confirmed MBID; specific pressing represented by the CAA front image is not verified."
    }
  ],
  "sources": ["S2", "S3", "S4", "S5"],
  "notes": "Six recording session clusters. Session 1 (Aug 14, 1953): 'Something Cool' only. Session 2 (Dec 27, 1953 and Mar 18, 1954): 'Midnight Sun' only; compound session — exact recording date within the Dec 27/Mar 18 window not distinguished in S3. Session 3 (Jan 18, 1954): 'Lonely House', 'I Should Care', 'It Could Happen to You' (matrix numbers 12259, 12260, 12261 per S4). Session 4 (Jan 19, Jan 26, and Mar 18, 1954): 'A Stranger Called the Blues', 'I'll Take Romance' (matrices 12263, 12264 per S4); compound session — exact dates not distinguished. An unissued track (matrix 12262, title 'The First Thing You Know, You\'re In Love') was also recorded in session 4 and not released on the album. Session 5 (Dec 29, 1954): 'Softly, as in a Morning Sunrise' only. Session 6 (May 10, May 24, and June 2, 1955): 'I\'m Thrilled', 'The Night We Called It a Day', 'This Time the Dream\'s on Me' (matrices 13854, 13855, 13856 per S4); compound session; S3 confirms session 6 personnel was identical to session 5. Original 10-inch LP (Capitol H-516, released Aug 2, 1954) contained 7 tracks from sessions 1–4. Expanded 12-inch LP (Capitol T-516, released Aug 1, 1955) added 4 tracks from sessions 5–6. The 1960 stereo re-recording (Capitol SW-516) is a different album with different musicians — NOT documented here. Several musicians appearing in combined discography lists (Ollie Mitchell, Joe Castro, Jack Marshall, Larry Bunker, Phil Stephens, Buddy Collette, Paul Horn) are NOT confirmed for the 1953–1955 sessions and are likely from the 1960 stereo re-recording; they have been excluded from this record. Engineer unknown — no engineer credit found in any consulted source; Capitol Melrose Studios sessions of this era do not have engineer credits routinely documented in standard discographies. Producer Lee Gillette credit from Wikipedia infobox (S2); epistemic_production set to 'inf' pending liner-notes verification. Previous DB record had Bud Shank and Shelly Manne as 'unk'; both upgraded to 'obs' — S3 explicitly names them in specific sessions. Barney Kessel was previously 'unk'; upgraded to 'obs' — S3 confirms him in session 1 only (track: 'Something Cool')."
}
```

---

## 3. Summary Notes

### Incomplete Records

**Producer credit (Lee Gillette):** Sourced from the Wikipedia infobox (S2). AllMusic credits tab (S1) was blocked with HTTP 403 during this session, so the producer credit could not be cross-confirmed against the most authoritative secondary database. Marked `epistemic_production: "inf"`. Liner notes verification would upgrade this to `obs`.

**Engineer:** No engineer credit found in any source consulted. Capitol Melrose Studios sessions from 1953–1955 do not appear to have engineer credits routinely recorded in standard jazz discographies. Field set to `null`.

**Multi-date sessions (sessions 2, 4, 6):** Three session clusters span more than one calendar date (session 2: Dec 27, 1953 and Mar 18, 1954; session 4: Jan 19, Jan 26, and Mar 18, 1954; session 6: May 10, May 24, and June 2, 1955). The jazzdisco source documents these as single session entities without distinguishing which musicians were present on which sub-date, or which specific sub-date each track was completed. Track `session_date` values for these sessions use the first documented date and are marked `epistemic_track: "inf"`.

**Track `session_date` for "Midnight Sun":** S3 links this track to the Dec 27, 1953 / Mar 18, 1954 session. S3 treats both dates as a single session producing one track (matrix 12181). It is possible the track was recorded on one date with pickup or editing on the other. The recorded date is the session start date (1953-12-27) and the `epistemic_track` is `inf`.

### Track Assignment Coverage

**Track assignments complete: true.** All 11 tracks on the 1955 12-inch LP (Capitol T-516) have confirmed session assignments, derived from S3 (session-level data) and S4 (matrix-number-to-title matching). Sessions 1, 2, and 5 named their tracks directly in S3. Sessions 3, 4, and 6 were resolved via matrix numbers 12259–12261, 12263–12264, and 13854–13856, matched to titles in S4.

The `tracks` array is fully populated with personnel for each of the 11 tracks, with personnel lists derived from session membership. This album has zero tracks with empty `personnel` arrays.

### Name Variant Conflicts

**Johnny Rotella / John Rotella:** S3 (jazzdisco catalog) uses "Johnny Rotella." S2 (Wikipedia) and the Amazon listing use "John Rotella." Canonical form chosen: "Johnny Rotella" per S3, which is the most session-specific source. Variant recorded in `name_variants`.

**Fred Fallensby / Fred Falensby:** S3 uses "Fred Fallensby." Amazon listing and some secondary sources use "Fred Falensby." Canonical form: "Fred Fallensby" per S3. Variant recorded in `name_variants`.

**Nick DiMaio / Nick Dimaio:** S3 uses "Nick DiMaio." Amazon listing uses "Nick Dimaio." Canonical form: "Nick DiMaio" per S3. No variant recorded (difference is capitalization only, not a substantive conflict).

**No conflict** between S3 and S4 on any musician name.

### Source Quality Notes

**S3 (JazzDisco.org catalog) — highest quality.** Session-level authority for this album. Provides full personnel per session with instruments, studio name, and session dates. Named the tracks for sessions 1, 2, and 5 directly. This is the spine of the record.

**S4 (JazzDisco.org discography) — strong supplement.** Provided track-to-matrix number mappings that unlocked the track titles for sessions 3, 4, and 6. Also surfaced the unissued session 4 track (matrix 12262). The two jazzdisco fetches are internally consistent.

**S2 (Wikipedia) — good for structure and production.** Provided the track listing with durations, composers, side assignments, and the producer credit. Also provided confirmation that the 1960 stereo re-recording introduced a different set of musicians. However, the Wikipedia article's personnel section covers all three versions of the album (1954/1955/1960) without clearly separating them, which is the source of confusion about musicians like Ollie Mitchell, Joe Castro, and Larry Bunker.

**S1 (AllMusic) — unavailable.** Credits tab returned HTTP 403 during this session. AllMusic is typically the most complete single secondary source for production credits; its absence means the producer credit and any track-level credits it carries could not be verified. This is the largest gap in source coverage.

**S5 (Wikidata) — narrow but reliable.** Used solely to confirm the MusicBrainz release group MBID `fb5bcd7c-a62d-4741-b024-35e702d861e3`. Wikidata's structured property (MusicBrainz release group ID) is a direct, human-curated link; this MBID is treated as confirmed.

### Unusual Findings

**Scale of personnel.** This album has 40 distinct credited personnel entries (39 musicians plus Pete Rugolo as arranger), drawn from six session clusters, with only Conrad Gozzo playing on every track. It is by far the most complex personnel record in this canon. The rotating three-section approach (session 1 through 6 each bringing a different configuration) reflects Rugolo's film-score-style orchestral writing.

**Unissued track from session 4.** Matrix 12262, titled "The First Thing You Know, You're In Love," was recorded during the January 19–March 18, 1954 session but was not released on the album. Documented here as a note; not included in the `tracks` array.

**Barney Kessel on only one track.** Kessel — the most celebrated guitarist on the album's combined personnel list — appears only on the title track "Something Cool" (session 1, August 14, 1953). The previous DB record listed him without session context and marked him `unk`; this gap-fill confirms and narrows his appearance to a single track.

**Session 6 personnel identical to session 5.** S3 explicitly states session 6 (May 10, May 24, June 2, 1955) had the same personnel as session 5 (December 29, 1954). This means the same 18 musicians — including Frank Rosolino, Vincent DeRosa, and Harry Babasin — appear on four of the album's eleven tracks.

**1960 stereo re-recording contamination in combined lists.** Amazon's combined personnel listing includes Ollie Mitchell (trumpet), Joe Castro (piano), Jack Marshall (guitar), Larry Bunker (drums), Phil Stephens (tuba), Buddy Collette (reeds), and Paul Horn (reeds). None of these musicians appear in S3's documented session data for the 1953–1955 recordings. They are consistent with a 1960 West Coast orchestra and are excluded from this record with an explanatory note. Downstream systems should not conflate the two recordings.

**Bob Cooper — family connection.** Bob Cooper (tenor saxophone, sessions 1, 3, 4) was June Christy's husband. He does not appear in sessions 2, 5, or 6.
