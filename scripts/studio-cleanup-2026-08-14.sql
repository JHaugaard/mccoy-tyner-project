-- studio-cleanup-2026-08-14.sql
-- Executes the ratified studios cleanup worksheet (research/studios-cleanup-worksheet.md,
-- all 46 items accepted by John 2026-08-14). Run as _jazzcanon_app:
--   psql "$JAZZCANON_APP_DB_URL" -f scripts/studio-cleanup-2026-08-14.sql
-- One transaction. No DELETEs (role has none, by design): merged-away rows stay,
-- de-slugged and marked, with zero sessions — invisible to the exporter.
-- Requires migrate-5a (kind/address/location_epistemic/location_source).
\set ON_ERROR_STOP on
BEGIN;

-- =====================================================================
-- 0. Merged-away rows: free their slugs first (avoids UNIQUE collisions
--    with canonical renames below), mark notes, log.
--    120->121, 123->117+122, 128->139+VG-Hackensack, 151->143+144,
--    160->113, 179->118, 196->118 (ruling D1), 198->195 (ruling B4)
-- =====================================================================
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','studio', id::text, 'place_merged_away', name||' / '||COALESCE(city,''),
  CASE id WHEN 120 THEN 'merged into #121 (item B3)' WHEN 123 THEN 'split into #117 and #122 (item C7)'
          WHEN 128 THEN 'split into #139 and Van Gelder Hackensack (item C2)'
          WHEN 151 THEN 'split into #143 and #144 (item C11)' WHEN 160 THEN 'merged into #113 (item B2)'
          WHEN 179 THEN 'merged into #118 (item B1)' WHEN 196 THEN 'merged into #118 (item D1)'
          WHEN 198 THEN 'merged into #195 (item B4)' END,
  'John: studios worksheet ratified 2026-08-14, all items accepted.'
FROM _jazzcanon.studio WHERE id IN (120,123,128,151,160,179,196,198);

UPDATE _jazzcanon.studio SET name_slug = 'merged-'||id,
  notes = CASE id WHEN 120 THEN 'MERGED into #121 Contemporary Records Studio (worksheet B3, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 123 THEN 'SPLIT into #117 Capitol Melrose and #122 Forum Theatre (worksheet C7, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 128 THEN 'SPLIT into #139 WOR Studios and Van Gelder Studio Hackensack (worksheet C2, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 151 THEN 'SPLIT into #143 RCA Hollywood and #144 RCA New York; Karma city corrected Hollywood->NYC (worksheet C11/E1, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 160 THEN 'MERGED into #113 A & R Recording 112 W 48th St (worksheet B2, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 179 THEN 'MERGED into #118 CBS 30th Street Studio (worksheet B1, 2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 196 THEN 'MERGED into #118 CBS 30th Street Studio per ruling D1 (2026-08-14). Row retained: app role has no DELETE.'
                  WHEN 198 THEN 'MERGED into #195 Studio Bauer (worksheet B4, 2026-08-14; same-room inference flagged medium). Row retained: app role has no DELETE.' END
WHERE id IN (120,123,128,151,160,179,196,198);

-- =====================================================================
-- 1. Canonical keep-rows: name/city normalization + kind/address/
--    location_epistemic/location_source (+ editorial note where ratified).
--    Epistemic rule: obs = street/block/intersection documented in source;
--    inf = city-level only.
-- =====================================================================
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','studio', id::text, 'place_canonicalization', name||' / '||COALESCE(city,''), 'see studio row after 2026-08-14 cleanup',
  'John: studios worksheet ratified 2026-08-14, all items accepted.'
FROM _jazzcanon.studio
WHERE id IN (113,114,115,116,117,118,119,121,122,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,161,162,163,178,180,190,191,195,199,202);

UPDATE _jazzcanon.studio SET
  name='A & R Recording (112 West 48th Street)', city='New York, NY', name_slug='a-r-recording-112-west-48th-street',
  kind='studio', address='112 West 48th Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/A_%26_R_Recording',
  notes='Opened 1959 by Jack Arnold and Phil Ramone, next door to Jim & Andy''s Bar and Manny''s Music.'
WHERE id=113;

UPDATE _jazzcanon.studio SET
  name='Atlantic Studios', city='New York, NY', name_slug='atlantic-studios',
  kind='studio', address='1841 Broadway (at 60th Street)', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Atlantic_Studios',
  notes='Atlantic''s house studio. Address applies from 1959; the Feb 1959 session may fall at the prior 157 W 57th St location — move month undocumented (worksheet A5/E7).'
