-- =============================================================================
-- McCoy Tyner Jazz Canon — Relational Schema (Phase 3 design)
-- Target: Postgres 16 on vps8-core (127.0.0.1:5433), schema _jazzcanon
-- Status: APPLIED AT PHASE 4. This file is the design artifact, not yet run.
--
-- Namespace `_jazzcanon` is DECIDED (2026-06-10). Schema is created at Phase 4.
-- To rebind: search/replace `_jazzcanon` throughout, plus the role names below.
--
-- Requires extensions: vector (pgvector, installed 0.8.2). gen_random_uuid() is
-- core in PG13+. Embedding dimension 768 assumes a local nomic-embed-text model;
-- change vector(768) if the Phase 4 model choice differs.
-- =============================================================================

BEGIN;

CREATE SCHEMA IF NOT EXISTS _jazzcanon;
SET search_path TO _jazzcanon, public;

CREATE EXTENSION IF NOT EXISTS vector;  -- pgvector

-- -----------------------------------------------------------------------------
-- Enumerated types
-- -----------------------------------------------------------------------------
CREATE TYPE epistemic_label   AS ENUM ('obs', 'inf', 'unk');
CREATE TYPE canon_status      AS ENUM ('candidate', 'included', 'excluded');
CREATE TYPE canon_tier        AS ENUM ('consensus_core', 'contested', 'scope_call', 'exclude_suggested');
CREATE TYPE priority_label    AS ENUM ('must_have', 'strong', 'consider');
CREATE TYPE performance_scope AS ENUM ('all-tracks', 'selected-tracks', 'unknown');
CREATE TYPE production_role    AS ENUM ('producer', 'engineer', 'arranger', 'mixing', 'mastering', 'supervisor', 'other');
CREATE TYPE instrument_family AS ENUM ('brass', 'woodwinds', 'keyboards', 'strings', 'percussion', 'other');
CREATE TYPE source_type       AS ENUM ('book', 'web', 'liner-notes', 'discography', 'other');

-- -----------------------------------------------------------------------------
-- Reference / vocabulary tables
-- -----------------------------------------------------------------------------
CREATE TABLE instrument (
    id      serial PRIMARY KEY,
    name    text NOT NULL UNIQUE,            -- exact taxonomy string, e.g. 'tenor saxophone'
    family  instrument_family NOT NULL
);

CREATE TABLE style (
    id           serial PRIMARY KEY,
    code         text NOT NULL UNIQUE,        -- 'hard-bop' | 'soul-jazz' | 'cool-jazz' | 'modal-jazz' | 'post-bop'
    display_name text NOT NULL,
    description  text
);

CREATE TABLE label (
    id        serial PRIMARY KEY,
    name      text NOT NULL UNIQUE,
    name_slug text NOT NULL UNIQUE,
    notes     text
);

CREATE TABLE studio (
    id        serial PRIMARY KEY,
    name      text NOT NULL,
    city      text,
    name_slug text NOT NULL UNIQUE,
    notes     text,
    UNIQUE (name, city)
);

CREATE TABLE source (
    id          serial PRIMARY KEY,
    title       text NOT NULL,
    source_type source_type NOT NULL,
    url         text,
    notes       text
);

