# ArchFlow Execution Manifesto

This repository executes ArchFlow delivery through governance-first engineering.

## Execution Rules
- CI is the execution authority for build, test, and simulation.
- No mock engineering outputs; unresolved deterministic work is marked BLOCKED.
- Every new event is registered with schema and documented failure conditions.
- TwinGraph schema and architecture-impacting changes require decision log updates.
- Releases require passing workflows, traceable artifacts, and human review.
