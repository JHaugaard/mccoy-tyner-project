# McCoy — Hermes Agent Profile Spec (v1.0 — BUILT)

> **Status:** Built by Claude Code (Fable 5), 2026-07-15, from the v0.3 draft.
> All §10 steps executed; Round-3 build decisions logged in §11. The profile
> constitution (`~/.hermes/profiles/mccoy/SOUL.md`), rubric
> (`config/canon-rubric.md`), edit contract (`config/edit-contract.md`), and
> mission playbook (`config/gather-mission.md`) are live. Nightly drip
> scheduled (job `canon-drip`, 06:00, telegram).
> Markers used throughout:
> **⚑ OPEN** = a decision that still needs John's call (or Fable's judgment).
> **[Fable]** / **[Opus]** / **[Sonnet]** = suggested model tier for that piece of work.

---

## 1. One-sentence objective

**McCoy is a first-class Hermes agent profile that serves as John's private,
conversational front-end to the live jazz-canon database (`jcdb`) — for
exploration and light editing — and as the curator-driven engine that brings
sourced candidate albums forward for possible inclusion in the canon and on the
public site.**

Name: **McCoy** (after McCoy Tyner; the profile is the agent, `mccoy-tyner` stays
the project codename). Modeled on the existing Hermes **Vulcan** profile.
*Decided 2026-07-15.*

---

## 2. What McCoy is — and is not

| McCoy IS | McCoy is NOT |
|---|---|
| John's **private** conversational interface to the **live** `jcdb` | The **public** website (`jazz-canon-site` — a static JSON snapshot) |
| Read-first, with a **scoped, audited** write path | A blanket-writable admin panel |
| A **candidate finder** that proposes to a review queue | An autonomous curator — `include` is always John's decision |
| A Hermes profile (persona + tools + guardrails) | A new app or service to host |

The public static site and McCoy are two consumers of one source of truth. The
**publication axis** (see §5) is the gate between the live DB and the public
export.

---

## 3. Two modes, one profile

McCoy is a single Hermes profile that operates in two modes with **different DB
identities and different stakes**.

### Mode A — Explorer (read, and light edit)
- Free-form poking around the canon: albums, musicians, sideman networks,
  composer works, timelines — all already exposed as `v_*` views (§6).
- Q&A, link-forming for writing ideas, semantic search over `search_document` /
  `embedding`.
- **Light editing**: "fix/update one bit of information on a record" via a
  scoped **edit contract** (§7), not a general write surface.
- Default DB identity: read-only; edits escalate to the app role for the one
  whitelisted mutation.

### Mode B — Canon Builder (propose candidates)
Two dispatch shapes, both landing candidates in a **review queue**, never in the
canon directly:
1. **Mission** — "go add 10 hard-bop candidates from 1961–63" / "fill the gaps in
   soul-jazz." Bulk, bounded, on demand.
2. **Nightly drip** — an automated task that surfaces **~2 candidates/night**
   against a written rubric, for John's review. Purpose is *engagement pacing*:
   keep John returning regularly and the canon growing, without a firehose.

Both modes gather each candidate's **full personnel_record in one pass** (the
"merge" — the specialist collects personnel while it researches the album), so a
review is a genuine yes/no, not a "now go do the work."

---

## 4. Guardrails (non-negotiable)

1. **`include` stays John's.** McCoy proposes; John promotes. No auto-inclusion.
2. **Scope discipline — non-negotiable *when set*, but movable without breaking
   anything.** The boundaries live as **editable fields in the rubric config**
   (`year_min`, `year_max`, `excluded_styles`), NOT in schema or code. McCoy
   enforces whatever is *currently* set as a hard gate — a candidate outside the
   window is refused, no exceptions. But moving the window is a one-line config
   edit with **zero migration**: `album.year`'s only DB constraint is
   `1900–2100`, so widening (e.g. 1972→1975, or pushing back into bebop at 1940)
   can never break existing data. Current window: **1940–1972, no Free Jazz**
   (John expects this to widen soon — the design assumes it will).
3. **Source-grounding is preserved.** Every candidate carries epistemic labels
   (`obs`/`inf`/`unk`) and citations. Hand-edits that change a *fact* must update
   its epistemic label / citation too, or provenance rots.
4. **Derived fields are never hand-edited.** `embedding`, `search_document` are
   regenerated, not typed.
5. **Backlog cap.** The nightly drip cannot outrun John's review — it stops
   proposing when the queue hits **10** unreviewed candidates. *Decided 2026-07-15.*