WHERE id=114;

UPDATE _jazzcanon.studio SET
  name='Birdland', city='New York, NY', name_slug='birdland',
  kind='club', address='1678 Broadway (at West 52nd Street)', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Birdland_(New_York_jazz_club)',
  notes='"The Jazz Corner of the World" — named for Charlie Parker; this location 1949-1965.'
WHERE id=115;

UPDATE _jazzcanon.studio SET
  name='CBS Studios, Paris', city='Paris, France', name_slug='cbs-studios-paris',
  kind='studio', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/Our_Man_in_Paris',
  notes='One-day Dexter Gordon session at Alfred Lion''s invitation; no street address documented.'
WHERE id=116;

UPDATE _jazzcanon.studio SET
  name='Capitol Records Studio (Melrose Avenue)', city='Hollywood, CA', name_slug='capitol-records-studio-melrose-avenue',
  kind='studio', address='5515 Melrose Avenue', location_epistemic='obs',
  location_source='https://jdisc.columbia.edu/session/clifford-brown-and-max-roach-august-5-1954',
  notes='Ex-KHJ radio building, Capitol''s studio before the Capitol Tower opened in April 1956 — not the circular tower.'
WHERE id=117;

UPDATE _jazzcanon.studio SET
  name='CBS 30th Street Studio', city='New York, NY', name_slug='cbs-30th-street-studio',
  kind='studio', address='207 East 30th Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/CBS_30th_Street_Studio',
  notes='"The Church" — a converted 1875 Presbyterian church; Columbia''s flagship room, 1948-1981.'
WHERE id=118;

UPDATE _jazzcanon.studio SET
  name='Columbia Records Hollywood Studio (Columbia Square)', city='Hollywood, CA', name_slug='columbia-records-hollywood-studio-columbia-square',
  kind='studio', address='6121 Sunset Boulevard', location_epistemic='obs',
  location_source='https://forums.stevehoffman.tv/threads/columbia-studios-sunset-and-gower.44945/',
  notes='CBS Radio''s Studio A inside Columbia Square, renovated into a record studio 1961-1972.'
WHERE id=119;

UPDATE _jazzcanon.studio SET
  name='Contemporary Records Studio', city='Los Angeles, CA', name_slug='contemporary-records-studio',
  kind='studio', address='8481 Melrose Place', location_epistemic='obs',
  location_source='https://www.8481melrose.com/posts/about-contemporary-records',
  notes='Lester Koenig''s converted stockroom behind the label office, built with engineer Roy DuNann, late 1955.'
WHERE id=121;

UPDATE _jazzcanon.studio SET
  name='Forum Theatre', city='Los Angeles, CA', name_slug='forum-theatre',
  kind='other', address='4050 West Pico Boulevard', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Chet_Baker_%26_Crew',
  notes='A movie theater Pacific Jazz''s Dick Bock rented as an audience-less recording room, July 1956.'
WHERE id=122;

UPDATE _jazzcanon.studio SET
  name='Lennie Tristano''s home studio', city='New York, NY', name_slug='lennie-tristanos-home-studio',
  kind='home', address='317 East 32nd Street', location_epistemic='obs',
  location_source='https://www.jazzdisco.org/lennie-tristano/discography/',
  notes='The track "East Thirty-Second Street" names this address.'
WHERE id=124;

UPDATE _jazzcanon.studio SET
  name='Los Angeles (venue unidentified)', city='Los Angeles, CA', name_slug='los-angeles-venue-unidentified',
  kind='other', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/Grand_Encounter',
  notes='Grand Encounter (1956-02-10): venue rescue attempted and unresolved — sources give city only (worksheet C8).'
WHERE id=125;

UPDATE _jazzcanon.studio SET
  name='Monterey Jazz Festival (Monterey County Fairgrounds)', city='Monterey, CA', name_slug='monterey-jazz-festival',
  kind='festival', address='2004 Fairground Road', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Monterey_County_Fairgrounds',
  notes='Held at the fairgrounds since its 1958 founding.'
WHERE id=126;

UPDATE _jazzcanon.studio SET
  name='New York City (venue unidentified)', city='New York, NY', name_slug='new-york-city-venue-unidentified',
  kind='other', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/New_Bottle_Old_Wine',
  notes='New Bottle Old Wine (1958): all sources give "New York City" only — genuinely undocumented, not under-searched (worksheet A26).'
