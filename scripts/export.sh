#!/usr/bin/env bash
# Export The Jazz Canon contract from the SYSTEM OF RECORD (postgres._jazzcanon)
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
  WHERE NOT EXISTS (SELECT 1 FROM _jazzcanon.performance p WHERE p.album_id=a.id)")
[ "$noperf" = "0" ] || { echo "✗ INVARIANT FAILED: $noperf albums with zero performances" >&2; exit 1; }

# --- albums.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/albums.json"
SELECT json_agg(r ORDER BY r.year, r.id)
FROM (
  SELECT a.id, a.title, a.artist_name AS artist, a.year,
         l.name AS label, a.catalog_number AS catalog,
         s.display_name AS style, s.code AS "styleCode",
         aa.source_url AS "artUrl", a.apple_album_id AS "appleAlbumId"
  FROM _jazzcanon.album a
  LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
  JOIN _jazzcanon.style s ON s.id = a.style_primary_id
  LEFT JOIN _jazzcanon.album_art aa ON aa.album_id = a.id AND aa.is_primary
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
LEFT JOIN _jazzcanon.person lead ON lead.id = a.leader_person_id;
SQL

# --- graph.json ---
"${PSQL[@]}" <<'SQL' > "$OUT/graph.json"
SELECT json_build_object(
  'people', (
     SELECT json_object_agg(pe.id, pe.canonical_name)
     FROM _jazzcanon.person pe
     WHERE EXISTS (SELECT 1 FROM _jazzcanon.performance p WHERE p.person_id = pe.id)),
  'edges', (
     SELECT json_agg(e) FROM (
       SELECT p.person_id AS p, p.album_id AS a,
              json_agg(json_build_object('instrument', i.name, 'e', p.epistemic)
                       ORDER BY i.name) AS entries
       FROM _jazzcanon.performance p
       JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
       GROUP BY p.person_id, p.album_id
     ) e)
);
SQL

# --- structural invariants (no magic numbers — hold at any canon size) ---
node - "$OUT" <<'JS'
const fs = require('fs'), path = process.argv[2];
const rd = f => JSON.parse(fs.readFileSync(path + '/' + f, 'utf8'));
const albums = rd('albums.json'), details = rd('details.json'), graph = rd('graph.json');
const fail = m => { console.error('✗ INVARIANT FAILED: ' + m); process.exit(1); };
if (albums.length !== Object.keys(details).length)
  fail(`albums ${albums.length} != details ${Object.keys(details).length}`);
for (const a of albums) {
  for (const k of ['title','artist','year','artUrl'])
    if (!a[k]) fail(`album ${a.id} missing ${k}`);
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
const kb = f => Math.round(fs.statSync(path + '/' + f).size / 1024);
console.log(`✓ Export valid — albums=${albums.length} people=${Object.keys(graph.people).length} `
  + `edges=${graph.edges.length}  (${kb('albums.json')}+${kb('details.json')}+${kb('graph.json')} KB)`);
JS
