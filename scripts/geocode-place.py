#!/usr/bin/env python3
"""
geocode-place.py — resolve a recording place to coordinates, John's way.

Wraps the geocoding method ratified 2026-08-14 (studios-map session,
decision 7) so that an unattended agent never hand-rolls HTTP against a
public geocoder and never invents precision. Emits the four columns
`_jazzcanon.studio` needs for a coordinate:

    {"lat": ..., "lon": ..., "location_epistemic": "obs"|"inf",
     "location_source": "..."}

The chain, in order — the first rung that answers wins:

  1. **Wikidata / Wikipedia coordinate** (P625), when the caller names the
     entity. Street-grade and citable ⇒ `obs`.
  2. **OSM Nominatim on a documented address** ⇒ `obs`. Per the standing
     ruling, geocoding an address a source documents is a *mechanical
     transformation*: the address stays `obs` and the derivation is
     recorded in `location_source`. It does not manufacture precision,
     it only expresses documented precision as numbers.
  3. **City centroid, rounded to 3 decimals** ⇒ `inf`. This is the honest
     answer when no street address is documented. A 3-decimal centroid is
     deliberately blunt: the site's `precision` field renders it as
     city-grade so the map never implies a street-level pin.

Rung 1 is opt-in by identifier (`--wikidata` / `--wikipedia`), never by
blind search. An unattended agent guessing which Wikidata entity is "the
right Birdland" is exactly the failure this script exists to prevent — if
the caller cannot name the entity, the chain falls through to the address
or the city, both of which are self-verifying.

`--address` is what a SOURCE documents. Never pass an address you inferred,
reconstructed, or found only on a map: absent documentation, omit it and
take the city centroid. That is rung 3's whole purpose.

Stdlib only (urllib) — no new dependency. Nominatim's usage policy is
honoured: a real User-Agent, and a hard 1 request/second floor.

Usage:
  scripts/geocode-place.py --city "New York, NY" --address "178 Seventh Avenue South" \
      --address-source "https://en.wikipedia.org/wiki/Village_Vanguard"
  scripts/geocode-place.py --city "Ludwigsburg, Germany"
  scripts/geocode-place.py --city "New York, NY" --wikipedia "Atlantic Studios"

Exit 0 with JSON on stdout; exit 1 with a reason on stderr if no rung answered.
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

USER_AGENT = "jazzcanon-geocoder/1.0 (A Jazz Canon research project; contact jhaugaard@mac.com)"
NOMINATIM = "https://nominatim.openstreetmap.org/search"
WIKIDATA_ENTITY = "https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"

# Nominatim's usage policy is one request per second, absolute. This is a
# floor across the whole process, not a per-call sleep, so a batch caller
# cannot accidentally burst by constructing fresh objects.
_MIN_INTERVAL = 1.0
_last_request = [0.0]


def _get(url, params=None, timeout=20):
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    elapsed = time.monotonic() - _last_request[0]
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
    finally:
        _last_request[0] = time.monotonic()
    return json.loads(body)


# ── Rung 1: Wikidata / Wikipedia ────────────────────────────────────────────

def qid_from_wikipedia(title):
    """Resolve an en.wikipedia article title to its Wikidata QID."""
    data = _get(WIKIPEDIA_API, {
        "action": "query", "prop": "pageprops", "ppprop": "wikibase_item",
        "titles": title, "format": "json", "redirects": "1",
    })
    for page in (data.get("query", {}).get("pages") or {}).values():
        qid = (page.get("pageprops") or {}).get("wikibase_item")
        if qid:
            return qid
    return None


def coord_from_wikidata(qid):
    """Return (lat, lon) from the entity's P625 coordinate claim, or None."""
    data = _get(WIKIDATA_ENTITY.format(qid=qid))
    entity = (data.get("entities") or {}).get(qid) or {}
    for claim in (entity.get("claims") or {}).get("P625") or []:
        value = ((claim.get("mainsnak") or {}).get("datavalue") or {}).get("value")
        if value and "latitude" in value and "longitude" in value:
            return float(value["latitude"]), float(value["longitude"])
    return None


# ── Rungs 2 and 3: Nominatim ────────────────────────────────────────────────

def nominatim(query):
    """Return (lat, lon) for a free-text query, or None."""
    results = _get(NOMINATIM, {"q": query, "format": "json", "limit": 1})
    if not results:
        return None
    return float(results[0]["lat"]), float(results[0]["lon"])


# Nominatim parses "178 7th Avenue South" and rejects "178 Seventh Avenue
# South". The house style for `studio.address` is whatever the SOURCE printed,
# which for older addresses is often the spelled-out ordinal — so the stored
# form is exactly the form the geocoder cannot read. Found by running the real
# service against the real corpus: the spelled-out form returned no result and
# the coordinate silently degraded to a city centroid 2.6 km away.
_ORDINALS = {
    "first": "1st", "second": "2nd", "third": "3rd", "fourth": "4th",
    "fifth": "5th", "sixth": "6th", "seventh": "7th", "eighth": "8th",
    "ninth": "9th", "tenth": "10th", "eleventh": "11th", "twelfth": "12th",
    "thirteenth": "13th", "fourteenth": "14th", "fifteenth": "15th",
    "sixteenth": "16th", "seventeenth": "17th", "eighteenth": "18th",
    "nineteenth": "19th", "twentieth": "20th", "thirtieth": "30th",
    "fortieth": "40th", "fiftieth": "50th", "sixtieth": "60th",
}