WHERE id=127;

UPDATE _jazzcanon.studio SET
  name='Phil Turetsky''s home', city='Los Angeles, CA', name_slug='phil-turetskys-home',
  kind='home', address=NULL, location_epistemic='inf',
  location_source='https://jazzprofiles.blogspot.com/2019/10/the-gerry-mulligan-quartet-19521953.html',
  notes='Laurel Canyon bungalow where Dick Bock cut the first Gerry Mulligan Quartet sides, launching Pacific Jazz.'
WHERE id=129;

UPDATE _jazzcanon.studio SET
  name='Radio Recorders', city='Hollywood, CA', name_slug='radio-recorders',
  kind='studio', address='7000 Santa Monica Boulevard', location_epistemic='obs',
  location_source='https://www.hmdb.org/m.asp?m=204730',
  notes='One of the busiest independent LA studios of the era; also Elvis Presley''s and Nat King Cole''s room.'
WHERE id=130;

UPDATE _jazzcanon.studio SET
  name='Reeves Sound Studios', city='New York, NY', name_slug='reeves-sound-studios',
  kind='studio', address='304 East 44th Street', location_epistemic='obs',
  location_source='https://www.loc.gov/item/ny0943/',
  notes='Film-sound post-production house frequently booked by jazz labels for its acoustics.'
WHERE id=131;

UPDATE _jazzcanon.studio SET
  name='The Jazz Workshop', city='San Francisco, CA', name_slug='the-jazz-workshop',
  kind='club', address='473 Broadway', location_epistemic='obs',
  location_source='https://www.hmdb.org/m.asp?m=152646',
  notes='Operated 1957-1971; inherited much of the Blackhawk''s booking after 1963.'
WHERE id=132;

UPDATE _jazzcanon.studio SET
  name='The Lighthouse', city='Hermosa Beach, CA', name_slug='the-lighthouse',
  kind='club', address='30 Pier Avenue', location_epistemic='obs',
  location_source='https://www.thelighthousecafe.net/history',
  notes='Jazz began 1949 when Howard Rumsey talked the owner into a trial Sunday jam session.'
WHERE id=133;

UPDATE _jazzcanon.studio SET
  name='The Strollers', city='Long Beach, CA', name_slug='the-strollers',
  kind='club', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/Chico_Hamilton_Quintet_featuring_Buddy_Collette',
  notes='Harry Rubin''s club; the original Chico Hamilton Quintet''s breakout room. No street address documented.'
WHERE id=134;

UPDATE _jazzcanon.studio SET
  name='Tsubo', city='Berkeley, CA', name_slug='tsubo',
  kind='club', address='2901 Telegraph Avenue', location_epistemic='obs',
  location_source='http://berkeleyfolk.blogspot.com/2009/09/october-15-1962-closing-of-tsubos.html',
  notes='Coffee-house jazz room, open Sept 1961 - Oct 1962. Address rests on a single blog source (worksheet A22).'
WHERE id=135;

UPDATE _jazzcanon.studio SET
  name='Universal Recording Corporation', city='Chicago, IL', name_slug='universal-recording-corporation',
  kind='studio', address='111 East Ontario Street', location_epistemic='obs',
  location_source='https://tdwaw.ellingtonweb.ca/supportingwebpages/UniversalRecordingCorporation.html',
  notes='Bill Putnam''s studio. Address is the 1955-era location; the better-known 46 E Walton address is mid-1956 onward.'
WHERE id=136;

UPDATE _jazzcanon.studio SET
  name='Van Gelder Studio, Englewood Cliffs', city='Englewood Cliffs, NJ', name_slug='van-gelder-studio-englewood-cliffs',
  kind='studio', address='445 Sylvan Avenue', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Van_Gelder_Studio',
  notes='Custom-built by architect David Henken, Frank Lloyd Wright-inspired, 39-foot ceiling; opened July 20, 1959.'
WHERE id=137;

UPDATE _jazzcanon.studio SET
  name='Village Vanguard', city='New York, NY', name_slug='village-vanguard',
  kind='club', address='178 Seventh Avenue South', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Village_Vanguard',
  notes='130-seat triangular basement room; same address since 1935, the oldest continuously operating jazz club in NYC.'
WHERE id=138;

UPDATE _jazzcanon.studio SET
  name='WOR Studios', city='New York, NY', name_slug='wor-studios',
  kind='studio', address='1440 Broadway', location_epistemic='obs',
  location_source='https://www.fybush.com/sites/2005/site-050429.html',
  notes='WOR radio''s studio, booked commercially for jazz dates through the 1940s-50s.'