6. **Dedup.** Candidates are checked against the existing 100 **and** the ~19
   already-identified next-batch before surfacing.

---

## 5. Schema readiness — findings and the one change needed

Live inspection of `jcdb` on 2026-07-15:

### Genres — already fully extensible ✅ (no change)
`style` is a **lookup table** (`code`, `display_name`, `description`);
`album_style` is many-to-many with `is_primary`. Adding a genre is one `INSERT`.
No enum, no ceiling. Current five: cool-jazz, hard-bop, modal-jazz, post-bop,
soul-jazz. (Aside: `instrument_family` *is* a hardcoded enum; exotic instruments
fall to `other` — fine for now.)

### Curation lifecycle — already modeled ✅ (no change)
`album.canon_status` is an enum `candidate → included → excluded`, **defaulting to
`candidate`**. The schema was built expecting candidates to flow in and be
promoted. **This means the builder's staging is already modeled**: a new find is
`INSERT … canon_status='candidate'`; John's include gate is the flip to
`included`. `canon_tier` (`consensus_core`/`contested`/`scope_call`/
`exclude_suggested`) and `priority` (`must_have`/`strong`/`consider`) already
exist to carry the ballot.

### Publication lifecycle — **the one real gap** ⚑
John's desired states — found / reviewed / approved-for-site / on-site — are a
**second, orthogonal axis**. An album can be `included` in the canon yet not built
onto the site. Do **not** overload `canon_status`.

**Recommendation [Opus]:** add a separate **`site_status`** for the publication
pipeline, and model it as a **lookup table** (like `style`), *not* an enum —
because Postgres enums can't drop values or be altered inside a transaction,
whereas a lookup table John can edit as config. This axis is what the static
export (§6) filters on.

**Decided 2026-07-15 — five states:** `found → reviewed → approved → live →
retired`. Meanings: `found` (surfaced by builder) · `reviewed` (John has looked)
· `approved` (greenlit for site) · `live` (on the public site) · `retired`
(pulled from site, kept in DB). **Export filter = `approved` OR `live`.**

### The two held `jcdb` fixes — now load-bearing, fold into this work
- **Ownership (held item 2):** the mandated owner role `_jazzcanon_role` **does
  not exist**; schema + all objects are owned by `postgres`. The owner role is a
  **prerequisite** for every migration below (adding `site_status`, etc.). Create
  it and reassign ownership *scoped to `_jazzcanon` only* (never
  `REASSIGN OWNED BY postgres` on this shared instance). **[Sonnet]** once
  approved.
- **Citations (held item 1):** `source` and `citation` tables are empty — the
  ingest never populated them. The raw provenance exists (per-record `sources:
  ["S1",…]` in `canon-draft.json`; the S-token legends live in the nine
  `research/*-candidates*.md` files, scoped per file). A source-grounded builder
  **has nowhere to put citations** until these tables are part of the write
  contract. **Decided 2026-07-15: album-level for v1** (`citation.album_id`
  filled; per-line FKs left null). Per-line is a deferred, **purely-additive**
  backfill — the `source` registry is built once in v1 and reused unchanged; the
  upgrade is one re-runnable script (`scripts/citation-backfill.py --depth
  per-line`), triggered when the UI needs per-musician citations or to restore
  parity with the builder's per-line output. **[Sonnet]** backfill.

**Both held fixes greenlit for the build sequence 2026-07-15.**
✅ **Ownership DONE 2026-07-15** — `_jazzcanon_role` created (NOLOGIN owner), all
44 objects (20 tables, 13 views, 6 sequences, 1 function, 10 types) reassigned
from `postgres`; `_jazzcanon_ro` preserved. Ran via `scripts/fix-ownership.sql`.
✅ **Citation backfill DONE 2026-07-15 (build day)** — `scripts/citation-backfill.py`
executed: 191 sources, 393 album-level citations, 100/100 albums covered, 0
anomalies; all 14 kimi-only albums resolved to real sourced citations from the
`mccoy-tyner-kc` twin (nothing fabricated). Idempotency verified (second
`--execute` creates 0). Per-line upgrade remains the deferred additive backfill.

---

## 6. Read contract — mostly already built ✅

`jcdb` already exposes **13 `v_*` views** that form a clean read surface:
`v_album_card`, `v_album_detail`, `v_album_personnel`, `v_track_personnel`,
`v_musician_albums`, `v_musician_timeline`, `v_sideman_network`,
`v_composer_works`, `v_engineer_sessions`, `v_collection_albums`,
`v_album_primary_art`, `v_album_search_source`, `v_person_search_source`.

