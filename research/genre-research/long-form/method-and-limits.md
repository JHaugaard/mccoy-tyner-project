# genre-research — research dossier for the jazzcanon.com "Inside/Outside" page

**Created 2026-09-28 by space-bunny, at John's request.**

## What this is

John is writing a new page on jazzcanon.com called **Inside/Outside** — a plain-language
(not scholarly) orientation to jazz genres, covering bebop, cool jazz, hard bop, post bop,
modal, soul jazz, and a catch-all for free jazz / fusion / avant-garde.

**John writes all the prose.** This corpus is the research and argument underneath it. No
page design work was done, no canon data was modified, and nothing here is page copy.

## Start here

Open **`inside-outside.html`** — the single orientation artifact. It carries the verdict, the
three-axes correction, the canon's 94:6 ratio, the genre map, the hinge records, the mislabel
traps, five key dates, a proposed page shape, and three questions awaiting John's decision.

In a terminal browser:

```
$ cd ~/dev/active/mccoy-tyner/research/genre-research
$ python3 -m http.server 8000
# then open http://localhost:8000/inside-outside.html
```

## The three things to know before reading anything else

**1. The name is real, sourced musician's vocabulary — not a metaphor.** "Inside/outside"
is a term of art: improvising within a standard's chord changes versus stepping outside them
entirely. It has a textbook chapter (Mark Levine, *The Jazz Theory Book*), a period label
("out music," Gridley), and Miles Davis's own phrase "the way-out thing." Anchored on Justin
Duhaime, "Eric Dolphy & Outness" (2011).

**2. The word is relative, and that is the page's best material.** Levine: *"Bird was
considered 'out' by many musicians in the 1940s."* Charlie Parker — the foundation of the
"inside" tradition — was once the radical outsider. The boundary has moved at least twice.
Whether the page makes this its argument or a passing hedge is **Open Question 1**.

**3. Fusion is not "outside," and lumping it in is the main risk to the page.** Fusion is
electric and groove-driven but harmonically *inside* — vamps, riffs, ostinatos. *Bitches Brew*
is radical in texture and studio construction, not in abandoning the changes. mccoy and I
reached this independently. The page needs three crossing axes, not one. **Open Question 2.**

## Map of the corpus

| Folder | Contents |
|---|---|
| `inside-outside.html` | **The orientation artifact.** Open this first. |
| `00-orientation/` | This file. |
| `01-genres/` | One file per genre — bebop, cool jazz, hard bop, post bop, modal, soul jazz, free jazz, fusion, avant-garde — plus `outside-glossary.md`. |
| `02-timeline/` | `master-timeline.md` (1945–85, canon density by year, confidence marks on every anchor) and two seam analyses. |
| `03-listeners-guide/` | How to enter each genre, gateway records, and an honest account of what puts a newcomer off. |
| `04-players/` | `canon-inventory.md` — all 254 canon albums by style, the 94:6 ratio, hinge records, and a data-quality flag. |
| `05-sources/` | `sources.md` — every source with a confidence mark, plus a log of what I got wrong. |
| `06-inside-outside-thesis/` | The core argument: `thesis-and-page-architecture.md` (read first), the terminology case, and the three-outside-branches comparison. |
| `raw/` | Verbatim source captures, mccoy's consultation, and search results. |

## How to read the genre files

They are **research, not copy** — dense, cited, and written to be argued from. Every genre
file carries the same ten sections, ending with two that matter most:

- **CONTESTED AND UNCERTAIN** — what historians actually dispute. These sections are the
  honest part of the corpus. Post-bop's is four separate live arguments.
- **Sources** — numbered URLs, each with a note on what it supports.

Where a file says a claim is recalled rather than retrieved, it says so. **Check the
uncertainty sections before putting anything on a public page.**

## Method and honest limits

- **Canon figures are derived mechanically** from the live export
  `jazz-canon/app/public/data/albums.json` (254 albums, 1945–1983), not estimated.
- **mccoy's advisory** is preserved verbatim at `raw/consultation-mccoy-2026-09-28.txt` and is
  credited inline wherever used. It supplied the gateway records, the hinge list, the mislabel
  traps, and a briefing on John's standing positions.
- **Three research subagents** produced the per-genre files. Their output was checked for
  required structure and sourcing; spot checks confirmed genuine engagement with contested
  scholarship. They are drafts to argue with, not finished authority.
- **I could not complete the researcher consultation.** The `researcher` profile returns
  `HTTP 401: User not found` from its OpenRouter route. Short single-turn queries work when
  the model is explicitly pinned; anything longer fails when the turn re-resolves to the
  profile's own (broken) route. This is a credential/config fault on that profile, not a
  research failure — its brief was covered by the subagents instead. **Needs a fix from John
  or the-super.**
- **A second infrastructure fault:** mccoy's outbound bot DM failed at spawn with
  `No module named 'ruamel'`. Its answer still reached me (it preserved the text to disk), but
  the delivery path is broken on the shared venv.
- **Nothing was written outside this folder.**

## Known correction made during the work

An early pass read `mccoy-tyner/data/canon-draft.json` — a 100-album *working draft* — and
concluded the canon contained no bebop and no outside material. That was wrong: the live
export holds 5 bebop and 16 outside albums. The draft-based claim was corrected in
`04-players/canon-inventory.md`, and the mistake is logged in `05-sources/sources.md` §4.

## Open questions for John

1. Make the "outside is a relative term" argument the page's spine, or state it once and move on?
2. Split fusion out as "the electric turn" on its own axis?
3. One outside section (free + avant-garde) or two?
