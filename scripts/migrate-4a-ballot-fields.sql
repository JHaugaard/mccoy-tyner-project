-- migrate-4a-ballot-fields.sql — promote council ballot prose into the DB
-- Handoff: docs/handoffs/2026-07-26-ballot-fields-into-db.md
--
-- RUN VIA THE WRAPPER:
--   bash scripts/run-migrate-4a.sh
-- Or directly:
--   sudo -u postgres psql -p 5433 -d postgres -f scripts/migrate-4a-ballot-fields.sql
--
-- Superuser is needed only to SET ROLE _jazzcanon_role, which owns album and
-- v_album_detail. Grants are not ownership: ALTER TABLE fails as _jazzcanon_app
-- no matter how permissive its grants look.
--
-- Safe to re-run. Strictly scoped to _jazzcanon. No data is written here —
-- the backfill is a separate step (scripts/backfill-ballot-fields.py), so
-- every prose value lands through the app role with an edit_log row.
--
-- Design decisions (John, 2026-07-26 — handoff "Answers" section):
--   * case_for / case_against only. No council_tier: album.canon_tier already
--     holds the ballot's tier, written by stage-candidate.py.
--   * recommendation, confidence, disagreement and scope_check stay in the
--     dossier JSON for now. The dossiers remain the archival source; these
--     columns are a projection, not a move.
--   * v_album_detail enumerates its columns explicitly, so new album columns
--     do NOT propagate automatically. The two are appended AFTER leader_name:
--     inserting them in table order would rename existing view columns and
--     CREATE OR REPLACE VIEW would fail with "cannot change name of view
--     column". Column order is cosmetically odd; that is accepted.
--   * v_album_search_source is deliberately NOT touched. It builds a search
--     document that embed.py does not read (see docs/follow-ups.md) —
--     reconciling the two is a separate decision, not migration work.

\set ON_ERROR_STOP on

BEGIN;

SET ROLE _jazzcanon_role;

-- ---------------------------------------------------------------------------
-- 1. Ballot prose columns
-- ---------------------------------------------------------------------------
ALTER TABLE _jazzcanon.album
  ADD COLUMN IF NOT EXISTS case_for     text,
  ADD COLUMN IF NOT EXISTS case_against text;

COMMENT ON COLUMN _jazzcanon.album.case_for IS
  'Council ballot: the argument for inclusion. Projection of ballot.case_for '
  'in the album''s research dossier. NULL for albums that never got a ballot.';
COMMENT ON COLUMN _jazzcanon.album.case_against IS
  'Council ballot: the argument against inclusion, retained even for included '
  'albums. Projection of ballot.case_against. NULL where no ballot exists.';
COMMENT ON COLUMN _jazzcanon.album.inclusion_rationale IS
  'The dossier''s top-level `rationale`: what the album IS, source-tagged. '
  'Distinct from case_for, which is what the council ARGUED. Both paths in '
  'stage-candidate.py write this field from `rationale` (see migrate-4a).';

-- ---------------------------------------------------------------------------
-- 2. v_album_detail — new columns appended last (see header)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE VIEW _jazzcanon.v_album_detail AS
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
    lead.canonical_name AS leader_name,
    a.case_for,
    a.case_against
   FROM _jazzcanon.album a
     LEFT JOIN _jazzcanon.label l ON l.id = a.label_id
     LEFT JOIN _jazzcanon.style s ON s.id = a.style_primary_id
     LEFT JOIN _jazzcanon.person lead ON lead.id = a.leader_person_id;

RESET ROLE;

COMMIT;

-- ---------------------------------------------------------------------------
-- Verify
-- ---------------------------------------------------------------------------
\echo '--- new album columns ---'
SELECT column_name, data_type, is_nullable
  FROM information_schema.columns
 WHERE table_schema = '_jazzcanon' AND table_name = 'album'
   AND column_name IN ('case_for', 'case_against');

\echo '--- v_album_detail tail (new columns must be last) ---'
SELECT ordinal_position, column_name
  FROM information_schema.columns
 WHERE table_schema = '_jazzcanon' AND table_name = 'v_album_detail'
   AND ordinal_position > 25
 ORDER BY ordinal_position;

\echo '--- app-role grants on album (SELECT/INSERT/UPDATE, no DELETE) ---'
SELECT privilege_type
  FROM information_schema.role_table_grants
 WHERE table_schema = '_jazzcanon' AND table_name = 'album'
   AND grantee = '_jazzcanon_app'
 ORDER BY privilege_type;

\echo '--- ballot columns are empty until the backfill runs ---'
SELECT count(*) FILTER (WHERE case_for IS NOT NULL)     AS case_for_set,
       count(*) FILTER (WHERE case_against IS NOT NULL) AS case_against_set,
       count(*)                                         AS total
  FROM _jazzcanon.album;
