from __future__ import annotations


def build_perception_snapshot(space_graph: dict) -> dict:
    return {
        "space_count": len(space_graph.get("spaces", [])),
        "visibility_links": len(space_graph.get("visibility", [])),
    }
