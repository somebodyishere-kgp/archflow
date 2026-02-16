from __future__ import annotations


def resolve_spatial_hierarchy(zones: list[dict]) -> list[dict]:
    resolved = []
    for zone in zones:
        level = "primary" if zone.get("zone") in {"public", "stage"} else "secondary"
        resolved.append({**zone, "hierarchy_level": level})
    return resolved
