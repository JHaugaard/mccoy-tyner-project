#!/usr/bin/env python3
"""
Backfill 3c — populate `_jazzcanon.source` and `_jazzcanon.citation` at
ALBUM-level depth (v1). Per-line citations are a deferred, purely-additive
backfill (see docs — --depth per-line is a stub here).

Reads data/canon-draft.json for the 100 `include:true` albums. Each album's
`sources` array holds S-tokens (e.g. "S1") scoped to the markdown file named
in its `_source_file` field — every album's "## 1. Source Map" table in that
file resolves S-tokens to (title, type, url, notes). The 14 kimi_only albums
have no `_source_file`; their `sources` is a single "kimi:slug1; slug2; ..."
string, and the slugs resolve against the sibling repo's per-album research
record: ../mccoy-tyner-kc/research/phase4-albums/<album-id>-<year>.json
("sources" array, keyed by short_name). That sibling repo is assumed to be
a directory next to this one (../mccoy-tyner-kc) — if it's missing, kimi
albums are reported as anomalies rather than guessed at.

Idempotent: sources are deduped globally (by URL, case-insensitive; by
normalized title when URL is absent) and citations are unique per
(album_id, source_id) — re-running only fills gaps, never duplicates. Nothing
is fabricated: a source with no URL in the record gets url=NULL, not a
guessed link.

Usage (from repo root, in the venv):
  .venv/bin/python3 scripts/citation-backfill.py                # dry run (default)
  .venv/bin/python3 scripts/citation-backfill.py --execute       # write for real
  .venv/bin/python3 scripts/citation-backfill.py --depth per-line  # not implemented
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import psycopg2

REPO_ROOT = Path(__file__).resolve().parent.parent
KC_REPO = REPO_ROOT.parent / "mccoy-tyner-kc"
KC_ALBUMS_DIR = KC_REPO / "research" / "phase4-albums"

SOURCE_MAP_HEADER_RE = re.compile(r"## 1\. Source Map\n\n(.*?)\n\n---", re.S)

PLACEHOLDER_URLS = {"https://example.com", "https://example.com/"}


# ── Env / DB ────────────────────────────────────────────────────────────────

def load_env(path=".env.local"):
    """Mirror apple_previews.py: shallow .env.local loader, environment wins."""
    p = REPO_ROOT / path
    if not p.exists():
        return
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())


# ── Source-map parsing (markdown files) ──────────────────────────────────────

_source_map_cache = {}

def parse_source_map(rel_path):
    """Parse a research/*-candidates*.md '## 1. Source Map' table into
    {token: {title, type, url, notes}}. Cached per file."""
    if rel_path in _source_map_cache:
        return _source_map_cache[rel_path]

    path = REPO_ROOT / rel_path
    text = path.read_text()
    m = SOURCE_MAP_HEADER_RE.search(text)
    result = {}
    if not m:
        _source_map_cache[rel_path] = result
        return result

    lines = [l for l in m.group(1).splitlines() if l.strip().startswith("|")]
    rows = lines[2:]  # skip header + separator row
    for line in rows:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            continue
        token, title, type_, url, notes = cells

        # Some cells hold two URLs separated by " ; " — keep the first, note the rest.
        extra_note = None
        if " ; " in url:
            first, rest = [p.strip() for p in url.split(" ; ", 1)]
            url = first
            extra_note = f"Additional URL: {rest}"
        if url in ("—", "-", ""):
            url = None
        if extra_note:
            notes = f"{notes} {extra_note}".strip() if notes else extra_note

        result[token] = {"title": title, "type": type_, "url": url, "notes": notes or None}

    _source_map_cache[rel_path] = result
    return result


# ── Kimi (mccoy-tyner-kc) source resolution ──────────────────────────────────

def find_kc_file(album_id):
    """Locate the sibling repo's per-album research record for a kimi_only
    album. Filenames are '<album_id>-<year>.json'."""
    if not KC_ALBUMS_DIR.is_dir():
        return None
    matches = sorted(KC_ALBUMS_DIR.glob(f"{album_id}-*.json"))
    if matches:
        return matches[0]
    direct = KC_ALBUMS_DIR / f"{album_id}.json"
    return direct if direct.exists() else None


def load_kc_sources(kc_file):
    """{short_name: {full_citation, url, reliability_notes}}"""
    data = json.loads(kc_file.read_text())
    return {s["short_name"]: s for s in data.get("sources", [])}


def parse_kimi_tokens(raw_sources):
    """canon-draft kimi records store one string: 'kimi:slug1; slug2; ...'."""
    tokens = []
    for entry in raw_sources:
        e = entry[len("kimi:"):] if entry.lower().startswith("kimi:") else entry
        tokens.extend(p.strip() for p in e.split(";") if p.strip())
    return tokens


# ── Source-type inference ────────────────────────────────────────────────────

def infer_type_from_markdown(explicit_type):
    """Map a source-map 'Type' column value (controlled-ish vocabulary) to
    the source_type ENUM. Unmatched web-ish things default to 'web' per
    spec; the project's own scope doc maps to 'other'."""
    t = (explicit_type or "").lower()
    if "book" in t:
        return "book"
    if "liner" in t:
        return "liner-notes"
    if "discog" in t:
        return "discography"
    if "project doc" in t:
        return "other"
    return "web"


def infer_type_from_kimi(short_name, url):
    """Kimi records carry no 'Type' column, so classify from the URL's
    domain (and short_name for file:// process references) instead of the
    free-text citation — free text like 'AllMusic artist page and
    discography' would otherwise false-positive on keyword search."""
    sn = (short_name or "").lower()
    u = (url or "").lower()
    if u.startswith("file://") or sn.startswith("task"):
        return "other"
    if "discogs.com" in u or "jazzdisco.org" in u or "tomlord" in u:
        return "discography"
    if "albumlinernotes.com" in u or "linernotes" in u:
        return "liner-notes"
    return "web"


# ── Dedup keys ────────────────────────────────────────────────────────────────

def normalize_url(url):
    if not url or url.strip() in ("—", "-", ""):
        return None
    u = url.strip().lower().rstrip("/")
    if u in PLACEHOLDER_URLS:
        return None
    return u

def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()

def source_key(title, url):
    u = normalize_url(url)
    return ("url", u) if u else ("title", normalize_title(title))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--execute", action="store_true", help="Write to the DB (default: dry run)")
    parser.add_argument("--depth", choices=["album", "per-line"], default="album")
    args = parser.parse_args()

    if args.depth == "per-line":
        print("not implemented — deferred backfill, see spec §5")
        sys.exit(1)

    dry_run = not args.execute

    load_env()
    db_url = os.environ.get("JAZZCANON_APP_DB_URL")
    if not db_url:
        print("✗ JAZZCANON_APP_DB_URL not set (check .env.local)", file=sys.stderr)
        sys.exit(1)

    draft_path = REPO_ROOT / "data" / "canon-draft.json"
    data = json.loads(draft_path.read_text())
    draft_albums = [a for a in data["albums"] if a.get("include") is True]
    print(f"Loaded {len(draft_albums)} active (include:true) albums from canon-draft.json")
    if dry_run:
        print("DRY RUN — will roll back (pass --execute to write)")

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()
    cur.execute("SET search_path TO _jazzcanon, public")

    # ── Reconcile album ids: draft vs DB ─────────────────────────────────────
    cur.execute("SELECT id FROM album")
    db_ids = {row[0] for row in cur.fetchall()}
    draft_ids = {a["id"] for a in draft_albums}

    anomalies = []
    for aid in sorted(draft_ids - db_ids):
        anomalies.append(f"canon-draft album {aid!r} (include:true) not found in DB — skipped")
    for aid in sorted(db_ids - draft_ids):
        anomalies.append(f"DB album {aid!r} has no matching include:true record in canon-draft.json")

    albums = [a for a in draft_albums if a["id"] in db_ids]

    # ── Preload existing sources/citations for idempotency ───────────────────
    cur.execute("SELECT id, title, url FROM source")
    source_registry = {}
    for sid, title, url in cur.fetchall():
        source_registry[source_key(title, url)] = sid
    sources_before = len(source_registry)

    cur.execute("SELECT album_id, source_id FROM citation WHERE album_id IS NOT NULL")
    citation_registry = {(aid, sid) for aid, sid in cur.fetchall()}
    citations_before = len(citation_registry)

    def get_or_create_source(title, source_type, url, notes):
        key = source_key(title, url)
        if key in source_registry:
            return source_registry[key]
        clean_url = url.strip() if normalize_url(url) else None
        cur.execute("""
            INSERT INTO source (title, source_type, url, notes)
            VALUES (%s, %s::source_type, %s, %s)
            RETURNING id
        """, (title, source_type, clean_url, notes))
        sid = cur.fetchone()[0]
        source_registry[key] = sid
        return sid

    def add_citation(album_id, sid, locator):
        key = (album_id, sid)
        if key in citation_registry:
            return False
        cur.execute("""
            INSERT INTO citation (source_id, album_id, locator)
            VALUES (%s, %s, %s)
        """, (sid, album_id, locator))
        citation_registry.add(key)
        return True

    # ── Walk albums, resolve tokens, create sources + citations ─────────────
    print("\n── Resolving citations ──")

    for a in albums:
        aid = a["id"]
        source_file = a.get("_source_file")
        raw_sources = a.get("sources") or []

        if source_file:
            smap = parse_source_map(source_file)
            tokens = list(raw_sources)
            origin = "markdown"
            kc_file = None
        else:
            origin = "kimi"
            kc_file = find_kc_file(aid)
            if kc_file is None:
                anomalies.append(f"{aid}: kimi_only record — no matching file under "
                                  f"mccoy-tyner-kc/research/phase4-albums/")
                smap = {}
            else:
                smap = load_kc_sources(kc_file)
            tokens = parse_kimi_tokens(raw_sources)

        for token in tokens:
            if token == "general":
                anomalies.append(f"{aid}: skipped placeholder source token 'general' (not a real citation)")
                continue

            row = smap.get(token)
            if row is None:
                where = str(kc_file) if kc_file else (source_file or "mccoy-tyner-kc")
                anomalies.append(f"{aid}: token {token!r} not found in {where}")
                continue

            if origin == "markdown":
                title, url, notes = row["title"], row["url"], row["notes"]
                source_type = infer_type_from_markdown(row["type"])
                locator = f"{token} @ {source_file}"
            else:
                title = row.get("full_citation") or token
                url = row.get("url")
                if normalize_url(url) is None:
                    url = None
                notes = row.get("reliability_notes")
                source_type = infer_type_from_kimi(token, url)
                rel = kc_file.relative_to(KC_REPO.parent) if kc_file else Path(str(kc_file))
                locator = f"{token} @ {rel}"

            sid = get_or_create_source(title, source_type, url, notes)
            add_citation(aid, sid, locator)

    sources_created = len(source_registry) - sources_before
    citations_created = len(citation_registry) - citations_before

    # ── Coverage (final state: pre-existing + new) ───────────────────────────
    coverage = {}
    for (album_id, _sid) in citation_registry:
        coverage[album_id] = coverage.get(album_id, 0) + 1

    covered = sorted(aid for aid in db_ids if coverage.get(aid, 0) > 0)
    uncovered = sorted(aid for aid in db_ids if coverage.get(aid, 0) == 0)

    # ── Commit or rollback ────────────────────────────────────────────────────
    if dry_run:
        conn.rollback()
        print("\nDRY RUN — rolled back, nothing written to DB")
    else:
        conn.commit()
        print("\nCommitted.")

    # ── Report ────────────────────────────────────────────────────────────────
    print("\n── Summary ──")
    print(f"  sources created   : {sources_created}")
    print(f"  citations created : {citations_created}")
    print(f"  albums with ≥1 citation : {len(covered)} / {len(db_ids)}")
    print(f"  albums with ZERO citations : {len(uncovered)}")
    if uncovered:
        for aid in uncovered:
            print(f"    - {aid}")

    if anomalies:
        print(f"\n── Anomalies ({len(anomalies)}) ──")
        for w in anomalies[:50]:
            print(f"  {w}")
        if len(anomalies) > 50:
            print(f"  ... +{len(anomalies) - 50} more")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
