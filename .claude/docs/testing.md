# Testing

## Data Validation (Phases 1–3)

| Gate | Check |
|------|-------|
| Phase 1 | John reviews canon-draft.json, confirms or adjusts the ~100 |
| Phase 2 | John spot-checks 5–10 albums for personnel accuracy |
| Phase 3 | John confirms data model supports exploration goals |
| Phase 4 | John reviews schema before any app work begins |

## Epistemic Labeling

Every personnel claim in JSON data carries one of:
- `direct` — confirmed from liner notes, official discography
- `inference` — derived from sessionography cross-reference
- `uncertain` — single source, unverified

## App Testing (Phase 6)

Commands TBD — added when stack is selected in Phase 5.

## Data Integrity Rules

- Source URLs preserved for every research claim
- Data files are git-tracked (versioned)
- Validation scripts run before schema lock in Phase 4
