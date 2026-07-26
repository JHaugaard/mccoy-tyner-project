-- fix-ownership.sql — jcdb held item 2 (spec §10 step 3a)
-- Purpose: create the missing owner role _jazzcanon_role and hand it ownership of
--          every object in schema _jazzcanon, so future migrations don't fail with
--          "must be owner of table ...". Read-only role _jazzcanon_ro is preserved.
--
-- RUN AS A SUPERUSER, e.g. from the Claude Code prompt:
--   ! sudo -u postgres psql -p 5433 -d postgres -f /home/john/dev/active/mccoy-tyner/scripts/fix-ownership.sql
--
-- Safe to re-run. Strictly scoped to _jazzcanon — touches nothing in public or
-- any other project's schema. NOT `REASSIGN OWNED BY postgres` (that would grab
-- postgres-owned objects across this shared instance).

\set ON_ERROR_STOP on

BEGIN;

-- 1. Owner role (NOLOGIN — owns objects, used only for migrations)
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '_jazzcanon_role') THEN
    CREATE ROLE _jazzcanon_role NOLOGIN;
    RAISE NOTICE 'created role _jazzcanon_role';
  ELSE
    RAISE NOTICE 'role _jazzcanon_role already exists — skipping create';
  END IF;
END $$;

-- 2. Schema itself
ALTER SCHEMA _jazzcanon OWNER TO _jazzcanon_role;

-- 3. Tables, views, materialized views, and STANDALONE sequences.
--    Indexes and owned (SERIAL/identity) sequences follow their table
--    automatically, so we skip owned sequences to avoid
--    "cannot change owner of sequence ... is linked to table ...".
DO $$
DECLARE r record;
BEGIN
  FOR r IN
    SELECT c.relkind, c.relname
    FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE n.nspname = '_jazzcanon' AND c.relkind IN ('r','v','m','S')
      AND NOT (c.relkind = 'S' AND EXISTS (
        SELECT 1 FROM pg_depend d
        WHERE d.objid = c.oid AND d.deptype IN ('a','i') AND d.refobjsubid > 0))
  LOOP
    EXECUTE format('ALTER %s _jazzcanon.%I OWNER TO _jazzcanon_role',
      CASE r.relkind
        WHEN 'r' THEN 'TABLE'
        WHEN 'v' THEN 'VIEW'
        WHEN 'm' THEN 'MATERIALIZED VIEW'
        WHEN 'S' THEN 'SEQUENCE'
      END, r.relname);
  END LOOP;
END $$;

-- 4. Functions
DO $$
DECLARE r record;
BEGIN
  FOR r IN
    SELECT p.oid::regprocedure AS sig
    FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
    WHERE n.nspname = '_jazzcanon'
  LOOP
    EXECUTE format('ALTER FUNCTION %s OWNER TO _jazzcanon_role', r.sig);
  END LOOP;
END $$;

-- 5. User-defined enums / domains (all the _jazzcanon.* label types)
DO $$
DECLARE r record;
BEGIN
  FOR r IN
    SELECT t.typname
    FROM pg_type t JOIN pg_namespace n ON n.oid = t.typnamespace
    WHERE n.nspname = '_jazzcanon' AND t.typtype IN ('e','d')
  LOOP
    EXECUTE format('ALTER TYPE _jazzcanon.%I OWNER TO _jazzcanon_role', r.typname);
  END LOOP;
END $$;

-- 6. Preserve the read-only role + future-proof it via default privileges
GRANT USAGE ON SCHEMA _jazzcanon TO _jazzcanon_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA _jazzcanon TO _jazzcanon_ro;
ALTER DEFAULT PRIVILEGES FOR ROLE _jazzcanon_role IN SCHEMA _jazzcanon
  GRANT SELECT ON TABLES TO _jazzcanon_ro;

COMMIT;

-- 7. Verification — should report ZERO objects still owned by postgres
SELECT 'objects still owned by postgres in _jazzcanon' AS check,
       count(*) AS remaining
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
JOIN pg_roles o ON o.oid = c.relowner
WHERE n.nspname = '_jazzcanon' AND c.relkind IN ('r','v','m','S')
  AND o.rolname = 'postgres';

SELECT nspname AS schema, r.rolname AS owner
FROM pg_namespace n JOIN pg_roles r ON r.oid = n.nspowner
WHERE nspname = '_jazzcanon';
