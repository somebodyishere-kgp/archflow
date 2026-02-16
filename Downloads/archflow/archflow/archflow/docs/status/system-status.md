# System Status

Last Updated: 2026-02-16
Phase: Execution Era E6 (CAD Completion & Stability)
Stability Rating: Experimental

## Active Modules
- Repository governance and documentation scaffolding
- Schema baseline (`spec/twingraph-schema.json`, event schemas)
- CI workflow skeletons under `.github/workflows/`
- Human interface deterministic interpretation modules (`orchestration-layer/human-interface/`)
- Runtime kernel human phase adapter (`orchestration-layer/runtime-kernel/kernel_human_adapter.py`)
- Desktop runtime shell (`desktop-runtime/`)
- MU rendering overlays (`rendering-client/src/mu/`)
- Design synthesis engine (`orchestration-layer/design-synthesis/`)
- Geometry kernel deterministic modeling (`geometry-kernel/core/`, `geometry-kernel/modeling/`, `geometry-kernel/converters/`)
- Geometry drawing engine (`geometry-kernel/drawing-engine/`)
- Desktop CAD shell layer (`desktop-runtime/app-shell/CADViewport.tsx`, `ToolPalette.tsx`, `LayerManager.tsx`, `ParametricInspector.tsx`)
- XI rendering overlays (`rendering-client/src/xi/`)
- Generative intelligence LLM adapter (`orchestration-layer/generative-intelligence/llm-adapter/`)
- Generative reasoning engine (`orchestration-layer/generative-intelligence/reasoning-engine/`)
- Generative safety layer (`orchestration-layer/generative-intelligence/safety/`)
- Reflective LLM alignment checks (`orchestration-layer/reflective-core/analysis/reflection_llm_alignment.py`)
- Natural language intent entry (`orchestration-layer/human-interface/nlp-intent-entry.py`, `desktop-runtime/app-shell/NaturalLanguageInput.tsx`)
- XII rendering overlays (`rendering-client/src/xii/`)
- Geometry execution generators (`geometry-kernel/generators/`)
- Structural grid engine (`geometry-kernel/structure/`)
- BIM-like assembly builder (`geometry-kernel/assembly/`)
- XI++ rendering overlays (`rendering-client/src/xipp/`)
- Desktop assembly inspection surfaces (`desktop-runtime/app-shell/ParametricEditor.tsx`, `AssemblyInspector.tsx`, `PlanView.tsx`, `SectionView.tsx`)
- Co-design runtime stream engine (`orchestration-layer/codesign-runtime/`)
- Realtime generative suggestion modules (`orchestration-layer/generative-intelligence/realtime/`)
- Realtime intent stream (`orchestration-layer/human-interface/realtime-intent-stream.py`)
- XIII rendering overlays (`rendering-client/src/xiii/`)
- Co-design desktop surfaces (`desktop-runtime/app-shell/CoDesignPanel.tsx`, `SuggestionTimeline.tsx`, `RealtimeIntentBar.tsx`)
- Spatial cognition core (`orchestration-layer/spatial-cognition/`)
- Spatial reasoning bridge (`orchestration-layer/generative-intelligence/spatial_reasoning_bridge.py`)
- Spatial reflection alignment (`orchestration-layer/reflective-core/analysis/reflection_spatial_alignment.py`)
- XIV overlays (`rendering-client/src/xiv/`)
- Spatial desktop panels (`desktop-runtime/app-shell/SpatialCognitionPanel.tsx`, `ExperienceHeatmap.tsx`, `MovementGraphView.ts`)
- World model engines (`orchestration-layer/world-model/`)
- World context bridge (`orchestration-layer/generative-intelligence/world-context-bridge.py`)
- World alignment reflection (`orchestration-layer/reflective-core/analysis/reflection_world_alignment.py`)
- XVI overlays (`rendering-client/src/xvi/`)
- World desktop panels (`desktop-runtime/app-shell/WorldContextPanel.tsx`, `SolarCompassView.tsx`, `UrbanFlowGraph.ts`)
- Building systems engine (`orchestration-layer/building-systems/`)
- Building systems bridge (`orchestration-layer/generative-intelligence/building-systems-bridge.py`)
- Systems reflection alignment (`orchestration-layer/reflective-core/analysis/reflection_systems_alignment.py`)
- XV overlays (`rendering-client/src/xv/`)
- Building systems desktop panels (`desktop-runtime/app-shell/BuildingSystemsPanel.tsx`, `AssemblyGraphView.ts`, `MaterialStackInspector.tsx`, `LoadPathDiagram.tsx`)
- Project consciousness engine (`orchestration-layer/project-consciousness/`)
- Consciousness bridge (`orchestration-layer/generative-intelligence/consciousness-bridge.py`)
- Temporal reflection alignment (`orchestration-layer/reflective-core/analysis/reflection_temporal_alignment.py`)
- XVII overlays (`rendering-client/src/xvii/`)
- Consciousness desktop panels (`desktop-runtime/app-shell/ProjectMemoryPanel.tsx`, `DesignTimelineView.tsx`, `IntentEvolutionGraph.ts`)
- Geometry interaction constraint engine (`geometry-kernel/interactions/constraint_engine.py`)
- Incremental preview pipeline (`geometry-kernel/execution/preview_pipeline.py`)
- Desktop interaction state machine (`desktop-runtime/app-shell/InteractionStateMachine.ts`)
- Snap bridge and overlay (`rendering-client/src/interactions/`)
- Interaction runtime adapter (`orchestration-layer/runtime-kernel/kernel_interaction_adapter.py`)
- Workspace state engine (`desktop-runtime/workspace/WorkspaceStateEngine.ts`)
- Workspace focus and preset managers (`desktop-runtime/workspace/AIFocusModeManager.ts`, `desktop-runtime/workspace/WorkspacePresetManager.ts`)
- Viewport layout manager and workspace UI controls (`desktop-runtime/app-shell/ViewportLayoutManager.tsx`, `WorkspaceToolbar.tsx`, `LayoutSwitcher.tsx`, `FocusModeIndicator.tsx`, `ViewportTabs.tsx`)
- Workspace runtime adapter (`orchestration-layer/runtime-kernel/kernel_workspace_adapter.py`)
- Design flow controller (`desktop-runtime/workspace/DesignFlowController.ts`)
- Design flow profiles (`desktop-runtime/workspace/design_flow_models.ts`)
- Design flow UI surfaces (`desktop-runtime/app-shell/DesignFlowBar.tsx`, `FlowStageIndicator.tsx`, `FlowTransitionPanel.tsx`)
- Design flow runtime adapter (`orchestration-layer/runtime-kernel/kernel_design_flow_adapter.py`)
- Live feedback controller stack (`desktop-runtime/feedback/`)
- CAD interaction engine (`desktop-runtime/app-shell/CADInteractionEngine.ts`)
- Ghost preview runtime pipeline (`geometry-kernel/execution/ghost_preview_pipeline.py`)
- Parametric constraint solver (`geometry-kernel/interactions/parametric_constraint_solver.py`)
- OCCT adapter (`geometry-kernel/adapters/occt_adapter.py`)
- E5 rendering overlays (`rendering-client/src/e5/`)
- Feedback runtime adapter (`orchestration-layer/runtime-kernel/kernel_feedback_adapter.py`)
- Topology stability manager (`geometry-kernel/execution/topology_stability_manager.py`)
- Edit history manager (`geometry-kernel/execution/edit_history_manager.py`)
- Runtime execution guard (`orchestration-layer/runtime-kernel/kernel_execution_guard.py`)

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
- Human interface direct TwinGraph writes: BLOCKED by governance (proposal-only)
- Design synthesis direct TwinGraph writes: BLOCKED by governance (proposal executor boundary only)
- LLM direct TwinGraph writes or execution authority: BLOCKED by governance (reasoning-only contract)
- Geometry kernel direct TwinGraph writes: BLOCKED by governance (executor-only write boundary)
- Realtime co-design direct TwinGraph writes: BLOCKED by governance (observation/suggestion only)
- Spatial cognition direct TwinGraph writes: BLOCKED by governance (analysis only)
- World model direct TwinGraph writes: BLOCKED by governance (analysis only)
- Building systems direct TwinGraph writes: BLOCKED by governance (analysis only)
- Project consciousness direct TwinGraph writes: BLOCKED by governance (runtime memory only)
- Interaction layer direct TwinGraph writes: BLOCKED by governance (interaction intents + rebuild only)
- Workspace engine direct TwinGraph writes: BLOCKED by governance (local runtime state only)
- Design flow engine direct TwinGraph writes: BLOCKED by governance (orchestration-only local runtime layer)
- Feedback layer direct TwinGraph writes: BLOCKED by governance (visual/runtime orchestration only)
- OCCT runtime package availability on CI images: BLOCKED pending OCP/OCCT dependency provisioning for full boolean execution
- Full workflow discovery on default branch: BLOCKED until repository default branch is switched to a branch containing `.github/workflows/` (e.g. `ci-root` or `feature/init-repo`)

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
