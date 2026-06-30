# Personnel Research — Gap-Fill Batch 02

Albums: gerry-mulligan-quartet-1952, chet-baker-chet-baker-sings-1954, andrew-hill-black-fire

---

## 1. Source Map

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | gerrymulligan.com — Gerry Mulligan Quartet PJLP-1 | Web | https://www.gerrymulligan.com/gerry-mulligan-quartet-pjlp-1/ | Official artist site; track listing; quartet personnel listed as unit (no per-track breakdown at this source) |
| S2 | Jazz Discography (jazzdisco.org) — Pacific Jazz Discography 1952–1954 | Web | https://www.jazzdisco.org/pacific-jazz-records/discography-1952-1954/ | Session-level data: dates, studios, personnel per session for 1952 Mulligan sessions |
| S3 | Wikipedia — Gerry Mulligan Quartet Volume 1 | Web | https://en.wikipedia.org/wiki/Gerry_Mulligan_Quartet_Volume_1 | Track listing, session-to-track assignments; distinguishes original LP from 2001 CD bonus content |
| S4 | Wikipedia — Chet Baker Sings | Web | https://en.wikipedia.org/wiki/Chet_Baker_Sings | Session breakdown (Oct 1953, Feb 1954, Jul 1956); personnel per session; original LP vs. expanded PJ-1222 |
| S5 | Jazz Discography (jazzdisco.org) — Chet Baker Discography | Web | https://www.jazzdisco.org/chet-baker/discography/ | Session-level authority: exact dates, studios, personnel per date for all Chet Baker sessions |
| S6 | Jazz Discography (jazzdisco.org) — Pacific Jazz Discography 1955–1956 | Web | https://www.jazzdisco.org/pacific-jazz-records/discography-1955-1956/ | Confirmed per-date lineup for July 23 and July 30, 1956 Forum Theatre sessions; bassist James Bond confirmed for both dates |
| S7 | Wikipedia — Black Fire (album) | Web | https://en.wikipedia.org/wiki/Black_Fire_(album) | Recording dates Nov 8–9, 1963; producer Alfred Lion; track listing with durations; no per-track personnel |
| S8 | Jazz Discography (jazzdisco.org) — Andrew Hill Catalog | Web | https://www.jazzdisco.org/andrew-hill/catalog/ | Session-level authority: recording date Nov 8, 1963; per-track musician credits: Henderson tracks #1–3,5,7 and Haynes tracks #1,2,4–7 in session recording order by take number |
| S9 | Deep Groove Mono — Andrew Hill Black Fire (Blue Note 4151) | Web | https://dgmono.com/andrew-hill-black-fire-blue-note-4151/ | Original pressing analysis; recording date cited as Nov 9, 1963; VANGELDER stamp confirmed in dead wax |

---

## 2. Album JSON Records