The Explorer reads these + semantic search over `album.embedding` (768-dim, HNSW
index already present). **No new read modeling required** to stand up Mode A.

The public **static export** (`export.sh` → `jazz-canon-site/data/*.json`) is a
separate, existing pipeline; McCoy does not replace it. `site_status` becomes its
inclusion filter.

---

## 7. Write contract — the linchpin

Everything write-related (UI edits **and** builder staging) shares one design.
This is the single most important section for the spec to nail.

### Role model (matches John's `database-conventions.md`)
| Role | Type | Used by | State |
|---|---|---|---|
| `_jazzcanon_role` | NOLOGIN **owner** | migrations | **create (held item 2)** |
| `_jazzcanon_ro` | read-only | Explorer default | exists ✅ |
| `_jazzcanon_app` | DML grants, **no ownership** | UI edits + builder staging | **create** |

### Edit contract (Mode A writes)
- **Whitelist** of hand-editable fields (e.g. `title`, `year`, a personnel line's
  instrument). Derived fields (`embedding`, `search_document`) excluded.
- **Audit:** `updated_at` already exists on `album`; add an **`edit_log`**
  (who/what/old→new/when) so manual touches are traceable.
- **Epistemic pairing:** editing a *fact* prompts for its epistemic label /
  citation update.

### Staging contract (Mode B writes)
- Candidate = `INSERT … canon_status='candidate'` + full `personnel_record` +
  `citation` rows (depth per §5 ⚑) + `canon_tier`/`priority` from the ballot.
- Promotion (`candidate → included`) is a **John-only** action, surfaced in the
  review queue.

**Decided 2026-07-15: direct-to-tables.** McCoy holds `_jazzcanon_app` and writes
through the whitelisted edit contract directly. No thin API — the public site is
a read-only static export and never writes, so the API's only justification
doesn't apply. Fits the single-user model; less to build and maintain.

---

## 8. Canon Builder — researcher architecture (Mode B internals)

The builder runs in **Hermes** (v0.18), not Claude Code. It is **one lead agent
in charge** — McCoy's builder mode itself; no separate standing "Researcher"
profile — that fans work across **two structurally different lanes.** The key
insight: **MoA and parallel research are not the same mechanism**, and mixing
them up is the trap.

### The two lanes

```
McCoy (builder mode) = the lead researcher, in charge
│
├── GATHER lane — tool-driven, PARALLEL, via Hermes `delegate_task(batch)`
│     Spawns child agents (isolated context, toolsets ["web","file"], no recursion).
│     Each child: a batch of albums + docs/personnel-contract.md → structured
│     personnel records in one pass (the "merge"). This is the old
│     jazz-personnel-researcher pattern, now Hermes-native.
│     WHY NOT MoA: MoA reference models are stripped of all tools — they answer
│     from parametric memory, i.e. they hallucinate personnel. That is the exact
│     transcription trap the project guards against. Gathering MUST be real tool
│     work, so it uses delegation, never MoA.
│
└── JUDGE lane — reasoning-driven, MULTI-PERSPECTIVE, via a named MoA advisory preset
      "canon-council": 2 diverse-family references argue case-for / case-against
      → aggregator synthesizes a ballot (tier + priority) → McCoy records it.
      Runs PER-CANDIDATE (decided 2026-07-15). This is the jazz-canon-orchestrator
      decision-compression layer, now multi-model. `include` stays John's — the
      council proposes a ballot, never sets include.
```

This **collapses the five genre-specific researchers into one lead + a rubric**:
genre becomes a *dispatch parameter* (and a scope field in the movable rubric,
§4), not five agent files.

### Runtime model layer (decided 2026-07-15)

Assigned by **cost-shape**: high-volume tool roles → the zero-marginal Kimi plan;
low-volume no-tool roles → pay-per-use frontier. No Claude models in Hermes (cost).

