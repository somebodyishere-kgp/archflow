# System Status

Last Updated: 2026-02-16
Phase: Sprint 0 (Initialization)
Stability Rating: Experimental

## Active Modules
- Repository governance and documentation scaffolding
- Schema baseline (`spec/twingraph-schema.json`, event schemas)
- CI workflow skeletons under `.github/workflows/`

## In-Progress Modules
- Core TwinGraph deterministic ingestion pipeline
- Agent service implementations and deterministic solver integrations
- Documentation generation pipeline from TwinGraph query execution

## Experimental Modules
- Geometry kernel wrapper strategy (OpenCascade C++ service + WASM path)
- Dual backend adapter strategy (PostGIS and Neo4j overlay)

## Blocked Systems
- Regulation deterministic rule execution for NBC + local municipal packs: BLOCKED pending clause dataset packaging and parser integration
- Structure deterministic sizing solver integration: BLOCKED pending solver container wiring and verified load-case corpus
- Acoustic deterministic simulation pipeline: BLOCKED pending ray-tracing container baseline
- MEP deterministic route/clash engine: BLOCKED pending clearance-rule pack and route solver
- Documentation engine plan-view PDF generation from production TwinGraph query: BLOCKED pending query runtime and style rule compiler

## Blockers
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
