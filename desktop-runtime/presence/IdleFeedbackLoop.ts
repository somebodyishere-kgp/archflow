import { type IdleFeedbackSample } from "./presence_models";

type IdleLoopListener = (sample: IdleFeedbackSample) => void;

export class IdleFeedbackLoop {
  private rafId: number | null = null;
  private lastTs = 0;
  private frameId = 0;

  start(listener: IdleLoopListener): void {
    if (this.rafId !== null) return;
    const tick = (ts: number) => {
      if (this.lastTs === 0) this.lastTs = ts;
      const delta = ts - this.lastTs;
      if (delta >= 16) {
        this.lastTs = ts;
        this.frameId += 1;
        const pulse = 0.5 + 0.5 * Math.sin((ts / 1000) * Math.PI * 2);
        listener({
          frameId: this.frameId,
          pulse,
          overlayFade: Math.max(0.2, 1 - pulse * 0.4),
          timestampMs: ts,
        });
      }
      this.rafId = window.requestAnimationFrame(tick);
    };
    this.rafId = window.requestAnimationFrame(tick);
  }

  stop(): void {
    if (this.rafId !== null) {
      window.cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }
    this.lastTs = 0;
  }
}

