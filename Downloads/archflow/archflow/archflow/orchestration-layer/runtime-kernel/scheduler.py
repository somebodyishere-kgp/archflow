from __future__ import annotations

PHASE_ORDER = [
    "human.intent.interpretation",
    "design.intent.generation",
    "design.synthesis",
    "geometry.execution",
    "pipeline.execution",
    "spatial.cognition.analysis",
    "reflection.analysis",
    "codesign.observe",
    "codesign.suggest",
    "human.feedback",
]


def event_phase_index(event_name: str) -> int:
    if event_name in PHASE_ORDER:
        return PHASE_ORDER.index(event_name)
    return len(PHASE_ORDER)
