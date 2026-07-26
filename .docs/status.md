# Status

## Where are we?

**McCoy is built and running.** The Fable 5 build session (this one) took the
spec from last session and made all of it real, verified piece by piece:

- **Talk to it now:** type `mccoy` in any terminal on vps8 and you're chatting
  with McCoy — it queries the live canon database, answers in its own voice,
  and can make small audited edits when you ask. `docs/mccoy-runbook.md` is
  the how-to.
- **The review pipeline works end to end, proven with a real album.** *Shorty
  Rogers and His Giants* (1953) went through the whole machine — researched
  record, judged by the canon-council (two models argue for/against, a third
  writes the ballot: it scored consensus-core, must-have), and staged into the
  database as a candidate. It's sitting in your review queue right now, and it
  did NOT leak onto the public site (that gate was tested).
- **The nightly drip is scheduled.** Starting tomorrow at 6:00 AM, up to 2
  fresh candidates arrive on Telegram each morning. It stays silent when your
  queue has 10 unreviewed or there's nothing worth proposing. All the
  guardrails (dedup against everything known, the year window, the cap) are
  enforced by code, not by trusting the model.
- **The database got its queued upgrades.** Publication states
  (found → reviewed → approved → live → retired), an edit audit log, a writer
  role that physically cannot delete rows, and — held item closed — all 393
  album-level citations loaded (every one of the 100 albums now has its
  sources on record; nothing fabricated, including the 14 Kimi-only albums).
- **You steer it by editing markdown, never code:** `config/canon-rubric.md`
  (the year window and quality bar), `config/edit-contract.md` (what McCoy may
  touch), `config/gather-mission.md` (how missions run). Widening the canon to
  1975 is a one-line edit.

## Update 2026-07-17 — drip incident, repaired

The second nightly drip failed safely: it re-picked the previous night's
candidates instead of finding new ones, the database guard refused them
(nothing corrupted), but the run reported itself as a success. Root causes
found and fixed the same day:

- Deduplication is now enforced by code, not by trusting the model — the
  precheck archives already-staged files before the agent runs, and a new
  `scripts/check-candidate.py` gate must pass before any research starts.
- A refused candidate is now reported as "DRIP FAILED", never dressed up
  as a result.
- A path bug meant both drips were judged by the wrong council (the
  default one, not the canon-council). Fixed, and both queued candidates
  were re-judged by the real council — Art Blakey's *Free for All* was
  upgraded to consensus-core in the process.

## What's unresolved?

Nothing is blocked. Small open threads:

- **Three staged candidates await your verdict** — Shorty Rogers, Art
  Blakey (*Free for All*), Horace Silver (*Serenade to a Soul Sister*):
  include / reject / later. Tell McCoy in chat, or reply when a drip card
  arrives. The next drip fires 2026-07-18 06:00.
- **One untested-in-anger path:** a full interactive gather mission ("find me
  3 soul-jazz candidates from 1958–64") — every piece is verified separately,
  but the first whole run happens when you ask for one in `mccoy` chat.
- **Nothing is committed to git yet** — this session created/changed a lot
  (migration scripts, config files, the runbook, the spec now marked BUILT).
  Waiting on your say-so.
- **Two carried-over deferrals:** per-musician citations (album-level is live;
  the upgrade is additive, reminder saved) and rotating the read-only DB
  password (it's now been on screen twice).

## What's next?

If you sat down right now, in order of payoff:

1. **Type `mccoy` and review the Shorty Rogers candidate** — your first real
   include/reject through the new machinery.
2. **See what tomorrow's 6 AM drip brings** to Telegram — the first unattended
   run.
3. **Say "commit it"** here in Claude Code to get the session's work into git.
4. When you feel like it: run your first gather mission from `mccoy` chat.
