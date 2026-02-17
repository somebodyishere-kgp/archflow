# proposal-executor

Deterministic execution boundary for validated intent proposals.

## Scope (Sprint 6)
- Consume `intent.proposed` events via local transport adapter.
- Re-validate proposal payload schema before execution.
- Execute only proposals with `validation_status = VALID`.
- Convert supported proposals into TwinGraph ingest requests.
- Emit `proposal.executed` with execution lineage metadata.

## Hard Constraints
- Does not grant write authority to intent-gateway.
- Executes writes only through `POST /twingraph/ingest`.
- No NATS activation, no simulations, no rendering changes.
