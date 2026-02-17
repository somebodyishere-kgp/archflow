import type { GeometryViewResponse } from "../types/view";
import { TwinGraphClient } from "../services/twingraphClient";

type RuntimeEvent = {
  event_name: string;
  event_id: string;
  parent_event_id: string | null;
  source_module: string;
  timestamp: string;
  payload: Record<string, unknown>;
};

export class RuntimeSyncEngine {
  private viewRevisionId = "";
  private lastEventId = "";

  constructor(
    private readonly client: TwinGraphClient,
    private readonly onView: (view: GeometryViewResponse) => void
  ) {}

  get revisionId(): string {
    return this.viewRevisionId;
  }

  async handleEvent(event: RuntimeEvent): Promise<void> {
    if (event.event_id === this.lastEventId) return;
    this.lastEventId = event.event_id;

    if (
      event.event_name === "proposal.executed" ||
      event.event_name === "geometry.updated" ||
      event.event_name === "view.refresh"
    ) {
      const nextRevision = `${event.event_name}:${event.event_id}`;
      if (this.viewRevisionId === nextRevision) return;
      this.viewRevisionId = nextRevision;
      const view = await this.client.fetchGeometryView();
      this.onView(view);
    }
  }
}
