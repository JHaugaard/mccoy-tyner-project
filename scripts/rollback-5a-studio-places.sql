-- rollback-5a-studio-places.sql — reverses migrate-5a-studio-places.sql
\set ON_ERROR_STOP on
SET ROLE _jazzcanon_role;
ALTER TABLE _jazzcanon.studio
  DROP COLUMN IF EXISTS kind,
  DROP COLUMN IF EXISTS address,
  DROP COLUMN IF EXISTS location_epistemic,
  DROP COLUMN IF EXISTS location_source;
RESET ROLE;
