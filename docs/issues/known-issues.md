# Known Issues

issue_id: ISSUE-0001
module: geometry-kernel
symptoms: deterministic WKB sanitation pipeline not yet implemented for non-manifold edge cases
root_cause: cleanup pass specification exists but service implementation deferred to Sprint 1
affected_events: geometry.updated, twingraph.mutation
severity_level: high

issue_id: ISSUE-0002
module: regulation-agent
symptoms: deterministic clause validation unavailable for full NBC and local municipal corpus
root_cause: rule pack ingestion and clause text indexing pending
affected_events: compliance.report
severity_level: high

issue_id: ISSUE-0003
module: structure-agent
symptoms: deterministic sizing and load-path calculations unavailable in runtime
root_cause: solver container integration and contract tests pending
affected_events: structure.updated
severity_level: high

issue_id: ISSUE-0004
module: acoustic-agent
symptoms: RT60 simulation verification unavailable
root_cause: acoustic simulation container baseline missing
affected_events: acoustic.updated
severity_level: high

issue_id: ISSUE-0005
module: mep-agent
symptoms: clash report and route engine unavailable
root_cause: deterministic route and clearance constraint solver pending
affected_events: mep.updated
severity_level: high
