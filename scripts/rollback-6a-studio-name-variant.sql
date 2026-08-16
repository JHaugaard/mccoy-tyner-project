-- rollback-6a-studio-name-variant.sql — reverses migrate-6a-studio-name-variant.sql
--
-- Drops the alias table AND its seeded rows. Nothing else references it:
-- studio_name_variant is a leaf, so there is no FK to unwind and no other
-- table loses data. The 2026-08-14 edit_log audit trail the seed was derived
-- from is untouched, so the table can be rebuilt from scratch by re-running
-- the migration and scripts/seed-studio-name-variants.py.
\set ON_ERROR_STOP on

SET ROLE _jazzcanon_role;

DROP TRIGGER IF EXISTS trg_studio_name_variant_no_tombstone
  ON _jazzcanon.studio_name_variant;
DROP TABLE IF EXISTS _jazzcanon.studio_name_variant;
DROP FUNCTION IF EXISTS _jazzcanon.studio_name_variant_no_tombstone();

RESET ROLE;
