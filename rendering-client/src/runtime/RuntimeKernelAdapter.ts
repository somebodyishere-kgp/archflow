import type { GeometryViewResponse } from "../types/view";
import { RuntimeSyncEngine } from "./RuntimeSyncEngine";
import { TwinGraphClient } from "../services/twingraphClient";

type KernelEvent = {
  event_id: string;
  runtime_cycle_id: string | null;
  event_name: string;
  payload: Record<string, unknown>;
};

export class RuntimeKernelAdapter {
  private timer: ReturnType<typeof setInterval> | null = null;
  private readonly syncEngine: RuntimeSyncEngine;

  constructor(
    private readonly baseUrl: string,
    client: TwinGraphClient,
    onView: (view: GeometryViewResponse) => void,
    private readonly intervalMs = 2000
  ) {
    this.syncEngine = new RuntimeSyncEngine(client, onView);
  }

  start(): void {
    if (this.timer) return;
    this.timer = setInterval(() => {
      void this.poll();
    }, this.intervalMs);
  }

  stop(): void {
    if (!this.timer) return;
    clearInterval(this.timer);
    this.timer = null;
  }

  private async poll(): Promise<void> {
    const response = await fetch(`${this.baseUrl}/events/audit`);
    if (!response.ok) return;
    const payload = (await response.json()) as { events: KernelEvent[] };
    const latest = payload.events.at(-1);
    if (!latest) return;

    if (latest.event_name === "render.sync") {
      await this.syncEngine.handleEvent({
        ...latest,
        parent_event_id: null,
        source_module: "runtime-kernel",
        timestamp: new Date().toISOString(),
      });
    }
  }
}
