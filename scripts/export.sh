#!/usr/bin/env bash
# Export A Jazz Canon contract from the SYSTEM OF RECORD (postgres._jazzcanon)
# via the read-only role, into app-shaped JSON consumed by jazz-canon and evals.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL="$(grep -E '^JAZZCANON_DB_URL=' "$ROOT/.env.local" | cut -d= -f2-)"
[ -n "$URL" ] || { echo "✗ JAZZCANON_DB_URL not found in .env.local" >&2; exit 1; }
PSQL=(psql "$URL" -v ON_ERROR_STOP=1 -X -q -At)
OUT="$ROOT/exports/jazz-canon"
mkdir -p "$OUT"

# --- pre-flight referential integrity (abort before writing anything) ---
orphans=$("${PSQL[@]}" -c "SELECT count(*) FROM _jazzcanon.performance p
  LEFT JOIN _jazzcanon.person pe ON pe.id=p.person_id
  LEFT JOIN _jazzcanon.instrument i ON i.id=p.instrument_id
  WHERE pe.id IS NULL OR i.id IS NULL")
[ "$orphans" = "0" ] || { echo "✗ INVARIANT FAILED: $orphans performance rows with orphan person/instrument FK" >&2; exit 1; }
noperf=$("${PSQL[@]}" -c "SELECT count(*) FROM _jazzcanon.album a
  WHERE a.canon_status='included' AND a.site_status IN ('approved','live')
    AND NOT EXISTS (SELECT 1 FROM _jazzcanon.performance p WHERE p.album_id=a.id)")
[ "$noperf" = "0" ] || { echo "✗ INVARIANT FAILED: $noperf albums with zero performances" >&2; exit 1; }

# --- albums.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/albums.json"
SELECT json_agg(r ORDER BY r.year, r.id)
FROM (
  SELECT a.id, a.title, a.artist_name AS artist, a.year,
         l.name AS label, a.catalog_number AS catalog,
         s.display_name AS style, s.code AS "styleCode",
         -- secondary style codes (album_style holds tags only; the primary
         -- lives in album.style_primary_id). The site drives its opened-gate
         -- card accents off these — the `ecm` tag in particular can never
         -- appear as a primary style, so styleCode alone cannot express it.
         coalesce((SELECT json_agg(s2.code ORDER BY s2.code)
                   FROM _jazzcanon.album_style ast
                   JOIN _jazzcanon.style s2 ON s2.id = ast.style_id
                   WHERE ast.album_id = a.id
                     AND s2.id IS DISTINCT FROM a.style_primary_id), '[]'::json) AS "styleTags",
         aa.source_url AS "artUrl", a.apple_album_id AS "appleAlbumId"
  FROM _jazzcanon.album a
  LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
  -- inner join is safe here, and provably total: album.style_primary_id is
  -- NOT NULL with an FK to style(id), so it can never drop a publishable row.
  JOIN _jazzcanon.style s ON s.id = a.style_primary_id
  LEFT JOIN _jazzcanon.album_art aa ON aa.album_id = a.id AND aa.is_primary
  -- publication gate: only canon albums greenlit for the site (spec §5/§6)
  WHERE a.canon_status = 'included' AND a.site_status IN ('approved', 'live')
) r;
SQL

# --- details.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/details.json"
SELECT json_object_agg(a.id, json_build_object(
  'description', a.description,
  'recordingDates', a.recording_dates_text,
  'leader', lead.canonical_name,
  'studios', (
     SELECT coalesce(json_agg(DISTINCT st.name), '[]'::json)
     FROM _jazzcanon.session se
     JOIN _jazzcanon.studio st ON st.id = se.studio_id
     WHERE se.album_id = a.id),
  'tracks', (
     SELECT coalesce(json_agg(json_build_object(
              'n', t.track_number, 'title', t.title, 'side', t.side,
              'duration', t.duration_text, 'appleTrackId', t.apple_track_id,
              'e', t.epistemic_track,
              'personnel', (
                 SELECT coalesce(json_agg(json_build_object(
                          'personId', tp.person_id, 'name', tp.canonical_name,
                          'instrument', tp.instrument, 'e', tp.epistemic)
                        ORDER BY fam.ord, tp.instrument, tp.canonical_name), '[]'::json)
                 FROM _jazzcanon.v_track_personnel tp
                 JOIN _jazzcanon.instrument ins ON ins.name = tp.instrument
                 CROSS JOIN LATERAL (SELECT array_position(
                    ARRAY['brass','woodwinds','keyboards','strings','percussion','other']::text[],
                    ins.family::text) AS ord) fam
                 WHERE tp.track_id = t.id)
            ) ORDER BY t.track_number), '[]'::json)
     FROM _jazzcanon.track t WHERE t.album_id = a.id),
  'personnel', (
     SELECT coalesce(json_agg(json_build_object(
              'personId', row."personId", 'name', row.name,
              'entries', row.entries, 'scope', row.scope)
            ORDER BY row.ord, row.name), '[]'::json)
     FROM (
       SELECT pe.id AS "personId", pe.canonical_name AS name,
              json_agg(json_build_object('instrument', i.name, 'e', p.epistemic)
                       ORDER BY i.name) AS entries,
              min(p.scope::text) AS scope,
              min(array_position(
                 ARRAY['brass','woodwinds','keyboards','strings','percussion','other']::text[],
                 i.family::text)) AS ord
       FROM _jazzcanon.performance p
       JOIN _jazzcanon.person pe ON pe.id = p.person_id
       JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
       WHERE p.album_id = a.id
       GROUP BY pe.id, pe.canonical_name
     ) row)
))
FROM _jazzcanon.album a
LEFT JOIN _jazzcanon.person lead ON lead.id = a.leader_person_id
WHERE a.canon_status = 'included' AND a.site_status IN ('approved', 'live');
SQL

# --- graph.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/graph.json"
SELECT json_build_object(
  'people', (
     SELECT json_object_agg(pe.id, pe.canonical_name)
     FROM _jazzcanon.person pe
     WHERE EXISTS (SELECT 1 FROM _jazzcanon.performance p
                   JOIN _jazzcanon.album al ON al.id = p.album_id
                   WHERE p.person_id = pe.id
                     AND al.canon_status = 'included'
                     AND al.site_status IN ('approved', 'live'))),
  'edges', (
     SELECT json_agg(e) FROM (
       SELECT p.person_id AS p, p.album_id AS a,
              json_agg(json_build_object('instrument', i.name, 'e', p.epistemic)
                       ORDER BY i.name) AS entries
       FROM _jazzcanon.performance p
       JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
       JOIN _jazzcanon.album al ON al.id = p.album_id
       WHERE al.canon_status = 'included'
         AND al.site_status IN ('approved', 'live')
       GROUP BY p.person_id, p.album_id
     ) e)
);
SQL

# --- places.json ---
# Studios map contract (ratified 2026-08-14; confirmed with site session).
# One coordinate per place (moved venues are distinct places — R2); id is
# name_slug, deterministic run-to-run (R3); precision is the single
# unambiguous field the site renders from (R1): address = street/block-grade
# documented coordinate (location_epistemic obs), city = 3-decimal centroid
# (inf). Same publication gate as every other file. Places whose albums are
# all un-gated are omitted; their ids are stable when they later appear.
# The optional per-place editorial note is deferred until notes are curated.
"${PSQL[@]}" <<'SQL' > "$OUT/places.json"
SELECT json_agg(r ORDER BY r.id)
FROM (
  SELECT st.name_slug AS id, st.name, st.kind, st.city, st.lat, st.lon,
         CASE st.location_epistemic::text WHEN 'obs' THEN 'address' ELSE 'city' END AS precision,
         (SELECT json_agg(al_r ORDER BY al_r.year, al_r."albumId")
          FROM (
            SELECT a.id AS "albumId", a.year,
                   coalesce((SELECT json_agg(dd.d ORDER BY dd.d) FROM (
                      SELECT DISTINCT coalesce(se2.session_date::text, se2.session_date_text) AS d
                      FROM _jazzcanon.session se2
                      WHERE se2.studio_id = st.id AND se2.album_id = a.id
                        AND coalesce(se2.session_date::text, se2.session_date_text) IS NOT NULL) dd),
                    '[]'::json) AS dates
            FROM _jazzcanon.album a
            WHERE a.canon_status = 'included' AND a.site_status IN ('approved','live')
              AND EXISTS (SELECT 1 FROM _jazzcanon.session se
                          WHERE se.studio_id = st.id AND se.album_id = a.id)
          ) al_r) AS albums
  FROM _jazzcanon.studio st
  WHERE st.name_slug NOT LIKE 'merged-%'
    AND EXISTS (SELECT 1 FROM _jazzcanon.session se
                JOIN _jazzcanon.album a ON a.id = se.album_id
                WHERE se.studio_id = st.id
                  AND a.canon_status = 'included' AND a.site_status IN ('approved','live'))
) r;
SQL

# --- people-activity.json ---
# "Working" page contract (spec 2026-08-18, ratified with the site session).
# One lane per musician over time. Two rulings shape it:
#   D7 — an admitted date is session_date, OR session_date_text verbatim when
#        it is exactly YYYY-MM. String LENGTH is the precision contract (same
#        variable-precision convention places.json already uses), so the site
#        never has to guess whether a day was known. Compound ("1960 November
#        18 & 30"), spanning ("1953-08/1955-07") and year-only values are NOT
#        admitted — a single DATE cannot honestly hold them.
#   D5 — a person with zero admitted dates is omitted entirely rather than
#        drawn as an empty lane. meta counts what was left out, so the page
#        can footnote its own gaps instead of silently under-reporting.
# Attribution is album-level: a performance inherits that album's session
# dates, deduped by (person, date, album). Same publication gate as every
# other file. Sort is total and deterministic run-to-run.
"${PSQL[@]}" <<'SQL' > "$OUT/people-activity.json"
WITH gated AS (
  SELECT id FROM _jazzcanon.album
  WHERE canon_status = 'included' AND site_status IN ('approved', 'live')
),
adm AS (
  SELECT s.album_id,
         coalesce(s.session_date::text,
                  CASE WHEN s.session_date_text ~ '^[0-9]{4}-[0-9]{2}$'
                       THEN s.session_date_text END) AS d
  FROM _jazzcanon.session s
  JOIN gated g ON g.id = s.album_id
),
mk AS (
  SELECT DISTINCT p.person_id, a.d, a.album_id
  FROM _jazzcanon.performance p
  JOIN gated g ON g.id = p.album_id
  JOIN adm a ON a.album_id = p.album_id
  WHERE a.d IS NOT NULL
),
per AS (
  SELECT person_id, min(d) AS first, max(d) AS last,
         count(DISTINCT substr(d, 1, 4))::int AS years
  FROM mk GROUP BY person_id
),
undated AS (
  SELECT s.album_id
  FROM _jazzcanon.session s
  JOIN gated g ON g.id = s.album_id
  WHERE s.session_date IS NULL
    AND (s.session_date_text IS NULL
         OR s.session_date_text !~ '^[0-9]{4}-[0-9]{2}$')
)
SELECT json_build_object(
  'people', coalesce((
    SELECT json_agg(r ORDER BY r.first, r."personId")
    FROM (
      SELECT pe.id AS "personId", pe.canonical_name AS name,
             (SELECT coalesce(json_agg(DISTINCT i.name ORDER BY i.name), '[]'::json)
              FROM _jazzcanon.performance p2
              JOIN gated g2 ON g2.id = p2.album_id
              JOIN _jazzcanon.instrument i ON i.id = p2.instrument_id
              WHERE p2.person_id = per.person_id) AS instruments,
             per.years AS "yearsActive", per.first, per.last,
             (SELECT json_agg(json_build_object('date', m.d, 'albumId', m.album_id)
                              ORDER BY m.d, m.album_id)
              FROM mk m WHERE m.person_id = per.person_id) AS sessions
      FROM per
      JOIN _jazzcanon.person pe ON pe.id = per.person_id
    ) r), '[]'::json),
  'meta', json_build_object(
    'spanStart', (SELECT min(d) FROM mk),
    'spanEnd',   (SELECT max(d) FROM mk),
    'undatedSessions', (SELECT count(*) FROM undated),
    'undatedOnlyPeople', (
      SELECT count(*) FROM (
        SELECT DISTINCT p.person_id
        FROM _jazzcanon.performance p JOIN gated g ON g.id = p.album_id
      ) allp
      WHERE NOT EXISTS (SELECT 1 FROM mk WHERE mk.person_id = allp.person_id)),
    'undatedAlbums', coalesce((
      SELECT json_agg(DISTINCT album_id ORDER BY album_id) FROM undated), '[]'::json)
  )
);
SQL

# --- structural invariants (no magic numbers — hold at any canon size) ---
node - "$OUT" <<'JS'
const fs = require('fs'), path = process.argv[2];
const rd = f => JSON.parse(fs.readFileSync(path + '/' + f, 'utf8'));
const albums = rd('albums.json'), details = rd('details.json'), graph = rd('graph.json');
const places = rd('places.json'), activity = rd('people-activity.json');
const fail = m => { console.error('✗ INVARIANT FAILED: ' + m); process.exit(1); };
if (albums.length !== Object.keys(details).length)
  fail(`albums ${albums.length} != details ${Object.keys(details).length}`);
for (const a of albums) {
  for (const k of ['title','artist','year','artUrl','style','styleCode'])
    if (!a[k]) fail(`album ${a.id} missing ${k}`);
  if (!Array.isArray(a.styleTags)) fail(`album ${a.id} styleTags is not an array`);
  const d = details[a.id];
  if (!d) fail(`no details for album ${a.id}`);
  if (!d.tracks || d.tracks.length < 1) fail(`album ${a.id} has no tracks`);
  if (!d.personnel || d.personnel.length < 1) fail(`album ${a.id} has no personnel`);
}
if (Object.keys(graph.people).length < 1) fail('graph.people empty');
if (!graph.edges || graph.edges.length < 1) fail('graph.edges empty');
for (const e of graph.edges) {
  if (!graph.people[e.p]) fail(`edge references unknown person ${e.p}`);
  if (!e.entries || e.entries.length < 1) fail(`edge ${e.p}/${e.a} has no entries`);
}
const albumIds = new Set(albums.map(a => a.id));
const placeIds = new Set(), KINDS = ['studio','club','hall','festival','home','other'];
for (const p of places) {
  for (const k of ['id','name','kind','city','precision'])
    if (!p[k]) fail(`place ${p.id || '?'} missing ${k}`);
  if (placeIds.has(p.id)) fail(`duplicate place id ${p.id}`);
  placeIds.add(p.id);
  if (!KINDS.includes(p.kind)) fail(`place ${p.id} bad kind ${p.kind}`);
  if (!['address','city'].includes(p.precision)) fail(`place ${p.id} bad precision ${p.precision}`);
  if (typeof p.lat !== 'number' || p.lat < -90 || p.lat > 90) fail(`place ${p.id} bad lat`);
  if (typeof p.lon !== 'number' || p.lon < -180 || p.lon > 180) fail(`place ${p.id} bad lon`);
  if (!p.albums || p.albums.length < 1) fail(`place ${p.id} has no albums`);
  for (const pa of p.albums) {
    if (!albumIds.has(pa.albumId)) fail(`place ${p.id} references unknown album ${pa.albumId}`);
    if (!Array.isArray(pa.dates)) fail(`place ${p.id}/${pa.albumId} dates not an array`);
  }
}
// people-activity.json — lanes contract. Every rule here is structural: it
// holds at 100 albums or 1000, and none of it hard-codes a count.
const peopleIds = new Set(Object.keys(graph.people));
const seenPerson = new Set();
let prevPerson = null;
for (const pr of activity.people) {
  if (!pr.personId || !pr.name) fail(`activity person ${pr.personId || '?'} missing id/name`);
  if (seenPerson.has(pr.personId)) fail(`duplicate activity personId ${pr.personId}`);
  seenPerson.add(pr.personId);
  // the lanes page renders names/instruments out of graph.json, so an id the
  // graph does not carry would draw a lane the rest of the site cannot label
  if (!peopleIds.has(pr.personId)) fail(`activity person ${pr.personId} absent from graph.people`);
  if (!Array.isArray(pr.instruments)) fail(`activity ${pr.personId} instruments not an array`);
  if (!pr.sessions || pr.sessions.length < 1) fail(`activity ${pr.personId} has no sessions`);
  const dates = [], pairs = new Set();
  for (const se of pr.sessions) {
    if (!/^\d{4}-\d{2}(-\d{2})?$/.test(se.date)) fail(`activity ${pr.personId} bad date ${se.date}`);
    if (!albumIds.has(se.albumId)) fail(`activity ${pr.personId} unknown album ${se.albumId}`);
    const k = se.date + '|' + se.albumId;
    if (pairs.has(k)) fail(`activity ${pr.personId} duplicate session ${k}`);
    pairs.add(k);
    if (se.date < activity.meta.spanStart || se.date > activity.meta.spanEnd)
      fail(`activity ${pr.personId} date ${se.date} outside meta span`);
    dates.push(se.date);
  }
  // string compare is the ordering contract: YYYY-MM sorts before YYYY-MM-DD
  // of the same month, which is the intended "month, day unknown" placement
  const sorted = [...dates].sort();
  if (dates.join() !== sorted.join()) fail(`activity ${pr.personId} sessions not sorted by date`);
  if (pr.first !== sorted[0]) fail(`activity ${pr.personId} first != min(dates)`);
  if (pr.last !== sorted[sorted.length - 1]) fail(`activity ${pr.personId} last != max(dates)`);
  const years = new Set(dates.map(d => d.slice(0, 4)));
  if (pr.yearsActive !== years.size) fail(`activity ${pr.personId} yearsActive != distinct years`);
  if (prevPerson !== null &&
      (pr.first < prevPerson.first ||
       (pr.first === prevPerson.first && pr.personId < prevPerson.id)))
    fail(`activity people not sorted at ${pr.personId}`);
  prevPerson = { first: pr.first, id: pr.personId };
}
// D5: excluded people are exactly those the graph knows but the lanes omit —
// so the page's own footnote is checkable against the other contract file
if (activity.meta.undatedOnlyPeople !== peopleIds.size - activity.people.length)
  fail(`activity meta.undatedOnlyPeople ${activity.meta.undatedOnlyPeople} != graph.people - lanes `
       + `(${peopleIds.size - activity.people.length})`);
for (const id of activity.meta.undatedAlbums)
  if (!albumIds.has(id)) fail(`activity meta.undatedAlbums unknown album ${id}`);

const kb = f => Math.round(fs.statSync(path + '/' + f).size / 1024);
console.log(`✓ Export valid — albums=${albums.length} people=${Object.keys(graph.people).length} `
  + `edges=${graph.edges.length} places=${places.length}  `
  + `lanes=${activity.people.length} `
  + `(${kb('albums.json')}+${kb('details.json')}+${kb('graph.json')}+${kb('places.json')}`
  + `+${kb('people-activity.json')} KB)`);
JS