def address_variants(address):
    """Yield progressively cleaner forms of a documented address to try.

    The address column is never rewritten — these variants exist only to ask
    the geocoder a question it can answer. Order matters: the form the source
    documented is tried first, so an address that geocodes cleanly as written
    never gets normalised behind the caller's back.
    """
    seen = []

    def add(candidate):
        candidate = re.sub(r"\s+", " ", candidate).strip(" ,")
        if candidate and candidate not in seen:
            seen.append(candidate)

    add(address)
    # Spelled-out ordinals → numeric ("Seventh Avenue" → "7th Avenue").
    lowered = re.sub(r"\b(" + "|".join(_ORDINALS) + r")\b",
                     lambda m: _ORDINALS[m.group(1).lower()], address, flags=re.I)
    add(lowered)
    # Drop parenthetical qualifiers — "(at Thompson Street)", "(penthouse,
    # Steinway Hall)" — and trailing floor/suite detail, which Nominatim reads
    # as part of the street name and fails on.
    stripped = re.sub(r"\([^)]*\)", " ", lowered)
    stripped = re.sub(r",\s*\d+(st|nd|rd|th)\s+floor\b.*$", "", stripped, flags=re.I)
    add(stripped)
    return seen


def geocode(city, address=None, address_source=None, wikidata=None, wikipedia=None,
            allow_city_fallback=False):
    """Run the ratified chain. Returns the four studio columns as a dict."""
    if not city:
        raise ValueError("city is required — it is the floor of the chain")

    # Rung 1 — a citable coordinate for the entity itself.
    qid = wikidata
    if not qid and wikipedia:
        qid = qid_from_wikipedia(wikipedia)
    if qid:
        coord = coord_from_wikidata(qid)
        if coord:
            ref = (f"https://en.wikipedia.org/wiki/{urllib.parse.quote(wikipedia.replace(' ', '_'))}"
                   if wikipedia else f"https://www.wikidata.org/wiki/{qid}")
            return {
                "lat": round(coord[0], 5), "lon": round(coord[1], 5),
                "location_epistemic": "obs",
                "location_source": _compose(address_source, f"coords: {ref}"),
            }

    # Rung 2 — mechanical transformation of a DOCUMENTED address.
    if address:
        for variant in address_variants(address):
            coord = nominatim(f"{variant}, {city}")
            if coord:
                note = "" if variant == address else f" (queried as {variant!r})"
                return {
                    "lat": round(coord[0], 5), "lon": round(coord[1], 5),
                    "location_epistemic": "obs",
                    "location_source": _compose(
                        address_source,
                        f"coords: OSM Nominatim: {address}, {city} "
                        f"— geocoded from documented address{note}"),
                }
        # A documented address that will not geocode is a REFUSAL, not a
        # licence to publish a city pin. Falling through here would silently
        # rewrite an `obs` street-grade place into an `inf` centroid — the
        # caller would see a valid-looking row and never learn it lost 2-3 km
        # of precision. Make the caller choose.
        if not allow_city_fallback:
            raise LookupError(
                f"documented address {address!r} did not geocode in {city!r} "
                f"(tried {len(address_variants(address))} form(s)). Refusing to "
                f"silently degrade it to a city centroid. Either correct the "
                f"address, supply --wikidata/--wikipedia, or pass "
                f"--allow-city-fallback to accept city precision deliberately.")
        print(f"! address did not geocode, city fallback explicitly allowed: {address!r}",
              file=sys.stderr)

    # Rung 3 — the honest answer when nothing street-level is documented.
    coord = nominatim(city)
    if coord:
        return {
            "lat": round(coord[0], 3), "lon": round(coord[1], 3),
            "location_epistemic": "inf",
            "location_source": _compose(
                address_source,
                f"coords: city centroid (OSM Nominatim: {city}), 3-decimal precision "
                f"— no street address documented"),
        }
    return None


def _compose(address_source, derivation):
    """location_source = <address citation> | <coord derivation>, matching the
    convention the 2026-08-14 backfill wrote (scripts/studio-geocode-*.sql)."""
    return f"{address_source} | {derivation}" if address_source else derivation


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--city", required=True, help='City as it will be stored, e.g. "New York, NY"')
    p.add_argument("--address", help="Street address AS DOCUMENTED BY A SOURCE. Omit if undocumented.")
    p.add_argument("--address-source", help="Citation URL backing the address (and/or the place).")
    p.add_argument("--wikidata", help="Wikidata QID, e.g. Q1234567 — used for a citable P625 coordinate.")
    p.add_argument("--wikipedia", help="en.wikipedia article title; resolved to a QID, then P625.")
    p.add_argument("--name", help="Place name (recorded in output for the caller's convenience only).")
    p.add_argument("--allow-city-fallback", action="store_true",
                   help="Accept a city centroid even though a documented address was given. "
                        "Off by default: an address that will not geocode is a refusal, not a "
                        "licence to publish a 3-decimal pin as if it were street-grade.")
    args = p.parse_args()

    try:
        result = geocode(args.city, args.address, args.address_source,
                         args.wikidata, args.wikipedia, args.allow_city_fallback)
    except Exception as e:
        print(f"✗ geocode failed: {e}", file=sys.stderr)
        sys.exit(1)

    if not result:
        print(f"✗ no rung of the chain resolved {args.city!r} — "
              f"nothing emitted rather than a guessed coordinate", file=sys.stderr)
        sys.exit(1)

    if args.name:
        result = {"name": args.name, **result}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
