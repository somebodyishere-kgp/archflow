# Runtime Kernel Architecture (Phase Beta)

Runtime Kernel centralizes deterministic orchestration:

- Event routing with lineage (`event_id`, `parent_event_id`, `execution_id`, `runtime_cycle_id`)
- Scheduler phase ordering:
  1. `intent.proposed`
  2. `proposal.executed`
  3. `twingraph.mutation`
  4. `geometry.updated`
  5. `view.refresh`
  6. `render.sync`
- Runtime state propagation:
  - `runtime_cycle_id`
  - `last_execution_id`
  - `last_view_revision`
  - `active_modules`
  - `event_queue_depth`

Rendering integration:
- Rendering client syncs only when `render.sync` is observed via kernel adapter.
