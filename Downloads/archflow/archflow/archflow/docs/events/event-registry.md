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
