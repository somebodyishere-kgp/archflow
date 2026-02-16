import { type SnapIntent } from "../../rendering-client/src/interactions/SnapManager";
import { type FeedbackAnchor, type SnapPrediction } from "./feedback_models";

export function predictSnapFeedback(intent: SnapIntent, anchors: FeedbackAnchor[]): SnapPrediction | null {
  let closest: FeedbackAnchor | null = null;
  let closestDistance = Number.POSITIVE_INFINITY;
  for (const anchor of anchors) {
    const dx = intent.point.x - anchor.point.x;
    const dy = intent.point.y - anchor.point.y;
    const dz = intent.point.z - anchor.point.z;
    const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
    if (dist < closestDistance) {
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
    glowIntensity: Math.max(0.2, 1 - closestDistance / 250),
    axisGuides,
    constraintHints: [`align-${axisGuides[0]}`, "distance-lock"],
  };
}
