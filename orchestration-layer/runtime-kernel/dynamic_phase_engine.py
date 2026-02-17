from __future__ import annotations


def build_dynamic_phases(entity_types: list[str]) -> list[str]:
    base = ["intent.proposed", "proposal.executed", "twingraph.mutation", "view.refresh", "render.sync"]
    extras = [f"phase.{entity_type}" for entity_type in sorted(set(entity_types))]
    return base + extras