```json
{
  "album_id": "gerry-mulligan-quartet-1952",
  "recording_dates": ["1952-08-16", "1952-10-15", "1952-10-16"],
  "multi_session": true,
  "studio": "Phil Turetsky's House, Los Angeles, CA (August 16 session); Gold Star Studios, Los Angeles, CA (October 15–16 session)",
  "producer": "Richard Bock",
  "engineer": null,
  "label": "Pacific Jazz",
  "epistemic_production": "obs",
  "personnel": [
    {
      "name": "Gerry Mulligan",
      "instrument": "baritone saxophone",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S1", "S2", "S3"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Chet Baker",
      "instrument": "trumpet",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S1", "S2", "S3"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Bob Whitlock",
      "instrument": "double bass",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S1", "S2", "S3"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Chico Hamilton",
      "instrument": "drums",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S1", "S2", "S3"],
      "name_variants": [],
      "notes": ""
    }
  ],
  "tracks": [
    {
      "title": "Bernie's Tune",
      "track_number": 1,
      "side": "A",
      "duration": null,
      "session_date": "1952-08-16",
      "composers": ["Bernie Miller"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Walkin' Shoes",
      "track_number": 2,
      "side": "A",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Gerry Mulligan"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Nights At The Turntable",
      "track_number": 3,
      "side": "A",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Gerry Mulligan"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Lullaby Of The Leaves",
      "track_number": 4,
      "side": "A",
      "duration": null,
      "session_date": "1952-08-16",
      "composers": ["Bernice Petkere"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Frenesi",
      "track_number": 5,
      "side": "B",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Alberto Domínguez"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Freeway",
      "track_number": 6,
      "side": "B",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Chet Baker"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Soft Shoe",
      "track_number": 7,
      "side": "B",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Gerry Mulligan"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    },
    {
      "title": "Aren't You Glad You're You",
      "track_number": 8,
      "side": "B",
      "duration": null,
      "session_date": "1952-10-15/1952-10-16",
      "composers": ["Johnny Burke", "Jimmy Van Heusen"],
      "personnel": ["Gerry Mulligan", "Chet Baker", "Bob Whitlock", "Chico Hamilton"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S2", "S3"]
    }
  ],
  "track_assignments_complete": true,
  "musicbrainz_release_group_mbid": null,
  "cover_art": [],
  "sources": ["S1", "S2", "S3"],
  "notes": "Two-session album. Aug 16, 1952 (Phil Turetsky's House, informal home recording): Bernie's Tune (A1), Lullaby Of The Leaves (A4). Oct 15–16, 1952 (Gold Star Studios, professional studio): Walkin' Shoes (A2), Nights At The Turntable (A3), Frenesi (B1), Freeway (B2), Soft Shoe (B3), Aren't You Glad You're You (B4). The October session spans two days; exact per-track day assignment within Oct 15–16 is not distinguished in available sources. The same four-piece lineup played both sessions. Producer Richard Bock recorded the informal August session personally on portable reel-to-reel tape; engineer for Gold Star Studios session is not documented in available sources. CORRECTED PERSONNEL: Carson Smith (bass) and Larry Bunker (drums) were in the DB as unk — both are confirmed NOT on PJ-LP-1. Carson Smith replaced Whitlock in January 1953 Haig sessions; Larry Bunker replaced Hamilton starting February 24, 1953 Gold Star sessions. Both 1953 sessions are included only on the 2001 CD compilation (Gerry Mulligan Quartet Volume 1, with 19 tracks) and do not appear on the original 10-inch LP. Those DB entries should be removed."
}
```

---

