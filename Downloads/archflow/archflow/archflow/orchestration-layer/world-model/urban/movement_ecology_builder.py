from __future__ import annotations


def build_movement_ecology(public_flow_intensity: float) -> dict:
    return {"flow_bands": int(max(1, round(public_flow_intensity * 5))), "primary_edge": "north-east"}
