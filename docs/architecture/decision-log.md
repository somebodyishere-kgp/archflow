# Architecture Decision Log

decision_id: ADR-0001
date: 2026-02-16
reason: Initialize ArchFlow Sprint 0 with CI-first governance and deterministic contract baselines.
alternatives_considered: ad-hoc local build workflow; delayed doc governance setup
tradeoffs: higher upfront documentation and CI burden, lower architectural drift risk
impact_scope: repository structure, CI policy, schema governance, event catalog
rollback_strategy: revert scaffold commit and regenerate from approved template if governance diverges
arch_critical: true

decision_id: ADR-0002
date: 2026-02-16
reason: Select NATS as initial event bus for typed event contracts and lightweight operational model.
alternatives_considered: Kafka
tradeoffs: simpler deployment and lower latency; fewer built-in stream retention semantics than Kafka
impact_scope: event bus baseline, agent pub/sub contract assumptions
rollback_strategy: abstract bus adapter in orchestration-layer and migrate to Kafka when scale/retention constraints require
arch_critical: true

decision_id: ADR-MU-001
date: 2026-02-16
reason: Introduce a deterministic Human Intelligence Interface layer that converts human imagination into proposal-compatible intent and reflective feedback contracts.
alternatives_considered: rich client with local orchestration logic; direct TwinGraph interaction from UI
tradeoffs: more interface modules and CI guardrails in exchange for strict runtime boundaries and explainability
impact_scope: human-interface modules, runtime-kernel phase extension, desktop-runtime shell, MU rendering overlays, explainability human endpoints
rollback_strategy: disable MU interface adapters and route intent directly to pre-existing proposal interfaces
arch_critical: true

decision_id: ADR-XI-001
title: Design Synthesis Engine Introduced
date: 2026-02-16
reason: Add deterministic geometry/layout synthesis between intent interpretation and execution boundary.
alternatives_considered: direct geometry generation in rendering client; manual CAD-first drafting workflows
tradeoffs: additional synthesis/kernel modules in exchange for reproducible geometry proposals and BIM-like drawing DTOs
impact_scope: design-synthesis orchestration, geometry-kernel modeling and drawing engine, runtime design.synthesis phase, desktop CAD shell, XI rendering overlays
rollback_strategy: disable synthesis phase and fallback to existing proposal-only intent flow while preserving TwinGraph write boundary
arch_critical: true

decision_id: ADR-XII-001
title: Generative Design Intelligence Layer Introduced
date: 2026-02-16
reason: Add schema-bound LLM reasoning to translate natural language intent into deterministic proposal-ready design intent.
alternatives_considered: rule-only non-LLM strategy parser; LLM direct geometry generation path
tradeoffs: added validation/safety complexity in exchange for richer human-language reasoning while preserving runtime authority boundaries
impact_scope: generative-intelligence adapter/reasoning/safety modules, runtime design.intent.generation phase, natural-language UI entry, XII rendering overlays, reflective alignment checks
rollback_strategy: disable design.intent.generation phase and fall back to MU+XI deterministic intent parser path
arch_critical: true

decision_id: ADR-XIPP-001
title: Deep Geometry Execution Layer Introduced
date: 2026-02-16
reason: Convert structured design intent into deterministic geometry execution steps and assembly-level DTO outputs.
alternatives_considered: direct geometry authoring in desktop runtime; LLM direct geometry generation
tradeoffs: additional geometry and assembly rule modules in exchange for reproducible BIM-like generation and mm-accurate drawing DTOs
impact_scope: geometry-kernel generators/structure/assembly, synthesis execution logic, runtime geometry.execution phase, xipp overlays and desktop inspection surfaces
rollback_strategy: disable geometry.execution phase and keep XI synthesis outputs at intent-only granularity
arch_critical: true

