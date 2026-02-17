# E7 Continuous Design Presence Runtime

Execution Era E7 adds a micro-feedback runtime over E4-E6 without introducing new intelligence layers, CAD subsystems, or geometry logic.

## Scope
- `desktop-runtime/presence/DesignPresenceRuntime.ts`
- `desktop-runtime/presence/PresenceSignalRouter.ts`
- `desktop-runtime/presence/IdleFeedbackLoop.ts`
- `desktop-runtime/presence/MicroStatePredictor.ts`
- `rendering-client/src/e7/ViewportPulseScheduler.ts`
- `rendering-client/src/e7/PresenceGlowOverlay.tsx`
- `orchestration-layer/runtime-kernel/kernel_presence_adapter.py`

## Behavior
- Observes interaction, flow stage, and feedback context.
- Emits read-only presence signals for hover idle, snap proximity, constraint tension, AI idle intent pulse, and viewport focus shifts.
- Schedules idle micro-feedback with `requestAnimationFrame` and no blocking operations.
- Keeps presence update lightweight and stateless in scheduler ordering.

## Boundaries
- No TwinGraph writes.
- No geometry execution calls from presence runtime.
- No rendering mutation logic.
- No new AI or analysis engines.

