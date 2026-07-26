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

# Apple 30-sec preview URLs are not in the DB — fetch them from iTunes and write
# them into the site's details.json. Best-effort (resilient to per-album misses);
# non-fatal so a network hiccup can't block a ship — but the preview pause below
# is your chance to confirm previews actually play before deploying.
echo "… Enriching Apple previews (iTunes lookup; needs internet)…"
node "$SITE/scripts/enrich-previews.mjs" || echo "⚠ preview enrichment incomplete (non-fatal) — verify at the preview before deploying"
echo "✓ Previews enriched"

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
  # Publication axis: what was approved is now live (spec §5; edit-contract.md —
  # this flip belongs to the publish pipeline, not chat). Audited in edit_log.
  APP_URL="$(grep -E '^JAZZCANON_APP_DB_URL=' "$PLATFORM/.env.local" | cut -d= -f2- || true)"
  if [ -n "$APP_URL" ]; then
    flipped=$(psql "$APP_URL" -X -At <<'SQL'
WITH f AS (
  UPDATE _jazzcanon.album SET site_status='live'
   WHERE canon_status='included' AND site_status='approved'
  RETURNING id
), logged AS (
  INSERT INTO _jazzcanon.edit_log (editor, table_name, record_id, field, old_value, new_value, reason)
  SELECT 'ship.sh', 'album', id, 'site_status', 'approved', 'live', 'published by ship.sh deploy'
    FROM f RETURNING 1
)
SELECT count(*) FROM f;
SQL
)
    [ "$flipped" != "0" ] && echo "✓ site_status: $flipped album(s) approved → live"
  fi
  echo "✓ Done. Data already committed by publish; deploy is not a git act."
else
  echo "✗ Verify FAILED: HTTP $code — check the Cloudflare dashboard / rollback if needed" >&2
  exit 1
fi
