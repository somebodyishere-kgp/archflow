import { type GhostPreviewState } from "./feedback_models";

export class GhostPreviewManager {
  private previews = new Map<string, GhostPreviewState>();

  upsertPreview(preview: GhostPreviewState): GhostPreviewState {
    const normalized = { ...preview, nodeIds: [...preview.nodeIds], persistent: false as const };
    this.previews.set(preview.previewId, normalized);
    return normalized;
  }

  removePreview(previewId: string): void {
    this.previews.delete(previewId);
  }

  listPreviews(): GhostPreviewState[] {
    return Array.from(this.previews.values()).map((p) => ({ ...p, nodeIds: [...p.nodeIds], persistent: false }));
  }
}
