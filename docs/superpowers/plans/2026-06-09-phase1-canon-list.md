# Phase 1: Canon List Build — Three-Agent Research Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Compile a pool of ~150 candidate albums across Hard Bop, Cool Jazz, and Modal Jazz using three parallel specialist `jazz-researcher` agents, then synthesize into `data/canon-draft.json` (~100 albums) for John's final selection.

**Architecture:** Three style-scoped agents research their domain independently against canonical jazz sources. A **Canon Orchestrator** then reconciles their lists into a tiered, pre-argued decision ballot. John applies taste at the margin — on the ballot, not the raw pool — to reach the final ~100.

> **Update note (2026-06-10):**
> 1. **Authoritative schema:** The candidate record embedded in Task 1 below is an early draft. The
>    live contract is `research/candidate-schema.md` — it adds `priority` (`must_have`/`strong`/
>    `consider`) and `scope_flag`, and enriches the synthesis notes. Agents follow that file, not the
>    snapshot here.
> 2. **Canon Orchestrator inserted:** A new agent runs between the specialist compiles (Task 5) and
>    John's gate. It replaces the passive synthesis of Task 6 with an active *decision-compression*
>    pass and emits `data/canon-ballot.json`. Spec: `research/agent-briefs/canon-orchestrator-brief.md`.
>    Tasks 6–8 below are reframed accordingly (see the Orchestrator brief for the round structure).
> 3. **Post-Bop open question — resolved (Option A):** The Modal Jazz agent absorbs Post-Bop and tags
>    those albums `style_primary: post-bop`. No fourth specialist. (Confirm if you'd prefer Option B.)

**Tech Stack:** `jazz-researcher` subagent type, web search, JSON output, `docs/genre-definitions.md` as style authority, `docs/conventions.md` epistemic labeling standard.

---

## File Map

| File | Role | Created by |
|------|------|-----------|
| `research/candidate-schema.md` | Output schema all three agents must follow | Task 1 |
| `research/agent-briefs/hard-bop-brief.md` | Mandate for the Hard Bop specialist | Task 2 |
| `research/agent-briefs/cool-jazz-brief.md` | Mandate for the Cool Jazz specialist | Task 3 |
| `research/agent-briefs/modal-jazz-brief.md` | Mandate for the Modal Jazz specialist | Task 4 |
| `research/hard-bop-candidates.md` | Agent 1 output | Task 5 |
| `research/cool-jazz-candidates.md` | Agent 2 output | Task 5 |
| `research/modal-jazz-candidates.md` | Agent 3 output | Task 5 |
| `research/agent-briefs/canon-orchestrator-brief.md` | Orchestrator mandate + ballot schema | (done 2026-06-10) |
| `data/canon-ballot.json` | Tiered, pre-argued decision ballot (`include: null`) | Task 6 (Orchestrator) |
| `research/canon-synthesis.md` | Human-readable companion to the ballot | Task 6 (Orchestrator) |
| `data/canon-draft.json` | John's selection — `include` set | Task 7–8 |

---

## Open Question Before Dispatch

**Post-Bop coverage:** `docs/genre-definitions.md` includes Post-Bop (~1962–1968+) as a fifth in-scope style (Miles Davis Second Quintet, Wayne Shorter, Herbie Hancock). The three-agent plan as written does not give it dedicated coverage.

Two options:
- **A)** Modal Jazz agent absorbs Post-Bop (close enough in spirit; agents flag post-bop albums with `style_primary: post-bop`)
- **B)** Add a fourth Post-Bop specialist agent

John decides before Task 4 is complete. If B, create `research/agent-briefs/post-bop-brief.md` following the same template as Tasks 2–4.

---

## Task 1: Define the Candidate Output Schema

**Files:**
- Create: `research/candidate-schema.md`

- [ ] **Step 1: Write the schema file**

