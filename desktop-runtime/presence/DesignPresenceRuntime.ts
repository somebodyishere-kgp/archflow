import { type InteractionContext } from "../app-shell/InteractionStateMachine";
import { type SnapPrediction } from "../feedback/feedback_models";
import { type DesignFlowStage, type AIFocusMode } from "../workspace/workspace_models";
import { IdleFeedbackLoop } from "./IdleFeedbackLoop";
import { MicroStatePredictor } from "./MicroStatePredictor";
import { PresenceSignalRouter } from "./PresenceSignalRouter";
import { type PresenceFrameState } from "./presence_models";

type PointerPoint = { x: number; y: number; t: number };

export class DesignPresenceRuntime {
  private predictor = new MicroStatePredictor();
  private idleLoop = new IdleFeedbackLoop();
  private active = false;
  private lastPointer?: PointerPoint;

  constructor(
    private router: PresenceSignalRouter,
    private workspaceId: string,
    private viewportId: string,
  ) {}

  start(): void {
    if (this.active) return;
    this.active = true;
    this.idleLoop.start((sample) => {
      this.router.emit({
        signalType: "ai.intent.idle",
        source: "workspace",
        workspaceId: this.workspaceId,
        viewportId: this.viewportId,
        intensity: sample.pulse,
        timestampMs: sample.timestampMs,
        metadata: { overlayFade: sample.overlayFade, frameId: sample.frameId },
      });
    });
  }

  stop(): void {
    this.active = false;
    this.idleLoop.stop();
  }

  updateInteraction(
    interaction: InteractionContext,
    flowStage: DesignFlowStage,
    focusMode: AIFocusMode,
    snap?: SnapPrediction | null,
  ): void {
    const pointerVelocity = this.lastPointer ? this.predictor.pushPointerSample(this.lastPointer.x, this.lastPointer.y, this.lastPointer.t) : 0;
    this.predictor.pushHover(interaction.hoverId);
    const frameState: PresenceFrameState = {
      hoverId: interaction.hoverId,
      snapDistance: snap?.distance,
      constraintHints: interaction.constraintDragPreview || [],
      stage: flowStage,
      focusMode,
      pointerVelocity,
    };
    const anticipation = this.predictor.predict(frameState);
    anticipation.forEach((signal) => {
      if (signal.type === "snap.prehighlight") {
        this.router.emit({
          signalType: "snap.proximity",
          source: "interaction",
          workspaceId: this.workspaceId,
          viewportId: this.viewportId,
          intensity: signal.score,
          timestampMs: Date.now(),
          metadata: { targetId: signal.targetId || "", predicted: true },
        });
      } else if (signal.type === "focus.soft-shift") {
        this.router.emit({
          signalType: "viewport.focus.shift",
          source: "design-flow",
          workspaceId: this.workspaceId,
          viewportId: this.viewportId,
          intensity: signal.score,
          timestampMs: Date.now(),
          metadata: { stage: flowStage, mode: focusMode },
        });
      } else {
        this.router.emit({
          signalType: "hover.idle",
          source: "feedback",
          workspaceId: this.workspaceId,
          viewportId: this.viewportId,
          intensity: signal.score,
          timestampMs: Date.now(),
        });
      }
    });
    if ((interaction.constraintDragPreview || []).length > 0) {
      this.router.emit({
        signalType: "constraint.tension",
        source: "feedback",
        workspaceId: this.workspaceId,
        viewportId: this.viewportId,
        intensity: Math.min(1, (interaction.constraintDragPreview || []).length / 4),
        timestampMs: Date.now(),
        metadata: { hintCount: (interaction.constraintDragPreview || []).length },
      });
    }
  }

  updatePointer(x: number, y: number, timestampMs: number): void {
    this.lastPointer = { x, y, t: timestampMs };
  }
}