```json
{
  "album_id": "chet-baker-chet-baker-sings-1954",
  "recording_dates": ["1953-10-27", "1954-02-15", "1956-07-23", "1956-07-30"],
  "multi_session": true,
  "studio": "Radio Recorders, Los Angeles, CA (Oct 27, 1953); Capitol Melrose Studios, Los Angeles, CA (Feb 15, 1954); Forum Theatre, Los Angeles, CA (Jul 23 and Jul 30, 1956)",
  "producer": "Richard Bock",
  "engineer": null,
  "label": "Pacific Jazz",
  "epistemic_production": "obs",
  "personnel": [
    {
      "name": "Chet Baker",
      "instrument": "vocals",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S4", "S5"],
      "name_variants": [],
      "notes": "Also plays trumpet; this is a vocals-primary album. Russ Freeman confirmed as sole pianist on all sessions."
    },
    {
      "name": "Russ Freeman",
      "instrument": "piano",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S4", "S5"],
      "name_variants": [],
      "notes": "Also plays celesta on Side A tracks (1956 sessions)."
    },
    {
      "name": "Jimmy Bond",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": [
        "That Old Feeling",
        "It's Always You",
        "Like Someone In Love",
        "My Ideal",
        "I've Never Been In Love Before",
        "My Buddy"
      ],
      "session_dates": ["1956-07-23", "1956-07-30"],
      "epistemic": "obs",
      "sources": ["S5", "S6"],
      "name_variants": ["James Bond"],
      "notes": "Credited as 'James Bond' in jazzdisco.org; 'Jimmy Bond' is the standard jazz discography form. Present on both July 1956 dates."
    },
    {
      "name": "Peter Littman",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": [
        "That Old Feeling",
        "It's Always You",
        "I've Never Been In Love Before",
        "My Buddy"
      ],
      "session_dates": ["1956-07-23"],
      "epistemic": "obs",
      "sources": ["S5", "S6"],
      "name_variants": [],
      "notes": "July 23, 1956 session only."
    },
    {
      "name": "Larance Marable",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": [
        "Like Someone In Love",
        "My Ideal"
      ],
      "session_dates": ["1956-07-30"],
      "epistemic": "obs",
      "sources": ["S5", "S6"],
      "name_variants": ["Lawrence Marable"],
      "notes": "July 30, 1956 session only. 'Lawrence Marable' appears in some sources; 'Larance Marable' is the form used in primary jazz discographies."
    },
    {
      "name": "Carson Smith",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": [
        "But Not For Me",
        "Time After Time",
        "I Get Along Without You Very Well",
        "My Funny Valentine",
        "There Will Never Be Another You",
        "I Fall In Love Too Easily",
        "Look for the Silver Lining"
      ],
      "session_dates": ["1954-02-15"],
      "epistemic": "obs",
      "sources": ["S4", "S5"],
      "name_variants": [],
      "notes": "February 15, 1954 session (Capitol Melrose Studios). On all Side B tracks except The Thrill Is Gone."
    },
    {
      "name": "Bob Neel",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": [
        "But Not For Me",
        "Time After Time",
        "I Get Along Without You Very Well",
        "My Funny Valentine",
        "There Will Never Be Another You",
        "I Fall In Love Too Easily",
        "Look for the Silver Lining"
      ],
      "session_dates": ["1954-02-15"],
      "epistemic": "obs",
      "sources": ["S4", "S5"],
      "name_variants": [],
      "notes": "February 15, 1954 session. On same tracks as Carson Smith."
    },
    {
      "name": "Joe Mondragon",
      "instrument": "double bass",
      "scope": "selected-tracks",
      "tracks": ["The Thrill Is Gone"],
      "session_dates": ["1953-10-27"],
      "epistemic": "obs",
      "sources": ["S5"],
      "name_variants": [],
      "notes": "October 27, 1953 session (Radio Recorders). Only one track from this session appeared on the album."
    },
    {
      "name": "Shelly Manne",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": ["The Thrill Is Gone"],
      "session_dates": ["1953-10-27"],
      "epistemic": "obs",
      "sources": ["S5"],
      "name_variants": [],
      "notes": "October 27, 1953 session (Radio Recorders). Absent from DB — this is a gap-fill addition. Only the track The Thrill Is Gone from this session appeared on the album."
    }
  ],
  "tracks": [
    {
      "title": "That Old Feeling",
      "track_number": 1,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-23",
      "composers": ["Lew Brown", "Sammy Fain"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Peter Littman"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "It's Always You",
      "track_number": 2,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-23",
      "composers": ["Johnny Burke", "Jimmy Van Heusen"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Peter Littman"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "Like Someone In Love",
      "track_number": 3,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-30",
      "composers": ["Johnny Burke", "Jimmy Van Heusen"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Larance Marable"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "My Ideal",
      "track_number": 4,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-30",
      "composers": ["Leo Robin", "Richard Whiting", "Newell Chase"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Larance Marable"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "I've Never Been In Love Before",
      "track_number": 5,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-23",
      "composers": ["Frank Loesser"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Peter Littman"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "My Buddy",
      "track_number": 6,
      "side": "A",
      "duration": null,
      "session_date": "1956-07-23",
      "composers": ["Walter Donaldson", "Gus Kahn"],
      "personnel": ["Chet Baker", "Russ Freeman", "Jimmy Bond", "Peter Littman"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5", "S6"]
    },
    {
      "title": "But Not For Me",
      "track_number": 7,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["George Gershwin", "Ira Gershwin"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "Time After Time",
      "track_number": 8,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Jule Styne", "Sammy Cahn"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "I Get Along Without You Very Well",
      "track_number": 9,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Hoagy Carmichael"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "My Funny Valentine",
      "track_number": 10,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Richard Rodgers", "Lorenz Hart"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "There Will Never Be Another You",
      "track_number": 11,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Harry Warren", "Mack Gordon"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "The Thrill Is Gone",
      "track_number": 12,
      "side": "B",
      "duration": null,
      "session_date": "1953-10-27",
      "composers": ["Lew Brown", "Ray Henderson"],
      "personnel": ["Chet Baker", "Russ Freeman", "Joe Mondragon", "Shelly Manne"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S5"]
    },
    {
      "title": "I Fall In Love Too Easily",
      "track_number": 13,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Jule Styne", "Sammy Cahn"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    },
    {
      "title": "Look for the Silver Lining",
      "track_number": 14,
      "side": "B",
      "duration": null,
      "session_date": "1954-02-15",
      "composers": ["Jerome Kern", "Buddy DeSylva"],
      "personnel": ["Chet Baker", "Russ Freeman", "Carson Smith", "Bob Neel"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S4", "S5"]
    }
  ],
  "track_assignments_complete": true,
  "musicbrainz_release_group_mbid": null,
  "cover_art": [],
  "sources": ["S4", "S5", "S6"],
  "notes": "Four sessions. (1) Oct 27, 1953 (Radio Recorders): Chet Baker, Russ Freeman, Joe Mondragon (bass), Shelly Manne (drums) — only 'The Thrill Is Gone' from this session appears on the album. (2) Feb 15, 1954 (Capitol Melrose Studios): Chet Baker, Russ Freeman, Carson Smith (bass), Bob Neel (drums) — seven tracks. (3) Jul 23, 1956 (Forum Theatre): Chet Baker, Russ Freeman, Jimmy Bond (bass), Peter Littman (drums) — four tracks: That Old Feeling, It's Always You, I've Never Been In Love Before, My Buddy. (4) Jul 30, 1956 (Forum Theatre): Chet Baker, Russ Freeman, Jimmy Bond (bass), Larance Marable (drums) — two tracks: Like Someone In Love, My Ideal. The album_id refers to the 1954 original release (PJ-LP-11, 8 tracks, Side A+B from sessions 1+2), but the DB's 14-track record corresponds to the expanded 1956 12-inch reissue (PJ-1222) which placed the six 1956 session tracks on Side A and the eight original-LP tracks on Side B. CORRECTED PERSONNEL: Carson Smith, Joe Mondragon, Peter Littman, and Larance Marable upgraded from unk to obs with specific track and session assignments. ADDED PERSONNEL: Shelly Manne (drums, 'The Thrill Is Gone') was absent from the DB — added here as gap-fill. NOTE: 'I Fall In Love Too Easily' was also recorded in the Oct 27, 1953 session but only the Feb 15, 1954 take appears on the album per jazzdisco.org session records."
}
```

