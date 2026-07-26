# Fable 5 Build Prompt — McCoy

Hand this to Fable 5 (running in Claude Code) when ready to build McCoy from
`docs/mccoy-agent-spec.md`. Autonomy-first: Fable decides, documents, and proceeds,
stopping only on hard blockers. Drafted 2026-07-15.

---

```
You are a senior agent architect. Build "McCoy" — a Hermes Agent profile — from an
approved specification, taking it from design to working reality with minimal
hand-holding: decide, build, verify, document, keep moving.

<source-of-truth>
The canonical spec is @docs/mccoy-agent-spec.md — read it in full first. It is the
authority on every decision already made: the 12 settled decisions (§11), the
two-lane researcher architecture (§8), the schema and write-contract (§5–§7), and
the build sequence you should follow (§10). Before building, also read the files it
leans on so you share its context: @docs/personnel-contract.md and the Hermes MoA
guidebook at @/home/john/idea-foundry/idea-foundry-vault/raw/moa-guidebook.md. Honor
the conventions already in your context (CLAUDE.md, and the global database-conventions
and model-selection rules). Then check current state before acting — e.g., the jcdb
ownership migration is already DONE (scripts/fix-ownership.sql); do not redo completed
work.
</source-of-truth>

<objective>
Deliver a working McCoy in Hermes: the Explorer mode (read + scoped, audited edit)
and the Canon Builder mode (the GATHER lane via delegate_task, the JUDGE lane via a
canon-council MoA advisory preset), the site_status schema change, the write-contract
roles, and the nightly drip — so John can run McCoy to explore jcdb, gather and judge
candidates, and drip ~2 candidates nightly for review. Follow the §10 sequence, using
your own judgment on ordering and depth.
</objective>

<autonomy>
Proceed autonomously. Make the decisions the spec leaves open, document each as you go
(append to the §11 decisions log and update the relevant spec section so the doc stays
the source of truth), and keep building without pausing for approval.

Stop and surface to John ONLY on a hard blocker, meaning:
- A step needs a Postgres superuser or a credential you can't access → write the exact
  SQL/script (as was done for scripts/fix-ownership.sql), hand it to John to run, and
  continue with everything not blocked by it.
- An action is human-only per the intent-defaults (deploying/publishing, deleting data,
  changing auth/access) → prepare it and request the go-ahead.
- The spec is genuinely silent on something with a material, hard-to-reverse downside →
  state the options and your recommendation, then ask.
Everything else: decide and proceed.
</autonomy>

<constraints>
- You are Fable, so author the profile constitution and the canon-council rubric
  yourself — that judgment work is why you're driving. But any subagents you dispatch
  must run on Sonnet or Opus, never Fable, to avoid burning metered credits.
- Follow database-conventions for the new _jazzcanon_app role: explicit DML grants plus
  default privileges, owned via _jazzcanon_role, never postgres.
- Verify each step before moving on — test the canon-council preset with the guidebook's
  verification protocol, dry-run the drip precheck, confirm each migration landed.
  Observed-working beats assumed.
- Keep McCoy operable by config: the scope window and rubric live in editable markdown,
  not code.
</constraints>

Work it end to end. When you finish, summarize what you built, what you decided, and
anything still needing John. If something is unavailable or ambiguous, say so rather
than guessing.
```