decision_id: ADR-XIII-001
title: Real-Time Co-Design Intelligence Introduced
date: 2026-02-16
reason: Enable deterministic continuous suggestion loops combining human deltas, LLM reasoning, and reflection checks.
alternatives_considered: one-shot request-response loop only; autonomous uncontrolled suggestion streams
tradeoffs: increased runtime phase complexity in exchange for adaptive collaboration and safer live guidance
impact_scope: codesign-runtime, realtime generative modules, runtime codesign phases, realtime desktop/render overlays, reflective safety validator
rollback_strategy: disable codesign phases and fallback to discrete XII/XI cycle execution
arch_critical: true

decision_id: ADR-XIV-001
title: Spatial Cognition Engine Introduced
date: 2026-02-16
reason: Add deterministic perception and movement intelligence to evaluate experiential quality before reflection and co-design decisions.
alternatives_considered: rely only on geometry/systems metrics; simulation-based crowd/visual engines
tradeoffs: added analysis modules in exchange for measurable spatial-experience signals without simulation overhead
impact_scope: spatial-cognition core and sub-engines, runtime spatial phase, generative bridge, reflection spatial alignment, xiv overlays
rollback_strategy: disable spatial.cognition.analysis phase and fallback to geometry/system-only analysis stack
arch_critical: true

decision_id: ADR-XVI-001
title: Adaptive Architectural World Model Introduced
date: 2026-02-16
reason: Provide deterministic environmental and urban context intelligence to guide generative and synthesis decisions.
alternatives_considered: static orientation heuristics; external API-driven context services
tradeoffs: additional world-analysis modules in exchange for context-aware design proposals without simulation overhead
impact_scope: world-model engines, world context bridge, runtime world context phase, synthesis world-aware adjustments, xvi overlays
rollback_strategy: disable world.context.analysis and fallback to intent-only generation path
arch_critical: true

decision_id: ADR-XV-001
title: Living Building Systems Engine Introduced
date: 2026-02-16
reason: Add deterministic systems intelligence for structural hierarchy, material layering, and passive behavior indicators.
alternatives_considered: defer systems reasoning to reflection only; simulation-heavy structural/energy engines
tradeoffs: broader analysis graph complexity in exchange for early systems feasibility signals without simulation overhead
impact_scope: building-systems engines, runtime building.systems.analysis phase, generative systems bridge, xv overlays and desktop inspectors
rollback_strategy: disable building.systems.analysis and fallback to geometry/world/spatial-only decision loop
arch_critical: true

decision_id: ADR-XVII-001
title: Continuous Architectural Consciousness Introduced
date: 2026-02-16
reason: Add persistent temporal project intelligence so ArchFlow can track design evolution and emit awareness signals across revisions.
alternatives_considered: stateless runtime cycles only; uncontrolled background autonomous adaptation
tradeoffs: additional temporal memory and scheduling modules in exchange for continuity-aware guidance and decision lineage
impact_scope: project-consciousness memory/context/awareness modules, runtime project.consciousness.update phase, consciousness bridge, xvii overlays and desktop memory views
rollback_strategy: disable project.consciousness.update and revert to stateless per-cycle runtime behavior
arch_critical: true

decision_id: ADR-E2-001
title: Interaction & Constraint Engine Introduced
date: 2026-02-16
reason: Upgrade XI++ execution authoring depth with deterministic selection/snap/transform/preview and constraint-driven incremental rebuild.
alternatives_considered: direct geometry mutation in React; full imperative CAD editing bypassing runtime execution
tradeoffs: added interaction orchestration complexity in exchange for safe parametric editing and low-latency non-destructive preview
impact_scope: geometry-kernel interaction/preview modules, runtime interaction.update phase, desktop interaction state machine, snap/preview overlays, performance throttling
rollback_strategy: disable interaction.update phase and revert desktop to selection-only inspection mode
arch_critical: true

decision_id: ADR-E3-001
title: Single User Workspace Intelligence Introduced
date: 2026-02-16
reason: Add deterministic single-user workspace orchestration for layout/focus/preset switching without altering TwinGraph or geometry execution.
alternatives_considered: multi-user collaboration state; embedding workspace state in project consciousness memory
tradeoffs: extra desktop/runtime state coordination in exchange for stable studio-like workspace continuity and viewport isolation
impact_scope: desktop-runtime workspace engine/preset/focus modules, viewport layout manager, runtime workspace.update phase, viewport state isolator extensions, workspace event contracts
rollback_strategy: disable workspace.update and revert to fixed single viewport shell with static panels
arch_critical: true

