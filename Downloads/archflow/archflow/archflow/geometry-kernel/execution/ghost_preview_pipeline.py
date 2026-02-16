from __future__ import annotations

from typing import Any


def build_ghost_preview(
    node_ids: list[str],
    transform: dict[str, Any],
    source: str,
    constraints: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    constraints = constraints or []
    ghost_meshes = [
        {
            "node_id": node_id,
            "preview_type": "ghost",
            "source": source,
            "transform": transform,
            "opacity": 0.42,
        }
        for node_id in node_ids
    ]
    constraint_overlays = [
        {
            "constraint_id": str(item.get("id", f"constraint-{index}")),
            "kind": str(item.get("kind", "generic")),
        }
        for index, item in enumerate(constraints)
    ]
    return {
        "event_name": "feedback.preview.updated",
        "ghost_meshes": ghost_meshes,
        "constraint_overlays": constraint_overlays,
        "persistent": False,
    }
