# Architecture

## Overview

Seven-phase project: research → data extraction → schema → web app. Each phase gates on John's review before proceeding. Hermes orchestrates; Kimi Code implements.

## Phases

| Phase | Goal | Key Output |
|-------|------|------------|
| 0 | Infrastructure & conventions | `docs/conventions.md`, directory structure |
| 1 | Compile ~100-album canon | `data/canon-draft.json` |
| 2 | Primary musicians & production personnel | `data/personnel-draft.json` |
| 3 | Track-level personnel | `data/track-personnel.json` |
| 4 | Data model & schema design | `docs/schema.md`, `data/seed.json` |
| 5 | Web app architecture & stack selection | `docs/architecture.md` update, `app/` skeleton |
| 6 | Web app implementation | Working app in `app/` |
| 7 | Deployment & wrap | Live URL, `docs/maintenance.md` |

## Directory Structure

```
mccoy-tyner/
├── research/        # per-source compiles, synthesis docs
├── data/            # JSON drafts → validated seed data
├── app/             # web app (created in Phase 5)
└── docs/            # schema, conventions, deployment
```

## Data Flow

Research sources → per-source compile (markdown) → cross-source synthesis → canon-draft.json → personnel overlays → schema lock → seed.json → web app

## Parallel Agent Opportunities

- **Phase 1**: Multiple source compiles can run simultaneously (Penguin Guide, DownBeat, NPR, etc.)
- **Phase 2**: Personnel extraction batched by decade or label
- **Phase 6**: Frontend, backend, and data ingestion as separate Kimi Code agents

## External Dependencies

| Service | Purpose |
|---------|---------|
| AllMusic | Personnel discographies |
| Wikipedia | Album pages, sessionographies |
| Apple Music | Listening / verification |
| Kimi Code | Implementation harness |

## Decisions

<!-- Key architectural decisions. Add as made. -->
