# The canon as it actually stands: inventory by style

> **STATUS: DEMOTED — read this before using the file.**
>
> An earlier draft of the Inside/Outside orientation argued the title was justified by this
> canon's proportions (238 inside / 16 outside ≈ 94:6). **That argument has been
> withdrawn**, for two reasons:
>
> 1. **It expires.** These are 254 albums on 2026-09-28. The canon was opened to bebop in
>    the week before this was written and is growing fast; the ratio will move.
> 2. **It is the wrong kind of evidence.** A page for people who have never heard of jazz
>    cannot be argued from one collector's inventory. *"What should I tell them to listen
>    to?"* is a question about listening, not about holdings.
>
> **What this file is now for:** a data-hygiene record. The ECM albums filed by genre rather
> than by lane, and the mis-tagged solo memorial, are real cataloguing issues for mccoy. The
> per-style lists are also a useful snapshot of where the collection's weight sits — useful
> for seeing that it is Blue Note-centred, and for nothing more.
>
> **Do not use this file to select recommendations for any page.** That is the specific
> error it was drawn into, and the selection bias it introduced is why every entry point in
> the orientation document is now flagged as needing re-derivation.

Derived mechanically from the **live published export** at

`jazz-canon/app/public/data/albums.json` on 2026-09-28. 254 albums.


> **Provenance note.** An earlier draft of this file was built from

> `mccoy-tyner/data/canon-draft.json`, which is a 100-album *working draft*

> from 2026-06-25, not the live canon. It showed no bebop and no outside

> material at all, and that was wrong. The live export below supersedes it.

> If the two disagree, the live export is the truth.


## The site's own style taxonomy — twelve styles, not seven

John named seven genres for the page. The site already classifies into twelve.

The mapping is not one-to-one, and the extras are informative:

| Site style | Albums | Page genre it maps to | Note |
|---|---:|---|---|
| Hard Bop | 98 | hard bop | |
| Post-Bop | 61 | post bop | |
| Cool Jazz | 34 | cool jazz | |
| Modal Jazz | 30 | modal | |
| Soul Jazz | 10 | soul jazz | |
| Free Jazz | 7 | catch-all (outside) | |
| Bebop | 5 | bebop | |
| Fusion | 3 | catch-all (outside) | |
| Jazz-Rock | 2 | catch-all (outside) — site splits this out of fusion | |
| Avant-Garde Jazz | 2 | catch-all (outside) | |
| Jazz-Funk | 1 | catch-all (outside) — site splits this out too | |
| European Jazz | 1 | catch-all (outside) / the ECM lane | |

Total: 254 albums. The seven genres John named cover 254 of them — i.e. the site has no styles outside the seven-genre frame, which is itself a finding.


## The centre of gravity, and the size of the outside

- **Inside** (bebop through soul jazz): **238 albums, 94%**

- **Outside** (free jazz, fusion, avant-garde, jazz-rock, jazz-funk, European): **16 albums, 6%**


So the Inside/Outside name is not a rhetorical flourish — but note the status header
on this file. The 94:6 figure is a dated snapshot, and the title's real warrant is
the documented musician's vocabulary behind the words, not this collection's
proportions. The ratio is useful here only to show that the outside branch is a
genuinely thin slice of the collection, which makes the four ECM mis-filings below
worth fixing.


## Every outside-branch album in the canon — the complete list

This is a short list, and it is the load-bearing evidence for the outside half of

the page. There are only 16.


### Free Jazz (7)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1960 | Change of the Century | Ornette Coleman | Atlantic |
| 1960 | Free Jazz: A Collective Improvisation | Ornette Coleman | Atlantic |
| 1964 | Spiritual Unity | Albert Ayler Trio | ESP-Disk' |
| 1965 | Ascension | John Coltrane | Impulse! |
| 1965 | The Heliocentric Worlds of Sun Ra, Vol. 1 | Sun Ra and His Solar Arkestra | ESP-Disk' |
| 1966 | Unit Structures | Cecil Taylor | Blue Note |
| 1980 | Playing | Old and New Dreams | ECM |

### Fusion (3)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1970 | Red Clay | Freddie Hubbard | CTI Records |
| 1970 | Bitches Brew | Miles Davis | Columbia |
| 1982 | Offramp | Pat Metheny Group | ECM |

### Jazz-Rock (2)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1969 | Emergency! | The Tony Williams Lifetime | Polydor |
| 1971 | The Inner Mounting Flame | Mahavishnu Orchestra | Columbia |

### Jazz-Funk (1)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1973 | Head Hunters | Herbie Hancock | Columbia |

