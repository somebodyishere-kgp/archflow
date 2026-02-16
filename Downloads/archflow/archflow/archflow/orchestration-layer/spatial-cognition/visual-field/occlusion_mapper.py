from __future__ import annotations


def map_occlusions(geometry_items: list[dict]) -> dict:
    occluders = [item for item in geometry_items if item.get("occludes") is True]
    return {"occlusion_count": len(occluders), "occluder_ids": [item.get("id") for item in occluders]}
