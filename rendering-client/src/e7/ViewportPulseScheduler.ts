export type PresencePulse = {
  viewportId: string;
  glow: number;
  tension: number;
  idleFade: number;
  focusShift: number;
  timestampMs: number;
};

type PulseListener = (pulse: PresencePulse) => void;

export class ViewportPulseScheduler {
  private rafId: number | null = null;
  private listeners = new Set<PulseListener>();
  private running = false;
  private lastFrameMs = 0;

  subscribe(listener: PulseListener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  start(viewportId: string): void {
    if (this.running) return;
    this.running = true;
    const tick = (timestampMs: number) => {
      if (!this.running) return;
      if (this.lastFrameMs === 0) this.lastFrameMs = timestampMs;
      const delta = timestampMs - this.lastFrameMs;
      if (delta >= 16) {
        this.lastFrameMs = timestampMs;
        const phase = (timestampMs / 1000) * Math.PI * 2;
        const pulse: PresencePulse = {
          viewportId,
          glow: 0.5 + 0.5 * Math.sin(phase),
          tension: 0.4 + 0.6 * Math.sin(phase * 0.5),
          idleFade: 0.6 + 0.4 * Math.cos(phase),
          focusShift: 0.5 + 0.5 * Math.sin(phase * 0.25),
          timestampMs,
        };
        this.listeners.forEach((listener) => listener(pulse));
      }
      this.rafId = window.requestAnimationFrame(tick);
    };
    this.rafId = window.requestAnimationFrame(tick);
  }

  stop(): void {
    this.running = false;
    if (this.rafId !== null) {
      window.cancelAnimationFrame(this.rafId);
      this.rafId = null;
    }
    this.lastFrameMs = 0;
  }
}

