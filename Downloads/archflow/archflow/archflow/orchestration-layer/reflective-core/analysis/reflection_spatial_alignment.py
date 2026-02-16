from __future__ import annotations


def check_spatial_alignment(design_intent: dict, spatial_insight: dict) -> dict:
    violations = []
    if spatial_insight.get("circulation_complexity", 0) > 2.5:
        violations.append("circulation_complexity_high")
    if design_intent.get("priority") == "clarity" and spatial_insight.get("visual_focus_index", 1) < 0.4:
        violations.append("visual_hierarchy_weak")
    return {"status": "misaligned" if violations else "aligned", "violations": violations}
