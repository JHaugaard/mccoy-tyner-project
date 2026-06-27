#!/usr/bin/env python3
"""
C5: Embeddings — nomic-embed-text (768-dim) via Ollama on vps4.

Populates:
  - album.search_document + album.embedding
  - person.search_document + person.embedding

Builds HNSW indexes after (they exist already; this just ensures up-to-date stats).

Run as postgres user:
  cp scripts/embed.py /tmp/ && chmod 644 /tmp/embed.py
  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/embed.py [--dry-run]

Idempotent: skips records where embedding IS NOT NULL (unless --force).
"""

import json
import sys
import time
import urllib.request
import urllib.error
import psycopg2

DRY_RUN = "--dry-run" in sys.argv
FORCE = "--force" in sys.argv
OLLAMA_URL = "http://172.18.0.1:11435/api/embeddings"
MODEL = "nomic-embed-text"

conn = psycopg2.connect(host="/var/run/postgresql", port=5433, dbname="postgres", user="postgres")
cur = conn.cursor()


def get_embedding(text, retries=3):
    """Call Ollama API and return 768-dim embedding list."""
    payload = json.dumps({"model": MODEL, "prompt": text}).encode()
    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                return data["embedding"]
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
            else:
                raise RuntimeError(f"Ollama error: {e}")


def vec_to_pg(embedding):
    """Convert embedding list to Postgres vector literal."""
    return '[' + ','.join(f'{x:.8f}' for x in embedding) + ']'


# ── Album embeddings ──────────────────────────────────────────────────────────

where_clause = "WHERE a.embedding IS NULL" if not FORCE else "WHERE true"
cur.execute(f"""
    SELECT a.id, a.title, a.artist_name, a.year,
           s.display_name as style,
           a.description,
           STRING_AGG(DISTINCT p.canonical_name || ' (' || inst.name || ')', ', ') as performers
    FROM _jazzcanon.album a
    JOIN _jazzcanon.style s ON s.id = a.style_primary_id
    LEFT JOIN _jazzcanon.performance perf ON perf.album_id = a.id
    LEFT JOIN _jazzcanon.person p ON p.id = perf.person_id
    LEFT JOIN _jazzcanon.instrument inst ON inst.id = perf.instrument_id
    {where_clause}
    GROUP BY a.id, a.title, a.artist_name, a.year, s.display_name, a.description
    ORDER BY a.artist_name, a.year
""")
albums = cur.fetchall()
print(f"Albums to embed: {len(albums)}")

album_ok, album_err = 0, 0
for album_id, title, artist, year, style, description, performers in albums:
    parts = [f"{title} by {artist}, {year}", f"Style: {style}"]
    if performers:
        parts.append(f"Performers: {performers}")
    if description:
        parts.append(description)
    doc = ". ".join(parts) + "."

    if DRY_RUN:
        print(f"  [album] {artist} — {title}: {doc[:80]}...")
        continue

    try:
        embedding = get_embedding(doc)
        vec = vec_to_pg(embedding)
        cur.execute("""
            UPDATE _jazzcanon.album
            SET search_document = %s, embedding = %s::vector
            WHERE id = %s
        """, (doc, vec, album_id))
        album_ok += 1
        if album_ok % 10 == 0:
            conn.commit()
            print(f"  {album_ok}/{len(albums)} albums done")
    except Exception as e:
        print(f"  ✗ {artist} — {title}: {e}")
        album_err += 1

if not DRY_RUN:
    conn.commit()
    print(f"Albums: {album_ok} ok, {album_err} errors")

# ── Person embeddings ─────────────────────────────────────────────────────────

where_clause_p = "WHERE p.embedding IS NULL" if not FORCE else "WHERE true"
cur.execute(f"""
    SELECT p.id, p.canonical_name,
           STRING_AGG(DISTINCT inst.name, ', ') as instruments,
           STRING_AGG(DISTINCT a.artist_name || ' — ' || a.title || ' (' || a.year::text || ')', '; '
                      ORDER BY a.artist_name || ' — ' || a.title || ' (' || a.year::text || ')') as album_list
    FROM _jazzcanon.person p
    LEFT JOIN _jazzcanon.performance perf ON perf.person_id = p.id
    LEFT JOIN _jazzcanon.instrument inst ON inst.id = perf.instrument_id
    LEFT JOIN _jazzcanon.album a ON a.id = perf.album_id
    {where_clause_p}
    GROUP BY p.id, p.canonical_name
    ORDER BY p.canonical_name
""")
persons = cur.fetchall()
print(f"\nPersons to embed: {len(persons)}")

person_ok, person_err = 0, 0
for person_id, name, instruments, album_list in persons:
    parts = [name]
    if instruments:
        parts.append(f"Plays: {instruments}")
    if album_list:
        parts.append(f"Albums: {album_list}")
    doc = ". ".join(parts) + "."

    if DRY_RUN:
        print(f"  [person] {name}: {doc[:80]}...")
        continue

    try:
        embedding = get_embedding(doc)
        vec = vec_to_pg(embedding)
        cur.execute("""
            UPDATE _jazzcanon.person
            SET search_document = %s, embedding = %s::vector
            WHERE id = %s
        """, (doc, vec, person_id))
        person_ok += 1
        if person_ok % 25 == 0:
            conn.commit()
            print(f"  {person_ok}/{len(persons)} persons done")
    except Exception as e:
        print(f"  ✗ {name}: {e}")
        person_err += 1

if not DRY_RUN:
    conn.commit()
    print(f"Persons: {person_ok} ok, {person_err} errors")

# ── Refresh HNSW indexes ──────────────────────────────────────────────────────
if not DRY_RUN and (album_ok > 0 or person_ok > 0):
    print("\nAnalyzing tables for HNSW index stats...")
    cur.execute("ANALYZE _jazzcanon.album")
    cur.execute("ANALYZE _jazzcanon.person")
    conn.commit()
    print("Done.")

if DRY_RUN:
    print("\n[DRY RUN — no DB writes]")

cur.close()
conn.close()
print("\nDone.")
