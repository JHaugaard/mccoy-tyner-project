#!/usr/bin/env python3
"""
Data quality sweep: Q1 person identity resolution, Q2 Cannonball merge, Q3 date verify.

Run as:
  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/data-quality-sweep.py
"""

import difflib
import re
import json
import urllib.request
import psycopg2

OLLAMA_URL = "http://172.18.0.1:11435/api/embeddings"
OLLAMA_MODEL = "nomic-embed-text"


def get_embedding(text):
    payload = json.dumps({"model": OLLAMA_MODEL, "prompt": text}).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data["embedding"]


def vec_to_pg(embedding):
    return "[" + ",".join(f"{x:.8f}" for x in embedding) + "]"


def normalize_name(name):
    """Normalize for comparison: strip quoted nicknames, lowercase, collapse spaces."""
    # Remove content in quotes (nicknames): "Bird", 'Cannonball'
    n = re.sub(r'"[^"]*"', '', name)
    n = re.sub(r"'[^']*'", '', n)
    # Lowercase
    n = n.lower()
    # Strip periods from abbreviations (J.J. → jj)
    n = re.sub(r'\.', '', n)
    # Strip remaining punctuation except spaces and hyphens
    n = re.sub(r"[^a-z0-9\s\-]", '', n)
    # Collapse spaces
    return ' '.join(n.split())


def last_name_token(normalized):
    parts = normalized.split()
    if not parts:
        return ''
    # Skip suffixes
    suffixes = {'jr', 'sr', 'ii', 'iii', 'iv'}
    if len(parts) > 1 and parts[-1] in suffixes:
        return parts[-2]
    return parts[-1]


def first_token(normalized):
    parts = normalized.split()
    return parts[0] if parts else ''


conn = psycopg2.connect(host="/var/run/postgresql", port=5433, dbname="postgres", user="postgres")
cur = conn.cursor()

# ============================================================
# Q3: Verify session_date_text — June Christy Something Cool
# ============================================================
print("=== Q3: Verify session_date_text (June Christy Something Cool) ===")
cur.execute("""
    SELECT id, session_date_text
    FROM _jazzcanon.session
    WHERE album_id = 'june-christy-something-cool-1955'
""")
rows = cur.fetchall()
needs_fix = False
for sid, dtxt in rows:
    # Malformed pattern: YYYY-MM/DD (day without year, e.g. "1953-08/19")
    if dtxt and re.match(r'^\d{4}-\d{2}/\d{2}$', dtxt):
        fixed = dtxt[:7] + '-' + dtxt[8:]  # "1953-08/19" → "1953-08-19"
        cur.execute("UPDATE _jazzcanon.session SET session_date_text = %s WHERE id = %s", (fixed, sid))
        print(f"  FIXED: {dtxt!r} → {fixed!r}")
        needs_fix = True
    else:
        print(f"  OK: {dtxt!r} (valid multi-session range, no fix needed)")
if not needs_fix:
    print("  Nothing to change.")
conn.commit()
print()


# ============================================================
# Q2: Merge Cannonball Adderley duplicate
# ============================================================
print("=== Q2: Merge Cannonball Adderley duplicate ===")
CANNONBALL_CANONICAL = '213b7ac6-98d5-405c-a48b-6736fba41d27'  # Cannonball Adderley (4 albums)
CANNONBALL_DUPE      = '7d454c4d-e867-4943-af64-b9a48440a9c6'  # Julian 'Cannonball' Adderley (1 album)

# What does the dupe own?
cur.execute("""
    SELECT perf.id, perf.album_id, perf.instrument_id, perf.scope, perf.epistemic
    FROM _jazzcanon.performance perf
    WHERE perf.person_id = %s
""", (CANNONBALL_DUPE,))
dupe_perfs = cur.fetchall()
print(f"  Dupe performances to migrate: {len(dupe_perfs)}")

for perf_id, album_id, instr_id, scope, epist in dupe_perfs:
    # Check if canonical already has this (album_id, instrument_id) pair
    cur.execute("""
        SELECT id FROM _jazzcanon.performance
        WHERE person_id = %s AND album_id = %s AND instrument_id = %s
    """, (CANNONBALL_CANONICAL, album_id, instr_id))
    existing = cur.fetchone()
    if existing:
        print(f"  album={album_id}: canonical already has this performance — deleting dupe perf {perf_id}")
        # Re-home any performance_session / performance_track rows to canonical's performance
        cur.execute("UPDATE _jazzcanon.performance_session SET performance_id = %s WHERE performance_id = %s",
                    (existing[0], perf_id))
        cur.execute("UPDATE _jazzcanon.performance_track SET performance_id = %s WHERE performance_id = %s",
                    (existing[0], perf_id))
        cur.execute("DELETE FROM _jazzcanon.performance WHERE id = %s", (perf_id,))
    else:
        print(f"  album={album_id}: moving performance {perf_id} to canonical")
        cur.execute("UPDATE _jazzcanon.performance SET person_id = %s WHERE id = %s",
                    (CANNONBALL_CANONICAL, perf_id))

