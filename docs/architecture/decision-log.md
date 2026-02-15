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
