#!/usr/bin/env python3
"""
C3: Cover Art Fetch — Cover Art Archive (primary) → iTunes (fallback).

For each album:
  1. If has musicbrainz_release_group_mbid → try Cover Art Archive
  2. If no MBID or CAA fails → try iTunes using apple_album_id
  3. Download front-cover image to data/album-art/
  4. INSERT into _jazzcanon.album_art (source, source_url, local_path, mime_type, bytes, sha256)

Run as postgres user:
  cp scripts/cover-art-fetch.py /tmp/ && chmod 644 /tmp/cover-art-fetch.py
  sudo -u postgres /tmp/pg-venv/bin/python3 /tmp/cover-art-fetch.py [--dry-run]

Idempotent: skips albums that already have is_primary=true in album_art.
"""

import hashlib
import json
import os
import sys
import time
import urllib.request
import urllib.error
import psycopg2

DRY_RUN = "--dry-run" in sys.argv
ART_DIR = "/tmp/album-art-staging"
ART_DIR_FINAL = "/home/john/dev/active/mccoy-tyner/data/album-art"
CAA_BASE = "https://coverartarchive.org/release-group"
ITUNES_ARTWORK = "https://itunes.apple.com/lookup?id={id}&entity=album"

conn = psycopg2.connect(host="/var/run/postgresql", port=5433, dbname="postgres", user="postgres")
cur = conn.cursor()

os.makedirs(ART_DIR, exist_ok=True)


def http_download(url, headers=None, retries=3):
    req = urllib.request.Request(url, headers=headers or {})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read(), resp.info().get("Content-Type", "").split(";")[0].strip()
        except urllib.error.HTTPError as e:
            if e.code in (404, 403):
                return None, None
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
            else:
                return None, None
        except Exception:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                return None, None


def http_get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def fetch_caa(mbid, album_id):
    """Fetch front cover from Cover Art Archive. Returns (data, mime, source_url) or (None, None, None)."""
    # Get image list
    data = http_get_json(f"{CAA_BASE}/{mbid}", headers={"User-Agent": "jazz-canon-app/1.0"})
    if not data:
        return None, None, None

    images = data.get("images", [])
    for img in images:
        if img.get("front", False) or "Front" in img.get("types", []):
            # Prefer 500px thumbnail
            thumbnails = img.get("thumbnails", {})
            url = thumbnails.get("500", thumbnails.get("large", img.get("image", "")))
            if not url:
                continue
            time.sleep(0.5)
            raw, mime = http_download(url)
            if raw:
                return raw, mime or "image/jpeg", url

    return None, None, None


def fetch_itunes(apple_id, album_id):
    """Fetch artwork URL from iTunes lookup. Returns (data, mime, source_url) or (None, None, None)."""
    data = http_get_json(ITUNES_ARTWORK.format(id=apple_id))
    if not data:
        return None, None, None

    results = data.get("results", [])
    for r in results:
        art_url = r.get("artworkUrl100", "")
        if art_url:
            # Upgrade to 1000px
            art_url_hq = art_url.replace("100x100bb", "1000x1000bb")
            raw, mime = http_download(art_url_hq)
            if raw:
                return raw, mime or "image/jpeg", art_url_hq
            raw, mime = http_download(art_url)
            if raw:
                return raw, mime or "image/jpeg", art_url

    return None, None, None


def ext_for_mime(mime):
    return {"image/jpeg": "jpg", "image/png": "png", "image/gif": "gif",
            "image/webp": "webp"}.get(mime, "jpg")


# ── Fetch albums needing cover art ────────────────────────────────────────────

cur.execute("""
    SELECT a.id, a.title, a.artist_name, a.year,
           a.musicbrainz_release_group_mbid, a.apple_album_id
    FROM _jazzcanon.album a
    WHERE NOT EXISTS (
        SELECT 1 FROM _jazzcanon.album_art aa
        WHERE aa.album_id = a.id AND aa.is_primary = true
    )
    ORDER BY a.artist_name, a.year
""")
targets = cur.fetchall()
print(f"Albums needing cover art: {len(targets)}")

# ── Process each album ────────────────────────────────────────────────────────

fetched, skipped = 0, 0
for album_id, title, artist, year, mbid, apple_id in targets:
    raw, mime, source_url = None, None, None
    art_source = None

    if mbid:
        time.sleep(0.5)
        raw, mime, source_url = fetch_caa(mbid, album_id)
        if raw:
            art_source = "cover-art-archive"

    if not raw and apple_id:
        time.sleep(0.3)
        raw, mime, source_url = fetch_itunes(apple_id, album_id)
        if raw:
            art_source = "itunes"

    if not raw:
        print(f"  ✗ {artist} — {title}: no art found (mbid={mbid}, apple={apple_id})")
        skipped += 1
        continue

    ext = ext_for_mime(mime)
    local_file = f"{album_id}.{ext}"
    local_path = os.path.join(ART_DIR, local_file)
    sha256 = hashlib.sha256(raw).hexdigest()

    print(f"  ✓ {artist} — {title}: {art_source} ({len(raw)} bytes, {mime})")

    if not DRY_RUN:
        with open(local_path, "wb") as f:
            f.write(raw)

        # Store final path (files will be moved from staging after script completes)
        final_path = os.path.join(ART_DIR_FINAL, local_file)
        cur.execute("""
            INSERT INTO _jazzcanon.album_art
                (album_id, role, source, source_url, local_path, mime_type, bytes, sha256, is_primary, epistemic)
            VALUES (%s, 'front', %s, %s, %s, %s, %s, %s, true, 'obs')
            ON CONFLICT (album_id, role, source) DO UPDATE SET
                source_url = EXCLUDED.source_url,
                local_path = EXCLUDED.local_path,
                mime_type  = EXCLUDED.mime_type,
                bytes      = EXCLUDED.bytes,
                sha256     = EXCLUDED.sha256,
                is_primary = true,
                fetched_at = now()
        """, (album_id, art_source, source_url, final_path, mime, len(raw), sha256))

    fetched += 1

if not DRY_RUN:
    conn.commit()

print(f"\nFetched: {fetched}, skipped: {skipped}")
if DRY_RUN:
    print("[DRY RUN — no files written, no DB updates]")

cur.close()
conn.close()
print("Done.")
