# Genre Definitions

Working reference for the McCoy Tyner project. Rules evolve as the list develops — this is a personal canon, not an academic taxonomy.

**Version:** draft 2 — 2026-06-18 (eras relaxed to guidance, not gates)

---

## On Eras (read first)

The **Era** line under each genre is a *center of gravity, not a fence*. It tells you where the style clusters — it does **not** reject an album for landing a few years outside. The governing test is always the Test Question at the bottom (swings with structure, post-bebop, pre-fusion in spirit — **regardless of year**). Do not flag or down-rank a candidate for date alone; only the spirit test and the hard Out-of-Scope marker (pre-1949 bebop) exclude — free jazz and fusion moved from *excluded* to *gated* on 2026-07-28, see **The Opened Gates** below. When a record sits near an edge, keep it and note *why it belongs*, not *which year it missed*.

## In Scope

### Cool Jazz
**Era:** Late 1940s–mid 1950s  
**Character:** Reaction against bebop's intensity. Relaxed tempos, lighter tone, emphasis on arrangement over improvisation. Influence of classical music and big band. West Coast Jazz is a close subgenre.  
**Anchor album:** Miles Davis — *Birth of the Cool* (recorded 1949–50)  
**Key figures:** Miles Davis, Chet Baker, Dave Brubeck, Stan Getz, Gerry Mulligan

### Hard Bop
**Era:** ~1955–1965  
**Character:** Extended bebop with R&B, gospel, and blues woven in. Heavy backbeat, medium tempos, soulful melodies. The dominant genre for a solid decade. Deeply tied to the Civil Rights era.  
**Anchor albums:** Art Blakey & Jazz Messengers — *Moanin'* (1958); Horace Silver — *Song for My Father* (1964)  
**Key figures:** Art Blakey, Horace Silver, Clifford Brown, Lee Morgan, Freddie Hubbard, Sonny Rollins

### Soul Jazz
**Era:** Late 1950s–1960s  
**Character:** Offshoot of hard bop leaning toward gospel and R&B grooves. Often organ-led. Soulful, funky, accessible — but firmly pre-fusion. Evaluate on a per-album basis.  
**Anchor albums:** Jimmy Smith — *The Sermon!* (1958); Lou Donaldson — *Alligator Bogaloo* (1967)  
**Key figures:** Jimmy Smith, Horace Silver (crossover), Lou Donaldson, Gene Ammons

### Modal Jazz
**Era:** 1958–1970s and beyond  
**Character:** Improvisation over static modes/scales rather than cycling chord changes. More space, more freedom within structure. The longest tail of any genre here — the modal sensibility didn't die in 1970; it migrated into solo careers and continued into the 1980s.  
**Anchor album:** Miles Davis — *Kind of Blue* (1959)  
**Key figures:** Miles Davis, John Coltrane (with McCoy Tyner, 1960–65), Bill Evans, McCoy Tyner (solo), Keith Jarrett, Chick Corea, Herbie Hancock

### Post-Bop
**Era:** ~1962–1968+  
**Character:** Synthesis zone — hard bop meets modal and a controlled amount of avant-garde experimentation, without dissolving into free jazz. Still swings with structure. The Miles Davis Second Quintet is the canonical example.  
**Anchor albums:** Miles Davis — *E.S.P.* (1965), *Miles Smiles* (1966)  
**Key figures:** Miles Davis Second Quintet (Shorter, Hancock, Carter, Williams), Wayne Shorter, Herbie Hancock

---

## Out of Scope

| Genre | Reason |
|-------|--------|
| Bebop (pre-1949) | Too early — the starting point, not part of the list. Transition records inside the 1940–1948 band are `scope_call`; see the rubric. |

---

## The Opened Gates (2026-07-28)

**Free jazz and fusion are no longer out of scope.** `excluded_styles` in
`config/canon-rubric.md` is now empty, and three specialists own the newly admissible
territory. This is a *permeable boundary*, not an annexation — the canon's center of
gravity stays in the post-bebop, hard-bop, and modal tradition.

| Gate | Owner | Window | Governing test |
|------|-------|--------|----------------|
| Fusion / jazz-rock / jazz-funk | `jazz-fusion-researcher` | 1968–1979 | The **bridge test**: what does this record connect, on both ends? Excellent fusion is not by itself an argument. |
| Free jazz / avant-garde / free improvisation | `jazz-free-jazz-researcher` | 1959–1979 | Does it **teach the idiom** and connect audibly to what is already in the canon? Every record also carries an honest `gateway` / `intermediate` / `demanding` rating. |
| ECM Records (the label, 1969–1979) | `jazz-ecm-researcher` | 1969–1979 | **Continuity** with the 1960s modal tradition — and *would I make the same case if the label were not ECM?* |

Three standing rules apply to all three:

1. Arrivals from these gates lean **`scope_call` or `contested`** by default; `consensus_core`
   needs an exceptional for-case, and the boundary is named in the ballot. John rules.
2. **Incremental, not floodgate.** These gates open a few records at a time. No genre
   advocacy, no proposing records to "cover" a newly opened style — style quotas remain
   forbidden.
3. **The ECM agent owns the label, not the aesthetic.** The fusion and free-jazz agents hand
   every ECM release in the window to it and note the hand-off in their Gaps, so no record
   gets argued twice from two directions.

The full prose — including the free-jazz taste note and the fusion anti-drift note — lives in
`config/canon-rubric.md` under *The opened genre gates*, which is authoritative over this file.

---

## The Fuzzy Edges

- **Post-bop leaning avant-garde:** *Out to Lunch!*, *Point of Departure*, the Blue Note avant
  sides — shared between the modal and free-jazz specialists. Argue them as bridges, set
  `overlap_risk`, let the council resolve.
- **Late modal jazz (1970s–80s):** McCoy Tyner's solo work, Keith Jarrett's *Köln Concert* —
  eligible. Evaluate whether it feels continuous with the 1960s modal tradition. Where the
  record is an ECM release, check the ledger: the modal specialist keeps what it already
  collected, and new seam records go to the ECM specialist.
- **Soul jazz:** Per-album judgment. Funky but pre-fusion = modal/hard-bop territory. Once
  rock and backbeat organize the record, it is the fusion specialist's — no longer "out."
- **Coltrane:** classic quartet through *A Love Supreme* (1964) is modal territory.
  *Ascension* (1965) forward belongs to the free-jazz specialist.

---

## The Test Question

The original test still governs the **core** of the canon:

> *Does it swing with structure, post-bebop, and pre-fusion in spirit — regardless of the year it was recorded?*

If yes, it's a candidate for one of the three original specialists.

If **no**, it is no longer automatically out. It may still be a candidate through one of the
opened gates — but only on that gate's own terms:

> *Does it bridge a lineage the canon cares about (fusion), teach an idiom John is studying
> (free jazz), or extend the 1960s modal tradition forward (ECM)?*

A record that passes neither test is out.

---

*This file lives at `docs/genre-definitions.md`. Update as the list develops.*
