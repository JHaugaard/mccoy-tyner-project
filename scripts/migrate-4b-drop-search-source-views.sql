-- migrate-4b-drop-search-source-views.sql — retire the dead search-source views
-- Follow-up #5 (docs/follow-ups.md), John's decision 2026-07-26.
--
--   sudo -u postgres psql -p 5433 -d postgres -f scripts/migrate-4b-drop-search-source-views.sql
--
-- WHY
-- There were two competing definitions of an album's (and a person's)
-- "search document", and they disagreed:
--
--   * scripts/embed.py builds the doc in Python and writes it to
--     album.search_document / person.search_document. This is the one that
--     actually produces embeddings, and since migrate-4a it includes the
--     council's case_for / case_against.
--   * _jazzcanon.v_album_search_source and v_person_search_source built a
--     different doc — the album view added label and notes and omitted
--     description; neither knew about the ballot columns.
--
-- embed.py has never read either view. They are Phase-3 design artifacts that
-- the implementation diverged from and then outgrew. A second, wrong
-- definition of the same concept is a trap for whoever reads the schema next,
-- so it goes.
--
-- EVIDENCE (verified 2026-07-26 before dropping)
--   * No .py/.sh/.mjs/.js/.ts file in mccoy-tyner reads either view.
--   * canon-search.py queries album.embedding / person.embedding directly.
--   * pg_depend reports no dependent views, rules, or constraints.
--   * The only remaining references are prose: docs/schema.md,
--     docs/mccoy-agent-spec.md, data/schema.sql (the Phase-3 design
--     artifact), and McCoy's Hermes config.yaml orientation text.
--
-- REVERSIBLE: scripts/rollback-4b-drop-search-source-views.sql recreates both
-- and re-grants. Grants must be restored explicitly — DROP discards them, and
-- three roles hold privileges here, including the cross-project reader
-- _foundry_app.

\set ON_ERROR_STOP on

BEGIN;

SET ROLE _jazzcanon_role;

DROP VIEW IF EXISTS _jazzcanon.v_album_search_source;
DROP VIEW IF EXISTS _jazzcanon.v_person_search_source;

RESET ROLE;

COMMIT;

-- ---------------------------------------------------------------------------
-- Verify
-- ---------------------------------------------------------------------------
\echo '--- search-source views (expect 0 rows) ---'
SELECT table_name FROM information_schema.views
 WHERE table_schema = '_jazzcanon'
   AND table_name IN ('v_album_search_source', 'v_person_search_source');

\echo '--- surviving _jazzcanon views (expect 11) ---'
SELECT count(*) AS view_count FROM information_schema.views
 WHERE table_schema = '_jazzcanon';

\echo '--- search documents still intact (the real ones) ---'
SELECT 'album'  AS tbl, count(*) FILTER (WHERE search_document IS NOT NULL) AS with_doc,
       count(*) AS total FROM _jazzcanon.album
UNION ALL
SELECT 'person', count(*) FILTER (WHERE search_document IS NOT NULL),
       count(*) FROM _jazzcanon.person;
