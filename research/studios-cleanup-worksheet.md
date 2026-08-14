# Studios Cleanup Worksheet

> **RATIFIED 2026-08-14** — John reviewed and accepted all 46 items ("All reviewed.
> All accepted."), including rulings D1 (Bitches Brew → 30th Street), D2 (Inner
> Mounting Flame held at city level), D3 (RCA Hollywood qualifier dropped).
> Executed same day: migration 5a + `scripts/studio-cleanup-2026-08-14.sql`
> (116 edit_log rows). Post-execution: 47 canonical places from these rulings,
> 8 merged-away rows retained de-slugged. One row (studio 207, Seven Steps to
> Heaven — added by the drip after this worksheet's survey) postdates the
> ratification and awaits its own ruling.

**Purpose**: John's per-item ruling document for the canonical place set (Studios map,
decision 1 of 7). Every raw `_jazzcanon.studio` row → proposed canonical place(s) →
merge/split/exclude → evidence. Nothing here touches the DB; rulings get executed
afterward per `config/edit-contract.md`.

**Provenance**: 46 rows researched 2026-08-12 by four parallel Sonnet agents
(grouped: Van Gelder+Columbia / NYC / West Coast+RCA / live+international), assembled
and cross-batch-reconciled by the session lead. Raw fragments preserved in the session
scratchpad. All addresses are source-cited or explicitly marked undocumented — no
invented precision, no geocoding yet.

**How to read**: Items are grouped by ruling type — clean keeps first (pattern forms
fast, bulk-accept candidate), then merges, then splits, then the genuine questions.
Each item ends with a `Ruling:` line to fill in. Epistemic shorthand: an address
marked *(documented)* has a cited source; *(undocumented)* means honestly absent from
sources found — those places will be city-precision on the map unless later research
upgrades them.

**Bottom line if all proposals are accepted**: 46 raw rows → ~47 canonical places
(25 keeps, 1 city-level keep, 5 rows merged away, 14 compound/split rows yielding
~20 constituent places, 1 newly discovered place, 2–3 pending your calls).

---

## A. Clean keeps (25) — identity confirmed, no structural change

#### A1. [115] Raw: "Birdland (live)" / "New York City"
- **Keep** — Birdland · club · New York, NY · 1678 Broadway at W 52nd St *(documented)*
- Operated 1949–1965 at this address; the 1954 Blakey date falls inside. Later revivals post-date the canon window. https://en.wikipedia.org/wiki/Birdland_(New_York_jazz_club)
- Confidence: high. **Ruling: ____**

#### A2. [138] Raw: "Village Vanguard" / "New York City (live)"
- **Keep** — Village Vanguard · club · New York, NY · 178 Seventh Ave South *(documented)*
- Same address continuously since 1935; covers Rollins 1957 and Evans 1961. https://en.wikipedia.org/wiki/Village_Vanguard
- Confidence: high. **Ruling: ____**

#### A3. [118] Raw: "Columbia 30th Street Studio" / "New York City"
- **Keep** (merge target for B1, possibly D1) — CBS 30th Street Studio · studio · New York, NY · 207 East 30th St *(documented)*
- Converted 1875 church ("The Church"), Columbia's flagship 1948–1981; Kind of Blue et al. https://en.wikipedia.org/wiki/CBS_30th_Street_Studio
- Naming call folded in: raw says "Columbia 30th Street", Wikipedia titles it "CBS 30th Street" — same building, pick house style.
- Confidence: high. **Ruling: ____**

#### A4. [119] Raw: "Columbia Studios" / "Hollywood, Los Angeles"
- **Keep** — Columbia Records Hollywood Studio (CBS Columbia Square, Studio A) · studio · Hollywood, CA · 6121 Sunset Blvd *(documented)*
- Ex-CBS-Radio Studio A, renovated 1961, ran to 1972; covers the E.S.P. dates (Jan 1965). One secondary source loosely says "Sunset and Gower" (a different intersection ~1 mi away) — judged a colloquial mix-up, flagged not erased. https://forums.stevehoffman.tv/threads/columbia-studios-sunset-and-gower.44945/ · https://en.wikipedia.org/wiki/E.S.P._(Miles_Davis_album)
- Confidence: medium-high. **Ruling: ____**