# production_credit
cur.execute("SELECT id, album_id, role FROM _jazzcanon.production_credit WHERE person_id = %s",
            (CANNONBALL_DUPE,))
dupe_creds = cur.fetchall()
print(f"  Dupe production credits to migrate: {len(dupe_creds)}")
for cred_id, album_id, role in dupe_creds:
    cur.execute("""
        SELECT id FROM _jazzcanon.production_credit
        WHERE person_id = %s AND album_id = %s AND role = %s
    """, (CANNONBALL_CANONICAL, album_id, role))
    if cur.fetchone():
        cur.execute("DELETE FROM _jazzcanon.production_credit WHERE id = %s", (cred_id,))
    else:
        cur.execute("UPDATE _jazzcanon.production_credit SET person_id = %s WHERE id = %s",
                    (CANNONBALL_CANONICAL, cred_id))

# track_composer
cur.execute("SELECT track_id FROM _jazzcanon.track_composer WHERE person_id = %s", (CANNONBALL_DUPE,))
dupe_tc = cur.fetchall()
print(f"  Dupe track_composer rows to migrate: {len(dupe_tc)}")
for (track_id,) in dupe_tc:
    cur.execute("SELECT 1 FROM _jazzcanon.track_composer WHERE person_id = %s AND track_id = %s",
                (CANNONBALL_CANONICAL, track_id))
    if cur.fetchone():
        cur.execute("DELETE FROM _jazzcanon.track_composer WHERE person_id = %s AND track_id = %s",
                    (CANNONBALL_DUPE, track_id))
    else:
        cur.execute("UPDATE _jazzcanon.track_composer SET person_id = %s WHERE person_id = %s AND track_id = %s",
                    (CANNONBALL_CANONICAL, CANNONBALL_DUPE, track_id))

# album.leader_person_id
cur.execute("UPDATE _jazzcanon.album SET leader_person_id = %s WHERE leader_person_id = %s",
            (CANNONBALL_CANONICAL, CANNONBALL_DUPE))
print(f"  Leader references updated: {cur.rowcount}")

# Add name variant
cur.execute("""
    INSERT INTO _jazzcanon.person_name_variant (person_id, variant_name, source_note)
    VALUES (%s, %s, 'legal name; merged duplicate record 2026-06-26')
    ON CONFLICT DO NOTHING
""", (CANNONBALL_CANONICAL, "Julian 'Cannonball' Adderley"))
print("  Added name variant: Julian 'Cannonball' Adderley")

cur.execute("""
    INSERT INTO _jazzcanon.person_name_variant (person_id, variant_name, source_note)
    VALUES (%s, %s, 'birth name; merged duplicate record 2026-06-26')
    ON CONFLICT DO NOTHING
""", (CANNONBALL_CANONICAL, "Julian Edwin Adderley"))
print("  Added name variant: Julian Edwin Adderley")

# Delete dupe person
cur.execute("DELETE FROM _jazzcanon.person WHERE id = %s", (CANNONBALL_DUPE,))
print(f"  Deleted dupe person record: Julian 'Cannonball' Adderley")

conn.commit()
print("  Q2 done.")
print()


# ============================================================
# Q1: Full person identity resolution sweep
# ============================================================
print("=== Q1: Person identity resolution sweep ===")

cur.execute("SELECT id, canonical_name FROM _jazzcanon.person ORDER BY canonical_name")
all_persons = cur.fetchall()
print(f"  Total persons: {len(all_persons)}")

# Build normalized lookup
persons = []
for pid, name in all_persons:
    norm = normalize_name(name)
    last = last_name_token(norm)
    first = first_token(norm)
    persons.append({
        'id': pid,
        'name': name,
        'norm': norm,
        'last': last,
        'first': first,
    })

# Group by last name token
from collections import defaultdict
by_last = defaultdict(list)
for p in persons:
    if p['last']:
        by_last[p['last']].append(p)

