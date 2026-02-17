import { type InteractionContext } from "../app-shell/InteractionStateMachine";
import { SnapManager, type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { buildConstraintVisuals } from "./ConstraintVisualizer";
import { GhostPreviewManager } from "./GhostPreviewManager";
import { animationForInteraction } from "./InteractionMicroAnimator";
import { predictSnapFeedback } from "./PredictiveSnapFeedback";
import { type FeedbackAnchor, type GhostPreviewState } from "./feedback_models";
import { type PresenceSignalRouter } from "../presence/PresenceSignalRouter";

export class LiveFeedbackController {
  private ghostManager = new GhostPreviewManager();
  private presenceRouter?: PresenceSignalRouter;

  constructor(private snapManager: SnapManager) {}

  attachPresenceRouter(router: PresenceSignalRouter): void {
    this.presenceRouter = router;
    this.ghostManager.attachPresenceRouter(router);
  }

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
    if (snapFeedback && this.presenceRouter) {
      this.presenceRouter.emit({
        signalType: "snap.proximity",
        source: "feedback",
        workspaceId: "local-workspace",
        viewportId: "main-viewport",
        intensity: Math.max(0.1, snapFeedback.glowIntensity),
        timestampMs: Date.now(),
        metadata: { anchorId: snapFeedback.anchorId, mode: snapFeedback.mode, distance: snapFeedback.distance },
      });
    }
    return {
      snapFeedback,
      microAnimation: animationForInteraction(interaction.state),
    };
  }

  updateConstraintFeedback(constraints: Array<Record<string, unknown>>) {
    const visuals = buildConstraintVisuals(constraints);
    if (this.presenceRouter && constraints.length > 0) {
      this.presenceRouter.emit({
        signalType: "constraint.tension",
        source: "feedback",
        workspaceId: "local-workspace",
        viewportId: "main-viewport",
        intensity: Math.min(1, constraints.length / 5),
        timestampMs: Date.now(),
        metadata: { constraintCount: constraints.length },
      });
    }
    return visuals;
  }

  updateGhostPreview(preview: GhostPreviewState): GhostPreviewState[] {
    this.ghostManager.upsertPreview(preview);
    return this.ghostManager.listPreviews();
  }

  invalidateGhostPreviewViewport(viewportId: string): number {
    return this.ghostManager.invalidateViewport(viewportId);
  }
}
