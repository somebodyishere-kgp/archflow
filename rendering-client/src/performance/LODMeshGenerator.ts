export type LODLevel = "high" | "medium" | "low";

export function selectLOD(distanceMeters: number): LODLevel {
  if (distanceMeters < 20) return "high";
  if (distanceMeters < 60) return "medium";
  return "low";
}

export function generateLODMeshDescriptor(nodeId: string, distanceMeters: number): Record<string, unknown> {
  const lod = selectLOD(distanceMeters);
  const segmentCount = lod === "high" ? 64 : lod === "medium" ? 24 : 8;
  return { nodeId, lod, segmentCount };
}

export function generatePreviewLODDescriptor(nodeId: string, distanceMeters: number): Record<string, unknown> {
  const lod = selectLOD(distanceMeters);
  const segmentCount = lod === "high" ? 16 : lod === "medium" ? 8 : 4;
  return { nodeId, lod, segmentCount, preview: true };
}

export function batchSnapOverlayAnchors(anchorCount: number): number {
  return Math.max(1, Math.ceil(anchorCount / 32));
}

export function batchInstancedOverlays(itemCount: number, instanceBudget = 256): number {
  return Math.max(1, Math.ceil(itemCount / Math.max(1, instanceBudget)));
}

export function frameBudgetLimiter(frameMs: number, budgetMs = 16.7): number {
  if (frameMs <= budgetMs) return 1;
  return Math.max(0.25, budgetMs / frameMs);
}

export function adaptiveOverlayDensity(nodeCount: number, overlayCount: number): number {
  const pressure = nodeCount + overlayCount;
  if (pressure < 500) return 1;
  if (pressure < 2000) return 0.7;
  return 0.45;
}