```markdown
# Candidate Album Schema

Every agent returns a markdown file containing: a source map table, then a JSON block per candidate album, then brief synthesis notes. No deviations.

## Source Map (one per agent file)

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Penguin Guide to Jazz, 10th ed. | Book | — | Core critical reference |
| S2 | DownBeat Critics Poll Archive | Web | https://downbeat.com | Historical polls |
| S3 | AllMusic genre page | Web | https://allmusic.com | Editor picks + ratings |

Sources are agent-local per file. Synthesis step merges source IDs.

## Candidate Record

Each album is one JSON block:

{
  "id": "<artist-slug>-<album-slug>-<year>",
  "artist": "Miles Davis",
  "album": "Kind of Blue",
  "year": 1959,
  "label": "Columbia",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2"],
  "epistemic": "obs",
  "rationale": "obs[S1]: Penguin Guide 4-star core collection. obs[S2]: DownBeat poll top-ranked. inf: universally recognized as defining modal jazz.",
  "overlap_risk": "",
  "include": null
}

## Field Definitions

- id: kebab-case. Use leader's name as artist for group recordings (e.g., art-blakey).
- style_primary: one of hard-bop | soul-jazz | cool-jazz | modal-jazz | post-bop
- style_tags: array — include secondary if genuinely dual (e.g., hard bop album with soul jazz elements)
- epistemic: obs if any source directly names it; inf if reasoned from pattern; unk if single-source or uncertain
- rationale: cite source IDs inline. Lead with obs: claims, then inf:, then unk:.
- overlap_risk: empty string if none; otherwise name the overlapping style (e.g., "hard-bop/soul-jazz border")
- include: null until John's review. Set to true or false at Task 8.

## Synthesis Notes (end of each agent file)

After all candidate records, each agent appends:

### Consensus Picks
Albums appearing in 3+ sources. High confidence.

### Single-Source Picks
Albums appearing in only one source but strong critical weight. Flag for John's attention.

### Scope Calls
Albums where the agent made a judgment call on the in/out boundary. Explain each.

### Gaps Noticed
Periods, figures, or labels the sources covered poorly.
```

- [ ] **Step 2: Commit**

```bash
git add research/candidate-schema.md
git commit -m "Add candidate output schema for Phase 1 agents"
```

---

## Task 2: Write the Hard Bop Agent Brief

**Files:**
- Create: `research/agent-briefs/hard-bop-brief.md`

Note: Soul Jazz is a Hard Bop subgenre — this agent covers both.

- [ ] **Step 1: Write the brief**

```markdown
# Hard Bop Specialist — Agent Brief

## Your Role
You are a Hard Bop (and Soul Jazz) specialist researcher for the McCoy Tyner jazz canon project. Your job is to produce a source-grounded list of 40–60 candidate albums in the Hard Bop and Soul Jazz styles.

## Style Scope

### Hard Bop
Era: ~1955–1965
Character: Extended bebop with R&B, gospel, and blues woven in. Heavy backbeat, medium tempos, soulful melodies. Deeply tied to the Civil Rights era.
Key figures: Art Blakey, Horace Silver, Clifford Brown, Lee Morgan, Freddie Hubbard, Sonny Rollins, Cannonball Adderley, Wes Montgomery, Hank Mobley

### Soul Jazz (subgenre of Hard Bop)
Era: Late 1950s–1960s
Character: Offshoot leaning toward gospel and R&B grooves. Often organ-led. Soulful, funky, accessible — but firmly pre-fusion.
Key figures: Jimmy Smith, Lou Donaldson, Gene Ammons, Brother Jack McDuff, Horace Silver (crossover)
Per-album rule: funky but pre-fusion = in; starts incorporating rock elements = out.

## Scope Rules
IN: Post-bebop, pre-Fusion, swings with structure
OUT: Bebop (pre-1949), Free Jazz (Ornette Coleman, late Coltrane post-1965), Fusion (Bitches Brew 1970 is the marker)
FUZZY RULE: Does it swing with structure, post-bebop, and pre-fusion in spirit — regardless of the year recorded? If yes, it's a candidate.

## Sources to Consult (in priority order)
1. Penguin Guide to Jazz (Cook & Morton) — web summaries, excerpt sites, reviews referencing its ratings
2. DownBeat Critics Polls 1955–1970 — annual album and recording picks
3. AllMusic Hard Bop genre page and highly rated albums
4. Rolling Stone jazz album lists
5. NPR Music jazz recommendations
6. Jazz Times Hard Bop retrospectives
7. Wikipedia "Hard bop" article — key albums section
8. Any critic-curated "best hard bop" or "essential Blue Note albums" lists you find

## Output Format
Follow the schema in `research/candidate-schema.md` exactly:
1. Source map table at the top
2. One JSON block per candidate album
3. Synthesis notes at the end (consensus picks, single-source picks, scope calls, gaps)

## Epistemic Rules (from docs/conventions.md)
- obs: directly stated in source
- inf: reasoned from source pattern (e.g., appears in 3+ lists → likely consensus)
- unk: uncertain or single-source with no corroboration

## Target
Aim for 40–60 candidates. Better to include a marginal album than miss a canonical one — John filters at review.
```

