#!/usr/bin/env bash
# run-migrate-5a.sh — wrapper for migrate-5a-studio-places.sql
# Adds studio.kind / address / location_epistemic / location_source.
# Schema only — no data is written; run scripts/studio-cleanup-2026-08-14.sql after.
#
# Run from the repo root:  bash scripts/run-migrate-5a.sh
#
# No roles or credentials touched. Superuser is needed only to
# SET ROLE _jazzcanon_role, which owns studio.
set -euo pipefail

cd "$(dirname "$0")/.."

sudo -u postgres psql -p 5433 -d postgres \
  -v ON_ERROR_STOP=1 \
  -f scripts/migrate-5a-studio-places.sql

echo ""
echo "OK — migration 5a applied."
echo "Next: psql \"\$JAZZCANON_APP_DB_URL\" -f scripts/studio-cleanup-2026-08-14.sql"