decision_id: ADR-E4-001
title: Design Flow Engine Introduced
date: 2026-02-16
reason: Introduce deterministic stage-based flow orchestration so single-user workspace behavior adapts by design phase without adding new intelligence layers.
alternatives_considered: static workspace controls only; direct geometry-triggered stage switching
tradeoffs: additional local orchestration state and UI wiring in exchange for guided continuity across concept/layout/systems/spatial/presentation workflows
impact_scope: desktop-runtime design flow controller/models/components, workspace state extensions, runtime design.flow.update phase, viewport overlay profile mapping, design flow event contracts
rollback_strategy: disable design.flow.update and fallback to E3 workspace-only controls
arch_critical: true

decision_id: ADR-E5-001
title: Live Design Feedback Engine + CAD Foundation Introduced
date: 2026-02-16
reason: Add continuous interaction feedback and production CAD foundation adapters to make single-user authoring responsive while preserving deterministic execution boundaries.
alternatives_considered: static feedback overlays; custom geometry kernel implementation from scratch
tradeoffs: increased runtime orchestration and adapter complexity in exchange for predictive snap UX, temporary ghost previews, and open-source-backed CAD operations
impact_scope: desktop feedback modules, CAD interaction engine, ghost preview pipeline, OCCT adapter, parametric constraint solver, runtime feedback.update phase, E5 overlays and event contracts
rollback_strategy: disable feedback.update and revert to E4 flow/runtime behavior with basic interaction previews only
arch_critical: true

decision_id: ADR-E6-001
title: CAD Completion & Stability Layer Introduced
date: 2026-02-16
reason: Consolidate CAD editing reliability with topology stability, history-aware execution, feedback hardening, and runtime write-guard enforcement.
alternatives_considered: defer stability to future phase; rely on ad-hoc per-module guards only
tradeoffs: deeper kernel/runtime orchestration complexity in exchange for safer edit continuity and predictable interaction behavior at scale
impact_scope: geometry stability managers, occt adapter hardening, interaction/feedback runtime refinements, performance batching controls, kernel execution guard and E6 CI artifacts
rollback_strategy: disable E6 stability adapters and fallback to E5 interaction/feedback runtime while preserving guardrails
arch_critical: true

decision_id: ADR-E7-001
title: Continuous Design Presence Runtime Introduced
date: 2026-02-17
reason: Add a lightweight runtime behavior layer for continuous micro-feedback and anticipation while preserving E4-E6 CAD execution boundaries.
alternatives_considered: static viewport-only overlays; adding new intelligence modules for interaction prediction
tradeoffs: additional low-latency signal routing and animation scheduling complexity in exchange for improved perceived continuity and motion without core logic changes
impact_scope: desktop presence runtime modules, E7 rendering overlays, runtime scheduler presence.update phase, presence event contracts, CI guard/artifact expansion
rollback_strategy: remove presence.update phase and disable desktop/rendering E7 modules while retaining E4-E6 feedback and interaction stack
arch_critical: true

decision_id: ADR-E8-001
title: Unified Desktop Runtime Boot Introduced
date: 2026-02-17
reason: Consolidate existing E3-E7 systems into a deterministic, launchable desktop lifecycle with safe runtime bridging and boot-time health signaling.
alternatives_considered: keep desktop runtime as disconnected modules; defer launch wiring until post-E8
tradeoffs: added boot orchestration and Electron lifecycle glue in exchange for executable launch readiness and runtime observability
impact_scope: desktop main/preload/window/bridge files, runtime bootstrap modules, default scene load path, system health panel, CI launch validations and E8 artifacts
rollback_strategy: disable E8 bootstrap entrypoint and fallback to module-level testing surfaces without desktop launch
arch_critical: true
