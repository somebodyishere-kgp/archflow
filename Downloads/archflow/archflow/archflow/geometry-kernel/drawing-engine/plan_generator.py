from __future__ import annotations


def generate_plan(geometry: dict) -> dict:
    return {
        "view_type": "plan",
        "units": "mm",
        "slices": geometry.get("profile", []),
        "dimension_anchors": geometry.get("dimension_anchors", []),
        "grid_annotations": geometry.get("grid_annotations", []),
        "level_markers": geometry.get("level_markers", [{"name": "L00", "elevation_mm": 0}]),
        "annotations": [],
    }
