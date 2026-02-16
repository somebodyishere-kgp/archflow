import { type GhostPreviewState } from "./feedback_models";

export class GhostPreviewManager {
  private previews = new Map<string, GhostPreviewState>();
  private viewportBuckets = new Map<string, Set<string>>();

  upsertPreview(preview: GhostPreviewState): GhostPreviewState {
    const normalized = { ...preview, nodeIds: [...preview.nodeIds], persistent: false as const };
    this.previews.set(preview.previewId, normalized);
    const bucket = this.viewportBuckets.get(preview.viewportId) || new Set<string>();
    bucket.add(preview.previewId);
    this.viewportBuckets.set(preview.viewportId, bucket);
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
