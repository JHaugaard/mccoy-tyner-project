#!/usr/bin/env python3
"""
C4: Catalog Number Gap-Fill via MusicBrainz.

For each album with empty catalog_number (86 claude/both records):
  1. Look up release-group MBID (use existing if available, otherwise search)
  2. Fetch releases in the release-group
  3. Find the earliest release with a catalog number (original issue)
  4. UPDATE album.catalog_number

Run as postgres user:
  cp scripts/catalog-lookup.py /tmp/ && chmod 644 /tmp/catalog-lookup.py
  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/catalog-lookup.py [--dry-run]

Idempotent: skips albums that already have a non-empty catalog_number.
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


def mb_get(path, params=""):
    url = f"{MB_BASE}/{path}?{params}&fmt=json"
    time.sleep(1.1)
    try:
        return http_get(url, headers={"User-Agent": MB_USER_AGENT})
    except Exception as e:
        print(f"  MB error [{path}]: {e}")
        return None


def is_good_catalog(cat, year):
    """Return True if the catalog number looks like an original LP issue."""
    if not cat:
        return False
    cat = cat.strip()
    if cat.lower() in ("none", "null", "[none]"):
        return False
    # Skip 45rpm singles (45-XXXX pattern)
    if cat.startswith("45-"):
        return False
    # Skip catalog numbers with CD-era patterns (common for reissues)
    for pattern in ("CD", "2CD", "SACD", "SHM", "UHQCD", "MQA"):
        if pattern in cat.upper():
            return False
    return len(cat) >= 3


def get_catalog_from_release_search(artist, title, year, label_hint=None):
    """Search for releases directly, return best original LP catalog number."""
    def esc(s):
        for ch in '+-&|!(){}[]^"~*?:\\/':
            s = s.replace(ch, ' ')
        return s.strip().replace('  ', ' ')

    # Build query
    q_parts = [f'artist:"{esc(artist)}"', f'release:"{esc(title)}"']
    q = urllib.parse.quote(' '.join(q_parts))
    data = mb_get("release", f"query={q}&inc=labels&limit=20")
    if not data:
        return None

    releases = data.get("releases", [])

    # Sort by date, prefer releases closest to the original year
    def sort_key(r):
        d = r.get("date", "9999")
        release_year = int(d[:4]) if d and len(d) >= 4 else 9999
        score = int(r.get("score", 0))
        # Score descending, then year ascending, then prefer years within 3 years of target
        year_dist = abs(release_year - year)
        return (100 - score, year_dist)

    releases_sorted = sorted(releases, key=sort_key)

    for rel in releases_sorted:
        score = int(rel.get("score", 0))
        if score < 80:
            break
        label_info_list = rel.get("label-info", [])
        for li in label_info_list:
            cat = li.get("catalog-number", "")
            if is_good_catalog(cat, year):
                # Check year is reasonable (within 10 years of recording)
                d = rel.get("date", "")
                release_year = int(d[:4]) if d and len(d) >= 4 else year
                if abs(release_year - year) <= 10:
                    return cat.strip()

    # Wider year range fallback (reissues within 20 years)
    for rel in releases_sorted:
        score = int(rel.get("score", 0))
        if score < 80:
            break
        label_info_list = rel.get("label-info", [])
        for li in label_info_list:
            cat = li.get("catalog-number", "")
            if is_good_catalog(cat, year):
                return cat.strip()

    return None


def mb_search_for_rgid(artist, title, year):
    """Search for release-group MBID."""
    def esc(s):
        for ch in '+-&|!(){}[]^"~*?:\\/':
            s = s.replace(ch, ' ')
        return s.strip().replace('  ', ' ')

    q = urllib.parse.quote(f'release:"{esc(title)}" artist:"{esc(artist)}"')
    data = mb_get("release-group", f"query={q}&limit=5")
    if not data:
        return None

    groups = data.get("release-groups", [])
    for rg in groups:
        score = int(rg.get("score", 0))
        if score < 85:
            break
        frd = rg.get("first-release-date", "")
        rg_year = int(frd[:4]) if frd and len(frd) >= 4 else None
        if rg_year is None or abs(rg_year - year) <= 2:
            return rg["id"]

    return None


# ── Fetch targets ─────────────────────────────────────────────────────────────

cur.execute("""
    SELECT id, title, artist_name, year, musicbrainz_release_group_mbid
    FROM _jazzcanon.album
    WHERE (catalog_number IS NULL OR catalog_number = '')
    ORDER BY artist_name, year
""")
targets = cur.fetchall()
print(f"Catalog number targets: {len(targets)} albums")

# ── Process each album ────────────────────────────────────────────────────────

results = {}  # album_id → catalog_number
for album_id, title, artist, year, existing_mbid in targets:
    cat = get_catalog_from_release_search(artist, title, year)
    if cat:
        print(f"  ✓ {artist} — {title} ({year}): {cat}")
        results[album_id] = cat
    else:
        print(f"  ✗ {artist} — {title} ({year}): no catalog found")

print(f"\nCatalog numbers: {len(results)}/{len(targets)} found")

# ── Write to DB ────────────────────────────────────────────────────────────────

if DRY_RUN:
    print("[DRY RUN — no DB writes]")
else:
    print("\n=== Writing to DB ===")
    count = 0
    for album_id, cat in results.items():
        cur.execute(
            "UPDATE _jazzcanon.album SET catalog_number = %s WHERE id = %s AND (catalog_number IS NULL OR catalog_number = '')",
            (cat, album_id)
        )
        count += 1
    conn.commit()
    print(f"Updated {count} catalog numbers")

cur.close()
conn.close()
print("Done.")
