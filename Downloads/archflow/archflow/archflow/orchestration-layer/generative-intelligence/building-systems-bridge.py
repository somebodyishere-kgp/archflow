from __future__ import annotations


def inject_building_systems_metrics(prompt_context: dict, systems_metrics: dict) -> dict:
    next_context = dict(prompt_context)
    next_context["building_systems_metrics"] = systems_metrics
    return next_context
