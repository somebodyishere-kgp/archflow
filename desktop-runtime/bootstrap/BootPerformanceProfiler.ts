export type BootMetrics = {
  windowOpenMs: number;
  viewportMountMs: number;
  firstRenderFrameMs: number;
  runtimeKernelReadyMs: number;
};

export class BootPerformanceProfiler {
  private marks = new Map<string, number>();

  mark(name: string): void {
    this.marks.set(name, performance.now());
  }

  buildMetrics(): BootMetrics {
    const start = this.marks.get("boot.start") || 0;
    const windowOpen = this.marks.get("window.open") || start;
    const viewportMount = this.marks.get("viewport.mount") || windowOpen;
    const firstFrame = this.marks.get("first.frame") || viewportMount;
    const kernelReady = this.marks.get("runtime.kernel.ready") || firstFrame;
    return {
      windowOpenMs: Math.max(0, windowOpen - start),
      viewportMountMs: Math.max(0, viewportMount - start),
      firstRenderFrameMs: Math.max(0, firstFrame - start),
      runtimeKernelReadyMs: Math.max(0, kernelReady - start),
    };
  }
}

