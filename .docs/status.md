# Status

## Where are we?

Phase 3 (Data Model & Schema) is now designed — and a few foundational questions that had been
floating got settled. We did this "contract-first": there's still no album data (Phase 1 and 2
haven't been run), so the schema was built against the two research schemas, which define the shape
the data will take.

Three things got decided up front. **Where the data lives:** this project gets its own schema inside
the shared Postgres database on vps8 — not its own separate database, and not dumped in among other
projects' tables. It's the same pattern the `_foundry` substrate already uses: shared infrastructure
(backups, pgvector, cron all already installed) with a clean wall around this project's tables.
**What it's called:** the official database name is now `_jazzcanon`; "mccoy-tyner" stays as the
casual working codename for as long as you like. The one naming question still open is the
*public-facing product name*, which doesn't need deciding yet. **How search works:** two engines —
one for "find albums/musicians like this" (vector similarity), one for the network questions like
six-degrees-of-McCoy-Tyner and musician timelines (regular SQL). Because the collection is small
(~100 albums), the app can ship as a simple static site with all the discovery features baked in.

The schema itself is complete: albums, people, tracks, sessions, who-played-what, production credits,
and full source-and-confidence tracking on every fact. The most important design choice was treating
performers, producers, engineers, and composers as one unified "person" — that's what makes questions
like "every album this engineer touched" or "every tune this person composed" answerable at all.

Separately, we designed a new **Canon Orchestrator** agent. The original plan had you personally
reading ~200 raw album candidates to cull down to 100. The Orchestrator does the clerical 90% —
merging the three specialists' lists, resolving overlaps, arguing the borderline cases — and hands
you a tidy ballot: rubber-stamp the ~65 obvious picks, rule on ~40 pre-argued judgment calls. It
never makes the final call itself; that stays yours.

Everything is written but **not yet committed to git** — that's your call.

## What's unresolved?

- **Commit the work?** Phase 3 docs and the Orchestrator brief are sitting in the working tree, ready
  when you want them in git.
- **A few Phase-4 questions, none urgent:** whether album/musician "fingerprints" stay private to this
  project or also feed the cross-project search system; whether the app ever needs a live "type a
  sentence" search box or can stay fully static; and the public-facing product name.
- **How far to reach into Phase 4** next time — you said we'd decide that together once Phase 3 was
  done.

## What's next?

If you sit down fresh: skim `docs/schema.md` (the design, in plain-ish terms) and the
`canon-orchestrator-brief.md`, decide whether to commit, then tell me how much of Phase 4 (the web
app's architecture and the data-loading/search build) you want to plan. The actual album research
(Phase 1) still hasn't launched — that's a separate "go" whenever you're ready to dispatch the
specialist agents and the new Orchestrator.

Resume this session with: `claude --resume fcc33e4f-9a0f-41ce-9d52-9fb7379f0fce`
