import { type InteractionState } from "../app-shell/InteractionStateMachine";
import { type InteractionMicroAnimation } from "./feedback_models";

export function animationForInteraction(interactionState: InteractionState): InteractionMicroAnimation {
  if (interactionState === "transform") {
    return {
      interactionState,
      easing: "ease-in-out",
      fadeMs: 120,
      gizmoInertia: 0.22,
      snapPulseMs: 180,
    };
  }
  if (interactionState === "constraint-adjust") {
    return {
      interactionState,
      easing: "ease-out",
      fadeMs: 100,
      gizmoInertia: 0.14,
      snapPulseMs: 140,
    };
  }
  return {
    interactionState,
    easing: "linear",
    fadeMs: 80,
    gizmoInertia: 0.1,
    snapPulseMs: 120,
  };
}