- [ ] **Step 2: Commit**

```bash
git add research/agent-briefs/hard-bop-brief.md
git commit -m "Add Hard Bop agent brief for Phase 1 dispatch"
```

---

## Task 3: Write the Cool Jazz Agent Brief

**Files:**
- Create: `research/agent-briefs/cool-jazz-brief.md`

Note: West Coast Jazz is a Cool Jazz subgenre — this agent covers both.

- [ ] **Step 1: Write the brief**

```markdown
# Cool Jazz Specialist — Agent Brief

## Your Role
You are a Cool Jazz (and West Coast Jazz) specialist researcher for the McCoy Tyner jazz canon project. Your job is to produce a source-grounded list of 30–50 candidate albums in the Cool Jazz style.

## Style Scope

### Cool Jazz
Era: Late 1940s–mid 1950s
Character: Reaction against bebop's intensity. Relaxed tempos, lighter tone, emphasis on arrangement over improvisation. Classical music and big band influences prominent.
Key figures: Miles Davis (early), Chet Baker, Dave Brubeck, Stan Getz, Gerry Mulligan, Paul Desmond, Bill Evans (early), Lennie Tristano

### West Coast Jazz (subgenre)
Same era. Based in Los Angeles. Often lighter, more arranged, contrapuntal. Closely aligned with Cool Jazz values.
Key figures: Shorty Rogers, Art Pepper, Shelly Manne, Howard Rumsey's Lighthouse All-Stars

## Scope Rules
IN: Post-bebop (late 1940s onward), pre-Fusion, swings with structure
OUT: Pure bebop (pre-1949), Free Jazz, Fusion
NOTE: Cool Jazz has an earlier starting line than Hard Bop and Modal — do not exclude 1949–1954 albums.
FUZZY RULE: Does it swing with structure, post-bebop, and pre-fusion in spirit? If yes, it's a candidate.

## Sources to Consult (in priority order)
1. Penguin Guide to Jazz (Cook & Morton) — web summaries and reviews
2. AllMusic Cool Jazz genre page — editor picks and highly rated albums
3. DownBeat Critics Polls 1949–1960
4. Rolling Stone jazz lists
5. NPR Music jazz recommendations
6. Wikipedia "Cool jazz" article — key albums section
7. Any "essential West Coast jazz" or "essential Chet Baker / Dave Brubeck / Stan Getz" lists
8. Pacific Jazz Records and Prestige Records discographies for era coverage

## Output Format
Follow the schema in `research/candidate-schema.md` exactly:
1. Source map table at the top
2. One JSON block per candidate album
3. Synthesis notes at the end (consensus picks, single-source picks, scope calls, gaps)

## Epistemic Rules (from docs/conventions.md)
- obs: directly stated in source
- inf: reasoned from source pattern
- unk: uncertain or single-source with no corroboration

## Target
Aim for 30–50 candidates. Cool Jazz has a shorter canon window than Hard Bop or Modal — 30 solid picks is fine. Do not pad with weaker albums to hit a number.
```

- [ ] **Step 2: Commit**

```bash
git add research/agent-briefs/cool-jazz-brief.md
git commit -m "Add Cool Jazz agent brief for Phase 1 dispatch"
```

---

## Task 4: Write the Modal Jazz Agent Brief

**Files:**
- Create: `research/agent-briefs/modal-jazz-brief.md`

