#!/usr/bin/env python3
"""A:B test — decision models vs curated style_primary ground truth.

Asks one Choice question per published album ("which primary style?")
over the 12 style codes actually used in the canon, once per model.
State carries only enumeration fields (title/artist/year/label/catalog)
— never the answer, never description or consensus text.

Usage:
  OPENROUTER_API_KEY=... python3 scripts/style-ab-test.py --model typesafe/jev-1.14 [--limit N]
  OPENROUTER_API_KEY=... python3 scripts/style-ab-test.py --model openai/gpt-6-luna-decisions

Writes research/style-ab-results-<slug>.jsonl (one raw response per line).
"""
import argparse, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib import request, error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(ROOT, "research", "style-ab-ground-truth.tsv")

STYLE_CRITERIA = {
    "bebop":            "The founding modern-jazz idiom — breakneck tempos, angular lines, small-group virtuosity",
    "cool-jazz":        "Relaxed, lyrical post-bebop from the late 1940s-50s",
    "hard-bop":         "Hard-driving post-bebop with blues and gospel roots",
    "soul-jazz":        "Blues and gospel inflected hard bop variant",
    "modal-jazz":       "Improvisation over modal scales rather than chord changes",
    "post-bop":         "Eclectic post-1960 jazz drawing from multiple traditions",
    "free-jazz":        "Collective improvisation released from fixed changes, meter, or key",
    "avant-garde-jazz": "Composition-minded experimentalism in the AACM lineage",
    "spiritual-jazz":   "Modal and free playing in a devotional, often non-Western frame",
    "european-jazz":    "Postwar European jazz with folk and chamber-music centre of gravity",
    "fusion":           "Jazz improvisation fused with rock and funk rhythm and electric instruments",
    "jazz-rock":        "Rock-weighted fusion variant driven by backbeat and amplified guitar",
}

QUESTIONS = {
    "style": {
        "type": "choice",
        "instructions": (
            "Which single primary style best describes this jazz album? "
            "Judge the music on the record, not the artist's general reputation."
        ),
        "criteria": STYLE_CRITERIA,
    }
}

def load_truth():
    rows = []
    with open(TSV) as f:
        for line in f:
            aid, title, artist, year, label, catalog, style = line.rstrip("\n").split("\t")
            rows.append(dict(id=aid, title=title, artist=artist, year=int(year),
                             label=label, catalog=catalog, truth=style))
    return rows

def call_model(api_key, model, album, attempts=4):
    state = {"album": {"title": album["title"], "artist": album["artist"],
                       "year": album["year"], "label": album["label"],
                       "catalog_number": album["catalog"]}}
    payload = json.dumps({"model": model, "state": state, "questions": QUESTIONS}).encode()
    for i in range(attempts):
        try:
            req = request.Request(
                "https://openrouter.ai/api/alpha/decisions", data=payload,
                headers={"Authorization": f"Bearer {api_key}",
                         "Content-Type": "application/json"})
            with request.urlopen(req, timeout=60) as r:
                body = json.loads(r.read())
            if "answers" in body:
                return {"id": album["id"], "truth": album["truth"], "ok": True,
                        "response": body}
            raise RuntimeError(f"no answers in body: {str(body)[:300]}")
        except Exception as e:
            if i == attempts - 1:
                return {"id": album["id"], "truth": album["truth"], "ok": False,
                        "error": str(e)[:500]}
            time.sleep(2 ** i)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        sys.exit("OPENROUTER_API_KEY not set")

    albums = load_truth()
    if args.limit:
        albums = albums[: args.limit]
    slug = args.model.replace("/", "-").replace("~", "")
    out_path = os.path.join(ROOT, "research", f"style-ab-results-{slug}.jsonl")

    t0 = time.time()
    done = fail = 0
    with open(out_path, "w") as out, ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(call_model, api_key, args.model, a): a for a in albums}
        for fut in as_completed(futs):
            rec = fut.result()
            out.write(json.dumps(rec) + "\n")
            done += 1
            fail += 0 if rec["ok"] else 1
            if done % 25 == 0 or done == len(albums):
                print(f"{done}/{len(albums)} ({fail} failed, {time.time()-t0:.0f}s)", flush=True)
    print(f"wrote {out_path}; {fail} failures of {len(albums)}")

if __name__ == "__main__":
    main()
