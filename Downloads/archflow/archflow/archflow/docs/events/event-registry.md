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
publisher_module: geometry-kernel  
subscriber_modules: structure-agent, acoustic-agent, mep-agent, documentation-agent  
payload_schema: /spec/event-schemas/geometry.updated.json  
failure_conditions: invalid geometry WKB, schema mismatch, missing node id

event_name: twingraph.mutation  
publisher_module: core-twingraph  
subscriber_modules: massing-generator, regulation-agent, documentation-agent  
payload_schema: /spec/event-schemas/twingraph.mutation.json  
failure_conditions: invalid node payload, version conflict, missing relation target

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

event_name: human.feedback.generated
publisher_module: orchestration-layer/human-interface/feedback-engine
subscriber_modules: desktop-runtime, rendering-client, explainability
payload_schema: /spec/event-schemas/human.feedback.generated.json
failure_conditions: missing reflection translation input, feedback block schema mismatch, forbidden TwinGraph write in human-interface

event_name: design.synthesis.proposed
publisher_module: orchestration-layer/design-synthesis
subscriber_modules: proposal-executor boundary, geometry-kernel converters, rendering-client/src/xi
payload_schema: /spec/event-schemas/design.synthesis.proposed.json
failure_conditions: invalid synthesis payload, missing context id, direct TwinGraph mutation attempt in synthesis modules

event_name: design.intent.generated
publisher_module: orchestration-layer/generative-intelligence/reasoning-engine
subscriber_modules: orchestration-layer/design-synthesis, intent-gateway validation path, reflective-core alignment checks
payload_schema: /spec/event-schemas/design.intent.generated.json
failure_conditions: schema enforcement failure, hallucination safety rejection, TwinGraph mutation directive found in LLM output

event_name: geometry.execution.proposed
publisher_module: geometry-kernel
subscriber_modules: orchestration-layer/proposal-executor, rendering-client/src/xipp
payload_schema: /spec/event-schemas/geometry.execution.proposed.json
failure_conditions: non-deterministic geometry step ordering, direct TwinGraph write attempt

event_name: assembly.generated
publisher_module: geometry-kernel/assembly
subscriber_modules: rendering-client/src/xipp, desktop-runtime assembly inspector
payload_schema: /spec/event-schemas/assembly.generated.json
failure_conditions: missing material_layers/thickness/metadata_version fields

event_name: design.suggestion.generated
publisher_module: orchestration-layer/generative-intelligence/realtime
subscriber_modules: orchestration-layer/codesign-runtime, rendering-client/src/xiii, desktop-runtime codesign panel
payload_schema: /spec/event-schemas/design.suggestion.generated.json
failure_conditions: realtime loop non-deterministic ordering, schema validation bypass, unsafe proposal detected by reflection
