from __future__ import annotations

from typing import Any


_preview_cache: dict[str, dict[str, Any]] = {}


def build_ghost_preview(
    node_ids: list[str],
    transform: dict[str, Any],
    source: str,
    constraints: list[dict[str, Any]] | None = None,
    viewport_id: str = "main",
) -> dict[str, Any]:
    constraints = constraints or []
    cache_key = f"{viewport_id}:{source}:{','.join(node_ids)}:{transform}"

    if cache_key in _preview_cache:
        cached = dict(_preview_cache[cache_key])
        cached["cache_hit"] = True
        return cached

    ghost_meshes = [
        {
            "node_id": node_id,
            "preview_type": "ghost",
            "source": source,
            "transform": transform,
            "opacity": 0.42,
            "lod": "high" if len(node_ids) < 20 else "medium" if len(node_ids) < 80 else "low",
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
    payload = {
        "event_name": "feedback.preview.updated",
        "viewport_id": viewport_id,
        "ghost_meshes": ghost_meshes,
        "constraint_overlays": constraint_overlays,
        "persistent": False,
        "cache_hit": False,
    }
    _preview_cache[cache_key] = dict(payload)
    return payload


def invalidate_ghost_preview_cache(viewport_id: str | None = None) -> int:
    if viewport_id is None:
        count = len(_preview_cache)
        _preview_cache.clear()
        return count
    keys = [key for key in _preview_cache if key.startswith(f"{viewport_id}:")]
    for key in keys:
        _preview_cache.pop(key, None)
    return len(keys)
