-- migrate-3b-site-status.sql — spec §10 step 3b
-- Adds the publication axis (site_status), the write-contract app role
-- (_jazzcanon_app), and the edit_log audit table.
--
-- RUN VIA THE WRAPPER (generates the app-role password, stores it in
-- .env.local, never commits it):
--   bash scripts/run-migrate-3b.sh
-- Or directly, supplying the password yourself:
--   sudo -u postgres psql -p 5433 -d postgres -v apppass='<password>' \
--     -f scripts/migrate-3b-site-status.sql
-- CREATE ROLE needs superuser; all object creation runs under
-- SET ROLE _jazzcanon_role so ownership lands correctly.
--
-- Safe to re-run. Strictly scoped to _jazzcanon.
--
-- Design decisions (spec §11):
--   * site_status is a lookup table keyed by text code (not serial id) so
--     album.site_status can DEFAULT 'found' and queries read plainly.
--   * All 100 currently-included albums backfill to 'live' (they are already
--     on the public site), so the export filter (approved|live) is a no-op today.
--   * _jazzcanon_app gets SELECT/INSERT/UPDATE — no DELETE. Rejection is
--     canon_status='excluded', never row removal; "never delete" is structural.
--   * edit_log is append-only for the app role (INSERT+SELECT, no UPDATE).

\set ON_ERROR_STOP on

BEGIN;

-- ---------------------------------------------------------------------------
-- 1. App role (LOGIN, DML-only, owns nothing)
-- ---------------------------------------------------------------------------
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '_jazzcanon_app') THEN
    CREATE ROLE _jazzcanon_app LOGIN;
    RAISE NOTICE 'created role _jazzcanon_app';
  ELSE
    RAISE NOTICE 'role _jazzcanon_app already exists — resetting password';
  END IF;
END $$;

-- Password comes in as a psql variable (never stored in this file)
ALTER ROLE _jazzcanon_app PASSWORD :'apppass';

-- ---------------------------------------------------------------------------
-- 2. New objects, created AS the owner role
-- ---------------------------------------------------------------------------
SET ROLE _jazzcanon_role;

-- 2a. Publication axis: lookup table (config, not enum — John edits rows)
CREATE TABLE IF NOT EXISTS _jazzcanon.site_status (
  code         text PRIMARY KEY,
  display_name text NOT NULL,
  description  text,
  sort_order   integer NOT NULL
);

INSERT INTO _jazzcanon.site_status (code, display_name, description, sort_order) VALUES
  ('found',    'Found',    'Surfaced by the canon builder; awaiting John''s review', 1),
  ('reviewed', 'Reviewed', 'John has looked at it; not yet greenlit for the site',   2),
  ('approved', 'Approved', 'Greenlit for the public site; next build picks it up',   3),
  ('live',     'Live',     'On the public site now',                                 4),
  ('retired',  'Retired',  'Pulled from the site; kept in the database',             5)
ON CONFLICT (code) DO NOTHING;

-- 2b. album.site_status — orthogonal to canon_status
ALTER TABLE _jazzcanon.album
  ADD COLUMN IF NOT EXISTS site_status text NOT NULL DEFAULT 'found'
  REFERENCES _jazzcanon.site_status(code);

CREATE INDEX IF NOT EXISTS idx_album_site_status ON _jazzcanon.album (site_status);

-- Backfill: everything currently included is already on the public site.
UPDATE _jazzcanon.album SET site_status = 'live'
 WHERE canon_status = 'included' AND site_status = 'found';

-- 2c. edit_log — audit trail for every hand/agent edit (append-only)
CREATE TABLE IF NOT EXISTS _jazzcanon.edit_log (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  edited_at  timestamptz NOT NULL DEFAULT now(),
  editor     text NOT NULL,             -- 'mccoy' | 'john' | script name
  table_name text NOT NULL,
  record_id  text NOT NULL,
  field      text NOT NULL,
  old_value  text,
  new_value  text,
  reason     text                       -- why, incl. epistemic/citation note
);

CREATE INDEX IF NOT EXISTS idx_edit_log_record ON _jazzcanon.edit_log (table_name, record_id);

RESET ROLE;

-- ---------------------------------------------------------------------------
-- 3. Grants for _jazzcanon_app (DML, no DELETE, no ownership)
-- ---------------------------------------------------------------------------
GRANT USAGE ON SCHEMA _jazzcanon TO _jazzcanon_app;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA _jazzcanon TO _jazzcanon_app;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA _jazzcanon TO _jazzcanon_app;

-- edit_log is append-only for the app role
REVOKE UPDATE ON _jazzcanon.edit_log FROM _jazzcanon_app;

-- Future tables/sequences created by the owner role inherit the same grants
ALTER DEFAULT PRIVILEGES FOR ROLE _jazzcanon_role IN SCHEMA _jazzcanon
  GRANT SELECT, INSERT, UPDATE ON TABLES TO _jazzcanon_app;
ALTER DEFAULT PRIVILEGES FOR ROLE _jazzcanon_role IN SCHEMA _jazzcanon
  GRANT USAGE ON SEQUENCES TO _jazzcanon_app;

COMMIT;

-- ---------------------------------------------------------------------------
-- Verify
-- ---------------------------------------------------------------------------
\echo '--- site_status rows ---'
SELECT code, sort_order FROM _jazzcanon.site_status ORDER BY sort_order;
\echo '--- album site_status distribution ---'
SELECT site_status, canon_status, count(*) FROM _jazzcanon.album GROUP BY 1, 2;
\echo '--- new table owners ---'
SELECT c.relname, pg_get_userbyid(c.relowner) AS owner
  FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
 WHERE n.nspname = '_jazzcanon' AND c.relname IN ('site_status', 'edit_log');
