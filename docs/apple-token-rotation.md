# 🔑 Apple Music token rotation (do this ~every 6 months)

**Full-album playback uses a developer token that Apple expires after ~6 months.**
When it expires, the "Play full album" / full-track buttons stop working for
subscribers (30-second previews keep working — they don't use this token).

**Current token expires: see the date printed by the script below, and the
comment next to `PUBLIC_APPLE_DEV_TOKEN` in `mccoy-tyner/.env.local`.**

If you're reading this because something broke, you probably just need to rotate.
It takes about 3 minutes (one extra step vs. before — see step 2 below, added
when this script moved to mccoy-tyner on 2026-07-01).

## How to rotate

From the mccoy-tyner repo root (`/home/john/dev/active/mccoy-tyner`) — this
script now lives here, not in jazz-canon-site:

```bash
scripts/.venv/bin/python3 scripts/gen_dev_token.py --write
```

That does two things:
1. Prints a fresh token and its new **expiry date**.
2. Updates `PUBLIC_APPLE_DEV_TOKEN` in **`mccoy-tyner/.env.local`** — this is
   NOT the file the site build reads.

You then need to carry the token across to jazz-canon-site yourself:
3. Copy the printed token.
4. Paste it into `PUBLIC_APPLE_DEV_TOKEN` in
   `/home/john/dev/active/jazz-canon-site/.env.local` (for local dev).

Then update **production**:
5. Go to your host's settings → **Environment variables** → set
   `PUBLIC_APPLE_DEV_TOKEN` to the new value.
   - Cloudflare Pages: *Settings → Environment variables → Production*
   - Fly.io: set it as a build arg / secret used at build time
6. **Redeploy** the site.

Done. Full playback works again.

## What you do NOT need to do

- You do **not** create a new key in the Apple portal.
- You do **not** touch the `.p8` file in `secrets/`.
- You do **not** change anything in the Apple Developer account.

The `.p8` private key is permanent; only the *token derived from it* expires.
The script re-signs a new token from the same key.

## If `gen_dev_token.py` errors

It needs these in `mccoy-tyner/.env.local` (already set up once):
`APPLE_MUSIC_TEAM_ID`, `APPLE_MUSIC_KEY_ID`, `APPLE_MUSIC_PRIVATE_KEY_PATH`
(pointing at `secrets/AuthKey_*.p8`, also now in `mccoy-tyner/secrets/`). If
the `.p8` is missing, recover it from your backup, or create a new MusicKit
key in the Apple Developer portal (Keys → + → MusicKit) and update
`APPLE_MUSIC_KEY_ID` + the `.p8` path.

## Why it's like this

The token is public by design (it only says "this app may use the Apple Music
API" — it can't touch anyone's account). Apple caps its lifetime, so rotation is
unavoidable. We chose the simplest approach (a baked token) over a server that
mints tokens on demand; the trade-off is this twice-a-year chore. See
`docs/data-pipeline-sop.md`.