WHERE id=139;

UPDATE _jazzcanon.studio SET
  name='Webster Hall', city='New York, NY', name_slug='webster-hall',
  kind='hall', address='125 East 11th Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Webster_Hall',
  notes='1886 event hall doubling as a large-ensemble recording room from the 1950s into the late 1960s.'
WHERE id=140;

UPDATE _jazzcanon.studio SET
  name='Pershing Lounge (Pershing Hotel)', city='Chicago, IL', name_slug='pershing-lounge-pershing-hotel',
  kind='club', address='East 64th Street at South Cottage Grove Avenue', location_epistemic='obs',
  location_source='https://southsideweekly.com/64th-cottage-grove/',
  notes='The Pershing Hotel''s lounge — Ahmad Jamal''s residency room. Intersection documented, street number not.'
WHERE id=141;

UPDATE _jazzcanon.studio SET
  name='RCA Victor Studios, Hollywood', city='Hollywood, CA', name_slug='rca-victor-studios-hollywood',
  kind='studio', address=NULL, location_epistemic='inf',
  location_source='https://www.wikidata.org/wiki/Q59314901',
  notes='Ruling D3: "(Music Center of the World)" qualifier dropped — that named facility opened 1959, after these 1953-54 sessions. 1953-era address undocumented (1016 N Sycamore likely, unconfirmed).'
WHERE id=143;

UPDATE _jazzcanon.studio SET
  name='RCA Victor Studios', city='New York, NY', name_slug='rca-victor-studios-new-york',
  kind='studio', address='155 East 24th Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/RCA_Studios_New_York',
  notes='Converted 1907 stable, active 1928-1969; also the site of Glenn Miller''s "In the Mood".'
WHERE id=144;

UPDATE _jazzcanon.studio SET
  name='Half Note Club', city='New York, NY', name_slug='half-note-club',
  kind='club', address='289 Hudson Street (at Spring Street)', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Smokin%27_at_the_Half_Note',
  notes='This location 1957-1972; the later West 54th Street location postdates the canon''s sessions here.'
WHERE id=161;

UPDATE _jazzcanon.studio SET
  name='Sound Makers Studios', city='New York, NY', name_slug='sound-makers-studios',
  kind='studio', address='West 57th Street between Sixth and Seventh Avenues', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Money_Jungle',
  notes='Site of the sole Ellington/Mingus/Roach trio session. Block documented, street number not.'
WHERE id=162;

UPDATE _jazzcanon.studio SET
  name='Nola Penthouse Sound Studios', city='New York, NY', name_slug='nola-penthouse-sound-studios',
  kind='studio', address='111 West 57th Street (penthouse, Steinway Hall)', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/We_Insist!',
  notes='Penthouse room atop Steinway Hall, open for business March 1960.'
WHERE id=163;

UPDATE _jazzcanon.studio SET
  name='Plaza Sound Studios', city='New York, NY', name_slug='plaza-sound-studios',
  kind='studio', address='55 West 50th Street, 8th floor', location_epistemic='obs',
  location_source='http://brucebase.wikidot.com/venue:plaza-sound-studios-new-york-city-ny',
  notes='Built as an NBC Symphony radio studio above Radio City Music Hall; closed 1979.'
WHERE id=178;

UPDATE _jazzcanon.studio SET
  name='Coltrane Home (Dix Hills)', city='Dix Hills, NY', name_slug='coltrane-home-dix-hills',
  kind='home', address='247 Candlewood Path', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/John_Coltrane_Home',
  notes='John and Alice Coltrane''s home 1964-1973; A Love Supreme was composed here. National Register of Historic Places, 2007.'
WHERE id=180;

UPDATE _jazzcanon.studio SET
  name='Arne Bendiksen Studio', city='Oslo, Norway', name_slug='arne-bendiksen-studio',
  kind='studio', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/Facing_You',
  notes='ECM''s Oslo room before Rainbow Studio; Jan Erik Kongshaug engineered here 1967-1975. No street address documented.'
WHERE id=190;

UPDATE _jazzcanon.studio SET
  name='Wally Heider Studios', city='San Francisco, CA', name_slug='wally-heider-studios',
  kind='studio', address='245 Hyde Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Wally_Heider_Studios',
  notes='Opened 1969; renamed Hyde Street Studios under new ownership in 1980.'
WHERE id=191;

