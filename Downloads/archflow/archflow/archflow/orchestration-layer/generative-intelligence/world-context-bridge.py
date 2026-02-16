from __future__ import annotations


def inject_world_context(prompt_context: dict, world_metrics: dict) -> dict:
    merged = dict(prompt_context)
    merged["world_context"] = world_metrics
    return merged