-- -----------------------------------------------------------------------------
-- People (unified: performers, leaders, producers, engineers, composers)
-- -----------------------------------------------------------------------------
CREATE TABLE person (
    id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    canonical_name  text NOT NULL UNIQUE,
    sort_name       text,
    name_slug       text NOT NULL UNIQUE,
    notes           text,
    search_document text,
    embedding       vector(768),
    created_at      timestamptz NOT NULL DEFAULT now(),
    updated_at      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE person_name_variant (
    id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    person_id    uuid NOT NULL REFERENCES person(id) ON DELETE CASCADE,
    variant_name text NOT NULL,
    source_note  text,
    UNIQUE (person_id, variant_name)
);

-- -----------------------------------------------------------------------------
-- Album (PK is the kebab-case canon slug — the join key to all research data)
-- -----------------------------------------------------------------------------
CREATE TABLE album (
    id                   text PRIMARY KEY,            -- e.g. 'miles-davis-kind-of-blue-1959'
    title                text NOT NULL,
    artist_name          text NOT NULL,               -- leader/primary as cited (display)
    leader_person_id     uuid REFERENCES person(id) ON DELETE SET NULL,
    year                 int CHECK (year BETWEEN 1940 AND 1990),
    label_id             int REFERENCES label(id),
    style_primary_id     int NOT NULL REFERENCES style(id),
    recording_dates_text text,
    multi_session        boolean NOT NULL DEFAULT false,
    canon_status         canon_status NOT NULL DEFAULT 'candidate',
    canon_tier           canon_tier,
    priority             priority_label,
    inclusion_rationale  text,
    epistemic            epistemic_label,
    notes                text,
    search_document      text,
    embedding            vector(768),
    created_at           timestamptz NOT NULL DEFAULT now(),
    updated_at           timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE album_style (
    album_id   text NOT NULL REFERENCES album(id) ON DELETE CASCADE,
    style_id   int  NOT NULL REFERENCES style(id),
    is_primary boolean NOT NULL DEFAULT false,
    PRIMARY KEY (album_id, style_id)
);

-- -----------------------------------------------------------------------------
-- Sessions & tracks
-- -----------------------------------------------------------------------------
CREATE TABLE session (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    album_id          text NOT NULL REFERENCES album(id) ON DELETE CASCADE,
    session_date      date,
    session_date_text text,                            -- range/uncertainty fallback
    studio_id         int REFERENCES studio(id),
    sequence          int,                             -- order within album
    epistemic         epistemic_label NOT NULL DEFAULT 'obs'
);

CREATE TABLE track (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    album_id       text NOT NULL REFERENCES album(id) ON DELETE CASCADE,
    session_id     uuid REFERENCES session(id) ON DELETE SET NULL,
    title          text NOT NULL,
    track_number   int,
    side           text CHECK (side IN ('A','B','C','D') OR side IS NULL),
    duration_text  text,
    bonus_track    boolean NOT NULL DEFAULT false,
    alternate_take boolean NOT NULL DEFAULT false,
    epistemic_track epistemic_label NOT NULL DEFAULT 'obs',
    UNIQUE (album_id, track_number, alternate_take)
);

CREATE TABLE track_composer (
    track_id  uuid NOT NULL REFERENCES track(id) ON DELETE CASCADE,
    person_id uuid NOT NULL REFERENCES person(id) ON DELETE CASCADE,
    PRIMARY KEY (track_id, person_id)
);

-- -----------------------------------------------------------------------------
-- Fact tables: performance (musical) and production_credit (non-instrumental)
-- -----------------------------------------------------------------------------
CREATE TABLE performance (
    id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    album_id      text NOT NULL REFERENCES album(id) ON DELETE CASCADE,
    person_id     uuid NOT NULL REFERENCES person(id) ON DELETE CASCADE,
    instrument_id int  NOT NULL REFERENCES instrument(id),
    scope         performance_scope NOT NULL DEFAULT 'all-tracks',
    epistemic     epistemic_label NOT NULL DEFAULT 'obs',
    notes         text,
    UNIQUE (album_id, person_id, instrument_id)
);

CREATE TABLE performance_track (
    performance_id uuid NOT NULL REFERENCES performance(id) ON DELETE CASCADE,
    track_id       uuid NOT NULL REFERENCES track(id) ON DELETE CASCADE,
    PRIMARY KEY (performance_id, track_id)
);

CREATE TABLE performance_session (
    performance_id uuid NOT NULL REFERENCES performance(id) ON DELETE CASCADE,
    session_id     uuid NOT NULL REFERENCES session(id) ON DELETE CASCADE,
    PRIMARY KEY (performance_id, session_id)
);

CREATE TABLE production_credit (
    id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    album_id   text NOT NULL REFERENCES album(id) ON DELETE CASCADE,
    session_id uuid REFERENCES session(id) ON DELETE SET NULL,  -- NULL = whole album
    person_id  uuid NOT NULL REFERENCES person(id) ON DELETE CASCADE,
    role       production_role NOT NULL,
    epistemic  epistemic_label NOT NULL DEFAULT 'obs',
    notes      text,
    UNIQUE (album_id, person_id, role, session_id)
);

-- -----------------------------------------------------------------------------
-- Provenance: one citation row per (source, single fact). FK integrity + 1 CHECK.
-- -----------------------------------------------------------------------------
CREATE TABLE citation (
    id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id            int  NOT NULL REFERENCES source(id) ON DELETE CASCADE,
    album_id             text REFERENCES album(id) ON DELETE CASCADE,
    performance_id       uuid REFERENCES performance(id) ON DELETE CASCADE,
    track_id             uuid REFERENCES track(id) ON DELETE CASCADE,
    production_credit_id uuid REFERENCES production_credit(id) ON DELETE CASCADE,
    locator              text,                          -- 'p.124', 'liner notes', etc.
    CHECK (num_nonnulls(album_id, performance_id, track_id, production_credit_id) = 1)
);

-- -----------------------------------------------------------------------------
-- Indexes
-- -----------------------------------------------------------------------------
CREATE INDEX idx_album_year         ON album(year);
CREATE INDEX idx_album_label        ON album(label_id);
CREATE INDEX idx_album_style        ON album(style_primary_id);
CREATE INDEX idx_album_canon        ON album(canon_status);
CREATE INDEX idx_session_album      ON session(album_id);
CREATE INDEX idx_session_date       ON session(session_date);
CREATE INDEX idx_track_album        ON track(album_id);
CREATE INDEX idx_track_session      ON track(session_id);
CREATE INDEX idx_perf_album         ON performance(album_id);
CREATE INDEX idx_perf_person        ON performance(person_id);
CREATE INDEX idx_perf_instrument    ON performance(instrument_id);
CREATE INDEX idx_prodcredit_person  ON production_credit(person_id);
CREATE INDEX idx_prodcredit_album   ON production_credit(album_id);
CREATE INDEX idx_prodcredit_role    ON production_credit(role);
CREATE INDEX idx_citation_source    ON citation(source_id);

-- Vector similarity (HNSW, cosine). Build after embeddings are populated.
CREATE INDEX idx_album_embedding  ON album  USING hnsw (embedding vector_cosine_ops);
CREATE INDEX idx_person_embedding ON person USING hnsw (embedding vector_cosine_ops);

-- =============================================================================
-- READ CONTRACT — views
-- =============================================================================

-- Album browse card
CREATE VIEW v_album_card AS
SELECT a.id, a.title, a.artist_name, a.year,
       l.name AS label, s.display_name AS style_primary,
       a.canon_status, a.canon_tier,
       (SELECT count(*) FROM track t WHERE t.album_id = a.id)       AS track_count,
       (SELECT count(*) FROM performance p WHERE p.album_id = a.id) AS personnel_count
FROM album a
LEFT JOIN label l ON l.id = a.label_id
LEFT JOIN style s ON s.id = a.style_primary_id;

-- Flattened album personnel (album × person × instrument)
CREATE VIEW v_album_personnel AS
SELECT a.id AS album_id, a.title, pe.id AS person_id, pe.canonical_name,
       i.name AS instrument, i.family, p.scope, p.epistemic
FROM performance p
JOIN album a      ON a.id = p.album_id
JOIN person pe    ON pe.id = p.person_id
JOIN instrument i ON i.id = p.instrument_id;

-- Album detail header (one row per album with aggregates)
CREATE VIEW v_album_detail AS
SELECT a.*, l.name AS label_name, s.display_name AS style_primary_name,
       lead.canonical_name AS leader_name
FROM album a
LEFT JOIN label l   ON l.id = a.label_id
LEFT JOIN style s   ON s.id = a.style_primary_id
LEFT JOIN person lead ON lead.id = a.leader_person_id;

-- Track-level personnel (track × person), explicit selected-tracks + implied all-tracks
CREATE VIEW v_track_personnel AS
SELECT t.album_id, t.id AS track_id, t.title AS track_title, t.track_number,
       pe.id AS person_id, pe.canonical_name, i.name AS instrument, p.epistemic
FROM track t
JOIN performance p     ON p.album_id = t.album_id
JOIN person pe         ON pe.id = p.person_id
JOIN instrument i      ON i.id = p.instrument_id
WHERE p.scope = 'all-tracks'
   OR EXISTS (SELECT 1 FROM performance_track pt
              WHERE pt.performance_id = p.id AND pt.track_id = t.id);

-- Musician -> albums (any role: performer)
CREATE VIEW v_musician_albums AS
SELECT pe.id AS person_id, pe.canonical_name, a.id AS album_id, a.title, a.year,
       string_agg(DISTINCT i.name, ', ' ORDER BY i.name) AS instruments
FROM person pe
JOIN performance p ON p.person_id = pe.id
JOIN album a       ON a.id = p.album_id
JOIN instrument i  ON i.id = p.instrument_id
GROUP BY pe.id, pe.canonical_name, a.id, a.title, a.year;

-- Musician timeline (person x session date x album)
CREATE VIEW v_musician_timeline AS
SELECT DISTINCT pe.id AS person_id, pe.canonical_name,
       se.session_date, a.id AS album_id, a.title
FROM person pe
JOIN performance p          ON p.person_id = pe.id
JOIN performance_session ps ON ps.performance_id = p.id
JOIN session se             ON se.id = ps.session_id
JOIN album a                ON a.id = se.album_id
WHERE se.session_date IS NOT NULL;

-- Engineer (or any production role) -> sessions -> albums
CREATE VIEW v_engineer_sessions AS
SELECT pe.id AS person_id, pe.canonical_name, pc.role,
       a.id AS album_id, a.title, se.session_date
FROM production_credit pc
JOIN person pe   ON pe.id = pc.person_id
JOIN album a     ON a.id = pc.album_id
LEFT JOIN session se ON se.id = pc.session_id;

-- Compositions by person across the canon
CREATE VIEW v_composer_works AS
SELECT pe.id AS person_id, pe.canonical_name,
       t.album_id, a.title AS album_title, t.title AS track_title
FROM track_composer tc
JOIN person pe ON pe.id = tc.person_id
JOIN track t   ON t.id = tc.track_id
JOIN album a   ON a.id = t.album_id;

-- Sideman co-occurrence network: ordered person pairs sharing >=1 album, weighted
CREATE VIEW v_sideman_network AS
SELECT p1.person_id AS person_a, p2.person_id AS person_b,
       count(DISTINCT p1.album_id) AS shared_albums
FROM performance p1
JOIN performance p2 ON p1.album_id = p2.album_id AND p1.person_id < p2.person_id
GROUP BY p1.person_id, p2.person_id;

-- =============================================================================
-- Six degrees of McCoy Tyner — shortest collaboration path between two people.
-- Returns the degree of separation (0 = same person, 1 = shared an album, ...).
-- =============================================================================
CREATE OR REPLACE FUNCTION fn_degrees_between(person_a uuid, person_b uuid)
RETURNS int LANGUAGE sql STABLE AS $$
    WITH RECURSIVE bfs(person_id, depth) AS (
        SELECT person_a, 0
        UNION
        SELECT CASE WHEN p2.person_id = b.person_id THEN p1.person_id
                    ELSE p2.person_id END,
               b.depth + 1
        FROM bfs b
        JOIN performance pa ON pa.person_id = b.person_id
        JOIN performance p1 ON p1.album_id = pa.album_id
        JOIN performance p2 ON p2.album_id = pa.album_id
        WHERE b.depth < 6
          AND (p1.person_id = b.person_id OR p2.person_id = b.person_id)
    )
    SELECT min(depth) FROM bfs WHERE person_id = person_b;
$$;

-- Embedding source views (feed the Phase 4 build that composes search_document text)
CREATE VIEW v_album_search_source AS
SELECT a.id AS album_id,
       a.title, a.artist_name, a.year,
       l.name AS label, s.display_name AS style,
       string_agg(DISTINCT pe.canonical_name || ' (' || i.name || ')', ', ') AS personnel,
       a.notes
FROM album a
LEFT JOIN label l       ON l.id = a.label_id
LEFT JOIN style s       ON s.id = a.style_primary_id
LEFT JOIN performance p ON p.album_id = a.id
LEFT JOIN person pe     ON pe.id = p.person_id
LEFT JOIN instrument i  ON i.id = p.instrument_id
GROUP BY a.id, a.title, a.artist_name, a.year, l.name, s.display_name, a.notes;

CREATE VIEW v_person_search_source AS
SELECT pe.id AS person_id, pe.canonical_name,
       string_agg(DISTINCT i.name, ', ')       AS instruments,
       string_agg(DISTINCT a.title, ', ')      AS albums,
       min(a.year) AS first_year, max(a.year)  AS last_year,
       pe.notes
FROM person pe
LEFT JOIN performance p ON p.person_id = pe.id
LEFT JOIN instrument i  ON i.id = p.instrument_id
LEFT JOIN album a       ON a.id = p.album_id
GROUP BY pe.id, pe.canonical_name, pe.notes;

COMMIT;

-- =============================================================================
-- Roles (run once, outside the schema transaction, at Phase 4). Namespaced so
-- they survive DROP SCHEMA, per database-conventions.md.
-- =============================================================================
-- CREATE ROLE _jazzcanon_role LOGIN PASSWORD '<set-in-vault>';
-- CREATE ROLE _jazzcanon_ro   LOGIN PASSWORD '<set-in-vault>';
-- GRANT USAGE ON SCHEMA _jazzcanon TO _jazzcanon_role, _jazzcanon_ro;
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA _jazzcanon TO _jazzcanon_role;
-- GRANT SELECT ON ALL TABLES IN SCHEMA _jazzcanon TO _jazzcanon_ro;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA _jazzcanon GRANT SELECT ON TABLES TO _jazzcanon_ro;
