from __future__ import annotations


def inject_spatial_metrics(prompt_context: dict, spatial_metrics: dict) -> dict:
    updated = dict(prompt_context)
    updated["spatial_metrics"] = spatial_metrics
    return updated
