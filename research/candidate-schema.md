# Candidate Album Schema

Every agent returns a markdown file containing three sections in order:
1. Source map table
2. One JSON block per candidate album
3. Synthesis notes

No deviations from this structure.

---

## Source Map (one per agent output file)

Each agent builds its own source map. IDs are local to that file (S1, S2, etc.).

| ID | Title | Type | URL or Location | Notes |
|----|-------|------|-----------------|-------|
| S1 | Penguin Guide to Jazz, 10th ed. | Book | — | Core critical reference |
| S2 | DownBeat Critics Poll Archive | Web | https://downbeat.com/polls | Historical polls |
| S3 | AllMusic genre page | Web | https://allmusic.com | Editor picks + ratings |

Add rows for every source consulted. Minimum 4 sources per agent.

---

## Candidate Record

One JSON block per album, using this exact structure:

```json
{
  "id": "artist-slug-album-slug-year",
  "artist": "Miles Davis",
  "album": "Kind of Blue",
  "year": 1959,
  "label": "Columbia",
  "style_primary": "modal-jazz",
  "style_tags": ["modal-jazz"],
  "sources": ["S1", "S2"],
  "epistemic": "obs",
  "rationale": "obs[S1]: Penguin Guide 4-star core collection. obs[S2]: DownBeat poll top-ranked. inf: universally recognized as defining modal jazz.",
  "priority": "must_have",
  "overlap_risk": "",
  "scope_flag": "",
  "include": null
}
```

### Field Definitions

| Field | Type | Rules |
|-------|------|-------|
| `id` | string | kebab-case. For group recordings use leader's name (e.g., `art-blakey-moanin-1958`). Year is the recording year if known, otherwise release year. |
| `artist` | string | Leader or primary artist name as commonly cited. |
| `album` | string | Full album title. |
| `year` | integer | Recording year preferred; release year if recording year unknown. |
| `label` | string | Original label (e.g., Blue Note, Prestige, Columbia). |
| `style_primary` | string | One of: `hard-bop` \| `soul-jazz` \| `cool-jazz` \| `modal-jazz` \| `post-bop` |
| `style_tags` | array | Include secondary style only if the album genuinely straddles two (e.g., hard bop with strong soul-jazz elements). Otherwise single-entry array. |
| `sources` | array | Source IDs from the file's source map. At least one required. |
| `epistemic` | string | `obs` if any source directly names the album; `inf` if reasoned from pattern; `unk` if single-source or uncertain. |
| `rationale` | string | Lead with `obs[ID]:` claims, then `inf:`, then `unk:`. Cite source IDs inline. |
| `priority` | string | Agent's own confidence signal. One of: `must_have` (non-negotiable; agent would advocate for this if cut) \| `strong` (clearly belongs, well-sourced) \| `consider` (worth including, lighter evidence or more marginal). |
| `overlap_risk` | string | Empty string if none. Otherwise name the overlapping style (e.g., `"hard-bop/soul-jazz border"`). |
| `scope_flag` | string | Empty string if clearly in scope. Otherwise state the concern (e.g., `"may be too bebop"`, `"1970 — check fusion proximity"`). |
| `include` | null | Always `null` from agents. John sets `true` or `false` at review. |

---

## Synthesis Notes (end of each agent file)

After all candidate records, append this section:

```markdown
## Synthesis Notes

### Must-Haves
The agent's own top 5–8 non-negotiables — albums it considers essential to this style's canon regardless of source count. These are the records the agent would advocate for most strongly if they were cut. One sentence per album explaining why.
[List here]

### Hidden Gems
Under-cited albums the agent considers underrated by the canonical lists — strong artistic merit, lighter consensus. These are the records John may not already know. One sentence per album.
[List here]

### Consensus Picks
Albums appearing in 3+ sources. These are the high-confidence core of the list.
[List here]

### Single-Source Picks
Albums from only one source but with strong critical weight. Flag for John's attention.
[List here]

### Scope Calls
Albums where a judgment call was made on the in/out boundary. One sentence per album explaining the call.
[List here]

### Gaps Noticed
Periods, figures, labels, or subgenres the consulted sources covered poorly.
[List here]
```
