import { type PresenceFrameState } from "./presence_models";

export type AnticipationSignal = {
  type: "snap.prehighlight" | "focus.soft-shift" | "idle.overlay.fade";
  score: number;
  targetId?: string;
};

type PointerSample = { x: number; y: number; t: number };

export class MicroStatePredictor {
  private pointerHistory: PointerSample[] = [];
  private hoverHistory: string[] = [];
  private readonly maxSamples = 8;

  pushPointerSample(x: number, y: number, timestampMs: number): number {
    this.pointerHistory.push({ x, y, t: timestampMs });
    if (this.pointerHistory.length > this.maxSamples) this.pointerHistory.shift();
    if (this.pointerHistory.length < 2) return 0;
    const a = this.pointerHistory[this.pointerHistory.length - 2];
    const b = this.pointerHistory[this.pointerHistory.length - 1];
    const dt = Math.max(1, b.t - a.t);
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    return Math.sqrt(dx * dx + dy * dy) / dt;
  }

  pushHover(hoverId?: string): void {
    if (!hoverId) return;
    this.hoverHistory.push(hoverId);
    if (this.hoverHistory.length > this.maxSamples) this.hoverHistory.shift();
  }

  predict(state: PresenceFrameState): AnticipationSignal[] {
    const signals: AnticipationSignal[] = [];
    const recentHover = this.hoverHistory[this.hoverHistory.length - 1];
    const slowPointer = state.pointerVelocity < 0.35;

    if (slowPointer && typeof state.snapDistance === "number" && state.snapDistance < 140) {
      signals.push({
        type: "snap.prehighlight",
        score: Math.max(0.2, 1 - state.snapDistance / 140),
        targetId: state.hoverId || recentHover,
      });
    }

    if (state.stage === "spatial" || state.focusMode === "spatial-mode") {
      signals.push({
        type: "focus.soft-shift",
        score: 0.5,
        targetId: state.hoverId || recentHover,
      });
    }

    if (!state.hoverId && state.constraintHints.length === 0) {
      signals.push({
        type: "idle.overlay.fade",
        score: 0.4,
      });
    }

    return signals;
  }
}