auto_merge_pairs = []   # (canonical, dupe, reason)
review_pairs = []       # (p1, p2, ratio, reason)

SUFFIXES = {'jr', 'sr', 'ii', 'iii', 'iv'}

for last_name, group in by_last.items():
    if len(group) < 2:
        continue

    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            a, b = group[i], group[j]

            # Skip if both are suffixed AND suffixes differ (different generations)
            a_suffix = 'jr' in a['norm'] or 'sr' in a['norm']
            b_suffix = 'jr' in b['norm'] or 'sr' in b['norm']
            if a_suffix != b_suffix:
                continue  # One has Jr, other doesn't — different people

            ratio = difflib.SequenceMatcher(None, a['norm'], b['norm']).ratio()

            # Pass 1: exact normalized match
            if a['norm'] == b['norm']:
                # Keep the one with more performances
                auto_merge_pairs.append((a, b, 'exact-normalized-match'))
                continue

            # Pass 2: containment (one name is a sub-sequence of the other, same last name)
            # e.g., "john coltrane" contained in "john william coltrane"
            shorter, longer = (a, b) if len(a['norm']) < len(b['norm']) else (b, a)
            if shorter['norm'] in longer['norm'] and ratio > 0.75:
                auto_merge_pairs.append((shorter, longer, f'containment (ratio={ratio:.2f})'))
                continue

            # Pass 3: very high similarity (same last name, ratio > 0.94)
            # Threshold is intentionally strict — short jazz names with shared last names
            # (e.g. "Sam Jones" / "Isham Jones") score 0.90 and must NOT be merged.
            if ratio > 0.94:
                # First names must be clearly similar (avoids "Jo Jones" vs "Hank Jones")
                first_sim = difflib.SequenceMatcher(None, a['first'], b['first']).ratio()
                if first_sim > 0.65:
                    auto_merge_pairs.append((a, b, f'high-similarity (ratio={ratio:.2f})'))
                    continue

            # Medium similarity → review list
            if ratio > 0.72:
                review_pairs.append((a, b, ratio))

print(f"  Auto-merge candidates: {len(auto_merge_pairs)}")
print(f"  Review candidates: {len(review_pairs)}")
print()

# Perform auto-merges
merged_canonical_ids = set()

if auto_merge_pairs:
    print("  --- Auto-merges ---")
    for canonical_p, dupe_p, reason in auto_merge_pairs:
        # Decide which is canonical: keep the one with more performances
        cur.execute("""
            SELECT COUNT(*) FROM _jazzcanon.performance WHERE person_id = %s
        """, (canonical_p['id'],))
        count_a = cur.fetchone()[0]
        cur.execute("""
            SELECT COUNT(*) FROM _jazzcanon.performance WHERE person_id = %s
        """, (dupe_p['id'],))
        count_b = cur.fetchone()[0]

        if count_b > count_a:
            canonical_p, dupe_p = dupe_p, canonical_p

        print(f"  MERGE: {dupe_p['name']!r} → {canonical_p['name']!r} ({reason})")

        # Move performances
        cur.execute("""
            UPDATE _jazzcanon.performance SET person_id = %s
            WHERE person_id = %s
              AND (album_id, instrument_id) NOT IN (
                  SELECT album_id, instrument_id FROM _jazzcanon.performance WHERE person_id = %s
              )
        """, (canonical_p['id'], dupe_p['id'], canonical_p['id']))
        perf_moved = cur.rowcount
        # Delete any remaining dupe performances (exact duplicates)
        cur.execute("DELETE FROM _jazzcanon.performance WHERE person_id = %s", (dupe_p['id'],))
        perf_deleted = cur.rowcount

        # Move production credits
        cur.execute("""
            UPDATE _jazzcanon.production_credit SET person_id = %s
            WHERE person_id = %s
              AND (album_id, role) NOT IN (
                  SELECT album_id, role FROM _jazzcanon.production_credit WHERE person_id = %s
              )
        """, (canonical_p['id'], dupe_p['id'], canonical_p['id']))
        cur.execute("DELETE FROM _jazzcanon.production_credit WHERE person_id = %s", (dupe_p['id'],))

        # Move track_composer
        cur.execute("""
            UPDATE _jazzcanon.track_composer SET person_id = %s
            WHERE person_id = %s
              AND track_id NOT IN (
                  SELECT track_id FROM _jazzcanon.track_composer WHERE person_id = %s
              )
        """, (canonical_p['id'], dupe_p['id'], canonical_p['id']))
        cur.execute("DELETE FROM _jazzcanon.track_composer WHERE person_id = %s", (dupe_p['id'],))

        # Update album leader references
        cur.execute("UPDATE _jazzcanon.album SET leader_person_id = %s WHERE leader_person_id = %s",
                    (canonical_p['id'], dupe_p['id']))

        # Add dupe's name as variant
        cur.execute("""
            INSERT INTO _jazzcanon.person_name_variant (person_id, variant_name, source_note)
            VALUES (%s, %s, 'merged duplicate 2026-06-26')
            ON CONFLICT DO NOTHING
        """, (canonical_p['id'], dupe_p['name']))

        # Delete dupe
        cur.execute("DELETE FROM _jazzcanon.person WHERE id = %s", (dupe_p['id'],))
        print(f"    Perfs moved: {perf_moved}, dupes deleted: {perf_deleted}")

        merged_canonical_ids.add(canonical_p['id'])

    conn.commit()
