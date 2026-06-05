# McCoy Tyner Project — Conventions

**Version:** 1.0  
**Date:** 2026-06-04

---

## Directory Structure

```
mccoy-tyner/
├── app/           # Web application (Phase 5+)
├── data/          # Structured data files (JSON, SQL seeds)
├── docs/          # Documentation, plans, architecture
├── research/      # Research compiler artifacts
├── .claude/       # Existing (pre-existing)
├── .env.example   # Template for environment variables
├── .env.local     # Local secrets (gitignored)
└── .gitignore
```

---

## Naming Conventions

- **Files/directories**: kebab-case (e.g., `canon-draft.json`, `source-penguin-guide.md`)
- **Research compiles**: `source-<name>-compile.md` (e.g., `source-penguin-guide-compile.md`)
- **Data files**: `<entity>-<stage>.json` (e.g., `canon-draft.json`, `personnel-draft.json`)
- **Dates in filenames**: ISO 8601 prefix (e.g., `2026-06-04-canon-synthesis.md`)

---

## Data Format (Phase 0–3)

- **Default**: JSON — human-readable, git-diffable, no dependencies
- **Encoding**: UTF-8
- **Indentation**: 2 spaces
- **Schema**: Documented in `docs/schema.md` (Phase 4); data files are authoritative until schema lock

---

## Epistemic Labels (Required on All Research Artifacts)

Every claim in research compiles and data files must carry one of:

| Label | Meaning | Prefix in Notes |
|-------|---------|-----------------|
| `obs` | Direct observation / tool output / source quote | `obs:` |
| `inf` | Inference / reasoned conclusion | `inf:` |
| `unk` | Unknown / absent / weakly supported | `unk:` |

Example:
```markdown
- obs: Penguin Guide lists "Kind of Blue" as 4-star core collection (p. 124)
- inf: This suggests consensus canonical status across jazz critics
- unk: No record of Japanese pressing personnel differences
```

---

## Source Citation Standard

Every research artifact must include a source map with:

```markdown
## Source Map

| ID | Title | Type | URL | Date Accessed | Notes |
|----|-------|------|-----|---------------|-------|
| S1 | Penguin Guide to Jazz, 10th ed. | Book | — | 2026-06-05 | Core reference |
| S2 | DownBeat Critics Poll 2023 | Web | https://... | 2026-06-05 | Contemporary list |
```

All claims reference source IDs (e.g., `[S1]`, `[S2p45]` for page 45).

---

## Version Control

- **Repo**: `git init` at project root
- **Branches**: `main` only (no feature branches for solo work)
- **Commits**: Conventional-ish subject lines (e.g., `Add canon draft from Penguin Guide`)
- **Ignored**: `.env.local`, `*.log`, `node_modules/`, `.DS_Store`, Apple Music cache files

---

## Research Compile Workflow

Per `research-compiler` skill:

1. **Scope**: Define question, depth (quick/standard/deep), output path
2. **Gather**: 4–8 quality sources (not exhaustive)
3. **Source notes**: Per-source, with epistemic labels
4. **Compare**: Agreement, disagreement, gaps, terminology drift
5. **Synthesize**: Separate obs / inf / unk explicitly
6. **Artifact**: Use `research-compile-template.md` structure
7. **Recommend**: Vault promotion? Honcho conclusions? Follow-up?

**Gate**: John reviews artifact before any data enters `data/`.

---

## Coding Model (Phase 5 Decision)

- Deferred to Phase 5
- Options: Kimi Code, Claude Code, Codex, other
- Decision criteria: Agent swarm support, code quality, John's prompt-crafting comfort
- Hermes drafts architecture + prompts; coding model implements

---

## Environment

- **vps8**: Postgres 5433, Hermes, Honcho, Syncthing, Caddy
- **vps4**: Ollama (local inference), dev projects
- **vps2**: Lightweight app hosting (deployment target)
- **Secrets**: `.env.local` (gitignored); template in `.env.example`

---

## Review Gates (Non-Negotiable)

| Phase | Gate |
|-------|------|
| 0 | Conventions approved |
| 1 | `canon-draft.json` ~100 albums confirmed |
| 2 | Personnel spot-check (5–10 albums) |
| 3 | Track-personnel model supports exploration |
| 4 | Schema supports album→track→personnel + musician→albums→tracks |
| 5 | Architecture + UX approved before code |
| 6 | App meets "fun, cool, informative" bar on vps2 |

---

*Update this file as conventions evolve. Commit changes.*