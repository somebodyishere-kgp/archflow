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

event_name: spatial.cognition.insight
publisher_module: orchestration-layer/spatial-cognition
subscriber_modules: reflective-core spatial alignment, rendering-client/src/xiv, desktop spatial cognition panel
payload_schema: /spec/event-schemas/spatial.cognition.insight.json
failure_conditions: missing perception metrics, direct mutation attempt, invalid cognition payload

event_name: spatial.flow.analysis
publisher_module: orchestration-layer/spatial-cognition/flow
subscriber_modules: codesign-runtime, rendering-client/src/xiv
payload_schema: /spec/event-schemas/spatial.flow.analysis.json
failure_conditions: invalid topology graph, missing flow metrics

event_name: world.context.insight
publisher_module: orchestration-layer/world-model
subscriber_modules: generative-intelligence world-context bridge, design-synthesis world-aware layout solver
payload_schema: /spec/event-schemas/world.context.insight.json
failure_conditions: missing world metrics, deterministic analysis contract violation

event_name: world.solar.analysis
publisher_module: orchestration-layer/world-model/solar
subscriber_modules: desktop world context panel, rendering-client/src/xvi
payload_schema: /spec/event-schemas/world.solar.analysis.json
failure_conditions: invalid orientation output, missing solar metrics

event_name: world.urban.flow
publisher_module: orchestration-layer/world-model/urban
subscriber_modules: rendering-client/src/xvi, design-synthesis entry strategy
payload_schema: /spec/event-schemas/world.urban.flow.json
failure_conditions: invalid flow graph, missing accessibility topology

event_name: building.systems.graph.updated
publisher_module: orchestration-layer/building-systems
subscriber_modules: reflective systems alignment, rendering-client/src/xv, desktop building systems panel
payload_schema: /spec/event-schemas/building.systems.graph.updated.json
failure_conditions: missing assembly relationships, invalid systems graph payload

event_name: building.material.analysis
publisher_module: orchestration-layer/building-systems/materials
subscriber_modules: generative building-systems bridge, rendering-client/src/xv
payload_schema: /spec/event-schemas/building.material.analysis.json
failure_conditions: incomplete material layer metadata, invalid analysis payload

event_name: project.memory.updated
publisher_module: orchestration-layer/project-consciousness
subscriber_modules: desktop project memory panel, rendering-client/src/xvii, reflective temporal alignment
payload_schema: /spec/event-schemas/project.memory.updated.json
failure_conditions: invalid memory graph linkage, revision continuity break

event_name: design.awareness.signal
publisher_module: orchestration-layer/project-consciousness/awareness
subscriber_modules: human feedback formatter, desktop timeline, rendering-client/src/xvii
payload_schema: /spec/event-schemas/design.awareness.signal.json
failure_conditions: non-deterministic awareness schedule, invalid priority signal payload

event_name: constraint.graph.updated
publisher_module: geometry-kernel/interactions
subscriber_modules: geometry execution runtime, preview mesh renderer, desktop constraint panel
payload_schema: /spec/event-schemas/constraint.graph.updated.json
failure_conditions: invalid constraint inheritance graph, dependency mismatch, direct TwinGraph write attempt

event_name: interaction.mode.changed
publisher_module: desktop-runtime interaction state machine
subscriber_modules: rendering-client interactions overlay, runtime interaction adapter
payload_schema: /spec/event-schemas/interaction.mode.changed.json
failure_conditions: illegal state transition, conflicting active tool modes

event_name: workspace.layout.changed
publisher_module: desktop-runtime/workspace
subscriber_modules: desktop-runtime viewport layout manager, rendering-client viewport isolator
payload_schema: /spec/event-schemas/workspace.layout.changed.json
failure_conditions: invalid preset mapping, missing viewport id set, workspace state routed into geometry execution

event_name: workspace.focus.mode
publisher_module: desktop-runtime/workspace
subscriber_modules: desktop runtime focus indicator, rendering-client overlay selection
payload_schema: /spec/event-schemas/workspace.focus.mode.json
failure_conditions: unsupported focus mode, workspace attempting TwinGraph mutation

event_name: design.flow.stage.changed
publisher_module: desktop-runtime/workspace/design-flow
subscriber_modules: workspace toolbar, viewport overlay isolator, runtime design flow adapter
payload_schema: /spec/event-schemas/design.flow.stage.changed.json
failure_conditions: invalid stage transition, flow update triggering geometry rebuild, workspace mutation boundary violation
