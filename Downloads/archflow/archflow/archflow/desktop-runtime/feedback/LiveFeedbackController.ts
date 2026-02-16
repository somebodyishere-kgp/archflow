import { type InteractionContext } from "../app-shell/InteractionStateMachine";
import { SnapManager, type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { buildConstraintVisuals } from "./ConstraintVisualizer";
import { GhostPreviewManager } from "./GhostPreviewManager";
import { animationForInteraction } from "./InteractionMicroAnimator";
import { predictSnapFeedback } from "./PredictiveSnapFeedback";
import { type FeedbackAnchor, type GhostPreviewState } from "./feedback_models";

export class LiveFeedbackController {
  private ghostManager = new GhostPreviewManager();

  constructor(private snapManager: SnapManager) {}

  evaluatePointerIntent(
    intent: SnapIntent,
    anchors: FeedbackAnchor[],
    interaction: InteractionContext,
  ): {
    snapFeedback: ReturnType<typeof predictSnapFeedback>;
    microAnimation: ReturnType<typeof animationForInteraction>;
  } {
    const activeIntent = this.snapManager.emitSnapIntent(intent);
    const snapFeedback = activeIntent ? predictSnapFeedback(activeIntent, anchors) : null;
    return {
      snapFeedback,
      microAnimation: animationForInteraction(interaction.state),
    };
  }

  updateConstraintFeedback(constraints: Array<Record<string, unknown>>) {
    return buildConstraintVisuals(constraints);
  }

  updateGhostPreview(preview: GhostPreviewState): GhostPreviewState[] {
    this.ghostManager.upsertPreview(preview);
    return this.ghostManager.listPreviews();
  }
}
