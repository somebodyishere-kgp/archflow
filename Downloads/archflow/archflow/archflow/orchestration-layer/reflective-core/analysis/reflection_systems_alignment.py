from __future__ import annotations


def check_systems_alignment(design_intent: dict, systems_analysis: dict) -> dict:
    issues = []
    if systems_analysis.get("support_risk") == "high":
        issues.append("structural_support_risk")
    if design_intent.get("thermal_goal") == "passive-cooling" and systems_analysis.get("daylight_distribution_index", 0) < 0.4:
        issues.append("passive_daylight_gap")
    return {"status": "misaligned" if issues else "aligned", "issues": issues}
