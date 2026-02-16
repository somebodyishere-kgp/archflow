export type ConstraintOverlayProfile = {
  distanceLines: boolean;
  alignmentBars: boolean;
  hierarchyHighlights: boolean;
  batchSize: number;
};

export function createConstraintOverlayProfile(stage: "layout" | "systems" | "spatial"): ConstraintOverlayProfile {
  if (stage === "layout") return { distanceLines: true, alignmentBars: true, hierarchyHighlights: false, batchSize: 64 };
  if (stage === "systems") return { distanceLines: true, alignmentBars: true, hierarchyHighlights: true, batchSize: 96 };
  return { distanceLines: true, alignmentBars: false, hierarchyHighlights: true, batchSize: 48 };
}

export function batchConstraintSegments(segmentCount: number, batchSize: number): number {
  return Math.max(1, Math.ceil(segmentCount / Math.max(1, batchSize)));
}
