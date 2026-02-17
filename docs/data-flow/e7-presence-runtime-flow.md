# Data Flow: E7 Presence Runtime

Feature: Continuous Design Presence Runtime

Input:
- `interaction.update` state snapshots (`desktop-runtime/app-shell/InteractionStateMachine.ts`)
- `design.flow.update` stage context (`desktop-runtime/workspace/DesignFlowController.ts`)
- E5 feedback state (`desktop-runtime/feedback/LiveFeedbackController.ts`)

Process:
- Presence runtime composes frame state from interaction + flow + feedback.
- Micro predictor computes deterministic anticipation signals from pointer velocity, snap distance, and hover history.
- Idle feedback loop emits frame-paced pulse/fade samples through `requestAnimationFrame`.
- Signal router distributes presence signals to rendering overlays.

Output:
- `presence.signal.generated`
- `presence.idle.feedback`
- Rendering-side pulse metrics via E7 overlay scheduler

Validation Layers:
- Scheduler phase order includes `presence.update` after `feedback.update`.
- CI guards reject geometry execution calls or TwinGraph mutation paths from presence modules.
- Presence loop constrained to frame-safe cadence and read-only behavior.

