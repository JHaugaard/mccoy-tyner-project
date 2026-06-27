#!/usr/bin/env python3
"""
adapt-kimi-record.py — Convert a Kimi phase4-albums JSON record to Claude's merged one-pass format.

Usage:
    python3 scripts/adapt-kimi-record.py path/to/kimi-record.json
    python3 scripts/adapt-kimi-record.py path/to/kimi-record.json --out data/adapted/

Wall rule: this script is READ ONLY with respect to Kimi's files.
Output lands in Claude's canon-draft space (stdout or --out dir), never back into mccoy-tyner-kc.

After running, the adapted record still needs:
  - Review for accuracy
  - producer / engineer: filled from Kimi if present, else marked FILL-REQUIRED
  - musicbrainz_release_group_mbid: FILL-REQUIRED (Kimi doesn't carry this)
  - apple_album_id: FILL-REQUIRED
  - cover_art: FILL-REQUIRED
  - include: set to true by John after curation gate
  - consensus: already set to "kimi_only"
"""

import json
import re
import sys
import os
from pathlib import Path

GENRE_MAP = {
    "Modal Jazz":        "modal-jazz",
    "Cool Jazz":         "cool-jazz",
    "Hard Bop":          "hard-bop",
    "Soul Jazz":         "soul-jazz",
    "Post-Bop":          "post-bop",
    "West Coast Jazz":   "cool-jazz",
    "Bebop":             "hard-bop",
    "Free Jazz":         "post-bop",
    "Jazz":              "modal-jazz",
    "Chamber Jazz":      "cool-jazz",
    "Piano Jazz":        "modal-jazz",
}


def norm_genre(genre_str):
    return GENRE_MAP.get(genre_str, genre_str.lower().replace(" ", "-"))


def seconds_to_mmss(secs):
    if not secs:
        return None
    m, s = divmod(int(secs), 60)
    return f"{m}:{s:02d}"


def build_id(artist, album):
    slug = f"{artist} {album}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def extract_production(album_personnel):
    producer = None
    engineer = None
    musicians = []
    for p in album_personnel:
        role = p.get("role", "").lower()
        if "producer" in role:
            producer = p.get("person_name")
        elif "engineer" in role:
            engineer = p.get("person_name")
        else:
            musicians.append(p)
    return producer, engineer, musicians


def adapt_personnel(kimi_musicians):
    result = []
    for p in kimi_musicians:
        result.append({
            "name": p.get("person_name", ""),
            "instrument": p.get("instrument", ""),
            "scope": "all-tracks" if p.get("applies_to_all_tracks") else "unknown",
            "tracks": None,
            "session_dates": None,
            "epistemic": p.get("label", "obs"),
            "sources": ["kimi"],
            "name_variants": [],
            "notes": "",
        })
    return result


def adapt_tracks(kimi_tracks):
    result = []
    for t in kimi_tracks:
        dur_secs = (t.get("duration_seconds") or {}).get("value")
        composers_raw = (t.get("composer") or {}).get("value", "")
        composers = [c.strip() for c in composers_raw.split(",") if c.strip()]
        result.append({
            "title": (t.get("title") or {}).get("value", ""),
            "track_number": (t.get("track_number") or {}).get("value"),
            "side": None,
            "duration": seconds_to_mmss(dur_secs),
            "session_date": (t.get("recording_date") or {}).get("value"),
            "composers": composers,
            "personnel": [],  # track-level personnel not ported from Kimi's padded rows
            "bonus_track": False,
            "alternate_take": False,
            "epistemic_track": "obs",
            "sources": ["kimi"],
        })
    return result


def adapt(kimi_path):
    with open(kimi_path) as f:
        k = json.load(f)

    album_block = k.get("album", {})
    title  = (album_block.get("title")  or {}).get("value", "")
    artist = (album_block.get("artist") or {}).get("value", "")
    year   = (album_block.get("release_year") or {}).get("value")
    label  = (album_block.get("label") or {}).get("value", "")
    catalog = (album_block.get("catalog_number") or {}).get("value", "")
    rec_date_raw = (album_block.get("recording_dates") or {}).get("value", "")

    genres = k.get("genres", [])
    style_primary = norm_genre(genres[0]["genre"]) if genres else "modal-jazz"
    style_tags = list({norm_genre(g["genre"]) for g in genres})

    kimi_personnel = k.get("album_personnel", [])
    producer, engineer, musicians = extract_production(kimi_personnel)

    # recording_dates: Kimi gives a string (e.g. "1958-01-16"); Claude wants an array
    recording_dates = []
    if rec_date_raw:
        # Could be comma-separated if multiple dates
        for d in re.split(r"[,;]\s*", str(rec_date_raw)):
            d = d.strip()
            if d:
                recording_dates.append(d)

    # Source citation summary (no full URLs — those stay in Kimi's file)
    source_summary = "; ".join(
        s["short_name"] for s in k.get("sources", [])
        if s.get("short_name") and s["short_name"] != "general"
    )

    tracks = adapt_tracks(k.get("tracks", []))
    personnel = adapt_personnel(musicians)

    record = {
        "id":            build_id(artist, title),
        "artist":        artist,
        "album":         title,
        "year":          year,
        "label":         label,
        "style_primary": style_primary,
        "style_tags":    style_tags,
        "sources":       [f"kimi:{source_summary}"],
        "epistemic":     "obs",
        "rationale":     f"Kimi Code research: {source_summary}. Adapted by adapt-kimi-record.py; review before ingest.",
        "priority":      "standard",
        "overlap_risk":  "",
        "scope_flag":    "",
        "include":       False,  # John sets True after curation gate
        "consensus":     "kimi_only",
        "catalog_number": catalog or "FILL-REQUIRED",
        "personnel_record": {
            "recording_dates":        recording_dates,
            "multi_session":          len(recording_dates) > 1,
            "studio":                 "FILL-REQUIRED",
            "producer":               producer or "FILL-REQUIRED",
            "engineer":               engineer or "FILL-REQUIRED",
            "epistemic_production":   "obs" if (producer or engineer) else "unk",
            "personnel":              personnel,
            "tracks":                 tracks,
            "track_assignments_complete": False,
            "musicbrainz_release_group_mbid": "FILL-REQUIRED",
            "apple_album_id":         "FILL-REQUIRED",
            "cover_art":              {
                "musicbrainz_url":  "FILL-REQUIRED",
                "itunes_url":       "FILL-REQUIRED",
                "local_path":       None,
                "fetched":          False,
            },
            "notes": f"Adapted from Kimi phase4-albums record. "
                     f"Track-level personnel not ported (Kimi pads album lineup per track; "
                     f"see mccoy-tyner-kc/research/phase4-albums/ for source). "
                     f"FILL-REQUIRED fields need research before Phase 4 ingest.",
        },
    }
    return record


def main():
    if len(sys.argv) < 2:
        print("Usage: adapt-kimi-record.py <kimi-json> [--out <dir>]", file=sys.stderr)
        sys.exit(1)

    kimi_path = sys.argv[1]
    out_dir = None
    if "--out" in sys.argv:
        idx = sys.argv.index("--out")
        if idx + 1 < len(sys.argv):
            out_dir = sys.argv[idx + 1]

    record = adapt(kimi_path)
    output = json.dumps(record, indent=2, ensure_ascii=False)

    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = Path(out_dir) / f"{record['id']}.json"
        with open(out_path, "w") as f:
            f.write(output)
        print(f"Written: {out_path}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
