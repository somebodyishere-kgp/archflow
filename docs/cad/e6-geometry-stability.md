# E6 Geometry Stability

E6 hardens the CAD geometry execution foundation for reliable authoring under repeated edits.

## Stability Modules
- `geometry-kernel/adapters/occt_adapter.py`
- `geometry-kernel/execution/topology_stability_manager.py`
- `geometry-kernel/execution/edit_history_manager.py`
- `geometry-kernel/interactions/parametric_constraint_solver.py`

## Guarantees
- Boolean ops pass through stable wrapper + edge healing + face merge safety checks.
- Topology identity is preserved across incremental rebuilds.
- Parametric bindings survive topology remapping when valid.
- Constraint solver reports conflicts and visual error diagnostics deterministically.

## Boundary
- No UI/workspace/feedback TwinGraph writes.
- No persistent ghost preview writes.
