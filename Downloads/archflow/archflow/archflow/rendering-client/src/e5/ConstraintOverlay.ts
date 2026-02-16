export type ConstraintOverlayProfile = {
  distanceLines: boolean;
  alignmentBars: boolean;
  hierarchyHighlights: boolean;
};

export function createConstraintOverlayProfile(stage: "layout" | "systems" | "spatial"): ConstraintOverlayProfile {
  if (stage === "layout") return { distanceLines: true, alignmentBars: true, hierarchyHighlights: false };
  if (stage === "systems") return { distanceLines: true, alignmentBars: true, hierarchyHighlights: true };
  return { distanceLines: true, alignmentBars: false, hierarchyHighlights: true };
}