| Role | Fires | Needs | **Model** | Provider | Rationale |
|---|---|---|---|---|---|
| **Gatherer** (delegate children) | High (parallel) | tool-calling, web | **Kimi K2.7-Code** | Kimi plan | The volume slot — zero marginal cost; proven tool-caller. What the annual plan is *for*. |
| **Lead/Actor** (McCoy builder) | Med | agentic, tools | **Kimi K2.7-Code** | Kimi plan | One consistent, free, tool-reliable backbone. Optional GPT override for heavy missions. |
| **Judge ref #1** (skeptic) | Low (per-cand.) | critical reasoning | **DeepSeek V4-Pro** | Nous | Argues *against*. Low volume fits $20/mo credits. |
| **Judge ref #2** (generalist) | Low (per-cand.) | broad knowledge | **Gemini 3.1 Pro** | Nous | Argues *for*; different family — diversity is the value. |
| **Aggregator** (ballot) | Low (per-cand.) | fair synthesis | **GPT-5.6 Terra** | OpenAI OAuth | Single-shot text synthesis = Terra's "scoped review" sweet spot; Sol's long-horizon edge is unused here, so half-price Terra is the disciplined pick. **Kimi = declared fallback** if OpenAI access lapses. |

Notes: **Tool-calling reliability concentrates entirely on Kimi** (gather+lead);
references + aggregator are text-only in advisory mode, so their tool ability is
irrelevant — which is why fluid-availability GPT and rare-credit Nous are safe
there. **OpenRouter** = pure overflow (e.g. mission fan-out past Kimi rate limits).

### Why 2 references, not 3 (decided 2026-07-15)
The canon call is a *bounded* judgment (in-scope? canon-worthy?), not open-ended
generation where MoA diversity pays most. Two diverse voices + a synthesizer =
a real for/against panel that operationalizes "don't erase disagreement," at
lower per-candidate latency/cost. Matches John's own `general` preset (2 refs).
Earn a 3rd only if the two consistently agree *and* miss things.

### The nightly drip = one scheduled invocation of the above
Runs via **Hermes cron** (`hermes cron create`), not system crontab — the
scheduled task *is* an agent run, with native model choice, skill loading, and
delivery. Rides existing Hermes infrastructure (**confirm the scheduler runs
persistently** before committing — the one footprint check).

```bash
hermes cron create "0 6 * * *" \
  "Run the canon nightly drip: propose up to 2 in-scope, deduped, fully-gathered,
   sourced candidates per the rubric. If backlog cap reached, respond [SILENT]." \
  --script ~/.hermes/scripts/canon-drip-precheck.py \
  --skills "research-workflows" --name "canon-drip" --deliver telegram
```

- **06:00** so fresh candidates wait at day-start. *Decided 2026-07-15.*
- **`--script` precheck enforces two guardrails as deterministic code, not LLM
  trust:** it queries `jcdb` for the existing 100 + 19 next-batch → builds the
  **dedup exclusion list** (§4 #6), and checks the **backlog cap** (§4 #5) → emits
  `[SILENT]` if ≥10 unreviewed already queued. Agent only reasons.
- **`--deliver`** is the review surface (Telegram, or `local` → a file McCoy reads
  in Explorer mode). `[SILENT]` = quiet nights stay quiet.
- **Rubric:** the markdown config McCoy loads each run (scope window, no-style-
  quota, priority signals, "what canonical means here"). John edits it to steer
  without code. **[Fable]** to author — judgment compounds over every candidate.
- **Review surface / learning loop:** each queued card shows case-for/against,
  tier, priority, sources, gathered personnel — one keystroke to include/reject.
  Rejections feed the cull-notes loop (`research/cull-notes.md`).

---

## 9. Building McCoy — model tiering (Claude Code, build-time only)

**Distinct from §8's runtime layer.** §8 is what McCoy runs *on* (Hermes: Kimi /
Nous / GPT-Terra). This section is how we *build* McCoy, in Claude Code, per
John's `model-selection.md` (no automatic routing; subagents inherit unless set):

- **Schema/migrations/wiring → Sonnet.** Bounded, evidenced (steps 3b–3f, §10).
- **Design judgment / synthesis / final review → Opus.**
- **Profile constitution + `canon-council` rubric → Fable** in its window — where
  taste compounds. **Never inherit Fable into subagents** (burns metered credits);
  when a Fable session dispatches, subagents still get Sonnet/Opus.

---

## 10. Build sequencing

1. **Now, on Opus:** this spec (done in draft), including the schema/write-
   contract layer.
2. **Fable window (through ~Jul 19):** John takes §4 guardrails, §8 rubric, and
   the **profile constitution** to Fable to stress-test and elevate. Everything
   Fable produces is captured to disk immediately so the build can continue on
   plan-covered models after the window.
