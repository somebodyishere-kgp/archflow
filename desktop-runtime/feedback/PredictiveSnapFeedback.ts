import { type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { type FeedbackAnchor, type SnapPrediction } from "./feedback_models";

export function predictSnapFeedback(intent: SnapIntent, anchors: FeedbackAnchor[]): SnapPrediction | null {
  let closest: FeedbackAnchor | null = null;
  let bestScore = Number.NEGATIVE_INFINITY;
  let closestDistance = Number.POSITIVE_INFINITY;
  const modeBias: Record<SnapIntent["mode"], number> = {
    axis: 1.2,
    "assembly-anchor": 1.1,
    "parametric-guide": 1.05,
    grid: 1.0,
  };
  for (const anchor of anchors) {
    const dx = intent.point.x - anchor.point.x;
    const dy = intent.point.y - anchor.point.y;
    const dz = intent.point.z - anchor.point.z;
    const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
    const falloff = Math.max(0, 1 - dist / 250);
    const axisBias = anchor.axis === "x" || anchor.axis === "y" || anchor.axis === "z" ? 1.08 : 1.0;
    const score = falloff * axisBias * modeBias[intent.mode];
    if (score > bestScore) {
      bestScore = score;
      closestDistance = dist;
      closest = anchor;
    }
  }
  if (!closest || closestDistance > 250) return null;
  const axisGuides = closest.axis ? [closest.axis] : ["x", "y", "z"];
  return {
    mode: intent.mode,
    anchorId: closest.id,
    distance: closestDistance,
    glowIntensity: Math.max(0.2, bestScore),
    priorityScore: bestScore,
    axisGuides,
    constraintHints: [`align-${axisGuides[0]}`, "distance-lock"],
  };
}
