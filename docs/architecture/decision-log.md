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
