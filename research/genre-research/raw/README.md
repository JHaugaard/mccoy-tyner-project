# `raw/` — what this folder is

**Created 2026-09-28 to 2026-09-29. 195 files, 42.5 MB.**

**Short answer to John's question: yes, mostly — but not a clean bibliography of excerpts.**
It is the raw capture layer for the whole project: the actual downloaded text of the sources
the research drew on, kept so that any claim in the corpus can be traced back to the bytes it
came from. It is closer to a research workbench than a library.

## Why it exists

Three reasons, in order of importance:

1. **Traceability.** Every claim in the dossiers is marked `RETRIEVED` or `RECALLED`. This
   folder is what makes `RETRIEVED` checkable rather than a boast.
2. **Recoverability.** Three subagents hit their tool-call ceilings during research and
   delivered nothing. Two more hit them again later. Every one of those runs still left its
   sources here, so a writing pass could be done later from the captures alone — which is
   exactly how the last three entry-point files got written. **The pattern that saved this
   project was: research to disk first, write second.**
3. **Honesty about failure.** Failed retrievals were left in place as zero-byte files rather
   than deleted, so the gaps are visible. See below.

## What is actually in it

| Group | Files | What they are |
|---|---|---|
| Top level | 162 | The first research pass: source dumps named by slug |
| `outs-*.md` | 20 | The free-jazz / avant-garde / fusion dossier's captures |
| `entry-late-*.txt` | 33 | The post-bop / modal / soul dossier's captures |
| `entry-points-inside-early/` | 33 | The bebop / cool / hard-bop dossier's captures — **the only group in its own subfolder** |

**158 of 194 text captures carry a source URL within the first 600 characters.** That is the
convention: the URL is in the header, so a capture is self-identifying.

The layout is **inconsistent** — three agents, three filing conventions, only one of which
used a subdirectory. Worth knowing before you go looking for something.

## The large files, and why they matter most

- **`amg2.txt` — 15.8 MB.** *The All Music Guide to Jazz*, full text. The single densest
  reference in the project.
- **`all_full.json` — 13.1 MB.** ~75 fetched pages in one blob. Awkward to read; useful for
  grepping across many sources at once.
- **`dg-jazz-woxx8.txt` (410KB) and `deveaux-birthofbebop2.txt` (411KB)** — the DeVeaux &
  Giddins *Jazz* textbook and "The Birth of Bebop." These two are the most readable
  *full-length scholarly* sources in the folder, and both are directly on your reading list.
- **`gioia-howtolisten.txt` (384KB)** — the whole of *How to Listen to Jazz*. **You can start
  reading tonight without buying anything.**
- **`lemponen-swingtobop.txt` (355KB)** — on the swing-to-bebop transition.

## Six zero-byte files

`deveaux-giddins-jazz-full.txt`, `deveaux-birthofbebop.txt`, `uncg-gelb-1959.txt`,
`writ-large-cecil.txt`, `dominickfarinacci-2ndliner.txt`, and the Reddit thread capture.

These are **retrievals that failed** — paywalls, dead links, or a site that refused the
fetch. They were left deliberately. A gap you can see is a gap you can close; a gap someone
tidied away is one you will trust by mistake.

Two of them produced real consequences. The DeVeaux full-text failure is why
`deveaux-birthofbebop2.txt` exists as a substitute capture. And one of the two
"unverified quotes" in the corpus — the Miles-on-Dolphy line — has been searched for across
this entire folder without success, which is a large part of why it is flagged rather than used.

## Honest caveats

- **This is not a controlled archive.** It is whatever the agents happened to fetch, in
  whatever order, with duplicates (`merriam-bebop.txt`, `merriam-bebop2.txt` and
  `merriam-parker.txt` are all 15,235 bytes — the same page saved under three names).
- **Britannica captures include AI-generated "Top Questions" panels.** Those are not
  Britannica editorial voice and are flagged wherever they were found. Do not quote them.
- **Some captures are truncated mid-argument**, including the Duhaime essay on one specific
  question. Noted in-file.
- **The folder is not needed to read the corpus.** Everything in `explainer/`, `long-form/`
  and `inside-outside.html` is written to stand alone. This is where you go to *check*
  something, not to begin.

## If you want to search it

```bash
cd ~/dev/active/mccoy-tyner/research/genre-research/raw
grep -ril "outside" . | head        # which sources even mention the term
grep -i -A3 "Hen Gates" .          # chase a specific claim to its capture
```

Start with `gioia-howtolisten.txt` and `dg-jazz-woxx8.txt`.
