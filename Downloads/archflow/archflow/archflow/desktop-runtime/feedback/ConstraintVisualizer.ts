import { type ConstraintVisualState } from "./feedback_models";

export function buildConstraintVisuals(constraints: Array<Record<string, unknown>>): ConstraintVisualState {
  const distanceLines: ConstraintVisualState["distanceLines"] = [];
  const alignmentBars: ConstraintVisualState["alignmentBars"] = [];
  const hierarchyHighlights: ConstraintVisualState["hierarchyHighlights"] = [];

  for (const c of constraints) {
    const kind = String(c.kind || "");
    if (kind === "distance") {
      distanceLines.push({
        from: String(c.from || ""),
        to: String(c.to || ""),
        valueMm: Number(c.value_mm || 0),
      });
    } else if (kind === "align") {
      alignmentBars.push({
        axis: (c.axis as "x" | "y" | "z") || "x",
        ids: [String(c.from || ""), String(c.to || "")].filter(Boolean),
      });
    } else if (kind === "hierarchy") {
      hierarchyHighlights.push({
        parentId: String(c.parent || ""),
        childIds: Array.isArray(c.children) ? c.children.map((id) => String(id)) : [],
      });
    }
  }

  return { distanceLines, alignmentBars, hierarchyHighlights };
}
