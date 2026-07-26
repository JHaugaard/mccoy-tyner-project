# A Jazz Canon — Organizational Map

Written 2026-07-26 (EDT) by McCoy, one month in. The mental map of the
enterprise: one product, five departments, one boss. Load this when the
"which workbench / whose job is this" question comes up.

Reviewed and amended by Claude Code the same day (schema-update session).
The departments, roles, and rules 1 and 3 were accurate as written and are
unchanged. Rule 2 was rewritten — it drew the two status axes as a single
chain, which is structurally wrong. `edit_log` was added to the database
department, the git ritual gained the one-repo-per-turn rule, and the
follow-ups list was refreshed.

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
- **`edit_log` is the audit spine, and it is where a decision becomes a
  fact.** Every write carries a row: who, which record, which field, old
  value, new value, why. It is append-only for the app role — `_jazzcanon_app`
  has INSERT and SELECT but deliberately no UPDATE, so a correction is a new
  row, never an amendment to history. This is what makes "John decided X"
  durable rather than inferred, and it is the reason a verdict must be
  *communicated* to be real: an unrecorded decision did not happen.
- **The schema includes the canon** (affirmed 2026-07-26): the canon
  proper is the subset where `canon_status='included'` and
  `site_status IN ('approved','live')` — the only rows the site export
  selects. Candidates, exclusions, ballots, and rejected reasoning all
  stay in the DB permanently, export-invisible, available for research
  and semantic search. Nothing assembled is ever deleted; rejection is
  `canon_status='excluded'`, not a DELETE.
- The **canon-council** (script + model panel) judges dossiers and
  attaches ballots. It proposes; it never disposes. Since migrate-4a
  (2026-07-26) the ballot's argument lives in the database as
  `album.case_for` / `album.case_against`, not only in the dossier JSON —
  so the deliberation is SQL-queryable and part of the semantic index.
  The dossiers remain the archival source; the columns are a projection.
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
2. **Status is the handoff protocol — and it is two dials, not one
   chain.** This section previously drew a single line from `candidate`
   through to `live`. That reads well and is structurally wrong; the two
   fields are orthogonal by design (migrate-3b says so explicitly).

   - **`canon_status`** answers *is it in the canon?* —
     `candidate → included | excluded`. This is John's editorial verdict,
     human-only, and it is irreducibly per-album.
   - **`site_status`** answers *where is it in the publication pipeline?* —
     `found → reviewed → approved → live | retired`. This is logistics:
     what gets published, and when. Only the deploy pipeline flips `live`.

   Neither implies the other. An album can be `included` and still sit at
   `found`. The export gate reads **both** —
   `canon_status='included' AND site_status IN ('approved','live')` — which
   is why one dial alone never tells you whether something is public. To
   ask "who's holding this album," read both fields.

   **Open question (feeds follow-ups #4):** `site_status='reviewed'` is
   defined as "John has looked at it; not yet greenlit," which is close to
   the same event as the `included` verdict. Today nothing distinguishes
   them and `reviewed` is unused in practice. Either it means something the
   canon verdict doesn't, or it should go. John's call.
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
- **One repo per turn.** Commits and pushes stay scoped to the repo that
  was actually touched; never push `mccoy-tyner` and `jazz-canon` in the
  same turn. `ship.sh` is the sanctioned path into the site repo. This
  matters more now the site is live — a cross-repo push is how an
  unreviewed change reaches production sideways.

## Known future refinements (noted, not scheduled)

- A possible `canon_status='reference'` value: fully gathered albums
  held for research (e.g. a 10-album Shorter deep dive) without
  inflating the review queue or tripping the backlog cap. Schema work —
  Claude Code's lane via handoff note, when bulk research-gathering
  becomes habitual.
- The open follow-ups in `docs/follow-ups.md`. As of 2026-07-26 two are
  closed (#1 embeddings backfill — all 121 albums and 629 persons now
  embedded; #5 dead search-source views — dropped by migrate-4b) and three
  remain: **#2** Apple preview backfill, **#3** drip `source_map` key
  mismatch, **#4** review-process redesign. #4 is the live one — see the
  open question under rule 2 above.
