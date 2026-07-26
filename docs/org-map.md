# The Jazz Canon — Organizational Map

Written 2026-07-26 (EDT), one month in. The mental map of the enterprise:
one product, five departments, one boss. Load this when the
"which workbench / whose job is this" question comes up.

```
                        JOHN
            editor-in-chief / sole decider
     include is his; every gate move is his;
     every deploy is his nod at the preview
                          |
   +----------+-----------+-----------+--------------+--------+
   |          |           |           |              |        |
 RESEARCH  DATABASE    WEBSITE    MACHINERY      COMMS     (ADJACENT
                                                            STAFF)
```

## 1. Research department

- **People:** the `researcher` Hermes profile (narrative compiles — career
  arcs, instrument histories; e.g. Shorter arc, Paul Chambers,
  arc-of-arco) and McCoy's gather lane (album dossiers: full personnel,
  sources on every claim, obs/inf/unk labels).
- **Workbenches:** researcher compiles →
  `~/.hermes/profiles/researcher/workspace/compiles/`; album dossiers →
  `mccoy-tyner/research/candidates-inbox|archive/`.
- **Rule:** gathering is tool work with sources, never model memory.

## 2. Database department (the system of record)

- The Postgres `_jazzcanon` schema on vps8:5433. **This IS the canon;**
  everything else is a view or a work order.
- **Department head:** McCoy — reads as `_jazzcanon_ro`, writes only
  through `_jazzcanon_app` under `config/edit-contract.md` (whitelisted
  fields, one edit_log row per change, epistemic pairing: a fact edit
  carries its label and citation in the same breath).
- **The schema includes the canon** (affirmed 2026-07-26): the canon
  proper is the subset where `canon_status='included'` and
  `site_status IN ('approved','live')` — the only rows the site export
  selects. Candidates, exclusions, ballots, and rejected reasoning all
  stay in the DB permanently, export-invisible, available for research
  and semantic search. Nothing assembled is ever deleted; rejection is
  `canon_status='excluded'`, not a DELETE.
- The **canon-council** (script + model panel) judges dossiers and
  attaches ballots. It proposes; it never disposes.
- **Steering file:** `config/canon-rubric.md` — the hard gates
  (1940–1979 window, no free-jazz/fusion, drip 2, backlog cap 10).
  John's one-line edits steer the whole department. Rubric edits get
  their own git commit.

## 3. Website department

- **Repo:** `~/dev/active/jazz-canon` (Svelte+Vite, Cloudflare Pages,
  manual deploy). A static export of the database — **the gallery, not
  the workshop**. It holds no truth of its own (sole exception:
  the hand-kept `recently-added.json`, a known wart).
- A/B eval builds (`jazz-canon-site`, `-kc`, `-moa-glm52`,
  `jazz-canon-test`, `mccoy-tyner-kc` in ~/dev/active) are sandboxes,
  not production.

## 4. Machinery department (the plumbing connecting 1–3)

- **canon-drip cron** (06:00, mccoy profile): precheck → gate → gather →
  council → stage. Two candidates each morning; silence when the backlog
  cap is hit. The pace is deliberate (rubric, 2026-07-26): mastery of
  the collection outranks growth of it.
- **ship.sh** (mccoy-tyner/scripts/): export from DB → copy into site
  repo → enrich Apple previews → build → preview (John's nod) →
  wrangler deploy → approved→live.
- **Playbooks:** the `canon-drip-operations` skill; SOPs in `docs/`.

## 5. Comms

- **Current:** Vulcan owns the single Telegram channel (the drip report
  arrives there). the-beav runs messaging ops (iMessage 415-610-6180)
  and John's round-2 workflow — adjacent to the enterprise, not inside
  it. McCoy currently has no dedicated channel.
- **Coming soon (spec + runbook exist, not yet implemented):** four
  separate Telegram channels under refinement with main Hermes Agent.
  **McCoy gets a dedicated channel** — no longer sharing comms with
  Vulcan or the-beav. Update this section when the cutover lands.

## The three rules that kill HITL confusion

1. **Truth flows one direction: DB → export → site.** A fact needing
   fixing is fixed in the database via the edit contract, never in the
   site repo. The site is regenerated; the DB is curated.
2. **Status is the handoff protocol.** candidate → included (John's
   verdict) → reviewed → approved (John's greenlight) → live (only the
   deploy pipeline flips this). If you wonder "who's holding this
   album," its two status fields answer it.
3. **Repo = role.** `mccoy-tyner` = workshop (research, DB, machinery,
   config). `jazz-canon` = gallery (site code + exported data). Touching
   dossiers, rubric, DB, or scripts → mccoy-tyner. Touching layout,
   components, brand → jazz-canon. You should rarely need to be in
   jazz-canon by hand at all — ship.sh writes there for you.

## Roles in one line each

- **John** decides.
- **McCoy** curates and operates.
- **researcher** writes.
- **canon-council** advises.
- **drip** delivers.
- **ship** publishes.
- **Claude Code** is the engineering contractor for schema/pipeline/
  site-code work too deep for chat (handoffs land as notes in the repo).
- Everyone else is adjacent staff.

## Git ritual (established 2026-07-26)

- End every canon work session with `git status` in
  /home/john/dev/active/mccoy-tyner; commit what the session touched.
- Rubric/config edits get their own commit — gate moves must be
  individually auditable.
- Push to origin (github.com/JHaugaard/mccoy-tyner-project) at session
  end.

## Known future refinements (noted, not scheduled)

- A possible `canon_status='reference'` value: fully gathered albums
  held for research (e.g. a 10-album Shorter deep dive) without
  inflating the review queue or tripping the backlog cap. Schema work —
  Claude Code's lane via handoff note, when bulk research-gathering
  becomes habitual.
- The four pending follow-ups in `docs/follow-ups.md` (embeddings
  backfill, Apple preview backfill, drip source_map mismatch,
  review-process redesign).
