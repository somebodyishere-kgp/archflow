# ArchFlow Sprint 0 Bootstrap

This repository is initialized for Sprint 0 under the ArchFlow Constitution.

## Scope
- TwinGraph-first architecture baseline
- Governance and documentation ledgers
- CI-first workflow skeletons (no local build execution)
- Module scaffolding with explicit BLOCKED tracking where implementation is deferred

## Sprint 0 Deliverables
- Repository layout for core modules, agents, simulation, orchestration, and rendering
- Initial canonical schemas in `spec/`
- Event registry and event payload schemas
- CI workflow skeletons in `.github/workflows/`
- Sample dataset under `samples/2026-auditorium-brief/`

## Blocking Issue Template
Use this template for any deferred deterministic subsystem:

```md
issue_id: ISSUE-XXXX
module: <module-name>
symptoms: <what cannot run deterministically yet>
root_cause: <dependency, solver, or integration blocker>
affected_events: <comma-separated event names>
severity_level: <low|medium|high|critical>
blocking: true
next_action: <exact implementation path>
owner: <team or role>
```
