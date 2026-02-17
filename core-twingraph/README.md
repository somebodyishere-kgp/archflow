# core-twingraph

TwinGraph ingestion, mutation validation, and backend adapter boundaries live here.

## Sprint 0 Intent
- Enforce canonical schema validation for all node mutations.
- Define adapter interfaces for PostGIS and Neo4j backends.
- Emit `twingraph.mutation` only after deterministic validation.

## Blocking Issue Template
issue_id: ISSUE-XXXX
module: core-twingraph
symptoms: <deterministic behavior missing>
root_cause: <exact blocker>
affected_events: twingraph.mutation
severity_level: <low|medium|high|critical>