UPDATE _jazzcanon.studio SET
  name='Studio Bauer', city='Ludwigsburg, Germany', name_slug='studio-bauer-ludwigsburg',
  kind='studio', address=NULL, location_epistemic='inf',
  location_source='https://en.wikipedia.org/wiki/Free_at_Last_(Mal_Waldron_album)',
  notes='ECM''s earliest studio — the label''s first release (ECM 1001) was cut here 1969. Merge of "Musikstudio Bauer"/"Tonstudio Bauer" rows per ruling B4; same-room inference is medium-confidence (different engineers 1969 vs 1975, no source confirms one room).'
WHERE id=195;

UPDATE _jazzcanon.studio SET
  name='Olmstead Sound Studios', city='New York, NY', name_slug='olmstead-sound-studios',
  kind='studio', address='1 East 54th Street', location_epistemic='obs',
  location_source='https://musicbrainz.org/place/8a1439fe-b446-4dc9-a3a4-87ac357c44cd',
  notes='Opened December 1954. Spelling: period sources use "Olmstead"; raw data had "Olmsted" (worksheet A12).'
WHERE id=199;

UPDATE _jazzcanon.studio SET
  name='RLA Studios', city='New York, NY', name_slug='rla-studios',
  kind='studio', address='West 65th Street', location_epistemic='obs',
  location_source='https://en.wikipedia.org/wiki/Richard_Alderson_(music_producer)',
  notes='Built 1962 by engineer Richard L. Alderson in a formerly condemned building; key ESP-Disk'' room. Street documented, number not.'
WHERE id=202;

-- =====================================================================
-- 2. New canonical places (splits + the discovered ballroom).
-- =====================================================================
INSERT INTO _jazzcanon.studio (name, city, name_slug, kind, address, location_epistemic, location_source, notes) VALUES
('Van Gelder Studio, Hackensack', 'Hackensack, NJ', 'van-gelder-studio-hackensack', 'studio',
 '25 Prospect Avenue', 'obs',
 'https://en.wikipedia.org/wiki/Van_Gelder_Studio https://en.wikipedia.org/wiki/From_Hackensack_to_Englewood_Cliffs',
 'Rudy Van Gelder''s parents'' living room; operated 1952 - July 1, 1959 (ruling C1: split from Englewood Cliffs).'),
('Manhattan Towers Hotel Ballroom', 'New York, NY', 'manhattan-towers-hotel-ballroom', 'hall',
 NULL, 'inf',
 'https://en.wikipedia.org/wiki/The_Sermon_(Jimmy_Smith_album)',
 'Hotel ballroom Van Gelder rented for larger groups 1957-58 while still running Hackensack; surfaced by worksheet C1 (The Sermon!).'),
('CBS Studios, New York', 'New York, NY', 'cbs-studios-new-york', 'studio',
 NULL, 'inf',
 'https://en.wikipedia.org/wiki/The_Inner_Mounting_Flame',
 'Ruling D2: building unresolved (30th Street vs 52nd Street both possible for 1971) — held at city level rather than guessed.'),
('A & R Recording (room undetermined)', 'New York, NY', 'a-r-recording-room-undetermined', 'studio',
 NULL, 'inf',
 'https://en.wikipedia.org/wiki/A_%26_R_Recording',
 'From 1968 A&R ran two rooms (112 W 48th St and 799 Seventh Ave); no source assigns the 1968/1970 sessions to either (worksheet C5).'),
('The Sing-Song Room, Confucius Restaurant', 'New York, NY', 'sing-song-room-confucius-restaurant', 'club',
 NULL, 'inf',
 'https://www.jazzdisco.org/lennie-tristano/discography/',
 'Restaurant performance room; Tristano/Konitz live set, June 11, 1955. No street address documented.'),
('Capitol Records Studio (Capitol Tower)', 'Hollywood, CA', 'capitol-records-studio-capitol-tower', 'studio',
 '1750 North Vine Street', 'obs',
 'https://www.jazzdisco.org/jimmy-giuffre/discography/session-index/',
 'The circular Capitol Tower, opened April 1956 — distinct from the pre-Tower Melrose Avenue studio.'),
('Gold Star Recording Studios', 'Hollywood, CA', 'gold-star-recording-studios', 'studio',
 '6252 Santa Monica Boulevard', 'obs',
 'https://en.wikipedia.org/wiki/Gold_Star_Studios',
 'Opened 1950 by Dave Gold and Stan Ross; later famous as the home of Phil Spector''s Wall of Sound.'),
