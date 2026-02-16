from __future__ import annotations


def building_systems_phase_order() -> list[str]:
    return [
        "human.intent.interpretation",
        "world.context.analysis",
        "design.intent.generation",
        "design.synthesis",
        "geometry.execution",
        "building.systems.analysis",
        "spatial.cognition.analysis",
        "reflection.analysis",
        "human.feedback",
    ]
