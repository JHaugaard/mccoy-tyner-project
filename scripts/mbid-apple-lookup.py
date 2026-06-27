#!/usr/bin/env python3
"""
C1/C2: MusicBrainz MBID + iTunes Apple ID lookup.

Targets:
  - All albums where musicbrainz_release_group_mbid IS NULL (C2 + kimi part of C1)
  - All albums where apple_album_id IS NULL (C1 kimi + a few others)

Run as postgres user (needs psycopg2 in pg-venv):
  sudo -u postgres /tmp/pg-venv/bin/python3 /home/john/dev/active/mccoy-tyner/scripts/mbid-apple-lookup.py

Add --dry-run to preview without writing.
"""

import json
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
import psycopg2

DRY_RUN = "--dry-run" in sys.argv
MB_USER_AGENT = "jazz-canon-app/1.0 (jhaugaard@mac.com)"
MB_BASE = "https://musicbrainz.org/ws/2"
ITUNES_BASE = "https://itunes.apple.com/search"

conn = psycopg2.connect(host="/var/run/postgresql", port=5433, dbname="postgres", user="postgres")
cur = conn.cursor()


def http_get(url, headers=None, retries=3):
    req = urllib.request.Request(url, headers=headers or {})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 503 and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
            else:
                raise
        except Exception:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise
    return None


def mb_search(artist, title, year):
    """Search MusicBrainz release-group. Returns (mbid, score) or (None, 0)."""
    # Escape special characters for Lucene query
    def esc(s):
        for ch in '+-&|!(){}[]^"~*?:\\/':
            s = s.replace(ch, ' ')
        return s.strip().replace('  ', ' ')

    q = urllib.parse.quote(f'release:"{esc(title)}" artist:"{esc(artist)}"')
    url = f"{MB_BASE}/release-group?query={q}&fmt=json&limit=5"
    time.sleep(1.1)  # MusicBrainz rate limit: 1 req/s

    try:
        data = http_get(url, headers={"User-Agent": MB_USER_AGENT})
    except Exception as e:
        print(f"  MB error for {artist} / {title}: {e}")
        return None, 0

    groups = data.get("release-groups", [])
    for rg in groups:
        score = int(rg.get("score", 0))
        if score < 85:
            break
        # Year check: first-release-date starts with the year
        frd = rg.get("first-release-date", "")
        rg_year = int(frd[:4]) if frd and len(frd) >= 4 else None
        year_ok = (rg_year is None) or (abs(rg_year - year) <= 2)
        if year_ok:
            return rg["id"], score

    return None, 0


def itunes_search(artist, title):
    """Search iTunes for album. Returns collection_id (int) or None."""
    term = urllib.parse.quote(f"{artist} {title}")
    url = f"{ITUNES_BASE}?term={term}&entity=album&limit=10&country=US"
    time.sleep(0.3)  # iTunes rate limit is lenient

    try:
        data = http_get(url)
    except Exception as e:
        print(f"  iTunes error for {artist} / {title}: {e}")
        return None

    # Normalize for matching
    def norm(s):
        return s.lower().replace("the ", "").replace("'", "").replace('"', '').strip()

    norm_title = norm(title)
    norm_artist = norm(artist)

    results = data.get("results", [])
    for r in results:
        if r.get("wrapperType") != "collection" and r.get("collectionType") != "Album":
            continue
        r_title = norm(r.get("collectionName", ""))
        r_artist = norm(r.get("artistName", ""))
        # Exact-ish title match + artist contains check
        if r_title == norm_title and norm_artist[:8] in r_artist:
            return r["collectionId"]

    # Looser match: title startswith
    for r in results:
        r_title = norm(r.get("collectionName", ""))
        r_artist = norm(r.get("artistName", ""))
        if r_title.startswith(norm_title[:15]) and norm_artist[:6] in r_artist:
            return r.get("collectionId")

    return None


# ── Fetch targets ─────────────────────────────────────────────────────────────

cur.execute("""
    SELECT id, title, artist_name, year
    FROM _jazzcanon.album
    WHERE musicbrainz_release_group_mbid IS NULL
    ORDER BY artist_name, year
""")
mbid_targets = cur.fetchall()
print(f"MBID targets: {len(mbid_targets)} albums")

cur.execute("""
    SELECT id, title, artist_name, year
    FROM _jazzcanon.album
    WHERE apple_album_id IS NULL
    ORDER BY artist_name, year
""")
apple_targets = cur.fetchall()
print(f"Apple ID targets: {len(apple_targets)} albums")
print()

# ── MBID lookup ───────────────────────────────────────────────────────────────

mbid_results = {}  # album_id → mbid
print("=== MusicBrainz MBID Lookup ===")
for album_id, title, artist, year in mbid_targets:
    mbid, score = mb_search(artist, title, year)
    status = f"✓ {mbid} (score={score})" if mbid else "✗ no match"
    print(f"  [{album_id}] {artist} — {title} ({year}): {status}")
    if mbid:
        mbid_results[album_id] = mbid

print(f"\nMBID: {len(mbid_results)}/{len(mbid_targets)} matched")

# ── Apple ID lookup ────────────────────────────────────────────────────────────

apple_results = {}  # album_id → apple_id
print("\n=== iTunes Apple ID Lookup ===")
for album_id, title, artist, year in apple_targets:
    apple_id = itunes_search(artist, title)
    status = f"✓ {apple_id}" if apple_id else "✗ no match"
    print(f"  [{album_id}] {artist} — {title} ({year}): {status}")
    if apple_id:
        apple_results[album_id] = str(apple_id)

print(f"\nApple ID: {len(apple_results)}/{len(apple_targets)} matched")

# ── Write to DB ────────────────────────────────────────────────────────────────

if DRY_RUN:
    print("\n[DRY RUN — no DB writes]")
else:
    print("\n=== Writing to DB ===")
    mbid_count = 0
    for album_id, mbid in mbid_results.items():
        cur.execute(
            "UPDATE _jazzcanon.album SET musicbrainz_release_group_mbid = %s WHERE id = %s",
            (mbid, album_id)
        )
        mbid_count += 1

    apple_count = 0
    for album_id, apple_id in apple_results.items():
        cur.execute(
            "UPDATE _jazzcanon.album SET apple_album_id = %s WHERE id = %s",
            (apple_id, album_id)
        )
        apple_count += 1

    conn.commit()
    print(f"Updated {mbid_count} MBID records, {apple_count} Apple ID records")

cur.close()
conn.close()
print("\nDone.")
