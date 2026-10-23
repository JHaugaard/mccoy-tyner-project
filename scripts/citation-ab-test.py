#!/usr/bin/env python3
"""A:B test 2 — citation/evidence audit via Noul questions.

For each claim in research/citation-ab-claims.json, the model is shown the
dossier's source map (titles + types only) and asked: is this claim
explicitly evidenced by the source map? Ground truth per the claims file.

Usage:
  OPENROUTER_API_KEY=... python3 scripts/citation-ab-test.py --model typesafe/jev-1.14

Writes research/citation-ab-results-<slug>.jsonl
"""
import argparse, json, os, sys, time
from urllib import request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAIMS_PATH = os.path.join(ROOT, "research", "citation-ab-claims.json")
DOSSIER_DIR = os.path.join(ROOT, "research", "candidates-archive")

INSTRUCTIONS = (
    "A candidate dossier's rationale asserts the claim below. Is the claim "
    "explicitly evidenced by at least one entry in the dossier's source map? "
    "Judge ONLY whether the source map carries this claim — not whether the "
    "claim is true in the world. A rating or accolade claim requires a "
    "source-map entry described as carrying that rating or review."
)
CRITERIA = {
    "true": "A source-map entry's description explicitly covers this claim.",
    "false": "No source-map entry evidences this claim; it may be true in the world, but the dossier does not cite it.",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--claims", default=CLAIMS_PATH,
                    help="claims JSON file (default: the Test 2 file)")
    ap.add_argument("--tag", default="",
                    help="tag inserted into the results filename, e.g. -test3")
    ap.add_argument("--append", action="store_true",
                    help="append to results file instead of overwriting")
    args = ap.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        sys.exit("OPENROUTER_API_KEY not set")

    spec = json.load(open(args.claims))
    # Two shapes: single-dossier {"dossier": ..., "claims": [...]} (Tests 1-2)
    # or multi {"sets": [{"dossier": ..., "claims": [...]}]} (Test 3+).
    sets = spec.get("sets") or [{"dossier": spec["dossier"], "claims": spec["claims"]}]

    slug = args.model.replace("/", "-").replace("~", "")
    out_path = os.path.join(ROOT, "research", f"citation-ab-results{args.tag}-{slug}.jsonl")
    mode = "a" if args.append else "w"
    with open(out_path, mode) as out:
        for s in sets:
            dossier = json.load(open(os.path.join(DOSSIER_DIR, s["dossier"])))
            source_map = {k: {"title": v["title"], "type": v["type"]}
                          for k, v in dossier["sources"].items()}
            for c in s["claims"]:
                cid = f"{s['dossier'].split('.')[0]}::{c['id']}"
                payload = json.dumps({
                    "model": args.model,
                    "state": {"claim_under_audit": c["claim"], "source_map": source_map},
                    "questions": {"evidenced": {
                        "type": "noul", "instructions": INSTRUCTIONS,
                        "criteria": CRITERIA}},
                }).encode()
                for attempt in range(4):
                    try:
                        req = request.Request(
                            "https://openrouter.ai/api/alpha/decisions", data=payload,
                            headers={"Authorization": f"Bearer {api_key}",
                                     "Content-Type": "application/json"})
                        with request.urlopen(req, timeout=60) as r:
                            body = json.loads(r.read())
                        ans = body["answers"]["evidenced"]
                        print(f"{cid}: p(yes)={json.dumps(ans)[:120]}  truth={c['truth']}")
                        out.write(json.dumps({"id": cid, "claim": c["claim"],
                                              "truth": c["truth"], "why": c["why"],
                                              "response": body}) + "\n")
                        break
                    except Exception as e:
                        if attempt == 3:
                            print(f"{cid}: FAILED {e}")
                            out.write(json.dumps({"id": cid, "truth": c["truth"],
                                                  "error": str(e)[:400]}) + "\n")
                        time.sleep(2 ** attempt)
    print(f"wrote {out_path}")

if __name__ == "__main__":
    main()