Note: This style has the longest tail — eligible into the 1980s if continuous with the 1960s modal tradition. Post-Bop overlaps here; see the Open Question above.

- [ ] **Step 1: Write the brief**

```markdown
# Modal Jazz Specialist — Agent Brief

## Your Role
You are a Modal Jazz specialist researcher for the McCoy Tyner jazz canon project. Your job is to produce a source-grounded list of 50–70 candidate albums in the Modal Jazz style, including Post-Bop where it overlaps.

## Style Scope

### Modal Jazz
Era: 1958–1980s (the modal sensibility did not die in 1970)
Character: Improvisation over static modes/scales rather than cycling chord changes. More space, more freedom within structure. The approach migrated from Miles Davis into solo careers and continued developing.
Key figures: Miles Davis (Kind of Blue era), John Coltrane (with McCoy Tyner, 1960–65), Bill Evans, McCoy Tyner (solo career), Keith Jarrett, Chick Corea, Herbie Hancock, Wayne Shorter

### Post-Bop (absorb here unless a Post-Bop specialist is added)
Era: ~1962–1968+
Character: Synthesis zone — hard bop meets modal with controlled experimentation. Still swings with structure. The Miles Davis Second Quintet is the canonical example.
Key figures: Miles Davis Second Quintet (Shorter, Hancock, Carter, Williams), Wayne Shorter solo, Herbie Hancock solo
Note: Flag these with style_primary: post-bop so they can be separated in synthesis.

## Scope Rules
IN: Post-bebop, pre-Fusion in spirit, swings with structure
OUT: Free Jazz (Ornette, late Coltrane post-1965 dissolves-into-noise end), Fusion (Bitches Brew 1970 marker)
FUZZY — late modal (1970s–80s): McCoy Tyner's solo work, Keith Jarrett's Köln Concert — eligible if it feels continuous with the 1960s modal tradition. Evaluate per album. Flag your judgment in scope_calls.
FUZZY — John Coltrane: His work with the classic quartet (1960–64) is firmly in. A Love Supreme (1964) is in. Ascension (1965) and beyond crosses into Free Jazz territory — out.

## Sources to Consult (in priority order)
1. Penguin Guide to Jazz (Cook & Morton) — web summaries, especially for Coltrane, Miles Davis, McCoy Tyner solo work
2. AllMusic Modal Jazz genre page — editor picks and highly rated albums
3. DownBeat Critics Polls 1958–1975
4. Rolling Stone jazz lists
5. NPR Music jazz recommendations
6. Wikipedia "Modal jazz" and "Post-bop" articles — key albums sections
7. Any "essential John Coltrane" or "essential McCoy Tyner" or "essential Bill Evans" lists
8. Blue Note, Impulse!, and ECM Records discographies for era coverage

## Output Format
Follow the schema in `research/candidate-schema.md` exactly:
1. Source map table at the top
2. One JSON block per candidate album
3. Synthesis notes at the end (consensus picks, single-source picks, scope calls, gaps)

## Epistemic Rules (from docs/conventions.md)
- obs: directly stated in source
- inf: reasoned from source pattern
- unk: uncertain or single-source with no corroboration

## Target
Aim for 50–70 candidates. Modal Jazz has the deepest and longest canon. No style quotas — 60 Modal picks is fine per CLAUDE.md.
```

- [ ] **Step 2: Commit**

```bash
git add research/agent-briefs/modal-jazz-brief.md
git commit -m "Add Modal Jazz agent brief for Phase 1 dispatch"
```

---

## Task 5: Dispatch Three Specialist Agents in Parallel

**Files:**
- Create: `research/hard-bop-candidates.md` (agent 1 output)
- Create: `research/cool-jazz-candidates.md` (agent 2 output)
- Create: `research/modal-jazz-candidates.md` (agent 3 output)

- [ ] **Step 1: Verify briefs and schema are in place**

Confirm all four files exist before dispatching:
```
research/candidate-schema.md
research/agent-briefs/hard-bop-brief.md
research/agent-briefs/cool-jazz-brief.md
research/agent-briefs/modal-jazz-brief.md
```

