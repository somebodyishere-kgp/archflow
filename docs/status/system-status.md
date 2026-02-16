# System Status

Last Updated: 2026-02-16
Phase: Program Kappa (Reflective Intelligence Core)
Stability Rating: Experimental

## Active Modules
- TwinGraph deterministic schema validation pipeline
- PostgreSQL + PostGIS TwinGraph adapter (`core-twingraph/src/twingraph/db.py`)
- TwinGraph ingest service with mutation and geometry event emission
- TwinGraph deterministic query API (`GET /twingraph/node/{id}`, `POST /twingraph/query`)
- Event transport abstraction with active local adapter
- TwinGraph read-only view adapter boundary (`core-twingraph/src/twingraph/views/`)
- Deterministic view endpoints (`GET /twingraph/view/geometry`, `POST /twingraph/view/section`)
- Sprint 4: Rendering Client Read Layer Active
- Rendering client data adapter and view subscription (`rendering-client/src/services/`)
- Deterministic viewport pipeline (`rendering-client/src/viewport/`)
- Intent Gateway deterministic proposal service (`orchestration-layer/intent-gateway/`)
- Proposal Executor deterministic execution boundary (`orchestration-layer/proposal-executor/`)
- Unified runtime health service (`orchestration-layer/runtime-health/`)
- Runtime kernel orchestration module (`orchestration-layer/runtime-kernel/`)
- Intelligence scaffold (no LLM execution) (`orchestration-layer/intelligence-scaffold/`)
- Autonomous intelligence engine (`orchestration-layer/autonomous-intelligence/`)
- Rendering intelligence overlays (`rendering-client/src/intelligence/`)
- Urban intelligence fabric (`orchestration-layer/autonomous-intelligence/infrastructure-fabric/`)
- Urban observability layer (`orchestration-layer/urban-observability/`)
- Urban rendering overlays (`rendering-client/src/urban/`)
- Design evolution engine (`orchestration-layer/design-evolution/`)
- Rendering evolution overlays (`rendering-client/src/evolution/`)
- Universal systems graph engine (`orchestration-layer/autonomous-intelligence/universal-systems/`)
- Adaptive intelligence engine (`orchestration-layer/autonomous-intelligence/adaptive-engine/`)
- Domain-neutral runtime kernel expansion (`runtime-kernel/dynamic_phase_engine.py`, `runtime-kernel/domain_context_manager.py`)
- Universal systems rendering (`rendering-client/src/systems/`)
- Reflective intelligence core (`orchestration-layer/reflective-core/`)
- Self-assembly blueprint feedback adapter (`orchestration-layer/self-assembly-runtime/`)
- Kappa visualization overlays (`rendering-client/src/kappa/`)
- CI-backed deterministic TwinGraph tests under `.github/workflows/test-twingraph.yml`

## In-Progress Modules
- TwinGraph relational and graph dual-backend strategy (Neo4j overlay pending)
- Agent service implementations and deterministic solver integrations
- Documentation generation pipeline from TwinGraph query execution

## Experimental Modules
- Geometry kernel wrapper strategy (OpenCascade C++ service + WASM path)
- Dual backend adapter strategy (PostGIS and Neo4j overlay)

## Blocked Systems
- NATS event transport adapter: BLOCKED pending deterministic transport integration and contract tests
- Intent proposal execution pipeline: BLOCKED until approved mutation executor layer is introduced
- NATS-backed proposal subscription transport: BLOCKED pending deterministic NATS rollout
- Runtime kernel to NATS transport bridge: BLOCKED by governance (local transport only)
- Neo4j adapter parity for TwinGraph backend abstraction: BLOCKED pending Sprint 1b implementation
- Regulation deterministic rule execution for NBC + local municipal packs: BLOCKED pending clause dataset packaging and parser integration
- Structure deterministic sizing solver integration: BLOCKED pending solver container wiring and verified load-case corpus
- Acoustic deterministic simulation pipeline: BLOCKED pending ray-tracing container baseline
- MEP deterministic route/clash engine: BLOCKED pending clearance-rule pack and route solver
- Documentation engine plan-view PDF generation from production TwinGraph query: BLOCKED pending query runtime and style rule compiler

## Blockers
- issue_id: ISSUE-0010
  module: orchestration-layer/intent-gateway
  symptoms: intent proposals cannot be executed by design
  root_cause: sprint scope enforces proposal-only gateway with no TwinGraph write authority
  affected_events: intent.proposed
  severity_level: medium
  blocking: true
- issue_id: ISSUE-0011
  module: orchestration-layer/proposal-executor
  symptoms: executor transport limited to local event audit adapter
  root_cause: NATS transport remains blocked by architecture governance
  affected_events: intent.proposed, proposal.executed
  severity_level: medium
  blocking: true
- issue_id: ISSUE-0008
  module: core-twingraph
  symptoms: NATS event transport cannot be used; local adapter only
  root_cause: transport abstraction introduced before deterministic NATS integration and CI contract validation
  affected_events: twingraph.mutation, geometry.updated
  severity_level: medium
  blocking: true
- issue_id: ISSUE-0009
  module: core-twingraph
  symptoms: rendering contract depends on view adapter endpoint stability and schema lock
  root_cause: read-layer introduced before downstream rendering-client integration cycle
  affected_events: view.refresh
  severity_level: medium
  blocking: true
- issue_id: ISSUE-0007
  module: core-twingraph
  symptoms: Neo4j backend adapter missing while PostGIS adapter is active
  root_cause: Sprint 1 scope constrained to PostgreSQL + PostGIS deterministic path
  affected_events: twingraph.mutation, geometry.updated
  severity_level: medium
  blocking: true
- issue_id: ISSUE-0002
  module: regulation-agent
  symptoms: cannot produce deterministic compliance outputs without source clause pack + parser
  root_cause: statutory corpus and clause index are not yet integrated
  affected_events: compliance.report
  severity_level: high
  blocking: true
- issue_id: ISSUE-0003
  module: structure-agent
  symptoms: deterministic member sizing unavailable
  root_cause: solver execution pipeline not yet wired in CI container
  affected_events: structure.updated
  severity_level: high
  blocking: true
- issue_id: ISSUE-0004
  module: acoustic-agent
  symptoms: RT60 validation path unavailable
  root_cause: acoustic simulation service container not yet integrated
  affected_events: acoustic.updated
  severity_level: high
  blocking: true
- issue_id: ISSUE-0005
  module: mep-agent
  symptoms: route and clash calculations not deterministic yet
  root_cause: clearance rule engine and route constraints incomplete
  affected_events: mep.updated
  severity_level: high
  blocking: true
- issue_id: ISSUE-0006
  module: documentation-agent
  symptoms: production-grade plan PDF generation query path incomplete
  root_cause: style compiler and projection query executor not integrated
  affected_events: documentation.refresh
  severity_level: medium
  blocking: true
