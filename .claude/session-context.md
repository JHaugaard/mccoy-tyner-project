# Session Context

## Session Name
new-agent-briefs

## Current Focus

Open the genre gates on the jazz canon. Three genres now admissible that no existing
agent brief covers: **fusion**, **free jazz**, and **ECM**. Remit: develop briefs for
these three categories (existing set lives in `research/agent-briefs/`).

## Honcho Context

peer=john, reasoning_level=low. John's position has evolved from "excluded" to
"provisional, permeable gates":

- **Fusion** — does not want the canon to become a fusion project, but a total exclusion
  is too blunt: walling it off loses the **lineage/bridge to later jazz** (Kamasi Washington,
  Charles Lloyd). Called his old "I don't understand it" rationale "lame."
- **Free jazz** — personal taste remains cool; explicitly says it doesn't currently resonate.
  But he is *studying* it rather than dismissing it, and asked how many free-jazz records
  might be canon-worthy (~20 / 50 / 100). Gate opens **incrementally**.
- **ECM** — the preferred middle path: a route from modal/post-bop into later, genre-fluid
  music without leaping to fusion. Investigated specifically as **"modal jazz after 1970."**
  Jarrett's *Köln Concert* is central — possibly his #2 after *Kind of Blue*, must eventually
  enter the canon. ECM records arrive as **scope_call / contested**, judged on continuity
  with the 1960s modal tradition — never accepted or rejected by label or decade alone.
- **Year boundary** — 1940–1972 was acknowledged scaffolding; pushed to 1979 to let the
  ECM-era bridge records be evaluated. Genre harness retained for now.

Read: keep the canon's center of gravity in the jazz John understands and loves, but make
the boundaries permeable enough to test important continuities.

**Divergence noted:** this instruction departs from the CLAUDE.md scope gate ("no free jazz,
no fusion") and the `config/canon-rubric.md` frontmatter `excluded_styles`. Flagged before
proceeding; newer instruction wins and the rubric is being edited to match.

## Key Decisions

- **Deliverable = agent files + briefs.** All three existing briefs are marked
  "Superseded 2026-06-11" by first-class agents in `~/.claude/agents/`. New work ships as
  three dispatchable agent files *plus* matching design-history briefs, cross-linked like
  the existing pairs.
- **Rubric edited this session.** `excluded_styles: [free-jazz, fusion]` is the gate;
  briefs alone would produce candidates the council rejects on sight.
- **ECM scoped 1969–1979 only.** John chose the small step: `year_max: 1979` stays put.
  He expects to push the end date out in coming weeks/months.

## Notes

- Session started: 2026-07-28
- `excluded_styles` is **prose-enforced only** — `check-candidate.py` and `stage-candidate.py`
  parse `year_min`/`year_max` from the frontmatter but never read `excluded_styles`.
  Style gating happens in agent/council judgment, not in code.

## Previous session (2026-07-26, `schema-update`) — carried-forward open items
- Deferred: per-line citation backfill; `_jazzcanon_ro` password rotation.
