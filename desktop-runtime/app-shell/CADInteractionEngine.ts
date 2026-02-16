import { LiveFeedbackController } from "../feedback/LiveFeedbackController";
import {
  setConstraintDragPreview,
  setInteractionHover,
  setSnapPrediction,
  type InteractionContext,
} from "./InteractionStateMachine";
import { setHover, updateSelection, updateSnapPredictionBuffer, type SelectionState } from "./SelectionSystem";
import { applyTransformDragPreview, type TransformState } from "./TransformGizmo";
import { type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { type FeedbackAnchor } from "../feedback/feedback_models";

export class CADInteractionEngine {
  constructor(private feedback: LiveFeedbackController) {}

  processPointerMove(
    intent: SnapIntent,
    anchors: FeedbackAnchor[],
    interaction: InteractionContext,
    selection: SelectionState,
    transform: TransformState,
  ) {
    const feedbackState = this.feedback.evaluatePointerIntent(intent, anchors, interaction);
    const dragPreview = applyTransformDragPreview(transform, intent.point);
    const predictedAxes = feedbackState.snapFeedback?.axisGuides || [];
    const nextSelection = updateSnapPredictionBuffer(selection, predictedAxes);
    const withHover = setHover(nextSelection, feedbackState.snapFeedback?.anchorId);
    const nextInteraction = setConstraintDragPreview(
      setSnapPrediction(
        setInteractionHover(interaction, feedbackState.snapFeedback?.anchorId),
        feedbackState.snapFeedback ? { axis: predictedAxes[0] || "x", score: feedbackState.snapFeedback.priorityScore } : undefined,
      ),
      feedbackState.snapFeedback?.constraintHints || [],
    );
    return { feedbackState, dragPreview, selection: withHover, interaction: nextInteraction };
  }

  processSelection(state: SelectionState, id: string, mode: "replace" | "toggle" = "replace"): SelectionState {
    return updateSelection(state, id, mode);
  }
}
