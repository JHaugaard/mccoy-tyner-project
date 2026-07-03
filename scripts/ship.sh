#!/usr/bin/env bash
# One transparent command: publish the contract, build the site, (preview),
# deploy to jazzcanon.com, verify. Preview pause is ON by default; pass --go
# to skip it. Data is committed by publish; deploy uses wrangler (not git).
set -euo pipefail

PLATFORM="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$HOME/dev/active/jazz-canon"
GO=0; case "${1:-}" in --go|--no-preview) GO=1 ;; esac

"$PLATFORM/scripts/publish.sh"

cp "$PLATFORM/exports/jazz-canon/"albums.json  "$SITE/app/public/data/"
cp "$PLATFORM/exports/jazz-canon/"details.json "$SITE/app/public/data/"
cp "$PLATFORM/exports/jazz-canon/"graph.json   "$SITE/app/public/data/"
echo "✓ Copied contract into site"

cd "$SITE/app"
npm run build >/dev/null
echo "✓ Built site (app/dist/)"

if [ "$GO" -eq 0 ]; then
  echo "… Preview at http://vps8-core:4173 — review it in your browser."
  npm run preview -- --host >/tmp/jazzcanon-preview.log 2>&1 &
  PREV=$!
  trap 'kill "$PREV" 2>/dev/null || true' EXIT
  read -rp "Press [Enter] to deploy to jazzcanon.com, or Ctrl-C to abort... "
  kill "$PREV" 2>/dev/null || true
  trap - EXIT
fi

set -a; source "$SITE/.env"; set +a
npx wrangler pages deploy dist --branch main
code="$(curl -s -o /dev/null -w '%{http_code}' https://jazzcanon.com/)"
if [ "$code" = "200" ]; then
  echo "✓ Deployed & verified (HTTP $code) — https://jazzcanon.com"
  echo "✓ Done. Data already committed by publish; deploy is not a git act."
else
  echo "✗ Verify FAILED: HTTP $code — check the Cloudflare dashboard / rollback if needed" >&2
  exit 1
fi