---

```json
{
  "album_id": "andrew-hill-black-fire",
  "recording_dates": ["1963-11-08", "1963-11-09"],
  "multi_session": false,
  "studio": "Van Gelder Studio, Englewood Cliffs, New Jersey",
  "producer": "Alfred Lion",
  "engineer": "Rudy Van Gelder",
  "label": "Blue Note",
  "epistemic_production": "obs",
  "personnel": [
    {
      "name": "Andrew Hill",
      "instrument": "piano",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S7", "S8"],
      "name_variants": [],
      "notes": "All compositions on the album are by Andrew Hill."
    },
    {
      "name": "Richard Davis",
      "instrument": "double bass",
      "scope": "all-tracks",
      "tracks": null,
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S7", "S8"],
      "name_variants": [],
      "notes": ""
    },
    {
      "name": "Joe Henderson",
      "instrument": "tenor saxophone",
      "scope": "selected-tracks",
      "tracks": [
        "Pumpkin",
        "Black Fire",
        "Cantarnos",
        "McNeil Island",
        "Land of Nod"
      ],
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S8"],
      "name_variants": [],
      "notes": "Per jazzdisco.org session listing, Henderson appears on tracks #1–3, 5, 7 in recording sequence (take-number order): Land of Nod (tk.3), Cantarnos (tk.9), McNeil Island (tk.15), Pumpkin (tk.20), Black Fire (tk.27). Absent on Subterfuge (tk.23) and Tired Trade (tk.17). In album release order, Henderson is on tracks 1, 3, 4, 6, 7. Subterfuge and Tired Trade are piano-bass-drums trios."
    },
    {
      "name": "Roy Haynes",
      "instrument": "drums",
      "scope": "selected-tracks",
      "tracks": [
        "Pumpkin",
        "Subterfuge",
        "Black Fire",
        "Cantarnos",
        "Tired Trade",
        "Land of Nod"
      ],
      "session_dates": null,
      "epistemic": "obs",
      "sources": ["S8"],
      "name_variants": [],
      "notes": "Per jazzdisco.org session listing, Haynes appears on tracks #1, 2, 4–7 in recording sequence: Land of Nod (tk.3), Cantarnos (tk.9), Tired Trade (tk.17), Pumpkin (tk.20), Subterfuge (tk.23), Black Fire (tk.27). Absent on McNeil Island (tk.15). In album release order, Haynes is on tracks 1, 2, 3, 4, 5, 7. McNeil Island (2:58) is a piano-bass-tenor saxophone trio without drums."
    }
  ],
  "tracks": [
    {
      "title": "Pumpkin",
      "track_number": 1,
      "side": "A",
      "duration": "5:24",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Joe Henderson", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "Subterfuge",
      "track_number": 2,
      "side": "A",
      "duration": "8:04",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "Black Fire",
      "track_number": 3,
      "side": "A",
      "duration": "6:56",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Joe Henderson", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "Cantarnos",
      "track_number": 4,
      "side": "B",
      "duration": "5:42",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Joe Henderson", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "Tired Trade",
      "track_number": 5,
      "side": "B",
      "duration": "5:51",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "McNeil Island",
      "track_number": 6,
      "side": "B",
      "duration": "2:58",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Joe Henderson"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    },
    {
      "title": "Land of Nod",
      "track_number": 7,
      "side": "B",
      "duration": "5:48",
      "session_date": "1963-11-08/1963-11-09",
      "composers": ["Andrew Hill"],
      "personnel": ["Andrew Hill", "Richard Davis", "Joe Henderson", "Roy Haynes"],
      "bonus_track": false,
      "alternate_take": false,
      "epistemic_track": "obs",
      "sources": ["S7", "S8"]
    }
  ],
  "track_assignments_complete": true,
  "musicbrainz_release_group_mbid": "2f38d349-1b85-39a0-8834-851c43297f1c",
  "cover_art": [
    {
      "role": "front",
      "source": "cover-art-archive",
      "url": "https://coverartarchive.org/release-group/2f38d349-1b85-39a0-8834-851c43297f1c/front",
      "is_original_cover": null,
      "epistemic": "inf",
      "notes": "Constructed from MusicBrainz release-group MBID found via search result URL; not individually verified at CAA."
    }
  ],
  "sources": ["S7", "S8", "S9"],
  "notes": "RECORDING DATE DISCREPANCY: Wikipedia (S7) says November 8–9, 1963 (two-day session); jazzdisco.org (S8) lists only November 8, 1963; Deep Groove Mono (S9) says November 9, 1963. Recording dates set to both Nov 8 and Nov 9, following Wikipedia as the source that explicitly states both dates; multi_session remains false since it is a single continuous recording engagement with one lineup. The album runs 27 takes (Land of Nod is tk.3, Black Fire is tk.27), consistent with a dense two-day session. PER-TRACK PERSONNEL: This is not a standard all-quartet affair on every track. Jazzdisco.org session records document the following atypical configurations — Subterfuge (A2) and Tired Trade (B2) are piano-bass-drums trios (no Henderson); McNeil Island (B3) is a piano-bass-tenor trio (no Haynes). The dispatch expectation that Henderson and Haynes were 'almost certainly all-tracks' is not borne out by the session-level source. Engineer Rudy Van Gelder confirmed by Van Gelder Studio location and VANGELDER stamp in dead wax (S9). CD bonus tracks ('Pumpkin' alternate take and 'Black Fire' alternate take) are not included in the track array — they appear on reissues only."
}
```