('Village Gate', 'New York, NY', 'village-gate', 'club',
 '160 Bleecker Street (at Thompson Street)', 'obs',
 'https://en.wikipedia.org/wiki/Village_Gate',
 'Greenwich Village club, 1958-1995; the upstairs room was "Top of the Gate".'),
('Different Fur Trading Co.', 'San Francisco, CA', 'different-fur-trading-co', 'studio',
 '3470 19th Street', 'obs',
 'https://en.wikipedia.org/wiki/Different_Fur',
 'Mission District studio operating at this address since 1968; shared the Head Hunters sessions with Wally Heider Studios.');

INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','studio', id::text, 'place_created', NULL, name||' / '||city,
  'John: studios worksheet ratified 2026-08-14 (new place from split/discovery).'
FROM _jazzcanon.studio
WHERE name_slug IN ('van-gelder-studio-hackensack','manhattan-towers-hotel-ballroom','cbs-studios-new-york',
  'a-r-recording-room-undetermined','sing-song-room-confucius-restaurant','capitol-records-studio-capitol-tower',
  'gold-star-recording-studios','village-gate','different-fur-trading-co');

-- =====================================================================
-- 3. Session reassignments (FK relinking — Claude Code's lane per the
--    edit contract). Log first, then update, same predicates.
-- =====================================================================

-- 3a. Van Gelder pre-boundary (C1): everything before 1959-07-20 except
--     The Sermon! goes to Hackensack.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '137',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='van-gelder-studio-hackensack'),
  'John: worksheet C1 — sessions before 1959-07-20 were at Hackensack, not Englewood Cliffs. Album: '||album_id
FROM _jazzcanon.session
WHERE studio_id=137 AND session_date < '1959-07-20' AND album_id <> 'jimmy-smith-the-sermon-1958';

UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='van-gelder-studio-hackensack')
WHERE studio_id=137 AND session_date < '1959-07-20' AND album_id <> 'jimmy-smith-the-sermon-1958';

-- 3b. The Sermon! -> Manhattan Towers (C1/E3).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '137',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='manhattan-towers-hotel-ballroom'),
  'John: worksheet C1/E3 — The Sermon! was recorded at the Manhattan Towers Hotel Ballroom, not Van Gelder Studio.'
FROM _jazzcanon.session WHERE studio_id=137 AND album_id='jimmy-smith-the-sermon-1958';

UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='manhattan-towers-hotel-ballroom')
WHERE studio_id=137 AND album_id='jimmy-smith-the-sermon-1958';

-- 3c. Row 128 (Django compound, C2): 1953 session -> WOR (#139); 1954/55 -> Hackensack.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '128',
  CASE WHEN session_date='1953-06-25' THEN '139'
       ELSE (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='van-gelder-studio-hackensack') END,
  'John: worksheet C2 — Django compound row split (WOR Studios / Van Gelder Hackensack).'
FROM _jazzcanon.session WHERE studio_id=128;

UPDATE _jazzcanon.session SET studio_id=139 WHERE studio_id=128 AND session_date='1953-06-25';
UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='van-gelder-studio-hackensack')
WHERE studio_id=128;

-- 3d. Row 161 (C3): studio re-recording session -> Englewood Cliffs (#137).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '161', '137',
  'John: worksheet C3 — Smokin'' at the Half Note studio tracks were cut at Van Gelder Englewood Cliffs.'
FROM _jazzcanon.session WHERE studio_id=161 AND session_date='1965-09-22';

UPDATE _jazzcanon.session SET studio_id=137 WHERE studio_id=161 AND session_date='1965-09-22';

-- 3e. Row 116 (C4/E2): Inner Mounting Flame -> CBS Studios, New York.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '116',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='cbs-studios-new-york'),
  'John: worksheet C4/E2 — The Inner Mounting Flame was recorded at CBS Studios New York, not Paris.'
FROM _jazzcanon.session WHERE studio_id=116 AND session_date='1971-08-14';

UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='cbs-studios-new-york')
WHERE studio_id=116 AND session_date='1971-08-14';

-- 3f. Row 113 (C5): 1968 + 1970 sessions -> A&R room-undetermined.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '113',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='a-r-recording-room-undetermined'),
  'John: worksheet C5 — A&R ran two rooms by 1968; these sessions cannot be pinned to 112 W 48th St.'
FROM _jazzcanon.session WHERE studio_id=113 AND session_date >= '1968-01-01';

UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='a-r-recording-room-undetermined')
WHERE studio_id=113 AND session_date >= '1968-01-01';

-- 3g. Row 160 (B2): Ole Coltrane -> #113 (only A&R room existing in 1961).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '160', '113',
  'John: worksheet B2 — A&R had exactly one facility in 1961.'
FROM _jazzcanon.session WHERE studio_id=160;
UPDATE _jazzcanon.session SET studio_id=113 WHERE studio_id=160;

-- 3h. Row 123 (C7): 1954 -> Capitol Melrose (#117); 1956 -> Forum Theatre (#122).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '123',
  CASE WHEN session_date='1954-02-15' THEN '117' ELSE '122' END,
  'John: worksheet C7 — Chet Baker Sings compound row split (Capitol Melrose 1954 / Forum Theatre 1956).'
FROM _jazzcanon.session WHERE studio_id=123;
UPDATE _jazzcanon.session SET studio_id=117 WHERE studio_id=123 AND session_date='1954-02-15';
UPDATE _jazzcanon.session SET studio_id=122 WHERE studio_id=123;

-- 3i. Row 125 (C8): Giuffre sessions -> Capitol Tower; Grand Encounter stays city-level.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '125',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='capitol-records-studio-capitol-tower'),
  'John: worksheet C8 — The Jimmy Giuffre 3 was recorded at the Capitol Tower (opened eight months earlier).'
FROM _jazzcanon.session WHERE studio_id=125 AND session_date >= '1956-12-01';
UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='capitol-records-studio-capitol-tower')
WHERE studio_id=125 AND session_date >= '1956-12-01';

-- 3j. Row 129 (C9): October 1952 sessions -> Gold Star.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '129',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='gold-star-recording-studios'),
  'John: worksheet C9 — the October 1952 Mulligan Quartet sessions moved to Gold Star Studios.'
FROM _jazzcanon.session WHERE studio_id=129 AND session_date >= '1952-10-01';
UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='gold-star-recording-studios')
WHERE studio_id=129 AND session_date >= '1952-10-01';

