from __future__ import annotations


def world_phase_order() -> list[str]:
    return [
        "human.intent.interpretation",
        "world.context.analysis",
        "design.intent.generation",
        "design.synthesis",
        "geometry.execution",
        "spatial.cognition.analysis",
        "reflection.analysis",
        "human.feedback",
    ]
