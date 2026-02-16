from __future__ import annotations


def generate_view_cones(view_points: list[dict], angle_deg: int = 60) -> list[dict]:
    return [{"origin": point, "angle_deg": angle_deg, "range_mm": 25000} for point in view_points]