3. **Build, plan-covered — ALL DONE 2026-07-15 (Fable 5 lead + Sonnet subagents):**
   a. ✅ owner role + ownership reassign (held item 2).
   b. ✅ `site_status` axis + `_jazzcanon_app` role + `edit_log`
      (`scripts/migrate-3b-site-status.sql` via `run-migrate-3b.sh`; grants
      verified live). Plus the `export.sh` publication gate (§11 #15).
   c. ✅ Citation/source backfill, album-level (`scripts/citation-backfill.py`,
      executed + idempotency-verified).
   d. ✅ Explorer mode — `mccoy` profile live (SOUL.md constitution, Kimi lead,
      verified identity + live DB read); `scripts/canon-search.py` semantic
      search verified.
   e. ✅ `canon-council` preset (in the *mccoy profile* config, §11 #16) +
      `~/.hermes/scripts/canon-council.py` JUDGE runner, verified end-to-end
      (real ballot). GATHER lane verified (child spawn → web_search/web_extract
      → file write). Full pipeline validated by staging a real candidate
      (Shorty Rogers and His Giants, 1953: dossier → real ballot →
      `stage-candidate.py` → candidate/found in DB → export unchanged at 100).
   f. ✅ Nightly drip: job `canon-drip` (default-profile scheduler, per-job Kimi
      override, 06:00, telegram) + `canon-drip-precheck.py` (both branches
      verified) + rubric wired. First fire: 2026-07-16 06:00.

The 4-day Fable clock gates **design elevation only** — the build is not gated on
Fable at all.

---

## 11. Decisions log ✅ (all 2026-07-15)

**Round 1 — schema & write contract**
1. ✅ Profile name = **McCoy**.
2. ✅ `site_status` = **found → reviewed → approved → live → retired** (export filter: approved | live).
3. ✅ Citation depth = **album-level for v1**; per-line deferred as additive backfill.
4. ✅ Edit path = **direct-to-tables** (`_jazzcanon_app`, no API).
5. ✅ Nightly drip = **06:00**, backlog cap **10**.
6. ✅ Both held `jcdb` fixes **greenlit** (ownership DONE; citation backfill pending).

**Round 2 — researcher architecture**
7. ✅ **One lead**, in charge — McCoy builder mode itself; no separate standing Researcher profile.
8. ✅ **Two lanes:** GATHER via `delegate_task` (never MoA); JUDGE via `canon-council` MoA advisory.
9. ✅ JUDGE runs **per-candidate**.
10. ✅ **2 references, not 3** (skeptic + generalist + synthesizer).
11. ✅ **Cron via Hermes** (`hermes cron`), not system crontab — with `--script` precheck + `--deliver`.
12. ✅ **Runtime model layer:** Gatherer+Lead = **Kimi K2.7-Code**; refs = **DeepSeek V4-Pro** + **Gemini 3.1 Pro** (Nous); aggregator = **GPT-5.6 Terra** (Kimi fallback). No Claude in Hermes.

**Round 3 — build decisions (Fable 5, 2026-07-15, during the build)**
13. ✅ `site_status` is keyed by **text `code`** (PK), not a serial id — so `album.site_status` can `DEFAULT 'found'` and queries read plainly. All 100 included albums backfilled to `live`. (`scripts/migrate-3b-site-status.sql`, run via `scripts/run-migrate-3b.sh`.)
14. ✅ `_jazzcanon_app` grants = SELECT/INSERT/UPDATE, **no DELETE** — "never delete" is structural; rejection is `canon_status='excluded'`. `edit_log` is append-only for the app role. Password in `.env.local` (`JAZZCANON_APP_DB_URL`) and the mccoy profile `.env`.
15. ✅ `export.sh` now enforces the **publication gate** (`canon_status='included' AND site_status IN ('approved','live')`) in all four query sites — it previously exported *every* album row, which would have leaked the first staged candidate onto the site. Verified content-identical output for the current 100.
16. ✅ The `canon-council` preset lives in the **mccoy profile's** `config.yaml` only; `~/.hermes/scripts/canon-council.py` pins `HERMES_HOME` there, so every caller (interactive McCoy, the drip in the default profile, John at a shell) resolves the same council. Aggregator **GPT-5.6 Terra via `openai-codex`** verified live.
17. ✅ JUDGE lane is an **agent-invocable script** (`canon-council.py`), not `/moa` — v0.18.2 has no in-agent MoA tool. And MoA advisory sends all refs the same prompt (no per-ref roles), so **each ref argues both the case-for and case-against**; family diversity (DeepSeek × Gemini) supplies the perspectives; the aggregator emits a strict-JSON ballot and preserves disagreement. Verified end-to-end (test ballot on Shorty Rogers, both refs answered, 60s).
18. ✅ Staging is **deterministic code** — `scripts/stage-candidate.py` (adapted from `ingest.py`: one record → normalized rows, candidate/found, dedup + window guards, one transaction, edit_log entry) — never agent-improvised multi-table SQL.
19. ✅ The drip cron lives in the **default profile** (its gateway is the confirmed always-on scheduler — zero new persistent process) with a **per-job model override** to Kimi K2.7-Code (`create_job(model=, provider=)`; the CLI doesn't expose it). Job `canon-drip`, `0 6 * * *`, `--script canon-drip-precheck.py`, workdir = project repo, deliver telegram. `[SILENT]` is a native gateway suppress marker — verified in source.
20. ✅ The **drip gathers inline** (one agent, web tools, 2 candidates) — `delegate_task` fan-out is reserved for John's interactive bulk missions in the mccoy profile. Fewer moving parts on the unattended path.
21. ✅ Hermes v0.18.2 **always backgrounds top-level delegations** (model can't opt out; results re-enter the conversation). Fine interactively; breaks only `-z` one-shot probes. Child spawn → web/file tools → output verified live.
22. ✅ Status transitions: McCoy **executes** John's explicit per-album verdicts (include/reject/reviewed/approved/retired) through the edit contract — the decision is John's, the typing is McCoy's. `approved → live` belongs to the publish pipeline, not chat.

**Round 4 — drip incident repairs (Opus, 2026-07-17)**

*Incident:* drip #2 (2026-07-17 06:00) re-selected drip #1's staged candidates from `research/candidates-inbox/`, re-researched and re-judged them, was refused by `stage-candidate.py`'s guard (DB untouched), then reported the refusals as "refreshed cards" — Hermes marked the run `ok` with zero new candidates. Contributing: `canon-council.py` pinned the mccoy profile with `setdefault` (a no-op under cron, where `HERMES_HOME` is pre-set), so **both** drips judged with the default `general` preset (Kimi aggregator) instead of `canon-council` (Terra); the bad "refreshed card" and `--preset general` fallback instructions came from a runbook the drip-#1 agent authored about itself mid-run.

23. ✅ Dedup is now **mechanical, not prompt-trust**: the precheck sweeps already-in-DB inbox files to `research/candidates-archive/` before the agent reasons (inbox = in-flight work only), and new `scripts/check-candidate.py` (exit 0/1: DB + next-batch + artifacts + year window) is a mandatory gate before any research. Same principle as #14/#18 — guardrails as code.
24. ✅ Success condition inverted: a drip card exists **only** for a newly inserted candidate/found row; a staging refusal is a `DRIP FAILED:` report, never a refreshed card. Cron prompt and runbook rewritten; council fallback to another preset is a hard failure (script exits 4 with instructions).
25. ✅ `canon-council.py` pins `HERMES_HOME` by **explicit assignment** (setdefault was the bug). Both queued candidates re-judged by the real council 2026-07-17 (ballots + DB updated via edit_log): Art Blakey *Free for All* contested/strong → **consensus_core/strong (high)**; Horace Silver *Serenade to a Soul Sister* held at contested/consider. The `mccoy-tyner` skill is now attached to the cron job.

**Still open (own loops, deferred by John)**
- ✅ Hermes scheduler persistence — **confirmed always-on** (2026-07-15); drip rides existing infra, zero new footprint.
- Per-line citation backfill trigger (deferred; reminder in memory).
- `delegation.subagent_auto_approve` stays **false** (default). It only gates *terminal* commands inside children — McCoy's children are web+file, so it's moot today. If a future mission needs terminal children unattended, that flip is John's call.

---

## 12. Fable hand-off — what to give Fable, and why

Point Fable at the **compounding-judgment** parts, not the mechanics:

- **§4 guardrails + §8 rubric** — the canon's quality bar lives here; every
  future nightly candidate inherits it.
- **The profile constitution** (not yet drafted — McCoy's voice, when it speaks
  up, how it balances helpfulness with source-grounding rigor). Use the
  `system-prompt-generator` intent-engineering shape.

Keep the schema/role/write-contract work (§5–§7) on Opus/Sonnet — it's bounded and
evidenced, and doesn't need Fable's ceiling.
