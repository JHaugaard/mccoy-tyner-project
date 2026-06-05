# McCoy Tyner

Compile ~100 canonical jazz albums (post-bebop through pre-Fusion), extract personnel data, and build an interactive web exploration app.

<intent>
Objective: Build a personal jazz discovery tool — curated canon, track-level personnel, searchable web app.
Outcomes: (1) ~100-album canon in structured data; (2) Track-level personnel records; (3) Fun, searchable web app for exploring albums and musicians.
Override: App stack TBD (decided in Phase 5); data storage decided in Phase 4 (JSON → possibly Postgres).
</intent>

<stack>
- runtime: TBD (Phase 5)
- framework: TBD (Phase 5)
- database: TBD — JSON draft files through Phase 3; schema locked in Phase 4
- deploy: vps2 or static host (decided in Phase 7)
</stack>

<gotchas>

- Scope = post-bebop, pre-Fusion; no Free Jazz. Albums too bebop or edging into Fusion are out.
- Personnel data is source-grounded — every claim carries an epistemic label (direct / inference / uncertain).
- No style quotas — 60 Modal Jazz albums is fine.
- Research/planning = Hermes; implementation = Kimi Code CLI/VS Code.
- Flag multi-agent parallel opportunities (Phase 1 source compiles, Phase 2 batch personnel extraction).

</gotchas>

<references>
<!-- ~/.claude/references/ — anthropic-best-practices/, contract-architecture/, agent-teams/ -->
<!-- Load on demand -->
</references>
