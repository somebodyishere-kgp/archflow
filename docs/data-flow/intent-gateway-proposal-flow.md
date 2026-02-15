# Data Flow: Intent Gateway Proposal Flow (Sprint 5)

Feature: Deterministic intent-to-proposal transformation

Input:
- REST request: `POST /intent/propose`
- Payload shape:
  - `intent_type`
  - `parameters`

Process:
1. Intent gateway validates required parameters by intent type.
2. Gateway verifies TwinGraph context references through read API lookups.
3. Deterministic parser maps intent to structured mutation templates.
4. Gateway sets `validation_status`:
   - `VALID` when checks pass
   - `BLOCKED` on any validation failure
5. Gateway emits `intent.proposed` event payload.

Output:
- `proposal_id`
- `proposed_mutations[]`
- `validation_status`
- `reasons[]` (when blocked)

Critical Constraint:
- Gateway does not write to TwinGraph.
- Intent output is proposal-only and awaits downstream approval/execution layers.
