# Fusion Specialist — Agent Brief

> **Canonical agent:** `~/.claude/agents/jazz-fusion-researcher.md` (self-contained, model-scoped: Opus).
> Written 2026-07-28, alongside the agent — unlike the 2026-06-11 briefs, this one was
> never the operative document. It is the **design record**: why the gate opened, what was
> decided, and what stayed open. The agent file is authoritative on behaviour; when the two
> disagree, the agent file wins and this brief is stale.

## Why this gate opened

Fusion was an excluded style in `config/canon-rubric.md` from the project's start. John's
own account of the original exclusion: it "didn't resonate," and he felt he did not
understand it. He has since called that rationale **lame** and opened the gate on 2026-07-28.

The reason is not that his taste changed. It is that a blanket exclusion was **too blunt an
instrument** — walling off fusion means losing the lineage and the bridge to later jazz.
The road runs from Miles' electric bands through the sidemen diaspora and forward toward
Charles Lloyd's later career and Kamasi Washington. A canon that cannot trace that road
cannot explain how the music it loves became the music that came after.

**What did not change:** John does not want the canon to become a fusion project. The
center of gravity stays post-bebop, hard bop, and modal.

## Design decisions

**1. The bridge test outranks the genre label.** The agent's governing question is what a
record *connects* — on both ends — not what bin a source files it in. Being excellent
fusion is explicitly not an argument. This is encoded as a **required `bridge_case` field**
on every candidate record, which the council reads first; a record with no defensible
bridge case is not proposed at all.

*Rationale:* John opened this gate to learn a lineage, not to acquire a genre. A required
field is stronger than prose guidance because it cannot be skipped quietly.

**2. Default run size 6, against the established specialists' 10.** Smaller by design; the
rubric's opened-gate rule is "incremental, not floodgate."

**3. `scope_flag` is never empty for this agent.** Every record states the boundary it sits
on and the strongest case against it. Records from a newly opened gate lean `scope_call` or
`contested`; `consensus_core` needs an exceptional for-case.

**4. Genre advocacy is a guardrail violation.** The agent is explicitly forbidden from
arguing that the canon needs fusion, needs balance, or looks incomplete without it. The
rubric already forbids style quotas; this makes it operative at the agent level, because a
specialist for a newly opened genre is exactly where quota-thinking would leak in.

**5. Jazz-funk absorbed here, with extra scrutiny.** *Head Hunters* and the groove wing sit
on the seam and are the most direct antecedent of the later music John wants to reach.
Tagged `style_primary: jazz-funk` so synthesis can track them separately. Commercial
crossover with decorative improvisation is named as the weakest case this gate can make.

**6. The pre-fusion bridge (1966–69) is in the agent's domain when the record is the hinge.**
*Forest Flower*, *In a Silent Way*, *Emergency!* — often the strongest cases available,
because the continuity is audible rather than argued. The ledger arbitrates against the
modal specialist's prior claims.

**7. Personnel contract stress noted, not amended.** Electric bands carry credits the
acoustic canon does not (synth models, Rhodes vs. Wurlitzer, effects) and studio-assembled
albums break the one-session assumption (*Bitches Brew*, *Get Up with It*). The agent
records every sourceable session date and puts un-taxonomized terms in notes. Teo Macero's
tape editing is treated as authorship, not a production footnote.

## Boundary ownership

| Border | Ruling |
|--------|--------|
| **ECM releases** | Belong to `jazz-ecm-researcher` — that agent owns the label 1969–1979, including its fusion edge (Return to Forever 1972, Metheny 1976–79). This agent hands them off in Gaps Noticed. |
| **Electric free improvisation** | Shared with `jazz-free-jazz-researcher` (Miles 1972–75, Sun Ra electric). Set `overlap_risk`; synthesis resolves. Never silently absorbed. |
| **Miles 1968–70** | The hinge. The modal specialist has leaned "in" on *In a Silent Way*. *Bitches Brew* is now this agent's to argue. Ledger checked first. |
| **Fusion-era leaders' acoustic 1970s records** | Not fusion. Milestone-era McCoy Tyner, Corea's *Piano Improvisations* → route to the modal specialist. |

## Open questions

- **How far past 1979 does the lineage need to run before it is legible?** The bridge to
  Kamasi Washington cannot actually be drawn inside a 1979 ceiling. The agent works within
  the window and names the reach forward in prose (the **Lineage Map** synthesis section);
  whether the canon eventually needs the 1980s to make its own argument is John's call.
- **Does the canon want an explicit "bridge" designation** in the schema, distinct from
  ordinary inclusion? Not proposed — noted because the `bridge_case` field is currently
  candidate-only and does not survive into `_jazzcanon.album`.
- **Size of the gate.** No target number was set, deliberately. Unlike free jazz, John has
  not asked "how many?" here.
