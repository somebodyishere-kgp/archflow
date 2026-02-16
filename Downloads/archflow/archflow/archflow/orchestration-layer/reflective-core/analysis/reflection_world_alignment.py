from __future__ import annotations


def check_world_alignment(design_strategy: dict, world_insight: dict) -> dict:
    issues = []
    if world_insight.get("solar_priority_index", 0) > 0.7 and design_strategy.get("orientation") == "west-heavy":
        issues.append("solar_misalignment")
    if world_insight.get("public_flow_intensity", 0) > 0.6 and design_strategy.get("entry_edge") != "north-east":
        issues.append("entry_flow_misalignment")
    return {"status": "misaligned" if issues else "aligned", "issues": issues}
