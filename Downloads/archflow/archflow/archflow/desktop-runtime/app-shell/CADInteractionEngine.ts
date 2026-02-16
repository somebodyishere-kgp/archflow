import { LiveFeedbackController } from "../feedback/LiveFeedbackController";
import { type InteractionContext } from "./InteractionStateMachine";
import { updateSelection, type SelectionState } from "./SelectionSystem";
import { applyTransformDragPreview, type TransformState } from "./TransformGizmo";
import { type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { type FeedbackAnchor } from "../feedback/feedback_models";

export class CADInteractionEngine {
  constructor(private feedback: LiveFeedbackController) {}

  processPointerMove(
    intent: SnapIntent,
    anchors: FeedbackAnchor[],
    interaction: InteractionContext,
    transform: TransformState,
  ) {
    const feedbackState = this.feedback.evaluatePointerIntent(intent, anchors, interaction);
    const dragPreview = applyTransformDragPreview(transform, intent.point);
    return { feedbackState, dragPreview };
  }

  processSelection(state: SelectionState, id: string, mode: "replace" | "toggle" = "replace"): SelectionState {
    return updateSelection(state, id, mode);
  }
}