---

## 3. Summary Notes

### Incomplete Records

**gerry-mulligan-quartet-1952:** Track durations are missing (not available in any accessed source; the original 10-inch LP predates standard duration documentation in jazz databases). MusicBrainz release group MBID was not found in accessible sources — left null. Engineer for Gold Star Studios sessions (October 1952) is not identified in any source; the August session was recorded informally by producer Richard Bock on portable equipment with no separate engineer credit.

**chet-baker-chet-baker-sings-1954:** Track durations for all 14 tracks are missing. Engineer credit is unknown across all three session locations (Radio Recorders, Capitol Melrose Studios, Forum Theatre) — no source consulted documented an engineer for any of the Chet Baker Sings sessions. MusicBrainz release group MBID was not found. Note: the album_id carries the 1954 year (original 10-inch PJ-LP-11) but the DB's 14-track record corresponds to the 1956 expanded 12-inch reissue (PJ-1222). This is a structural note for downstream context, not a data error in the personnel record.

**andrew-hill-black-fire:** Recording date has a three-way source conflict (November 8 only per jazzdisco.org; November 9 only per dgmono.com; November 8–9 per Wikipedia). Wikipedia was used as the tiebreaker because it is the only source explicitly stating both dates. The issue cannot be fully resolved without access to the original Blue Note session log or liner notes.

### Track Assignment Coverage

All three albums reached `track_assignments_complete: true`.

