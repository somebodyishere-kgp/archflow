# intent-gateway

Deterministic intent proposal gateway for ArchFlow orchestration.

## Scope (Sprint 5)
- Accept structured design intent via `POST /intent/propose`.
- Validate intent type, parameters, and TwinGraph context references.
- Produce structured mutation proposals only.
- Emit `intent.proposed` event payloads for downstream review.

## Hard Constraints
- No direct TwinGraph mutations.
- No LLM or probabilistic parsing.
- No simulation or agent expansion.
- NATS transport remains BLOCKED; local transport only.
