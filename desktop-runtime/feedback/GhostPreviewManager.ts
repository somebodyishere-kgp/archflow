import { type GhostPreviewState } from "./feedback_models";
import { type PresenceSignalRouter } from "../presence/PresenceSignalRouter";

export class GhostPreviewManager {
  private previews = new Map<string, GhostPreviewState>();
  private viewportBuckets = new Map<string, Set<string>>();
  private presenceRouter?: PresenceSignalRouter;

  attachPresenceRouter(router: PresenceSignalRouter): void {
    this.presenceRouter = router;
  }

  upsertPreview(preview: GhostPreviewState): GhostPreviewState {
    const normalized = { ...preview, nodeIds: [...preview.nodeIds], persistent: false as const };
    this.previews.set(preview.previewId, normalized);
    const bucket = this.viewportBuckets.get(preview.viewportId) || new Set<string>();
    bucket.add(preview.previewId);
    this.viewportBuckets.set(preview.viewportId, bucket);
    if (this.presenceRouter) {
      this.presenceRouter.emit({
        signalType: "ai.intent.idle",
        source: "feedback",
        workspaceId: "local-workspace",
        viewportId: preview.viewportId,
        intensity: 0.35,
        timestampMs: Date.now(),
        metadata: { previewId: preview.previewId, source: preview.source },
      });
    }
    return normalized;
  }

  removePreview(previewId: string): void {
    const preview = this.previews.get(previewId);
    this.previews.delete(previewId);
    if (preview) {
      const bucket = this.viewportBuckets.get(preview.viewportId);
      if (bucket) {
        bucket.delete(previewId);
      }
    }
  }

  listPreviews(): GhostPreviewState[] {
    return Array.from(this.previews.values()).map((p) => ({ ...p, nodeIds: [...p.nodeIds], persistent: false }));
  }

  invalidateViewport(viewportId: string): number {
    const bucket = this.viewportBuckets.get(viewportId);
    if (!bucket) return 0;
    const ids = Array.from(bucket.values());
    ids.forEach((id) => this.removePreview(id));
    this.viewportBuckets.delete(viewportId);
    return ids.length;
  }
}
