from __future__ import annotations


def suggest_orientation(solar_priority_index: float, public_flow_vector: str) -> dict:
    base_orientation = "north-south" if solar_priority_index > 0.7 else "east-west"
    return {"preferred_orientation": base_orientation, "entry_alignment": public_flow_vector}
