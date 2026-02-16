# Event Registry

This registry is authoritative for ArchFlow event contracts.

## Required Fields
- event_name
- publisher_module
- subscriber_modules
- payload_schema
- failure_conditions

## Registered Events

event_name: geometry.updated  
publisher_module: core-twingraph, geometry-kernel  
subscriber_modules: structure-agent, acoustic-agent, mep-agent, documentation-agent, rendering-client  
payload_schema: /spec/event-schemas/geometry.updated.json  
failure_conditions: invalid geometry WKB hex, schema mismatch, missing node id, transport emit failure

event_name: twingraph.mutation  
publisher_module: core-twingraph  
subscriber_modules: massing-generator, regulation-agent, documentation-agent, rendering-client  
payload_schema: /spec/event-schemas/twingraph.mutation.json  
failure_conditions: invalid node payload, schema validation failure, version conflict, missing relation target, transport emit failure

event_name: view.refresh
publisher_module: core-twingraph
subscriber_modules: rendering-client (primary consumer), documentation-agent
payload_schema: /spec/event-schemas/view.refresh.json
failure_conditions: view adapter schema mismatch, invalid limit bounds, transport emit failure

event_name: intent.proposed
publisher_module: orchestration-layer/intent-gateway
subscriber_modules: orchestration-layer/proposal-executor, human approval workflow
payload_schema: /spec/event-schemas/intent.proposed.json
failure_conditions: invalid intent parameters, missing TwinGraph context reference, proposal schema mismatch

event_name: proposal.executed
publisher_module: orchestration-layer/proposal-executor
subscriber_modules: core-twingraph audit trail, orchestration-layer observability
payload_schema: /spec/event-schemas/proposal.executed.json
failure_conditions: re-validation failure, ingest endpoint rejection, lineage metadata missing

event_name: proposal.blocked
publisher_module: orchestration-layer/proposal-executor
subscriber_modules: orchestration-layer observability, human review workflow
payload_schema: /spec/event-schemas/proposal.blocked.json
failure_conditions: invalid proposal schema, execution precondition failure, lineage metadata missing

event_name: render.sync
publisher_module: orchestration-layer/runtime-kernel
subscriber_modules: rendering-client runtime adapter
payload_schema: /spec/event-schemas/runtime.lineage.json
failure_conditions: missing runtime_cycle_id, scheduler out-of-order execution

event_name: design.insight.generated
publisher_module: orchestration-layer/autonomous-intelligence/agents
subscriber_modules: orchestration-layer/autonomous-intelligence/explainability, rendering-client intelligence overlay
payload_schema: /spec/event-schemas/design.insight.generated.json
failure_conditions: semantic graph missing context, invalid insight payload

event_name: design.evolution.updated
publisher_module: orchestration-layer/design-evolution
subscriber_modules: autonomous-intelligence proposal-generator, explainability
payload_schema: /spec/event-schemas/design.evolution.updated.json
failure_conditions: evolution lineage missing, context mismatch

event_name: design.evolution.insight
publisher_module: orchestration-layer/design-evolution
subscriber_modules: rendering-client evolution overlay, explainability
payload_schema: /spec/event-schemas/design.evolution.insight.json
failure_conditions: evolution insight payload invalid

event_name: design.proposal.generated
publisher_module: orchestration-layer/autonomous-intelligence/proposal-generator
subscriber_modules: intent-gateway intake bridge (future), explainability
payload_schema: /spec/event-schemas/intent.proposed.json
failure_conditions: adaptive strategy invalid, schema mismatch with intent contract

event_name: reflection.insight.generated
publisher_module: orchestration-layer/reflective-core/analysis
subscriber_modules: reflective-core/memory, explainability, runtime-kernel reflection adapter
payload_schema: /spec/event-schemas/reflection.insight.generated.json
failure_conditions: pipeline analysis payload incomplete, deterministic ordering violation

event_name: reflection.capability.proposed
publisher_module: orchestration-layer/reflective-core/capability-refactor
subscriber_modules: self-assembly-runtime blueprint feedback adapter
payload_schema: /spec/event-schemas/reflection.capability.proposed.json
failure_conditions: proposal missing capability list, direct mutation attempt bypassing blueprint adapter

## Transport Stabilization (Sprint 2)
- Active transport adapter: `LocalEventTransport` (`core-twingraph/src/twingraph/transport/local.py`)
- Planned transport adapter: `NatsEventTransport` (`core-twingraph/src/twingraph/transport/nats.py`)
- NATS status: BLOCKED (`ISSUE-0008`) until deterministic transport wiring and contract tests are implemented

event_name: structure.updated  
publisher_module: structure-agent  
subscriber_modules: documentation-agent, rendering-client  
payload_schema: /spec/event-schemas/structure.updated.json  
failure_conditions: solver unavailable, invalid load case, schema mismatch

event_name: acoustic.updated  
publisher_module: acoustic-agent  
subscriber_modules: documentation-agent, rendering-client  
payload_schema: /spec/event-schemas/acoustic.updated.json  
failure_conditions: simulation container failure, invalid material map

event_name: mep.updated  
publisher_module: mep-agent  
subscriber_modules: documentation-agent, rendering-client  
payload_schema: /spec/event-schemas/mep.updated.json  
failure_conditions: clash detection failure, clearance rule mismatch

event_name: documentation.refresh  
publisher_module: documentation-agent  
subscriber_modules: rendering-client, orchestration-layer  
payload_schema: /spec/event-schemas/documentation.refresh.json  
failure_conditions: query failure, template missing, schema mismatch

event_name: compliance.report  
publisher_module: regulation-agent  
subscriber_modules: documentation-agent, rendering-client, orchestration-layer  
payload_schema: /spec/event-schemas/compliance.report.json  
failure_conditions: rule pack missing, clause reference unresolved, schema mismatch
