# E6 Interaction Depth

E6 upgrades real CAD interaction depth while preserving deterministic runtime boundaries.

## Interaction Loop
- hover detection
- predictive snap scoring with axis bias + falloff
- pre-snap ghost transform
- constraint drag preview
- geometry execution handoff

## Performance Hardening
- instanced overlay batching
- frame budget limiter
- adaptive overlay density
- micro-animation inertia clamping

## Safety
- Feedback and interaction phases cannot trigger direct geometry writes.
- Rendering stays read-only.
