#!/usr/bin/env python3
"""Narrow credit-only enrichment of the SITE's details.json.

Commission: 2026-09-25 site-expansion spec (John) — Producer/Engineer display;
mccoy owns export generation/checksum refresh; coder owns UI. This script adds
`productionCredits` to the CURRENT site details.json from a verified workshop
export, restricted to EXACTLY the album IDs already on the site, preserving
every other field byte-value (Apple previews included). It never ships albums:
the export may legitimately contain more albums than the site; only site IDs
are written.

Assertions (any failure aborts BEFORE writing):
  1. set(site albums.json ids) == set(site details.json keys)
  2. every site id is present in the export details.json
  3. every export record used has productionCredits as a list
  4. post-merge, each record deep-equals its prior self except for the added
     productionCredits key (previews and all other fields provably unchanged)
  5. site id count unchanged; no id added or removed

Usage: enrich-production-credits.py --export exports/jazz-canon/details.json \
        --site /home/john/dev/active/jazz-canon/app [--dry-run]
"""
import argparse, copy, json, sys
from pathlib import Path


def load(p: Path):
    return json.loads(p.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", required=True, type=Path)
    ap.add_argument("--site", required=True, type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    site_data = a.site / "public" / "data"
    site_albums = load(site_data / "albums.json")
    site_details = load(site_data / "details.json")
    exp_details = load(a.export)

    site_ids = {r["id"] for r in site_albums}
    det_ids = set(site_details)
    assert site_ids == det_ids, (
        f"albums/details id mismatch: only-in-albums={sorted(site_ids - det_ids)}, "
        f"only-in-details={sorted(det_ids - site_ids)}"
    )
    missing = sorted(site_ids - set(exp_details))
    assert not missing, f"site ids absent from export: {missing}"

    merged = {}
    credited = 0
    for aid in site_ids:  # preserve nothing about export order; site order below
        old = site_details[aid]
        exp_rec = exp_details[aid]
        pc = exp_rec.get("productionCredits")
        assert isinstance(pc, list), f"export {aid} productionCredits not a list"
        for c in pc:
            assert all(k in c for k in ("personId", "name", "role", "e", "sessionId")), (
                f"export {aid} credit missing keys: {c}"
            )
        new = dict(old)  # preserves site key order
        new["productionCredits"] = pc
        if pc:
            credited += 1
        # deep-equality proof: every pre-existing field unchanged
        old_wo = copy.deepcopy(old)
        new_wo = {k: v for k, v in new.items() if k != "productionCredits"}
        assert new_wo == old_wo, f"{aid}: non-credit field changed"
        merged[aid] = new

    assert set(merged) == site_ids, "merged id set drifted"
    assert len(merged) == len(site_details), "record count drifted"

    out = json.dumps(merged, ensure_ascii=False, separators=(",", ":"))
    if a.dry_run:
        print(f"DRY RUN OK: {len(merged)} albums, {credited} with >=1 credit, "
              f"{len(out)} bytes; no write")
        return 0

    tmp = site_data / "details.json.tmp"
    tmp.write_text(out)
    tmp.replace(site_data / "details.json")
    print(f"OK: wrote {site_data/'details.json'} — {len(merged)} albums, "
          f"{credited} with >=1 credit, {len(out)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
