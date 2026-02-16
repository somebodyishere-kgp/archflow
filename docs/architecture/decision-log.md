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

decision_id: ADR-S3-001
date: 2026-02-16
reason: Introduce View Adapter Boundary between TwinGraph and rendering consumption.
alternatives_considered: direct rendering-client reads from TwinGraph query rows; embedding view transforms in rendering-client
tradeoffs: additional adapter maintenance overhead in exchange for preventing UI coupling to TwinGraph schema
impact_scope: core-twingraph read layer, API view endpoints, event contract (`view.refresh`), CI schema validation path
rollback_strategy: remove `/twingraph/view/*` endpoints and revert rendering contract to direct query payloads if boundary fails deterministic requirements
arch_critical: true

decision_id: ADR-S4-001
title: Rendering Client Activated as Read-Only Consumer
date: 2026-02-16
reason: Maintain TwinGraph sovereignty while enabling first live visualization path.
alternatives_considered: direct UI access to TwinGraph internals; editable client-side geometry state
tradeoffs: stricter client constraints and adapter validation overhead, in return for deterministic read-only rendering guarantees
impact_scope: rendering-client data adapter, viewport modules, view event subscription, desktop CI build/test contract
rollback_strategy: disable rendering-client view subscription and revert to static DTO fixture rendering until read path is revalidated
arch_critical: true

decision_id: ADR-S5-001
title: Intent Gateway Introduced as Deterministic Mutation Proposal Layer
date: 2026-02-16
reason: Enable AI-assisted workflows without breaking TwinGraph authority.
alternatives_considered: direct intent-to-mutation writes into TwinGraph; agent-owned mutation pipelines
tradeoffs: additional proposal-review stage but strict preservation of TwinGraph write sovereignty
impact_scope: orchestration-layer intent gateway API, intent parsing/validation contracts, `intent.proposed` event schema and CI validation
rollback_strategy: disable intent gateway endpoints and revert to manual mutation specification if proposal quality becomes unstable
arch_critical: true

decision_id: ADR-S6-001
title: Proposal Executor Introduced as Deterministic Execution Boundary
date: 2026-02-16
reason: Separate proposal generation from execution while preserving TwinGraph write authority through ingest API only.
alternatives_considered: intent gateway direct writes; agent-owned direct TwinGraph mutation paths
tradeoffs: additional service boundary and validation overhead in exchange for deterministic lineage and controlled writes
impact_scope: orchestration-layer/proposal-executor module, `proposal.executed` event schema, system-integrity CI execution checks
rollback_strategy: disable proposal-executor event consumption and revert to manual approval execution flow
arch_critical: true

decision_id: ADR-ALPHA-001
title: Unified Runtime Execution Loop Introduced
date: 2026-02-16
reason: Integrate proposal lifecycle into a deterministic closed loop from intent to rendering sync.
alternatives_considered: loosely coupled module polling; direct module-to-module ad-hoc triggers
tradeoffs: tighter runtime contract and lineage requirements in exchange for reproducible end-to-end execution
impact_scope: proposal-executor, ingest metadata, transport lineage, runtime health, CI integration traces
rollback_strategy: disable unified loop and revert to manual staged execution per module
arch_critical: true

decision_id: ADR-BETA-001
title: Runtime Kernel Introduced for Deterministic Orchestration
date: 2026-02-16
reason: Centralize event scheduling and state propagation with strict runtime cycle boundaries.
alternatives_considered: decentralized schedulers per module
tradeoffs: additional orchestration module complexity versus guaranteed phase ordering and lineage replay
impact_scope: runtime-kernel scheduler/state engine/router, rendering kernel adapter, runtime-state schemas
rollback_strategy: pause kernel dispatch and fallback to proposal-executor direct loop while preserving event logs
arch_critical: true

decision_id: ADR-SIGMA-001
title: Autonomous Design Intelligence Engine Introduced
date: 2026-02-16
reason: Introduce deterministic semantic context and proposal generation without violating TwinGraph write authority.
alternatives_considered: direct intent generation by runtime kernel; LLM-driven proposal generation
tradeoffs: higher scaffolding complexity in exchange for explainable deterministic intelligence cycles
impact_scope: autonomous-intelligence semantic graph, proposal-generator, agents, explainability, render overlays
rollback_strategy: disable autonomous cycle triggers and fallback to manual intent proposals
arch_critical: true

decision_id: ADR-DELTA-001
title: Urban Intelligence Fabric Introduced
date: 2026-02-16
reason: Scale ArchFlow runtime from project-level intelligence to district/city-level deterministic reasoning.
alternatives_considered: keep single-building scope; external urban analytics service
tradeoffs: larger schema/runtime complexity in exchange for multi-scale deterministic planning capabilities
impact_scope: urban TwinGraph schema fields, infrastructure fabric engines, multi-scale scheduler, urban observability, urban rendering overlays
rollback_strategy: disable urban modules and fallback to project-level runtime cycles
arch_critical: true

decision_id: ADR-EPSILON-001
title: Deterministic Design Evolution Engine Introduced
date: 2026-02-16
reason: Enable adaptive, explainable proposal behavior without probabilistic learning systems.
alternatives_considered: static proposal heuristics only; ML-based model training
tradeoffs: added memory/index complexity in exchange for deterministic self-improving proposal scoring
impact_scope: design-evolution engine, adaptive proposal bias, kernel evolution adapter, evolution overlays, evolution schemas
rollback_strategy: disable adaptive bias and run proposal generator in baseline scoring mode
arch_critical: true

decision_id: ADR-OMEGA-CORE-001
title: Universal Systems Intelligence Engine Introduced
date: 2026-02-16
reason: Replace domain-specific semantic assumptions with a domain-agnostic systems graph runtime model.
alternatives_considered: incremental per-domain adapters; static architecture-only semantic layer
tradeoffs: higher abstraction complexity in exchange for broad system adaptability without module rewrites
impact_scope: universal-systems engine, adaptive-engine, dynamic runtime phases, generic systems renderer, CI systems validation
rollback_strategy: freeze adaptive domain inference and fallback to prior architecture-specific semantic graph
arch_critical: true