#### A5. [114] Raw: "Atlantic Studios" / "New York"
- **Keep** — Atlantic Studios · studio · New York, NY · 1841 Broadway at 60th St *(documented, with one date caveat)*
- Atlantic's house studio moved twice before settling: 234 W 56th (1947–56) → 157 W 57th (1956–58) → 1841 Broadway (1959–90s). Giant Steps (Mar–Dec 1959) and Black Saint (1963) sit at 1841 Broadway; the row's Feb 1959 date is ambiguous — no source gives the exact move month. https://en.wikipedia.org/wiki/Atlantic_Studios
- Note for the precision field: if the Feb 1959 session matters, its *address* is uncertain between two documented buildings even though the *place identity* (Atlantic's house studio) is solid.
- Confidence: high identity / medium on the Feb-1959 address. **Ruling: ____**

#### A6. [131] Raw: "Reeves Sound Studios" / "New York City"
- **Keep** — Reeves Sound Studios · studio · New York, NY · 304 East 44th St *(documented — Library of Congress HABS)*
- https://www.loc.gov/item/ny0943/ · https://www.preservationsound.com/2014/02/reeves-sound-studios-nyc-1933-197x/
- Per-album re-verification of the four albums not individually done; studio identity certain.
- Confidence: high place / medium per-album. **Ruling: ____**

#### A7. [139] Raw: "WOR Studios" / "New York City"
- **Keep** (merge target for C2's WOR constituent) — WOR Studios · studio · New York, NY · 1440 Broadway *(documented)*
- All three Birth of the Cool dates (1949-01-21, 1949-04-22, 1950-03-09) cross-verify exactly. https://en.wikipedia.org/wiki/Birth_of_the_Cool
- Confidence: high. **Ruling: ____**

#### A8. [140] Raw: "Webster Hall" / "New York City"
- **Keep** — Webster Hall · hall · New York, NY · 125 East 11th St *(documented)*
- 1886 event hall doubling as a large-ensemble recording room; Focus (Getz/Sauter 1961), Take Ten (Desmond 1963). The "RCA operated it 1953–68" detail comes from a local-history blog — background, not fact. https://en.wikipedia.org/wiki/Webster_Hall
- Confidence: high identity / medium on the RCA-operation detail. **Ruling: ____**

#### A9. [162] Raw: "Sound Makers Studios" / "New York City (57th Street…)"
- **Keep** — Sound Makers Studios · studio · New York, NY · 57th St between 6th & 7th Aves *(block-level only — no street number in any source)*
- Money Jungle, Sept 17 1962. https://en.wikipedia.org/wiki/Money_Jungle
- Confidence: high identity; address stays block-level honestly. **Ruling: ____**

#### A10. [163] Raw: "Nola Penthouse Sound Studios" / "New York City"
- **Keep** — Nola Penthouse Sound Studios · studio · New York, NY · 111 West 57th St, penthouse atop Steinway Hall *(documented)*
- Penthouse room opened March 1960; the We Insist! dates (Aug/Sep 1960) just post-date the move, so the address applies. https://en.wikipedia.org/wiki/We_Insist!
- Confidence: high. **Ruling: ____**

#### A11. [178] Raw: "Plaza Sound Studios" / "New York City"
- **Keep** — Plaza Sound Studios · studio · New York, NY · 55 West 50th St, 8th floor (Radio City building) *(documented)*
- Power to the People (Henderson, May 1969). https://en.wikipedia.org/wiki/Power_to_the_People_(Joe_Henderson_album)
- Confidence: high. **Ruling: ____**

#### A12. [199] Raw: "Olmsted Sound Studios" / "New York, NY"
- **Keep** — Olmstead Sound Studios · studio · New York, NY · 1 East 54th St *(documented)*
- Emergency! (Tony Williams Lifetime, May 1969). Spelling: period sources mostly use "Olmstead"; our raw data has "Olmsted" — canonical name proposal uses the majority spelling, flag if you prefer matching the raw.
- Confidence: high. **Ruling: ____**

#### A13. [202] Raw: "RLA Studios" / "New York, NY"
- **Keep** — RLA Studios · studio · New York, NY · West 65th St *(street documented, no number found)*
- Richard L. Alderson's 1962-built room; Heliocentric Worlds Vol. 1 (Sun Ra, April 1965) and much of the ESP-Disk' catalog. https://en.wikipedia.org/wiki/Richard_Alderson_(music_producer)
- Confidence: high identity / medium address precision. **Ruling: ____**

#### A14. [117] Raw: "Capitol Studios" / "Hollywood"
- **Keep** (merge target for C7's 1954 component) — Capitol Records Studio (Melrose Ave) · studio · Hollywood, CA · 5515 Melrose Ave *(documented — J-DISC session sheets)*
- NOT the Capitol Tower — that opened April 1956; this row's 1954–55 dates all predate it. J-DISC cites the Brown/Roach Aug 1954 sessions to this address directly. https://jdisc.columbia.edu/session/clifford-brown-and-max-roach-august-5-1954
- Confidence: high (1954) / medium-high (Feb 1955). **Ruling: ____**

#### A15. [121] Raw: "Contemporary Records studio" / "Los Angeles"
- **Keep** (merge target for B3) — Contemporary Records Studio · studio · Los Angeles, CA · 8481 Melrose Place *(documented)*
- Lester Koenig's converted stockroom behind the label office, built with Roy DuNann late 1955; Art Pepper Meets…, Poll Winners, Way Out West (all 1957). https://www.8481melrose.com/posts/about-contemporary-records
- Confidence: high. **Ruling: ____**

#### A16. [122] Raw: "Forum Theater" / "Los Angeles"
- **Keep** (merge target for C7's 1956 component) — Forum Theatre · other · Los Angeles, CA · 4050 West Pico Blvd *(documented — theater-history sources)*
- A movie theater Dick Bock rented as an ad-hoc no-audience studio; Chet Baker & Crew week, July 1956. Kind is "other" deliberately — neither studio nor live venue. https://en.wikipedia.org/wiki/Chet_Baker_%26_Crew
- Confidence: high. **Ruling: ____**

#### A17. [130] Raw: "Radio Recorders" / "Hollywood, CA"
- **Keep** (merge target for C10's studio component) — Radio Recorders · studio · Hollywood, CA · 7000 Santa Monica Blvd *(documented — historical marker)*
- All three albums (1955–59) fall in the single-address era. https://www.hmdb.org/m.asp?m=204730
- Confidence: high. **Ruling: ____**

#### A18. [144] Raw: "RCA Victor Studios" / "New York City"
- **Keep** (merge target for C11's Karma component) — RCA Victor Studios · studio · New York, NY · 155 East 24th St *(documented)*
- Converted 1907 stable, active 1928–1969; The Bridge (Rollins, 1962). https://en.wikipedia.org/wiki/RCA_Studios_New_York
- Confidence: high. **Ruling: ____**

#### A19. [126] Raw: "Monterey Jazz Festival" / "Monterey, California (live)"
- **Keep** — Monterey Jazz Festival (Monterey County Fairgrounds) · festival · Monterey, CA · 2004 Fairground Rd *(documented)*
- Forest Flower (Lloyd, Sept 18 1966). https://en.wikipedia.org/wiki/Forest_Flower
- Confidence: high. **Ruling: ____**

#### A20. [132] Raw: "The Jazz Workshop (live)" / "San Francisco"
- **Keep** — The Jazz Workshop · club · San Francisco, CA · 473 Broadway *(documented — historical marker)*
- Adderley Quintet in San Francisco (Oct 1959). https://www.hmdb.org/m.asp?m=152646
- Confidence: high. **Ruling: ____**

#### A21. [133] Raw: "The Lighthouse" / "Hermosa Beach, California (live)"
- **Keep** — The Lighthouse · club · Hermosa Beach, CA · 30 Pier Ave *(documented — venue's own history + local history)*
- Sunday Jazz a la Lighthouse (Feb 1953). https://www.thelighthousecafe.net/history
- Confidence: high. **Ruling: ____**

#### A22. [135] Raw: "Tsubo (live)" / "Berkeley, California"
- **Keep** — Tsubo · club · Berkeley, CA · 2901 Telegraph Ave *(documented, single blog source — weakest address in the keeps)*
- Short-lived room (Sept 1961–Oct 1962); Full House (Wes Montgomery, June 25 1962). https://en.wikipedia.org/wiki/Full_House_(Wes_Montgomery_album)
- Confidence: medium on address / high identity. **Ruling: ____**

#### A23. [136] Raw: "Universal Recording" / "Chicago, IL"
- **Keep** — Universal Recording Corporation · studio · Chicago, IL · 111 East Ontario St *(documented for 1955 — the studio moved often)*
- Bill Putnam's studio; Contemporary Concepts (Kenton, July 1955) predates the better-known 46 E Walton address (mid-1956 on). Address history: Civic Opera Bldg (1947) → 100 E Ohio → 111 E Ontario (to mid-1956) → 46 E Walton (1956–70). https://tdwaw.ellingtonweb.ca/supportingwebpages/UniversalRecordingCorporation.html
- Confidence: medium — 1955 address rests on one detailed historical page. **Ruling: ____**

#### A24. [141] Raw: "Pershing Lounge, Pershing Hotel (live)" / "Chicago, Illinois"
- **Keep** — Pershing Lounge (Pershing Hotel) · club · Chicago, IL · E 64th St at S Cottage Grove Ave *(intersection documented, no street number found)*
- At the Pershing (Jamal, Jan 16 1958). Data check: most sources say the recordings span Jan 16 *and* 17; our session row has only the 16th. https://southsideweekly.com/64th-cottage-grove/
- Confidence: medium-high. **Ruling: ____**

#### A25. [190] Raw: "Arne Bendiksen Studio" / "Oslo"
- **Keep** — Arne Bendiksen Studio · studio · Oslo, Norway · *(no address documented)*
- ECM's primary Oslo room pre-Rainbow; Kongshaug engineered here 1967–75. Facing You (1971) directly cited; Crystal Silence (1972) and Witchi-Tai-To (1973) inferred from Kongshaug's tenure, not per-album session credits. https://en.wikipedia.org/wiki/Facing_You
- Confidence: high (1971) / medium (other two). Will be city-precision on the map unless an address surfaces. **Ruling: ____**

## A′. City-level keep (1)

#### A26. [127] Raw: "New York City" / "" (New Bottle Old Wine, Gil Evans, 1958)
- **Keep as city-level** — rescue attempted and honestly failed: Wikipedia, the Cannonball discography site, and Tone Poet reissue coverage all give only "New York City" for all four 1958 dates; no studio named anywhere. https://en.wikipedia.org/wiki/New_Bottle_Old_Wine · https://cannonball-adderley.com/159.htm
- Confidence that this is genuinely undocumented (not under-searched): high.
- Options per handoff decision 4: keep city-level with honest label (proposed), or exclude from map. **Ruling: ____**

---

## B. Merges (4 rows fold away)

#### B1. [179] "CBS 30th Street Studio" → merge into [118]
- Same building, 207 E 30th St. In a Silent Way (Feb 18 1969) explicitly at "CBS 30th Street Studio's Studio B". Minor loose end: the building's rooms are elsewhere described as Studios C and D — room-letter conflict only, building identity solid. https://en.wikipedia.org/wiki/In_a_Silent_Way
- Confidence: high. **Ruling: ____**

#### B2. [160] "A & R Recording" → merge into [113]'s 48th-Street place
- Olé Coltrane (May 25 1961): A&R had exactly one facility in 1961 (112 W 48th St — second room didn't open until 1968), so this merge is unambiguous even though row 113 itself splits (see C5). https://en.wikipedia.org/wiki/Ol%C3%A9_Coltrane
- Confidence: high. **Ruling: ____**

#### B3. [120] "Contemporary Records" → merge into [121]
- Same in-house studio at 8481 Melrose Place; the My Fair Lady date (Aug 1956) falls after the studio opened (late 1955) and after Capitol vacated the alternative Melrose building. Two raw name variants, one room. https://www.8481melrose.com/
- Confidence: medium-high. **Ruling: ____**

#### B4. [195] "Musikstudio Bauer" + [198] "Tonstudio Bauer" → merge as "Studio Bauer, Ludwigsburg" — **with a flag**
- Same city, same surname, same producer (Eicher): Free at Last (1969, ECM 1001, engineer Kurt Rapp) and Bright Size Life (1975, engineer Martin Wieland). **Not airtight**: no source confirms the 1969 and 1975 sessions used the identical physical room rather than a family business with more than one facility; six years and different engineers between them. No address documented for either. https://en.wikipedia.org/wiki/Free_at_Last_(Mal_Waldron_album) · https://ecmreviews.com/2010/03/27/bright-size-life/
- Proposed: merge (the parsimonious reading), city-precision, note the uncertainty in the place's evidence trail.
- Confidence: medium. **Ruling: ____**

---

## C. Splits — compound rows and mislocated constituents (14 rows)

#### C1. [137] "Van Gelder Studio" / "Englewood Cliffs" — **the big one: split 2 places + extract 1 album to a 3rd**
This is handoff decision 5 made concrete. Proposal: two canonical places (the site's R2
renderer constraint also wants this, but the historical case stands on its own — two
addresses, two rooms, different acoustics and eras):
- **Van Gelder Studio, Hackensack** · studio/home · Hackensack, NJ · 25 Prospect Ave *(documented — Rudy's parents' living room)* · operated 1952 – July 1, 1959
- **Van Gelder Studio, Englewood Cliffs** · studio · Englewood Cliffs, NJ · 445 Sylvan Ave *(documented)* · opened July 20, 1959
- **Date boundary is clean and documented**: last Hackensack session July 1 1959, first Englewood Cliffs session July 20 1959 (both on the aptly named Ike Quebec set *From Hackensack to Englewood Cliffs*). Every session in this row dated 1959-08-29 or later is correctly Englewood Cliffs as labeled. https://en.wikipedia.org/wiki/From_Hackensack_to_Englewood_Cliffs · https://en.wikipedia.org/wiki/Van_Gelder_Studio
- **12 albums move to the Hackensack side** (session dates verified against jazzdisco.org year listings): Horace Silver and the Jazz Messengers ('54–55), The Dual Role of Bob Brookmeyer ('55), Fontessa ('56), Relaxin' ('56), Tenor Madness ('56), Saxophone Colossus ('56), Brilliant Corners ('56), Blue Train ('57), Gil Evans & Ten ('57), Cool Struttin' ('58), Somethin' Else ('58), Moanin' ('58).
- **One album leaves Van Gelder entirely**: *The Sermon!* (Jimmy Smith; sessions 1957-08-25, 1958-02-25) was recorded at the **Manhattan Towers Hotel Ballroom, NYC** — a ballroom Van Gelder rented for larger groups while still running Hackensack. New place: kind hall, address beyond "Manhattan Towers hotel" undocumented. https://en.wikipedia.org/wiki/The_Sermon_(Jimmy_Smith_album)
- **Two orphan dates flagged, not guessed**: 1954-01-06 and 1956-01-22 match no jazzdisco Van Gelder session (nearest: Jan 8 '54; Jan 20/23 '56) — possible transcription slips; needs a data check against the albums they're attached to.
- Confidence: high on boundary, album split, and the Sermon extraction; low on the two orphan dates.
- **Ruling (one place or two + Sermon extraction): ____**

#### C2. [128] "New York City (1953-06-25); Van Gelder Studio…" — split 2, both fold into existing places
- 1953-06-25 (first Django session, pre-Van-Gelder) → **WOR Studios** — merge into [139]/A7. 1954-12-23 + 1955-01-09 (MJQ) → **Van Gelder Hackensack** (per C1), confirmed on jazzdisco's 1954/1955 Van Gelder listings.
- Confidence: high. **Ruling: ____**

#### C3. [161] "Half Note Club" + Van Gelder compound — split 2
- 1965-06-01 live tracks → **Half Note Club** · club · New York, NY · 289 Hudson St at Spring St *(documented)*. (The club's later 54th-St location is 1972–74, irrelevant to this 1965 date.) 1965-09-22 studio tracks → **Van Gelder Englewood Cliffs** (per C1). Track-level split confirmed: https://en.wikipedia.org/wiki/Smokin%27_at_the_Half_Note
- Confidence: high. **Ruling: ____**

#### C4. [116] "CBS Studios" / "Paris" — split: one real place + one filing error
- 1963-05-23 (Our Man in Paris, Dexter Gordon) → **CBS Studios, Paris** · studio · Paris, France · *(no address documented)*. Correct as filed.
- 1971-08-14 (The Inner Mounting Flame, Mahavishnu) → **does not belong in Paris at all** — recorded at "CBS Studios" in **New York** (engineer Don Puluse). Two unrelated CBS-branded sessions got filed under one row. Which NYC CBS building is unresolved → see D2. https://en.wikipedia.org/wiki/The_Inner_Mounting_Flame
- Confidence: high on both the Paris ID and the mislocation. **Ruling: ____**

#### C5. [113] "A&R Studios" / "New York" — split 2 (one sharp, one honest blur)
- 1960-12-21 (Free Jazz, Ornette) → **A & R Recording, 112 West 48th St** *(documented)* — the only A&R room that existed then. Merge target for B2.
- 1968 (Now He Sings…, Corea) + 1970 (Blackstone Legacy, Shaw) → **A & R Recording, NYC — room undetermined**: by 1968 A&R ran two rooms simultaneously (112 W 48th + 799 Seventh Ave at 52nd, the ex-Columbia Studio A bought Oct 1967), and no source says which room hosted either session. https://en.wikipedia.org/wiki/A_%26_R_Recording
- Representation question for you (ties to decision 3): one place "A&R Recording NYC" with the two-room caveat in evidence, or two address-places with these sessions marked location-uncertain? Proposal: single second place, city-precision, caveat in notes.
- Confidence: high (1960) / low (which room, 1968/70). **Ruling: ____**

#### C6. [124] Tristano home + Confucius Restaurant — split 2
- Studio/overdub tracks → **Lennie Tristano's home studio** · home · New York, NY · 317 East 32nd St *(documented — the track "East Thirty-Second Street" names it)*. Raw date "1954-01-01" is almost certainly a **placeholder** — jazzdisco dates these only "1954–1955". Data check flagged.
- 1955-06-11 live tracks → **The Sing-Song Room, Confucius Restaurant** · club · New York, NY · *(no address documented)*. https://www.jazzdisco.org/lennie-tristano/discography/
- Confidence: high identity / medium studio-track dating. **Ruling: ____**

#### C7. [123] "Hollywood (1954); Forum Theatre" — split 2, both fold into existing places
- 1954-02-15 → **Capitol Melrose** (merge into [117]/A14; pattern inference — Pacific Jazz's other 1953–55 Chet Baker dates consistently at 5515 Melrose; no date-specific citation). 1956-07-23 + 07-30 → **Forum Theatre** (merge into [122]/A16 — completes the July 23–31 1956 Forum week with A16's three dates).
- Confidence: high (Forum) / medium (1954 component). **Ruling: ____**

#### C8. [125] "Los Angeles" / "CA" — bare-city row, split: one rescue, one honest failure
- 1956-12-03/04 (The Jimmy Giuffre 3) → **Capitol Records Studio (Capitol Tower)** · studio · Hollywood, CA · 1750 North Vine St *(documented)* — the Tower had opened eight months earlier. **Distinct from A14's Melrose building — do not merge.** https://www.jazzdisco.org/jimmy-giuffre/discography/session-index/
- 1956-02-10 (Grand Encounter, John Lewis) → **unrescued**: Wikipedia/AllMusic/Discogs give city only. Stays city-level Los Angeles.
- Confidence: high (Giuffre) / honest-failure (Grand Encounter). **Ruling: ____**

#### C9. [129] "Phil Turetsky's home / Pacific Jazz sessions" — split 2
- 1952-08-16 → **Phil Turetsky's home** · home · Los Angeles (Laurel Canyon), CA · *(no address documented)* — where Dick Bock recorded the first Mulligan Quartet sides, launching Pacific Jazz.
- 1952-10-15/16 → **Gold Star Recording Studios** · studio · Hollywood, CA · 6252 Santa Monica Blvd *(documented)* — later of Spector Wall-of-Sound fame. https://en.wikipedia.org/wiki/Gold_Star_Studios
- Confidence: high. **Ruling: ____**

#### C10. [134] "The Strollers … Radio Recorders" — split 2
- 1955-08-04 live → **The Strollers** · club · Long Beach, CA · *(no address documented)* — Harry Rubin's club, the Chico Hamilton Quintet's breakout room.
- 1955-08-23 studio → **Radio Recorders** (merge into [130]/A17). https://en.wikipedia.org/wiki/Chico_Hamilton_Quintet_featuring_Buddy_Collette
- Confidence: high. **Ruling: ____**

#### C11. [151] "RCA Studios" / "Hollywood" — split 2, **contains a factual error**
- 1953 + 1954 Shorty Rogers dates → **RCA Victor Studios, Hollywood** (merge into [143]/D3).
- 1969-02-14/19 (*Karma*, Pharoah Sanders) → **RCA Victor Studios, New York** (merge into [144]/A18). **The raw "Hollywood" is wrong**: Wikipedia and Discogs agree Karma was cut at RCA in NYC (engineer Bob Simpson, producer Bob Thiele); no source supports Hollywood. https://en.wikipedia.org/wiki/Karma_(Pharoah_Sanders_album)
- Confidence: high on the correction. **Ruling: ____**

#### C12. [180] Coltrane home + Village Gate — split 2
- 1970-11-08 (tracks A1–B1, Journey in Satchidananda) → **Coltrane Home** · home · Dix Hills, NY · 247 Candlewood Path *(documented — National Register of Historic Places)*.
- 1970-07-04 (track B2, "Isis and Osiris", live) → **Village Gate** · club · New York, NY · 160 Bleecker St *(documented)*.
- Note: the raw string lists the places in the opposite order of their dates — the mapping above is the verified one. https://en.wikipedia.org/wiki/Journey_in_Satchidananda
- Confidence: high. **Ruling: ____**

#### C13. [191] "Wally Heider Studios and Different Fur Trading Co." — split 2
- **Wally Heider Studios** · studio · San Francisco, CA · 245 Hyde St *(documented)* and **Different Fur Trading Co.** · studio · San Francisco, CA · 3470 19th St *(documented)*.
- Head Hunters (Sept 1973) used both; **no source splits tracks/dates between them** — both places get the same "1973-09" session window, honestly shared. https://en.wikipedia.org/wiki/Head_Hunters
- Confidence: high places / low intra-album split (none exists in sources). **Ruling: ____**

#### C14. [143] "RCA Victor Studios (Music Center of the World)" / "Hollywood" — keep, but the name needs your call → see D3

---

## D. Needs-John — genuine questions (3)

#### D1. [196] "Columbia Recording Studio B" — *Bitches Brew*: 30th Street or 52nd Street?
- Real documented disagreement. Bitches Brew's article says "Columbia's Studio B in New York"; several secondary sources gloss that as **52nd Street** (Columbia's 49 E 52nd St building had session rooms from 1966); but Wikipedia's own category files it under **CBS 30th Street Studio** — which is what our raw data encodes — and In a Silent Way (six months earlier, B1) is explicitly at 30th Street's "Studio B", giving room-name continuity. No source directly places these sessions at 52nd St with a room letter. https://en.wikipedia.org/wiki/Bitches_Brew · https://en.wikipedia.org/wiki/CBS_Studio_Building
- **Options**: (a) merge into [118] (30th St) on category-tag + Studio-B continuity — the researcher's lean; (b) hold as its own uncertain place pending a better source (e.g. The Complete Bitches Brew Sessions liner notes, not accessible this pass).
- **Ruling: ____**

#### D2. [116-NYC] The Inner Mounting Flame's "CBS Studios, New York" — which building?
- Follows from C4. Candidates: 30th Street (118), the 52nd Street CBS Studio Building, or another Columbia NYC room. Unresolved this pass; 1971 Columbia sessions ran in both buildings. **Options**: (a) city-level "CBS Studios, New York" place until sourced; (b) fold into whichever building D1 resolves to *only if* a source ties them. Proposal: (a) — honest city-precision beats a plausible guess.
- **Ruling: ____**

#### D3. [143] RCA Hollywood — drop the anachronistic "(Music Center of the World)" qualifier?
- That named facility opened March 2, 1959 (1510 N Vine, later 6363 Sunset); this row's sessions are 1953–54 — six years before the name existed. The 1953-era RCA Hollywood address is undocumented in sources found (1016 N Sycamore is the likely candidate, unconfirmed). Proposal: canonical name "RCA Victor Studios, Hollywood", no qualifier, city-precision. https://www.wikidata.org/wiki/Q59314901
- **Ruling: ____**

---

## E. Data errors & checks surfaced (informational — fixes go through edit-contract, separately from place rulings)

1. **Karma (Pharoah Sanders)**: raw location "Hollywood" is wrong → RCA NYC (C11). High confidence.
2. **The Inner Mounting Flame**: filed under Paris → actually NYC (C4). High confidence.
3. **The Sermon! (Jimmy Smith)**: filed under Van Gelder → actually Manhattan Towers Hotel Ballroom (C1). High confidence, two independent pages.
4. **Tristano studio-track date 1954-01-01**: placeholder, real dating is "1954–1955" (C6).
5. **Two Van Gelder orphan dates** (1954-01-06, 1956-01-22) match no documented session (C1).
6. **Pershing dates**: sources say Jan 16–17 1958; we hold only Jan 16 (A24). Minor.
7. **Atlantic Feb-1959 date**: place identity solid, address ambiguous between two documented Atlantic buildings (A5). Affects precision labeling only.

---

## F. Resulting canonical place set (if all proposals accepted): ~47 places

**With documented addresses (map-pin grade, pending geocoding)** — 34: Birdland,
Village Vanguard, CBS 30th Street, Columbia Square Hollywood, Atlantic 1841 Broadway,
Reeves, WOR, Webster Hall, Nola Penthouse, Plaza Sound, Olmstead, Capitol Melrose,
Capitol Tower, Contemporary, Forum Theatre, Radio Recorders, Gold Star, RCA NYC,
Monterey Fairgrounds, Jazz Workshop, Lighthouse, Tsubo, Universal Chicago (1955 addr),
Van Gelder Hackensack, Van Gelder Englewood Cliffs, Half Note, A&R 48th St, Tristano
home, Coltrane Home Dix Hills, Village Gate, Wally Heider SF, Different Fur, Sound
Makers (block-level), RLA (street-level).

**City-precision (honest inf-grade)** — ~13: CBS Paris, Manhattan Towers Ballroom (NYC),
Sing-Song Room/Confucius (NYC), A&R NYC room-undetermined, Turetsky home (LA),
The Strollers (Long Beach), Pershing Lounge (intersection), Arne Bendiksen (Oslo),
Studio Bauer (Ludwigsburg), RCA Hollywood, NYC city-level (New Bottle Old Wine),
LA city-level (Grand Encounter), CBS NYC unresolved (Inner Mounting Flame — pending D2).

Plus/minus 1–2 depending on rulings D1 (Bitches Brew merge or standalone) and B4 (Bauer).
