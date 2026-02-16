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
