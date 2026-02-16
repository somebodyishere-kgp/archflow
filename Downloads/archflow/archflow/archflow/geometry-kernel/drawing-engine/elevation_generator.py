from __future__ import annotations


def generate_elevation(geometry: dict, axis: str = "north") -> dict:
    return {
        "view_type": "elevation",
        "units": "mm",
        "axis": axis,
        "outline": geometry,
        "dimension_anchors": geometry.get("dimension_anchors", []),
        "grid_annotations": geometry.get("grid_annotations", []),
        "level_markers": geometry.get("level_markers", [{"name": "L00", "elevation_mm": 0}]),
    }
