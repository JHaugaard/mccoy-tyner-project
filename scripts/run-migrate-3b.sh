#!/usr/bin/env bash
# run-migrate-3b.sh — wrapper for migrate-3b-site-status.sql
# Generates the _jazzcanon_app password, runs the migration as superuser,
# and records the connection URL in .env.local (gitignored). Idempotent:
# re-running rotates the app password and updates .env.local to match.
#
# Run from the repo root:  bash scripts/run-migrate-3b.sh
set -euo pipefail

cd "$(dirname "$0")/.."

ENV_FILE=".env.local"
PASS="$(openssl rand -hex 20)"

sudo -u postgres psql -p 5433 -d postgres \
  -v apppass="$PASS" \
  -f scripts/migrate-3b-site-status.sql

# Record/update the app-role URL in .env.local
URL="postgresql://_jazzcanon_app:${PASS}@localhost:5433/postgres"
if grep -q '^JAZZCANON_APP_DB_URL=' "$ENV_FILE" 2>/dev/null; then
  sed -i "s|^JAZZCANON_APP_DB_URL=.*|JAZZCANON_APP_DB_URL=${URL}|" "$ENV_FILE"
else
  {
    echo ""
    echo "# Database — _jazzcanon app role (DML: SELECT/INSERT/UPDATE, no DELETE)"
    echo "# Used by McCoy's edit contract + builder staging. Created by migrate-3b."
    echo "JAZZCANON_APP_DB_URL=${URL}"
  } >> "$ENV_FILE"
fi

echo ""
echo "OK — migration ran; JAZZCANON_APP_DB_URL written to ${ENV_FILE}"