-- 3k. Row 134 (C10): studio session -> Radio Recorders (#130).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '134', '130',
  'John: worksheet C10 — the Aug 23 1955 studio session was at Radio Recorders, Hollywood.'
FROM _jazzcanon.session WHERE studio_id=134 AND session_date='1955-08-23';
UPDATE _jazzcanon.session SET studio_id=130 WHERE studio_id=134 AND session_date='1955-08-23';

-- 3l. Row 151 (C11/E1): Shorty Rogers -> RCA Hollywood (#143); Karma -> RCA NYC (#144).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '151',
  CASE WHEN album_id='pharoah-sanders-karma-1969' THEN '144' ELSE '143' END,
  CASE WHEN album_id='pharoah-sanders-karma-1969'
    THEN 'John: worksheet C11/E1 — Karma was recorded at RCA New York; the raw "Hollywood" was a data error.'
    ELSE 'John: worksheet C11 — Shorty Rogers sessions merge into RCA Victor Studios, Hollywood.' END
FROM _jazzcanon.session WHERE studio_id=151;
UPDATE _jazzcanon.session SET studio_id=144 WHERE studio_id=151 AND album_id='pharoah-sanders-karma-1969';
UPDATE _jazzcanon.session SET studio_id=143 WHERE studio_id=151;

-- 3m. Rows 179 + 196 (B1/D1): -> CBS 30th Street (#118).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', studio_id::text, '118',
  CASE WHEN studio_id=179 THEN 'John: worksheet B1 — In a Silent Way at CBS 30th Street Studio B.'
       ELSE 'John: ruling D1 — Bitches Brew assigned to CBS 30th Street on category-tag + Studio B continuity.' END
FROM _jazzcanon.session WHERE studio_id IN (179,196);
UPDATE _jazzcanon.session SET studio_id=118 WHERE studio_id IN (179,196);

-- 3n. Row 120 (B3): -> Contemporary (#121).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '120', '121',
  'John: worksheet B3 — two name variants of Contemporary''s 8481 Melrose Place studio.'
FROM _jazzcanon.session WHERE studio_id=120;
UPDATE _jazzcanon.session SET studio_id=121 WHERE studio_id=120;

-- 3o. Row 198 (B4): -> Studio Bauer (#195).
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '198', '195',
  'John: worksheet B4 — Bauer rows merged (same-room inference, medium confidence, noted on the place).'
FROM _jazzcanon.session WHERE studio_id=198;
UPDATE _jazzcanon.session SET studio_id=195 WHERE studio_id=198;

-- 3p. Row 180 (C12): live track -> Village Gate.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '180',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='village-gate'),
  'John: worksheet C12 — "Isis and Osiris" was recorded live at the Village Gate, July 4 1970.'
FROM _jazzcanon.session WHERE studio_id=180 AND session_date='1970-07-04';
UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='village-gate')
WHERE studio_id=180 AND session_date='1970-07-04';

-- 3q. Row 124 (C6): live set -> Sing-Song Room.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'studio_id', '124',
  (SELECT id::text FROM _jazzcanon.studio WHERE name_slug='sing-song-room-confucius-restaurant'),
  'John: worksheet C6 — the June 11 1955 live set was at the Sing-Song Room, Confucius Restaurant.'
FROM _jazzcanon.session WHERE studio_id=124 AND session_date='1955-06-11';
UPDATE _jazzcanon.session
SET studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='sing-song-room-confucius-restaurant')
WHERE studio_id=124 AND session_date='1955-06-11';

-- =====================================================================
-- 4. Head Hunters: second session row so Different Fur carries the album
--    too (C13 — sources place the album at both studios, no finer split).
-- =====================================================================
INSERT INTO _jazzcanon.session (album_id, session_date, session_date_text, studio_id, epistemic)
SELECT album_id, session_date, session_date_text,
  (SELECT id FROM _jazzcanon.studio WHERE name_slug='different-fur-trading-co'), 'obs'
FROM _jazzcanon.session
WHERE studio_id=191 AND album_id='herbie-hancock-head-hunters-1973';

INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'session_created', NULL, 'Head Hunters @ Different Fur Trading Co.',
  'John: worksheet C13 — album recorded across both SF studios; parallel session row added, no track-level split exists in sources.'
FROM _jazzcanon.session
WHERE studio_id=(SELECT id FROM _jazzcanon.studio WHERE name_slug='different-fur-trading-co');

-- =====================================================================
-- 5. Ratified session-data fixes (worksheet E4/E5).
-- =====================================================================

-- E4: Tristano studio-track date 1954-01-01 is a placeholder; real dating "1954-1955".
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'session_date', '1954-01-01', 'NULL (text: 1954-1955)',
  'John: worksheet E4 — jazzdisco dates the overdub tracks only to 1954-1955; the Jan 1 date was a placeholder. Epistemic obs->inf in same change.'
FROM _jazzcanon.session WHERE studio_id=124 AND session_date='1954-01-01';
UPDATE _jazzcanon.session
SET session_date=NULL, session_date_text='1954-1955', epistemic='inf'
WHERE studio_id=124 AND session_date='1954-01-01';

-- E5: the two fuzzy Van Gelder dates (no matching jazzdisco session) degrade to inf.
INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
SELECT 'claude-code','session', id::text, 'epistemic', epistemic::text, 'inf',
  'John: worksheet E5 — date matches no documented Van Gelder session (nearest candidates days off); date kept, label degraded honestly.'
FROM _jazzcanon.session WHERE id IN ('7837c588-4ded-43f7-8030-8aa692dd357c','73eaa373-2272-4809-9e10-454c7b9d35a4');
UPDATE _jazzcanon.session SET epistemic='inf'
WHERE id IN ('7837c588-4ded-43f7-8030-8aa692dd357c','73eaa373-2272-4809-9e10-454c7b9d35a4');

COMMIT;

-- Post-run sanity (read-only):
SELECT 'canonical places' AS check, count(*) FROM _jazzcanon.studio WHERE name_slug NOT LIKE 'merged-%';
SELECT 'canonical missing kind' AS check, count(*) FROM _jazzcanon.studio WHERE name_slug NOT LIKE 'merged-%' AND kind IS NULL;
SELECT 'canonical missing location_epistemic' AS check, count(*) FROM _jazzcanon.studio WHERE name_slug NOT LIKE 'merged-%' AND location_epistemic IS NULL;
SELECT 'sessions still on merged rows' AS check, count(*) FROM _jazzcanon.session WHERE studio_id IN (120,123,128,151,160,179,196,198);
SELECT 'obs/inf split' AS check, location_epistemic, count(*) FROM _jazzcanon.studio WHERE name_slug NOT LIKE 'merged-%' GROUP BY location_epistemic ORDER BY location_epistemic;
