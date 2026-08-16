-- migrate-6a-studio-name-variant.sql
-- Alias table for recording places: the wordings sources use for a canonical
-- place, so the drip can resolve "Columbia 30th Street Studio" to
-- `cbs-30th-street-studio` instead of inventing a slug or refusing.
--
-- Ratified by John 2026-08-16. Schema only — data lands separately via
-- scripts/seed-studio-name-variants.py.
--
-- Mirrors _jazzcanon.person_name_variant, which solves the same problem for
-- people: uuid pk, FK with ON DELETE CASCADE, UNIQUE (owner, variant),
-- nullable source_note. Same shape, same insert-only lane in
-- config/edit-contract.md.
--
-- Grants are deliberately absent: ALTER DEFAULT PRIVILEGES on this schema
-- already gives _jazzcanon_ro SELECT and _jazzcanon_app INSERT/SELECT/UPDATE
-- (never DELETE) on any table _jazzcanon_role creates. Running this as
-- _jazzcanon_role is what puts the table in the right lane — an explicit GRANT
-- here would diverge from person_name_variant, which also has none.
\set ON_ERROR_STOP on

SET ROLE _jazzcanon_role;

CREATE TABLE IF NOT EXISTS _jazzcanon.studio_name_variant (
  id           uuid    PRIMARY KEY DEFAULT gen_random_uuid(),
  studio_id    integer NOT NULL REFERENCES _jazzcanon.studio(id) ON DELETE CASCADE,
  variant_name text    NOT NULL,
  source_note  text,
  UNIQUE (studio_id, variant_name)
);

COMMENT ON TABLE _jazzcanon.studio_name_variant IS
  'Wordings that resolve to a canonical place. A variant points FROM a raw '
  'source string TO a surviving studio row — never to a merged-* tombstone. '
  'Seeded 2026-08-16 from the 2026-08-14 cleanup audit trail; grows as strings '
  'are resolved by hand. Insert-only for McCoy per config/edit-contract.md.';
COMMENT ON COLUMN _jazzcanon.studio_name_variant.variant_name IS
  'The venue wording as a source might print it — never the slug, never a '
  'compound string naming two venues. One venue per row.';
COMMENT ON COLUMN _jazzcanon.studio_name_variant.source_note IS
  'Provenance: which edit_log field or ruling this variant came from, or '
  '"hand-written" for variants with no cleanup trail.';

CREATE INDEX IF NOT EXISTS idx_studio_name_variant_studio
  ON _jazzcanon.studio_name_variant (studio_id);

-- A variant must never resolve TO a tombstone. Tombstones (name_slug rewritten
-- to 'merged-<id>') record merge and split rulings John already made; pointing
-- an alias at one would hand the drip a slug that is not a place, and
-- export.sh filters those rows out entirely. Documented rules drift; this one
-- is enforced, because the table is written to by an unattended agent.
CREATE OR REPLACE FUNCTION _jazzcanon.studio_name_variant_no_tombstone()
RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE target_slug text;
BEGIN
  SELECT name_slug INTO target_slug FROM _jazzcanon.studio WHERE id = NEW.studio_id;
  IF target_slug LIKE 'merged-%' THEN
    RAISE EXCEPTION
      'studio_name_variant.studio_id % is tombstone %, not a canonical place — '
      'a variant points FROM a merged row''s raw string, never TO one',
      NEW.studio_id, target_slug;
  END IF;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_studio_name_variant_no_tombstone
  ON _jazzcanon.studio_name_variant;
CREATE TRIGGER trg_studio_name_variant_no_tombstone
  BEFORE INSERT OR UPDATE ON _jazzcanon.studio_name_variant
  FOR EACH ROW EXECUTE FUNCTION _jazzcanon.studio_name_variant_no_tombstone();

RESET ROLE;
