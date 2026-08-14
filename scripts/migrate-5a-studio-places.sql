-- migrate-5a-studio-places.sql
-- Studios map, phase 1: place metadata columns on _jazzcanon.studio.
-- Ratified by John 2026-08-14 (studios cleanup worksheet + schema proposal).
-- Schema only — data lands separately via scripts/studio-cleanup-2026-08-14.sql
-- run as _jazzcanon_app.
\set ON_ERROR_STOP on

SET ROLE _jazzcanon_role;

ALTER TABLE _jazzcanon.studio
  ADD COLUMN kind text
    CONSTRAINT studio_kind_check
    CHECK (kind IN ('studio','club','hall','festival','home','other')),
  ADD COLUMN address text,
  ADD COLUMN location_epistemic _jazzcanon.epistemic_label,
  ADD COLUMN location_source text;

COMMENT ON COLUMN _jazzcanon.studio.kind IS
  'Venue type for the Studios map: studio|club|hall|festival|home|other';
COMMENT ON COLUMN _jazzcanon.studio.address IS
  'Location as documented by sources — street address, block, or intersection. Never invented; NULL when sources give city only.';
COMMENT ON COLUMN _jazzcanon.studio.location_epistemic IS
  'obs = street-level documentation cited in location_source; inf = city-level only. Exporter maps obs->address, inf->city for the site''s precision field.';
COMMENT ON COLUMN _jazzcanon.studio.location_source IS
  'Citation URL(s) backing address (and later, coordinates).';

RESET ROLE;
