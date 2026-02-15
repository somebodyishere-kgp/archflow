# Unified Runtime Flow (Phase Alpha)

Deterministic runtime loop:

1. `POST /intent/propose`
2. `intent.proposed` emitted with lineage envelope
3. `proposal-executor` consumes and validates proposal
4. For `VALID` proposals:
   - execute via `POST /twingraph/ingest`
   - emit `proposal.executed`
5. TwinGraph emits:
   - `twingraph.mutation`
   - `geometry.updated`
6. View endpoint emits `view.refresh`
7. Rendering Runtime Sync Engine refetches view and updates read-only scene state

Constraints enforced:
- no direct DB writes outside TwinGraph ingest boundary
- no rendering mutations
- no NATS activation
