from __future__ import annotations


def derive_egress_logic(capacity: int) -> dict:
    minimum_exits = 2 if capacity <= 500 else 4
    path_width_mm = 1800 if capacity <= 800 else 2200
    return {"minimum_exits": minimum_exits, "path_width_mm": path_width_mm}