- [ ] **Step 2: Dispatch agents in parallel**

Send three `jazz-researcher` subagents simultaneously with the following prompts:

**Agent 1 — Hard Bop:**
```
You are a Hard Bop and Soul Jazz specialist researcher for the McCoy Tyner jazz canon project.

Read the following files in full before beginning:
- docs/genre-definitions.md (style definitions and scope rules)
- docs/conventions.md (epistemic labeling standard)
- research/candidate-schema.md (output schema you must follow)
- research/agent-briefs/hard-bop-brief.md (your full mandate)

Then research and compile 40–60 candidate Hard Bop and Soul Jazz albums. Use web search to consult the sources listed in your brief. Write your output to research/hard-bop-candidates.md following the schema exactly.
```

**Agent 2 — Cool Jazz:**
```
You are a Cool Jazz and West Coast Jazz specialist researcher for the McCoy Tyner jazz canon project.

Read the following files in full before beginning:
- docs/genre-definitions.md (style definitions and scope rules)
- docs/conventions.md (epistemic labeling standard)
- research/candidate-schema.md (output schema you must follow)
- research/agent-briefs/cool-jazz-brief.md (your full mandate)

Then research and compile 30–50 candidate Cool Jazz and West Coast Jazz albums. Use web search to consult the sources listed in your brief. Write your output to research/cool-jazz-candidates.md following the schema exactly.
```

**Agent 3 — Modal Jazz:**
```
You are a Modal Jazz specialist researcher for the McCoy Tyner jazz canon project.

Read the following files in full before beginning:
- docs/genre-definitions.md (style definitions and scope rules)
- docs/conventions.md (epistemic labeling standard)
- research/candidate-schema.md (output schema you must follow)
- research/agent-briefs/modal-jazz-brief.md (your full mandate)

Then research and compile 50–70 candidate Modal Jazz albums (including Post-Bop). Use web search to consult the sources listed in your brief. Write your output to research/modal-jazz-candidates.md following the schema exactly.
```

- [ ] **Step 3: Verify agent outputs**

Each output file must contain:
- A source map table with at least 4 sources
- At least 30 candidate JSON records
- Synthesis notes section at the end

If any file is missing or malformed, re-run that agent with the original brief unchanged.

- [ ] **Step 4: Commit**

```bash
git add research/hard-bop-candidates.md research/cool-jazz-candidates.md research/modal-jazz-candidates.md
git commit -m "Add Phase 1 candidate lists from three specialist agents"
```

---

## Task 6: Synthesize Into canon-synthesis.md

**Files:**
- Create: `research/canon-synthesis.md`

- [ ] **Step 1: Count and flag overlaps**

Read all three candidate files. Identify albums that appear in more than one file (same artist + album + year). For each overlap:
- Note which agents both included it
- Note whether the `style_primary` tags agree or conflict
- This is a signal of strong canonical status, not a problem

- [ ] **Step 2: Apply scope filter**

Walk through all records. Flag any that may violate the in/out rules from `docs/genre-definitions.md`:
- Year too early (pre-1949 bebop)
- Too Free Jazz (note specific reason)
- Too Fusion (note specific reason)
- Do not delete — mark as `"scope_flag": "reason"` for John to decide

- [ ] **Step 3: Write canon-synthesis.md**

```markdown
# Canon Synthesis — Phase 1

Date: 2026-06-09
Source files: research/hard-bop-candidates.md, research/cool-jazz-candidates.md, research/modal-jazz-candidates.md

## Counts

| Style | Candidates |
|-------|-----------|
| Hard Bop | N |
| Soul Jazz | N |
| Cool Jazz | N |
| Modal Jazz | N |
| Post-Bop | N |
| **Total** | **N** |

## Cross-Style Overlaps

Albums appearing in more than one agent's list:

| Artist | Album | Year | Agents | Style Agreement |
|--------|-------|------|--------|-----------------|
| ...    | ...   | ...  | ...    | ...             |

## Scope Flags

Albums flagged during scope filter review:

| Artist | Album | Year | Flag Reason | Recommendation |
|--------|-------|------|-------------|----------------|
| ...    | ...   | ...  | ...         | ...            |

## Consensus Pool (3+ sources across all agents)

The strongest canonical candidates — these should almost certainly make the final ~100.

[List here]

## Single-Source Picks Worth John's Attention

Interesting but lightly sourced candidates for John's judgment:

[List here]

## Gaps Identified

[Synthesis of gaps noted by all three agents]

## Notes for John

[Any cross-style observations, surprises, or decisions needed before producing the draft JSON]
```

