-- rollback-4a-ballot-fields.sql — undo migrate-4a-ballot-fields.sql
--
--   sudo -u postgres psql -p 5433 -d postgres -f scripts/rollback-4a-ballot-fields.sql
--
-- DESTRUCTIVE: dropping album.case_for / album.case_against discards the
-- backfilled ballot prose in the database. The dossier JSON files under
-- research/candidates-archive/ and research/candidates-inbox/ remain the
-- archival source, so the text is recoverable by re-running the backfill.
--
-- This does NOT revert inclusion_rationale. The backfill repointed it from
-- the ballot's case_for to the dossier's top-level `rationale` on 21 rows
-- (John's decision, 2026-07-26). Those prior values are preserved in
-- edit_log.old_value; restoring them is a deliberate data decision, not a
-- schema rollback, and belongs in its own script if ever wanted:
--
--   UPDATE _jazzcanon.album a SET inclusion_rationale = e.old_value
--     FROM _jazzcanon.edit_log e
--    WHERE e.table_name = 'album' AND e.record_id = a.id
--      AND e.field = 'inclusion_rationale'
--      AND e.reason LIKE 'ballot backfill 2026-07-26%';
--
-- Note on grants: v_album_detail must be dropped, not replaced (CREATE OR
-- REPLACE VIEW cannot remove columns), and DROP loses its grants. They are
-- re-granted below — _jazzcanon_ro, _jazzcanon_app and the cross-project
-- reader _foundry_app all hold SELECT on this view today.

\set ON_ERROR_STOP on

BEGIN;

SET ROLE _jazzcanon_role;

-- 1. Restore the pre-4a view definition (drops the two trailing columns)
DROP VIEW IF EXISTS _jazzcanon.v_album_detail;

CREATE VIEW _jazzcanon.v_album_detail AS
 SELECT a.id,
    a.title,
    a.artist_name,
    a.leader_person_id,
    a.year,
    a.label_id,
    a.catalog_number,
    a.style_primary_id,
    a.recording_dates_text,
    a.multi_session,
    a.musicbrainz_release_group_mbid,
    a.musicbrainz_release_mbid,
    a.apple_album_id,
    a.consensus,
    a.canon_status,
    a.canon_tier,
    a.priority,
    a.inclusion_rationale,
    a.epistemic,
    a.notes,
    a.description,
    a.search_document,
    a.embedding,
    a.created_at,
    a.updated_at,
    l.name AS label_name,
    s.display_name AS style_primary_name,
    lead.canonical_name AS leader_name
   FROM _jazzcanon.album a
     LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
     LEFT JOIN _jazzcanon.style s ON s.id = a.style_primary_id
     LEFT JOIN _jazzcanon.person lead ON lead.id = a.leader_person_id;

-- 2. Drop the columns
ALTER TABLE _jazzcanon.album
  DROP COLUMN IF EXISTS case_for,
  DROP COLUMN IF EXISTS case_against;

-- 3. Restore the inclusion_rationale comment to its pre-4a state (none)
COMMENT ON COLUMN _jazzcanon.album.inclusion_rationale IS NULL;

RESET ROLE;

-- 4. Re-grant on the recreated view (DROP VIEW discarded these)
GRANT SELECT, INSERT, UPDATE ON _jazzcanon.v_album_detail TO _jazzcanon_app;
GRANT SELECT ON _jazzcanon.v_album_detail TO _jazzcanon_ro;
GRANT SELECT ON _jazzcanon.v_album_detail TO _foundry_app;

COMMIT;

\echo '--- album ballot columns (expect 0 rows) ---'
SELECT column_name FROM information_schema.columns
 WHERE table_schema = '_jazzcanon' AND table_name = 'album'
   AND column_name IN ('case_for', 'case_against');

\echo '--- v_album_detail grants restored ---'
SELECT grantee, privilege_type FROM information_schema.role_table_grants
 WHERE table_schema = '_jazzcanon' AND table_name = 'v_album_detail'
 ORDER BY grantee, privilege_type;
