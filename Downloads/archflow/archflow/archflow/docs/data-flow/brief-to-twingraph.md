# Data Flow: Brief to TwinGraph (2026 Auditorium)

Feature: 2026 Auditorium Brief Ingestion Baseline

Input:
- `samples/2026-auditorium-brief/brief.md`
- `samples/2026-auditorium-brief/parsed.json`
- Trigger event: `brief.ingest` (planned in Sprint 1)

Process:
1. Brief parser service reads normalized brief content and extracts entities.
2. Parsed entity payload is validated against TwinGraph schema constraints.
3. Core TwinGraph ingestion emits `twingraph.mutation` for each node/relation change.
4. Massing generator (planned) subscribes to `twingraph.mutation` and emits `massing.generated`.
5. Regulation agent (planned deterministic checks) subscribes to `massing.generated` and emits `compliance.report`.
6. Documentation agent (planned) consumes compliance and massing events to emit `documentation.refresh`.

Validation Layers:
- Schema validation against `spec/twingraph-schema.json`
- Event payload validation against `spec/event-schemas/*`
- Deterministic checks only; no AI output accepted as final engineering truth

Output:
- TwinGraph node set persisted by backend adapters
- Compliance and documentation events registered for downstream modules

Current Sprint 0 Status:
- Flow documented
- Runtime implementation BLOCKED for deterministic parser/solver-backed steps (see `docs/status/system-status.md`)
