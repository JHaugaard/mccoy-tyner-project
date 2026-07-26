# McCoy Runbook

How to operate McCoy day to day. Built 2026-07-15; spec: `docs/mccoy-agent-spec.md`.

## Talk to McCoy

```bash
mccoy                # interactive chat (the normal way)
mccoy -z "prompt"    # one-shot: single answer, then exit
                     # (note: one-shots can't wait for delegate_task children;
                     #  anything that dispatches children needs interactive chat)
```

McCoy runs on Kimi K2.7-Code (coding plan, zero marginal cost). Its
constitution: `~/.hermes/profiles/mccoy/SOUL.md`.

## Explorer mode — just ask

- "Which albums did Elvin Jones play on, and with whom?"
- "Show me the personnel on Speak No Evil."
- "Fix the year on <album> — it should be 1958." (edit contract: McCoy
  shows the current value, asks for the source, logs to `edit_log`.)
- Semantic search: "find albums that feel like spiritual modal piano" —
  McCoy runs `scripts/canon-search.py` (also works from your shell).

## Canon Builder — missions

In `mccoy` chat: *"Run a gather mission: 3 soul-jazz candidates from
1958–1964."* McCoy follows `config/gather-mission.md`: dedup → children
research (web+file) → inbox JSON → canon-council ballot → staged as
candidate/found → cards to you. Children take minutes each; leave the
chat open (delegation results re-enter the conversation when done).

## The nightly drip

- Job `canon-drip`, default profile scheduler, 06:00 daily, delivers to
  Telegram. Up to 2 candidates/night; silent when your review backlog
  hits the cap or there's nothing worth proposing.
- **Review**: reply in Telegram (or tell McCoy in chat): *include /
  reject / later*, per album. Rejections should include a reason — it
  feeds `research/cull-notes.md`.
- Manage: `hermes cron list` · `hermes cron pause canon-drip` ·
  `hermes cron run canon-drip` (fire once, now).
- Guardrails are code, not trust: `~/.hermes/scripts/canon-drip-precheck.py`
  computes the dedup list and the backlog cap before the agent reasons.

## Steering McCoy (edit markdown, never code)

| File | Controls |
|---|---|
| `config/canon-rubric.md` | scope window (`year_min`/`year_max`), excluded styles, drip size, backlog cap, what "canonical" means |
| `config/edit-contract.md` | which fields McCoy may edit, status-transition rules |
| `config/gather-mission.md` | how missions run, bounds, verdict handling |
| `~/.hermes/profiles/mccoy/SOUL.md` | voice + non-negotiables |

Widening the canon (e.g. 1972 → 1975): edit `year_max` in the rubric.
That's the whole change.

## Review → site pipeline

Candidate flow: `found` → (you look) `reviewed` → (you greenlight)
`approved` → `ship.sh` publishes → `live`. The static export only ships
albums that are `included` **and** `approved|live` — staged candidates
can never leak onto the site.

After including an album: run `sudo -u postgres /tmp/pg-venv/bin/python3
/tmp/embed.py` (see `scripts/embed.py` header) so search covers it, then
`scripts/ship.sh` when you want it on the site.

## Under the hood (when something breaks)

- DB roles: `_jazzcanon_ro` (reads), `_jazzcanon_app` (McCoy's writes —
  no DELETE), `_jazzcanon_role` (owns everything; migrations only).
  URLs in `.env.local` and `~/.hermes/profiles/mccoy/.env`.
- Judge manually: `~/.hermes/scripts/canon-council.py <dossier.json>`
  (add `--raw` to see the full reference arguments on stderr).
- Stage manually: `python3 scripts/stage-candidate.py --dry-run <file>`.
- Council preset: `moa.presets.canon-council` in
  `~/.hermes/profiles/mccoy/config.yaml` (refs DeepSeek V4-Pro +
  Gemini 3.1 Pro via Nous; aggregator GPT-5.6 Terra via Codex OAuth).
- Rotate the app-role password: `bash scripts/run-migrate-3b.sh`
  (idempotent; updates `.env.local` — then copy the new URL into
  `~/.hermes/profiles/mccoy/.env`).
