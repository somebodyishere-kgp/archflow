# E5 Open-Source CAD Foundation

E5 expands XI++ with deterministic CAD foundation modules using established open-source patterns.

## Integrated Foundations
- OCCT adapter (`geometry-kernel/adapters/occt_adapter.py`) for boolean/topology operations through execution-runtime contracts.
- Parametric constraint solving (`geometry-kernel/interactions/parametric_constraint_solver.py`) inspired by SolveSpace/FreeCAD sketch logic.
- Three.js/react-three-fiber overlay path extensions under `rendering-client/src/e5/`.

## OCCT Runtime Status
- Adapter performs runtime availability checks for OCP/OCCT.
- If unavailable in environment, operation returns explicit `BLOCKED` status with reason.
- No fallback mutation paths are allowed.

## Architectural Guardrails
- UI/feedback layers orchestrate only; no direct geometry persistence.
- TwinGraph writes remain outside CAD interaction layers.
