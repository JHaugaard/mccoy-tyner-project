#!/usr/bin/env python3
"""
Phase 4 D2 — canon-draft.json → _jazzcanon schema on vps8-core (port 5433).

Run (pipe JSON via stdin so postgres user can read it):
  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/ingest.py [--dry-run] < data/canon-draft.json

Idempotent: ON CONFLICT DO NOTHING on all tables with natural unique constraints;
session/production_credit use SELECT-before-INSERT where constraints can't cover NULLs.
"""

import json, re, sys, uuid
import psycopg2
from psycopg2.extras import execute_values

DRY_RUN = "--dry-run" in sys.argv

# ── Vocabulary ────────────────────────────────────────────────────────────────

CANONICAL_INSTRUMENTS = {
    "trumpet":            "brass",
    "cornet":             "brass",
    "flugelhorn":         "brass",
    "trombone":           "brass",
    "valve trombone":     "brass",
    "bass trombone":      "brass",
    "French horn":        "brass",
    "tuba":               "brass",
    "euphonium":          "brass",
    "tenor saxophone":    "woodwinds",
    "alto saxophone":     "woodwinds",
    "soprano saxophone":  "woodwinds",
    "baritone saxophone": "woodwinds",
    "clarinet":           "woodwinds",
    "bass clarinet":      "woodwinds",
    "flute":              "woodwinds",
    "piccolo":            "woodwinds",
    "bassoon":            "woodwinds",
    "oboe":               "woodwinds",
    "piano":              "keyboards",
    "electric piano":     "keyboards",
    "organ (hammond)":    "keyboards",
    "guitar":             "strings",
    "electric guitar":    "strings",
    "double bass":        "strings",
    "electric bass":      "strings",
    "violin":             "strings",
    "viola":              "strings",
    "cello":              "strings",
    "harp":               "strings",
    "drums":              "percussion",
    "vibraphone":         "percussion",
    "congas":             "percussion",
    "percussion":         "percussion",
    "marimba":            "percussion",
    "voice":              "other",
    "conductor":          "other",
    "arranger":           "other",
}

# Entries that are NOT instruments — skip silently, no warning
NON_INSTRUMENTS = {"liner notes", "liner-notes", "notes"}

INSTRUMENT_NORMALIZE = {
    "bass":               "double bass",
    "upright bass":       "double bass",
    "contrabass":         "double bass",
    "string bass":        "double bass",
    "acoustic bass":      "double bass",
    "bass guitar":        "electric bass",
    "electric bass guitar": "electric bass",
    "organ":              "organ (hammond)",
    "hammond organ":      "organ (hammond)",
    "hammond b3":         "organ (hammond)",
    "b3":                 "organ (hammond)",
    "fender rhodes":      "electric piano",
    "rhodes":             "electric piano",
    "tenor sax":          "tenor saxophone",
    "alto sax":           "alto saxophone",
    "soprano sax":        "soprano saxophone",
    "baritone sax":       "baritone saxophone",
    "bari sax":           "baritone saxophone",
    "vocals":             "voice",
    "vocal":              "voice",
    "horn":               "French horn",
    "french horn":        "French horn",
}

STYLES = {
    "hard-bop":   ("Hard Bop",   "Hard-driving post-bebop with blues and gospel roots"),
    "soul-jazz":  ("Soul Jazz",  "Blues and gospel inflected hard bop variant"),
    "cool-jazz":  ("Cool Jazz",  "Relaxed, lyrical post-bebop from the late 1940s–50s"),
    "modal-jazz": ("Modal Jazz", "Improvisation over modal scales rather than chord changes"),
    "post-bop":   ("Post-Bop",   "Eclectic post-1960 jazz drawing from multiple traditions"),
}

PRIORITY_MAP = {
    "must_have": "must_have",
    "strong":    "strong",
    "consider":  "consider",
    "standard":  "strong",   # 'standard' not in ENUM; map to closest
}

EPISTEMIC_VALUES = {"obs", "inf", "unk"}

# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(s):
    if not s:
        return ""
    s = s.lower().strip()
    s = re.sub(r"['\"\.,!?&/]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]

def null(v):
    """Return None for absent/FILL-REQUIRED values, else v."""
    return None if v in (None, "", "FILL-REQUIRED", "null", "NULL") else v

def ep(v, default="obs"):
    """Coerce epistemic value to ENUM string or default."""
    return v if v in EPISTEMIC_VALUES else default

def safe_date(v):
    """Return ISO date string (YYYY-MM-DD) or None if unparseable."""
    if not v:
        return None
    s = str(v).strip()[:10]
    # Accept only YYYY-MM-DD
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    return None

def normalize_instruments(raw):
    """Return list of canonical instrument names, splitting on '/' and ','.
    Skips non-instruments silently. Returns [] if nothing maps."""
    if not raw:
        return []
    parts = re.split(r"[/,]", raw)
    results = []
    for part in parts:
        n = part.strip()
        if not n:
            continue
        if n.lower() in NON_INSTRUMENTS:
            continue
        # Try lowercase normalizer first, then case-sensitive canonical lookup
        canonical = INSTRUMENT_NORMALIZE.get(n.lower(), n.lower())
        # Also try title-case for things like 'French horn'
        if canonical not in CANONICAL_INSTRUMENTS:
            canonical = INSTRUMENT_NORMALIZE.get(n, n)
        if canonical in CANONICAL_INSTRUMENTS:
            if canonical not in results:
                results.append(canonical)
    return results

def parse_studio(s):
    """'Van Gelder Studio, Hackensack, NJ' → ('Van Gelder Studio', 'Hackensack, NJ')"""
    if not s or null(s) is None:
        return None, None
    parts = [p.strip() for p in s.split(",", 1)]
    return parts[0], (parts[1] if len(parts) > 1 else None)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    albums = [r for r in data["albums"] if r.get("include") is True]
    print(f"Loaded {len(albums)} active albums")
    if DRY_RUN:
        print("DRY RUN — will roll back")

    conn = psycopg2.connect(port=5433, dbname="postgres")
    cur = conn.cursor()
    cur.execute("SET search_path TO _jazzcanon, public")

    unknown_instruments = set()
    warnings = []

    # ── 1. Vocabulary tables ─────────────────────────────────────────────────
    print("\n── Seeding vocabulary ──")

    for code, (name, desc) in STYLES.items():
        cur.execute("""
            INSERT INTO style (code, display_name, description) VALUES (%s,%s,%s)
            ON CONFLICT (code) DO NOTHING
        """, (code, name, desc))

    for inst, family in CANONICAL_INSTRUMENTS.items():
        cur.execute("""
            INSERT INTO instrument (name, family) VALUES (%s, %s::instrument_family)
            ON CONFLICT (name) DO NOTHING
        """, (inst, family))

    label_names = sorted({r["label"] for r in albums if null(r.get("label"))})
    for lname in label_names:
        cur.execute("""
            INSERT INTO label (name, name_slug) VALUES (%s,%s)
            ON CONFLICT (name) DO NOTHING
        """, (lname, slugify(lname)))

    studio_map = {}  # name → (name, city)
    for r in albums:
        pr = r.get("personnel_record") or {}
        sname, scity = parse_studio(pr.get("studio"))
        if sname:
            studio_map[sname] = (sname, scity)
    for sname, (_, scity) in sorted(studio_map.items()):
        cur.execute("""
            INSERT INTO studio (name, city, name_slug) VALUES (%s,%s,%s)
            ON CONFLICT (name_slug) DO NOTHING
        """, (sname, scity, slugify(sname)))

    print(f"  {len(STYLES)} styles  {len(CANONICAL_INSTRUMENTS)} instruments  "
          f"{len(label_names)} labels  {len(studio_map)} studios")

    # ── 2. Person registry ───────────────────────────────────────────────────
    print("\n── Resolving persons ──")

    person_reg = {}   # canonical_name → uuid str
    variant_reg = {}  # variant_name → canonical_name

    def get_or_create_person(name, variants=None):
        if not name:
            return None
        name = name.strip()
        # Check direct or variant match
        if name in person_reg:
            return person_reg[name]
        if name in variant_reg:
            return person_reg[variant_reg[name]]

        pid = str(uuid.uuid4())
        base_slug = slugify(name)
        slug = base_slug
        attempt = 1
        while True:
            cur.execute("""
                INSERT INTO person (id, canonical_name, sort_name, name_slug)
                VALUES (%s,%s,%s,%s)
                ON CONFLICT (canonical_name) DO UPDATE SET name_slug = person.name_slug
                RETURNING id, name_slug
            """, (pid, name, name, slug))
            row = cur.fetchone()
            actual_id = str(row[0])
            person_reg[name] = actual_id

            if variants:
                for v in (variants or []):
                    v = v.strip() if v else ""
                    if v and v != name:
                        variant_reg[v] = name
                        cur.execute("""
                            INSERT INTO person_name_variant (person_id, variant_name)
                            VALUES (%s,%s) ON CONFLICT (person_id, variant_name) DO NOTHING
                        """, (actual_id, v))
            return actual_id

    for r in albums:
        pr = r.get("personnel_record") or {}
        for p in pr.get("personnel") or []:
            get_or_create_person(p.get("name"), p.get("name_variants") or [])
        for field in ("producer", "engineer"):
            get_or_create_person(null(pr.get(field)))
        for t in pr.get("tracks") or []:
            for c in t.get("composers") or []:
                get_or_create_person(null(c))

    print(f"  {len(person_reg)} unique persons")

    # ── 3. Albums ────────────────────────────────────────────────────────────
    print("\n── Ingesting albums ──")

    def style_id(code):
        if not code:
            return None
        cur.execute("SELECT id FROM style WHERE code = %s", (code,))
        row = cur.fetchone()
        return row[0] if row else None

    def label_id(name):
        if not null(name):
            return None
        cur.execute("SELECT id FROM label WHERE name = %s", (name,))
        row = cur.fetchone()
        return row[0] if row else None

    def studio_id(studio_str):
        sname, _ = parse_studio(studio_str)
        if not sname:
            return None
        cur.execute("SELECT id FROM studio WHERE name_slug = %s", (slugify(sname),))
        row = cur.fetchone()
        return row[0] if row else None

    def instr_ids(raw):
        """Return list of (instrument_id, canonical_name) for a raw instrument string."""
        canonicals = normalize_instruments(raw)
        if not canonicals and raw and raw.strip().lower() not in NON_INSTRUMENTS:
            unknown_instruments.add(raw)
        result = []
        for canonical in canonicals:
            cur.execute("SELECT id FROM instrument WHERE name = %s", (canonical,))
            row = cur.fetchone()
            if row:
                result.append((row[0], canonical))
        return result

    def find_leader(artist_str, personnel):
        """Match artist display name to a person in the personnel list."""
        if not artist_str:
            return None
        artist_lower = artist_str.lower()
        for p in personnel:
            name = (p.get("name") or "").strip()
            if name and name.lower() in artist_lower:
                return person_reg.get(name)
        return None

    counts = dict(albums=0, sessions=0, tracks=0, track_composers=0,
                  performances=0, perf_tracks=0, prod_credits=0, art_rows=0)

    for r in albums:
        aid = r["id"]
        pr  = r.get("personnel_record") or {}
        personnel = pr.get("personnel") or []

        leader_id = find_leader(r.get("artist", ""), personnel)
        style_code = r.get("style_primary", "")
        priority   = PRIORITY_MAP.get(r.get("priority"), None)
        mbid       = null(pr.get("musicbrainz_release_group_mbid"))
        apple_id   = null(pr.get("apple_album_id"))
        if apple_id is not None:
            apple_id = str(apple_id)
        catalog    = null(r.get("catalog_number")) or ""
        rec_dates  = pr.get("recording_dates") or []
        dates_text = ", ".join(str(d) for d in rec_dates if d) or None

        cur.execute("""
            INSERT INTO album (
                id, title, artist_name, leader_person_id, year, label_id,
                catalog_number, consensus, style_primary_id,
                recording_dates_text, multi_session,
                musicbrainz_release_group_mbid, apple_album_id,
                canon_status, priority, inclusion_rationale,
                epistemic, notes
            ) VALUES (
                %s,%s,%s,%s,%s,%s,
                %s,%s,%s,
                %s,%s,
                %s,%s,
                'included'::canon_status, %s::priority_label, %s,
                %s::epistemic_label, %s
            )
            ON CONFLICT (id) DO UPDATE SET
                musicbrainz_release_group_mbid = EXCLUDED.musicbrainz_release_group_mbid,
                apple_album_id                 = EXCLUDED.apple_album_id,
                catalog_number                 = EXCLUDED.catalog_number,
                consensus                      = EXCLUDED.consensus,
                updated_at                     = now()
        """, (
            aid,
            r.get("album", ""),
            r.get("artist", ""),
            leader_id,
            r.get("year"),
            label_id(r.get("label")),
            catalog,
            r.get("consensus"),
            style_id(style_code),
            dates_text,
            pr.get("multi_session", False),
            mbid,
            apple_id,
            priority,
            null(r.get("rationale")),
            ep(r.get("epistemic")),
            null(pr.get("notes")),
        ))
        counts["albums"] += 1

        # Secondary styles
        for tag in r.get("style_tags") or []:
            sid = style_id(tag)
            if sid:
                cur.execute("""
                    INSERT INTO album_style (album_id, style_id, is_primary)
                    VALUES (%s,%s,false) ON CONFLICT (album_id, style_id) DO NOTHING
                """, (aid, sid))

        # ── Sessions ─────────────────────────────────────────────────────────
        # Check if sessions already exist for this album (idempotency)
        cur.execute("SELECT COUNT(*) FROM session WHERE album_id = %s", (aid,))
        existing_sessions = cur.fetchone()[0]

        date_to_session = {}   # date_str → session_id
        primary_session_id = None

        if existing_sessions == 0:
            # Determine session dates: use recording_dates; fall back to single unknown session
            session_dates = rec_dates if rec_dates else [None]
            stid = studio_id(pr.get("studio"))

            for seq, date_val in enumerate(session_dates, start=1):
                sid_uuid = str(uuid.uuid4())
                date_str = safe_date(date_val)
                date_text = str(date_val) if date_val else None
                cur.execute("""
                    INSERT INTO session (id, album_id, session_date, session_date_text, studio_id, sequence, epistemic)
                    VALUES (%s,%s,%s,%s,%s,%s,'obs'::epistemic_label)
                """, (sid_uuid, aid, date_str, date_text, stid, seq))
                if date_str:
                    date_to_session[date_str] = sid_uuid
                    date_to_session[date_text] = sid_uuid  # also index raw text
                if seq == 1:
                    primary_session_id = sid_uuid
                counts["sessions"] += 1
        else:
            # Load existing sessions for track/perf linkage
            cur.execute("SELECT id, session_date::text, sequence FROM session WHERE album_id = %s ORDER BY sequence", (aid,))
            for row in cur.fetchall():
                if row[1]:
                    date_to_session[row[1]] = str(row[0])
                if row[2] == 1:
                    primary_session_id = str(row[0])

        # ── Tracks ────────────────────────────────────────────────────────────
        track_key_to_id = {}   # (track_number, title) → track_id

        for t in pr.get("tracks") or []:
            tnum  = t.get("track_number")
            title = t.get("title", "")
            tdate = safe_date(t.get("session_date"))
            sess  = date_to_session.get(tdate, primary_session_id)

            dur = t.get("duration") or t.get("duration_text")

            cur.execute("""
                INSERT INTO track (id, album_id, session_id, title, track_number, side,
                                   duration_text, bonus_track, alternate_take, epistemic_track)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::epistemic_label)
                ON CONFLICT (album_id, track_number, alternate_take) DO UPDATE SET
                    title = EXCLUDED.title
                RETURNING id
            """, (
                str(uuid.uuid4()), aid, sess, title, tnum,
                t.get("side"), dur,
                t.get("bonus_track", False),
                t.get("alternate_take", False),
                ep(t.get("epistemic_track")),
            ))
            actual_tid = str(cur.fetchone()[0])
            track_key_to_id[(tnum, title)] = actual_tid
            counts["tracks"] += 1

            for composer in t.get("composers") or []:
                cid = person_reg.get(composer) if composer else None
                if cid:
                    cur.execute("""
                        INSERT INTO track_composer (track_id, person_id)
                        VALUES (%s,%s) ON CONFLICT (track_id, person_id) DO NOTHING
                    """, (actual_tid, cid))
                    counts["track_composers"] += 1

        # ── Performances ──────────────────────────────────────────────────────
        # Build a name→track_ids map for selected-tracks linkage
        track_name_set = {title: tid for (_, title), tid in track_key_to_id.items()}

        for p in personnel:
            pname = (p.get("name") or "").strip()
            pid   = person_reg.get(pname)
            if not pid:
                warnings.append(f"{aid}: person not in registry: {pname!r}")
                continue

            instrument_list = instr_ids(p.get("instrument"))
            if not instrument_list:
                raw_inst = p.get("instrument", "")
                if raw_inst and raw_inst.strip().lower() not in NON_INSTRUMENTS:
                    warnings.append(f"{aid}: unmapped instrument {raw_inst!r} for {pname}")
                continue

            scope = p.get("scope", "all-tracks")
            if scope not in ("all-tracks", "selected-tracks", "unknown"):
                scope = "unknown"

            for iid, _ in instrument_list:
                cur.execute("""
                    INSERT INTO performance (id, album_id, person_id, instrument_id, scope, epistemic)
                    VALUES (%s,%s,%s,%s,%s::performance_scope,%s::epistemic_label)
                    ON CONFLICT (album_id, person_id, instrument_id) DO NOTHING
                    RETURNING id
                """, (str(uuid.uuid4()), aid, pid, iid, scope, ep(p.get("epistemic"))))
                perf_row = cur.fetchone()
                if not perf_row:
                    continue
                perf_id = str(perf_row[0])
                counts["performances"] += 1

                # Link selected-tracks performer to their specific tracks
                if scope == "selected-tracks" and p.get("tracks"):
                    for track_ref in (p["tracks"] or []):
                        tid = track_name_set.get(track_ref) or track_key_to_id.get((None, track_ref))
                        if tid:
                            cur.execute("""
                                INSERT INTO performance_track (performance_id, track_id)
                                VALUES (%s,%s) ON CONFLICT (performance_id, track_id) DO NOTHING
                            """, (perf_id, tid))
                            counts["perf_tracks"] += 1

        # ── Production credits ────────────────────────────────────────────────
        for field, role in (("producer", "producer"), ("engineer", "engineer")):
            val = null(pr.get(field))
            if not val:
                continue
            cred_person_id = person_reg.get(val)
            if not cred_person_id:
                continue
            # Unique constraint can't cover NULL session_id — SELECT first
            cur.execute("""
                SELECT id FROM production_credit
                WHERE album_id=%s AND person_id=%s AND role=%s::production_role AND session_id IS NULL
            """, (aid, cred_person_id, role))
            if not cur.fetchone():
                ep_prod = ep(null(pr.get("epistemic_production")))
                cur.execute("""
                    INSERT INTO production_credit (id, album_id, person_id, role, epistemic)
                    VALUES (%s,%s,%s,%s::production_role,%s::epistemic_label)
                """, (str(uuid.uuid4()), aid, cred_person_id, role, ep_prod))
                counts["prod_credits"] += 1

        # ── Cover art ─────────────────────────────────────────────────────────
        cover = pr.get("cover_art")
        if isinstance(cover, list):
            for ca in cover:
                url = null(ca.get("url") or ca.get("source_url"))
                if not url:
                    continue
                src = ca.get("source", "cover-art-archive")
                if src not in ("cover-art-archive", "itunes", "discogs", "wikimedia", "manual", "other"):
                    src = "other"
                cur.execute("""
                    INSERT INTO album_art (id, album_id, role, source, source_url, is_primary, epistemic)
                    VALUES (%s,%s,'front'::art_role,%s::art_source,%s,true,%s::epistemic_label)
                    ON CONFLICT (album_id, role, source) DO NOTHING
                """, (str(uuid.uuid4()), aid, src, url, ep(ca.get("epistemic"), "inf")))
                counts["art_rows"] += 1

        print(f"  ✓  {r['artist'][:35]:35s} | {r['album'][:30]:30s} | "
              f"{len(personnel)}p {len(pr.get('tracks') or [])}t")

    # ── 4. Seed collection ───────────────────────────────────────────────────
    print("\n── Seeding collection ──")
    cur.execute("""
        INSERT INTO collection (slug, name, description)
        VALUES ('the-jazz-canon', 'The Jazz Canon',
                'Founding 100-album canon: post-bebop through pre-Fusion, 1949–1972. '
                'Compiled 2026 via Claude Code + Kimi Code A/B research.')
        ON CONFLICT (slug) DO NOTHING
    """)
    cur.execute("SELECT id FROM collection WHERE slug = 'the-jazz-canon'")
    coll_id = cur.fetchone()[0]

    for pos, r in enumerate(albums, start=1):
        cur.execute("""
            INSERT INTO album_collection (album_id, collection_id, position)
            VALUES (%s,%s,%s) ON CONFLICT (album_id, collection_id) DO NOTHING
        """, (r["id"], coll_id, pos))

    print(f"  'the-jazz-canon' seeded with {len(albums)} albums")

    # ── 5. Commit or rollback ────────────────────────────────────────────────
    if DRY_RUN:
        conn.rollback()
        print("\nDRY RUN — rolled back, nothing written to DB")
    else:
        conn.commit()
        print("\nCommitted.")

    # ── 6. Summary ───────────────────────────────────────────────────────────
    print("\n── Summary ──")
    print(f"  albums         : {counts['albums']}")
    print(f"  sessions       : {counts['sessions']}")
    print(f"  tracks         : {counts['tracks']}")
    print(f"  track composers: {counts['track_composers']}")
    print(f"  performances   : {counts['performances']}")
    print(f"  perf→track     : {counts['perf_tracks']}")
    print(f"  prod credits   : {counts['prod_credits']}")
    print(f"  cover art rows : {counts['art_rows']}")
    print(f"  persons        : {len(person_reg)}")

    if unknown_instruments:
        print(f"\n── Unknown instruments (skipped) ──")
        for i in sorted(unknown_instruments):
            print(f"  {i!r}")

    if warnings:
        print(f"\n── Warnings ({len(warnings)}) ──")
        for w in warnings[:30]:
            print(f"  {w}")
        if len(warnings) > 30:
            print(f"  ... +{len(warnings)-30} more")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
