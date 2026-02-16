from __future__ import annotations


def generate_section(geometry: dict, cut_height: float) -> dict:
    return {
        "view_type": "section",
        "units": "mm",
        "cut_height_mm": int(cut_height),
        "shape": geometry,
        "dimension_anchors": geometry.get("dimension_anchors", []),
        "grid_annotations": geometry.get("grid_annotations", []),
        "level_markers": geometry.get("level_markers", [{"name": "L00", "elevation_mm": 0}]),
    }
