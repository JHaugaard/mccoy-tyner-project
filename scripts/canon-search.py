#!/usr/bin/env python3
"""
Semantic search over A Jazz Canon (albums + people).

Embeds the query with the SAME model that built the stored vectors
(nomic-embed-text, 768-dim, via the vps4 Ollama tunnel) and ranks by
cosine similarity against the HNSW-indexed embedding columns.

Usage (from repo root, or anywhere with JAZZCANON_DB_URL set):
  python3 scripts/canon-search.py "spiritual modal piano trios"
  python3 scripts/canon-search.py --people "engineers at Van Gelder"
  python3 scripts/canon-search.py --limit 5 "cool jazz on the west coast"

Read-only: connects as _jazzcanon_ro.
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

import psycopg2

OLLAMA_URL = "http://172.18.0.1:11435/api/embeddings"
MODEL = "nomic-embed-text"


def db_url():
    url = os.environ.get("JAZZCANON_DB_URL")
    if url:
        return url
    # fall back to the repo's .env.local relative to this script
    env = Path(__file__).resolve().parent.parent / ".env.local"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("JAZZCANON_DB_URL="):
                return line.split("=", 1)[1].strip()
    sys.exit("JAZZCANON_DB_URL not set and .env.local not found")


def embed(text):
    payload = json.dumps({"model": MODEL, "prompt": text}).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())["embedding"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="natural-language search query")
    ap.add_argument("--people", action="store_true", help="search people instead of albums")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    vec = embed(args.query)
    conn = psycopg2.connect(db_url())
    cur = conn.cursor()

    if args.people:
        cur.execute(
            """SELECT pe.canonical_name,
                      1 - (pe.embedding <=> %s::vector) AS sim,
                      left(pe.search_document, 100)
                 FROM _jazzcanon.person pe
                WHERE pe.embedding IS NOT NULL
                ORDER BY pe.embedding <=> %s::vector
                LIMIT %s""",
            (vec, vec, args.limit),
        )
        for name, sim, doc in cur.fetchall():
            print(f"{sim:.3f}  {name}  —  {doc}…")
    else:
        cur.execute(
            """SELECT a.title, a.artist_name, a.year, s.display_name,
                      a.canon_status, 1 - (a.embedding <=> %s::vector) AS sim
                 FROM _jazzcanon.album a
                 JOIN _jazzcanon.style s ON s.id = a.style_primary_id
                WHERE a.embedding IS NOT NULL
                ORDER BY a.embedding <=> %s::vector
                LIMIT %s""",
            (vec, vec, args.limit),
        )
        for title, artist, year, style, status, sim in cur.fetchall():
            tag = "" if status == "included" else f"  [{status}]"
            print(f"{sim:.3f}  {artist} — {title} ({year}, {style}){tag}")

    conn.close()


if __name__ == "__main__":
    main()
