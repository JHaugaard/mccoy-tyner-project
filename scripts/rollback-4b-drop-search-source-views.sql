-- rollback-4b-drop-search-source-views.sql — undo migrate-4b
--
--   sudo -u postgres psql -p 5433 -d postgres -f scripts/rollback-4b-drop-search-source-views.sql
--
-- Recreates both search-source views exactly as they were on 2026-07-26 and
-- restores their grants (DROP VIEW discarded them).
--
-- NOTE: these definitions are the DRIFTED ones — they do not match what
-- embed.py actually builds, and they know nothing about album.case_for /
-- album.case_against. Restoring them recreates the inconsistency that
-- migrate-4b removed. If the goal is to make a view the real definition,
-- write a new one that matches embed.py and change embed.py to read it;
-- don't resurrect these.

\set ON_ERROR_STOP on

BEGIN;

SET ROLE _jazzcanon_role;

CREATE VIEW _jazzcanon.v_album_search_source AS
 SELECT a.id AS album_id,
    a.title,
    a.artist_name,
    a.year,
    l.name AS label,
    s.display_name AS style,
    string_agg(DISTINCT ((pe.canonical_name || ' ('::text) || i.name) || ')'::text, ', '::text) AS personnel,
    a.notes
   FROM _jazzcanon.album a
     LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
     LEFT JOIN _jazzcanon.style s ON s.id = a.style_primary_id
     LEFT JOIN _jazzcanon.performance p ON p.album_id = a.id
     LEFT JOIN _jazzcanon.person pe ON pe.id = p.person_id
     LEFT JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
  GROUP BY a.id, a.title, a.artist_name, a.year, l.name, s.display_name, a.notes;

CREATE VIEW _jazzcanon.v_person_search_source AS
 SELECT pe.id AS person_id,
    pe.canonical_name,
    string_agg(DISTINCT i.name, ', '::text) AS instruments,
    string_agg(DISTINCT a.title, ', '::text) AS albums,
    min(a.year) AS first_year,
    max(a.year) AS last_year,
    pe.notes
   FROM _jazzcanon.person pe
     LEFT JOIN _jazzcanon.performance p ON p.person_id = pe.id
     LEFT JOIN _jazzcanon.instrument i ON i.id = p.instrument_id
     LEFT JOIN _jazzcanon.album a ON a.id = p.album_id
  GROUP BY pe.id, pe.canonical_name, pe.notes;

RESET ROLE;

-- Grants as they stood before the drop
GRANT SELECT, INSERT, UPDATE ON _jazzcanon.v_album_search_source  TO _jazzcanon_app;
GRANT SELECT, INSERT, UPDATE ON _jazzcanon.v_person_search_source TO _jazzcanon_app;
GRANT SELECT ON _jazzcanon.v_album_search_source  TO _jazzcanon_ro;
GRANT SELECT ON _jazzcanon.v_person_search_source TO _jazzcanon_ro;
GRANT SELECT ON _jazzcanon.v_album_search_source  TO _foundry_app;
GRANT SELECT ON _jazzcanon.v_person_search_source TO _foundry_app;

COMMIT;

\echo '--- views restored (expect 2 rows) ---'
SELECT table_name FROM information_schema.views
 WHERE table_schema = '_jazzcanon'
   AND table_name IN ('v_album_search_source', 'v_person_search_source');

\echo '--- grants restored ---'
SELECT table_name, grantee, privilege_type FROM information_schema.role_table_grants
 WHERE table_schema = '_jazzcanon'
   AND table_name IN ('v_album_search_source', 'v_person_search_source')
 ORDER BY table_name, grantee, privilege_type;
