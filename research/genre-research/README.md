# genre-research — the Inside/Outside project

**Two paths, as of 2026-09-29.**

John writes all prose. This is research and argument underneath it. No page design work has
been done and no canon data has been modified.

## The two paths

| | `explainer/` | `long-form/` |
|---|---|---|
| **For** | John's friends, and others who don't know jazz | John |
| **Job** | Orient a beginner | Support deep thinking, learning and writing |
| **Shape** | One short page, organised by ear rather than by genre | A research programme, not a deliverable |
| **Key file** | [`explainer/README.md`](explainer/README.md) | [`long-form/README.md`](long-form/README.md) |
| **Status** | Structure proposed, waiting on one research task | Four fronts defined, backlog of open questions |

They are deliberately divergent. The explainer organises by *experience* and introduces
genre names second; the long-form skips the genre structure entirely and goes after the
seams, the politics and the people. Neither is a longer version of the other.

## Start here

**[`inside-outside.html`](inside-outside.html)** — the orientation artifact. The verdict on
the name, the three-axes correction, the hinge records, the mislabel traps, five key dates
and the three open decisions. Validated: 11 anchors, no broken links.

```
$ cd ~/dev/active/mccoy-tyner/research/genre-research
$ python3 -m http.server 8000     # then open http://localhost:8000/inside-outside.html
```

## Layout

```
explainer/          the beginner path
  README.md           approach, principles, the core design problem
  structure.md        proposed page shape, section by section
  research/
    listener-paths.md how to enter each genre; what will put a newcomer off
long-form/          the deep path
  README.md           four research fronts, in priority order
  thesis/             the argument: page architecture, terminology, three-branch comparison
  genres/             ten genre files, each with a contested section
  timeline/           master timeline + two seam analyses
  canon/              canon inventory — DEMOTED to data hygiene, see its header
  sources/            every source with a confidence mark, plus a log of what I got wrong
raw/                ~39MB of verbatim source captures
```

## The core argument, in four lines

1. **"Inside/outside" is documented musician's vocabulary, not a metaphor** — a textbook
   chapter (Mark Levine), a period label (Gridley), and Miles Davis's own phrase "the
   way-out thing."
2. **The word is relative, and that is the best material on the page.** Levine: *"Bird was
   considered 'out' by many musicians in the 1940s."* The line moves; nobody is permanently
   outside.
3. **Fusion is not "outside."** Electric and groove-driven, but harmonically *inside* — vamps,
   riffs, ostinatos. It belongs on the acoustic/electric axis, not the harmonic one.
4. **Three axes, not one:** harmonic/formal, acoustic/electric, composed/improvised. They
   cross.

## Standing constraints

- **The canon is one lens, not the frame.** See the note at the top of
  [`long-form/canon/canon-inventory.md`](long-form/canon/canon-inventory.md) for why the
  94:6 argument was withdrawn, and the entry points in the orientation document that are
  therefore flagged for re-derivation.
- **Uncertainty stays visible.** Every genre file carries a contested section. Do not let
  flagged claims harden by being repeated.
- **Nothing is page copy.** It is research written to be argued from.

## ⏸ Three decisions waiting on John

**Parked at John's request — see [`DECISIONS.md`](DECISIONS.md)** for the full statement of
each, the evidence, the recommendation, and the cost of choosing otherwise.

1. Make the "outside is a relative term" argument the explainer's spine, or state it once
   and move on? *(Recommendation: spine — it is sourced, needs no music theory, and earns
   the title.)*
2. Split fusion out as "The Electric Turn" on its own axis? *(Recommendation: yes.)*
3. Outside section: one entry, or two? *(Leaning one section, two marked subsections.)*

A fourth question has since surfaced and is also open: **the explainer needs a name for the
thing that isn't a genre** — the beginner sections are currently organised by ear under a
working title only, and that choice is entangled with Decision 1.

## One task in flight

**Entry-point re-derivation**, commissioned to researcher on 2026-09-29. Every entry point in
the corpus was chosen by what's in the canon, which is the wrong criterion. The canon's bebop
holdings are five 1945–48 period transfers and compilations — fine for a collector, bad advice
for a beginner. Output will land at `explainer/research/entry-points.md`.

The brief asks for, per genre: gentle / moderate / demanding / controversial options, a
specific audible reason each works as a *first* record, a "listen for this" cue, and named
critics or teachers behind each pick. Plus the records beginners are commonly told to start
with that they should *not* start with; where a compilation or reissue is the kinder first
experience than the original mono session; two or three cross-genre starters that work for
anyone; and a test of my own hypothesis that good on-ramps are the era-accessible and melodic
records rather than the most radical ones.