else:
    print("  No auto-merge candidates found.")

print()

# Report review pairs (no action taken)
if review_pairs:
    print("  --- Review list (no action — manual judgment needed) ---")
    for a, b, ratio in sorted(review_pairs, key=lambda x: -x[2]):
        print(f"  ? {a['name']!r} vs {b['name']!r}  (ratio={ratio:.2f})")
else:
    print("  No review candidates.")

print()


# ============================================================
# Re-embed merged persons (search_document may now include more albums)
# ============================================================
if merged_canonical_ids:
    print("=== Re-embedding merged persons ===")
    for pid in merged_canonical_ids:
        cur.execute("""
            SELECT pe.canonical_name,
                   string_agg(DISTINCT i.name, ', ') AS instruments,
                   string_agg(DISTINCT a.title, ', ') AS albums
            FROM _jazzcanon.person pe
            LEFT JOIN _jazzcanon.performance p ON p.person_id = pe.id
            LEFT JOIN _jazzcanon.instrument i  ON i.id = p.instrument_id
            LEFT JOIN _jazzcanon.album a        ON a.id = p.album_id
            WHERE pe.id = %s
            GROUP BY pe.canonical_name
        """, (pid,))
        row = cur.fetchone()
        if not row:
            continue
        name, instruments, albums = row
        doc_parts = [name]
        if instruments:
            doc_parts.append(f"Plays: {instruments}.")
        if albums:
            doc_parts.append(f"Albums: {albums}.")
        doc = ' '.join(doc_parts)

        emb = get_embedding(doc)
        cur.execute("""
            UPDATE _jazzcanon.person
            SET search_document = %s, embedding = %s::vector, updated_at = now()
            WHERE id = %s
        """, (doc, vec_to_pg(emb), pid))
        print(f"  Re-embedded: {name}")

    conn.commit()
    print()

# Also re-embed Cannonball (Q2 merge added a new album)
print("=== Re-embedding Cannonball Adderley (Q2 merge added Milestones) ===")
cur.execute("""
    SELECT pe.canonical_name,
           string_agg(DISTINCT i.name, ', ') AS instruments,
           string_agg(DISTINCT a.title, ', ') AS albums
    FROM _jazzcanon.person pe
    LEFT JOIN _jazzcanon.performance p ON p.person_id = pe.id
    LEFT JOIN _jazzcanon.instrument i  ON i.id = p.instrument_id
    LEFT JOIN _jazzcanon.album a        ON a.id = p.album_id
    WHERE pe.id = %s
    GROUP BY pe.canonical_name
""", (CANNONBALL_CANONICAL,))
row = cur.fetchone()
if row:
    name, instruments, albums = row
    doc_parts = [name]
    if instruments:
        doc_parts.append(f"Plays: {instruments}.")
    if albums:
        doc_parts.append(f"Albums: {albums}.")
    doc = ' '.join(doc_parts)
    emb = get_embedding(doc)
    cur.execute("""
        UPDATE _jazzcanon.person
        SET search_document = %s, embedding = %s::vector, updated_at = now()
        WHERE id = %s
    """, (doc, vec_to_pg(emb), CANNONBALL_CANONICAL))
    conn.commit()
    print(f"  Re-embedded: {name} ({albums})")

print()
print("=== Summary ===")
cur.execute("SELECT COUNT(*) FROM _jazzcanon.person")
total = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM _jazzcanon.performance")
perfs = cur.fetchone()[0]
print(f"  Persons: {total}")
print(f"  Performances: {perfs}")
print("Done.")

cur.close()
conn.close()
