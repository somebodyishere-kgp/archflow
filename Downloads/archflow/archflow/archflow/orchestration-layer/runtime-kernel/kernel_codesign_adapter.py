from __future__ import annotations


def codesign_phase_order() -> list[str]:
    return [
        "human.intent.interpretation",
        "design.intent.generation",
        "design.synthesis",
        "pipeline.execution",
        "reflection.analysis",
        "codesign.observe",
        "codesign.suggest",
        "human.feedback",
    ]