- [ ] **Step 4: Commit**

```bash
git add research/canon-synthesis.md
git commit -m "Add canon synthesis from Phase 1 agent outputs"
```

---

## Task 7: Produce canon-draft.json

**Files:**
- Create: `data/canon-draft.json`

This is the structured input for John's review. All candidates go in — no pre-selection. John sets `include: true/false` in Task 8.

- [ ] **Step 1: Merge all candidate records into a single JSON array**

Combine all records from the three candidate files. For overlapping albums (same artist + album + year), keep one record and merge sources from both agent files. Set the merged record's `style_tags` to include all styles both agents assigned.

- [ ] **Step 2: Write data/canon-draft.json**

```json
{
  "generated": "2026-06-09",
  "phase": "1-draft",
  "total_candidates": 0,
  "albums": [
    {
      "id": "miles-davis-kind-of-blue-1959",
      "artist": "Miles Davis",
      "album": "Kind of Blue",
      "year": 1959,
      "label": "Columbia",
      "style_primary": "modal-jazz",
      "style_tags": ["modal-jazz"],
      "sources": ["hard-bop-agent:S1", "modal-agent:S1"],
      "epistemic": "obs",
      "rationale": "obs[S1]: Penguin Guide 4-star core collection. obs[S2]: DownBeat poll top-ranked. inf: universally recognized as defining modal jazz.",
      "overlap_risk": "",
      "scope_flag": "",
      "include": null
    }
  ]
}
```

- [ ] **Step 3: Validate**

Count total records. Confirm all records have:
- Non-null `id`, `artist`, `album`, `year`, `style_primary`
- At least one source
- `include: null` (not yet reviewed)

- [ ] **Step 4: Commit**

```bash
git add data/canon-draft.json
git commit -m "Add canon-draft.json with Phase 1 candidate pool"
```

---

## Task 8: John's Review Gate — Phase 1 Gate

**Files:**
- Modify: `data/canon-draft.json` (set `include` values)

This is the **Phase 1 Gate** per `docs/conventions.md`. John reviews. No code runs. No agent dispatched.

- [ ] **Step 1: John reviews canon-synthesis.md**

Read `research/canon-synthesis.md`. Note:
- Consensus pool (should make the ~100 unless John overrides)
- Scope flags (John decides in/out for each)
- Gaps (does anything obviously missing need a follow-up agent run?)

- [ ] **Step 2: John reviews canon-draft.json**

For each album, set:
- `"include": true` — in the canon
- `"include": false` — excluded (no deletion, just flagged)
- `"include": null` — uncertain, needs another look

Target: ~100 `include: true` records.

- [ ] **Step 3: Commit**

```bash
git add data/canon-draft.json
git commit -m "Phase 1 gate: John's canon selection (~100 albums marked include:true)"
```

**Phase 1 complete. Proceed to Phase 2 (primary musicians and production personnel).**

---

## Self-Review

**Spec coverage:**
- Three specialist agents: Tasks 2–5 ✓
- Candidate schema: Task 1 ✓
- Synthesis: Task 6 ✓
- Structured draft JSON: Task 7 ✓
- John's review gate: Task 8 ✓
- Post-Bop coverage: Flagged as open question before Task 4 ✓
- Epistemic labeling: Embedded in briefs and schema ✓
- Source citation standard: Embedded in schema ✓

**Scope not covered by this plan:**
- Phase 2 (personnel) — out of scope, separate plan
- The app (Phase 5+) — out of scope

**Placeholder scan:** None found. All code blocks contain actual content.

**Type consistency:** `include` field is `null | true | false` consistently across schema, JSON template, and Task 8.
