#!/bin/zsh
# disco snap helper — capture the Disco app window into the ui-reference folder.
# Usage:
#   ./snap.sh <label>          # bring Disco to front, capture immediately
#   ./snap.sh <label> -t       # timed: 4s delay, no raise (for hover/menu states)
#
# Files are named NN-<label>.png with an auto-incrementing 2-digit index.

set -e
DIR="${0:A:h}"
LABEL="${1:-shot}"
MODE="${2:-}"

# next index
last=$(print -rl -- "$DIR"/[0-9][0-9]-*.png(N) | sed -E 's|.*/([0-9]+)-.*|\1|' | sort -n | tail -1)
next=$(printf "%02d" $(( ${last:-0} + 1 )))
OUT="$DIR/${next}-${LABEL}.png"

if [[ "$MODE" == "-t" ]]; then
  echo "Timed capture in 4s — set up the hover/menu state now…"
  screencapture -T 4 -x "$OUT"
else
  osascript -e 'tell application "System Events" to set frontmost of (first process whose name is "Disco") to true'
  sleep 0.6
  screencapture -x "$OUT"
fi

echo "$OUT"