### Avant-Garde Jazz (2)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1972 | Conference of the Birds | Dave Holland | ECM |
| 1983 | The Ballad of the Fallen | Charlie Haden | ECM |

### European Jazz (1)

| Year | Album | Artist | Label |
|---|---|---|---|
| 1973 | Witchi-Tai-To | Jan Garbarek / Bobo Stenson Quartet | ECM |

## The hinge albums: canon records that straddle the line

These are the most useful records on the page, because they are the ones that

make the category boundary visible. All are in the canon.

| Record | Artist | Year | Label | Why it is a hinge |
|---|---|---|---|---|
| *Conference of the Birds* | Dave Holland | 1972 | ECM | Filed as Avant-Garde Jazz, but it is a modal/Third Stream record on ECM. A triple hinge: label-lane, genre, and inside/outside all disagree. |
| *Old and New Dreams — *Playing** | Old and New Dreams | 1980 | ECM | Filed as Free Jazz. The group is Gil Evans, Alan Skidmore, Jimmy Heath and Jack DeJohnette — a hard-bop/Miles sidemen band. Clearly inside by personnel, filed outside by sound. |
| *Offramp* | Pat Metheny Group | 1982 | ECM | Filed as Fusion. By 1982 this is a smooth, well-crafted acoustic-electric record — the commercial tail of fusion, and arguably not fusion at all. |
| *The Ballad of the Fallen* | Charlie Haden | 1983 | ECM | Filed as Avant-Garde Jazz. Solo album; a memorial, not an avant-garde statement. Filing looks like a tagging error. |
| *Kind of Blue-adjacent modal block (30 albums)* | various | 1959 | various | Modal Jazz is the single largest *tag* on the site (20 records). Modal is the site's most porous boundary — it is a technique the canons kept absorbing. |

## A data-quality flag worth raising with mccoy

Four of the sixteen outside albums are ECM releases filed by *genre* rather than by
*lane*. `mccoy-tyner/config/style-research/free-jazz.md` explicitly states the rule that
ECM releases belong to the `ecm` style and must be handed off rather than surfaced as
free jazz — and the live export appears to breach that rule. Either the rule is not being
enforced downstream, or the export predates it.

This is not a page-writing problem, but it does affect the page: if the page describes the
outside branch using these four records as examples, it will be describing ECM records as
avant-garde. *The Ballad of the Fallen* in particular looks like a straightforward
mis-tag. Worth raising with mccoy before the page leans on any of them.

*(Checked and cleared: `Bird on 52nd Street` carries the label "Jazz Workshop" in the
export, which looked wrong but is correct — Concord's own catalogue confirms the album was
made for the short-lived Jazz Workshop label. No action there.)*


## Labels

| Label | Albums |
|---|---:|
| Blue Note | 87 |
| Columbia | 25 |
| Riverside | 17 |
| Atlantic | 15 |
| ECM | 12 |
| Prestige | 11 |
| Verve | 11 |
| Impulse! | 11 |
| Pacific Jazz | 5 |
| Contemporary | 5 |
| RCA Victor | 5 |
| Capitol | 4 |
| EmArcy | 4 |
| United Artists | 3 |
| Blue Note Records | 3 |
| Milestone | 3 |

Blue Note is 87 of 254. The canon is a heavily Blue Note canon,
which shapes which history it can tell.


## Style tags (secondary styles)

| Tag | Records |
|---|---:|
| modal-jazz | 20 |
| post-bop | 16 |
| hard-bop | 15 |
| ecm | 11 |
| soul-jazz | 9 |
| fusion | 4 |
| cool-jazz | 3 |
| avant-garde-jazz | 3 |
| spiritual-jazz | 1 |
| free-improvisation | 1 |
| free-jazz | 1 |
| jazz-rock | 1 |

`ecm` appears as a **tag** on 11 records and never as a primary style — the export
already treats ECM as a lane rather than a genre, which is the right call and directly
supports one of the page's structural points. Every other tag duplicates a primary style,
which is what makes the multi-style reading possible: `hard-bop` records also tagged
`modal-jazz` and `post-bop` are the site's own admission that these genres overlap.


## Year coverage

| Decade | Albums |
|---|---:|
| 1940s | 5 |
| 1950s | 84 |
| 1960s | 140 |
| 1970s | 20 |
| 1980s | 5 |

The canon runs 1945–1983, with the mass in the 1950s–60s. Bebop is represented
by just five albums, all 1945–48 — the thinnest and earliest edge of the collection, and
the only genre where the canon's holdings are genuinely a gateway rather than a survey.