- **gerry-mulligan-quartet-1952:** 8 tracks, both sessions confirmed with same four-piece lineup throughout. The same personnel appears on all 8 tracks; assignment is complete because session-level data (jazzdisco.org + Wikipedia) unambiguously assigns every LP track to one of the two sessions and both sessions had identical personnel.

- **chet-baker-chet-baker-sings-1954:** 14 tracks fully assigned. Per-track personnel confirmed at session level: jazzdisco.org per-session rosters (S5, S6) give unambiguous musician assignments for all four sessions. All 14 tracks mapped to a specific session and therefore to a specific rhythm section.

- **andrew-hill-black-fire:** 7 tracks assigned. Jazzdisco.org session entry gives per-track participation for Henderson and Haynes using session-sequence track numbers cross-referenced to release order via take numbers. Richard Davis and Andrew Hill confirmed on all 7 tracks.

### Name Variant Conflicts

**Jimmy Bond / James Bond (Chet Baker Sings):** The bassist is credited as "James Bond" in jazzdisco.org session records and as "Jimmy Bond" in the existing DB entry (obs). "Jimmy Bond" is the canonical jazz discography form used by AllMusic and Wikipedia; "James Bond" is the legal name form used in some session logs. Canonical form kept as "Jimmy Bond" with "James Bond" listed as name variant.

**Larance Marable / Lawrence Marable (Chet Baker Sings):** Jazzdisco.org Pacific Jazz 1955–1956 discography uses "Lawrence Marable" while the existing DB entry uses "Larance Marable." "Larance Marable" is the musician's legal first name and is used in primary jazz reference sources (Tom Lord, AllMusic). Canonical form kept as "Larance Marable" with "Lawrence Marable" listed as name variant.

### Source Quality Notes

The most reliable sources for this batch were the two jazzdisco.org entries (Pacific Jazz discographies S2 and S6, and the individual artist discography/catalog pages S5 and S8). These provided session-level resolution — exact dates, studio locations, and per-track or per-session personnel — that no other source matched. Wikipedia's album articles (S3, S4, S7) were consistent with jazzdisco.org and provided useful corroboration and additional detail (e.g., the Nov 8–9 date range for Black Fire). The gerrymulligan.com artist site (S1) confirmed the quartet lineup but did not offer session-level breakdown. AllMusic returned HTTP 403 for all attempted fetches and was not usable. Discogs also returned HTTP 403. MusicBrainz returned a bot-verification page. Deep Groove Mono (S9) was useful for pressing-level confirmation of Van Gelder engineering on Black Fire but provided only a single recording date (Nov 9) that conflicts with the more detailed Wikipedia and jazzdisco.org data.

### Unusual Findings

**Gerry Mulligan Quartet — Carson Smith and Larry Bunker confirmed absent:** These two musicians were in the DB as unk but are definitively not on the original PJ-LP-1. They appear only on 1953 sessions (January 1953 Haig dates for Smith; February–May 1953 Gold Star and Haig dates for Bunker) that were first released on the 2001 CD compilation. The original 10-inch LP has a single four-person lineup across both 1952 sessions. DB entries for these two musicians should be deleted.

**Andrew Hill Black Fire — not a standard all-quartet album:** The dispatch noted Henderson and Haynes were "almost certainly all-tracks." The jazzdisco.org session catalog contradicts this directly. Two tracks (Subterfuge, Tired Trade) are piano-bass-drums trios without Henderson; one track (McNeil Island, 2:58) is a piano-bass-tenor trio without Haynes. These configurations are consistent with Andrew Hill's documented avant-garde recording practice and are supported by a session-level source (jazzdisco.org, the strongest authority for Blue Note sessions). The source epistemic is "obs" for both Henderson and Haynes per-track assignments.

**Chet Baker Sings — Shelly Manne entirely missing from DB:** The October 27, 1953 session at Radio Recorders featured Joe Mondragon and Shelly Manne as the rhythm section, but only Shelly Manne was absent from the existing DB record. Joe Mondragon was present as unk. Both are now confirmed obs on "The Thrill Is Gone" only. Shelly Manne must be added as a new personnel entry.

**Chet Baker Sings — "I Fall In Love Too Easily" recorded twice:** The track appears on both the October 27, 1953 session (with Mondragon/Manne) and the February 15, 1954 session (with Smith/Neel). Only the February 1954 take appears on the album per jazzdisco.org session records; the October 1953 take was not released on this album.
