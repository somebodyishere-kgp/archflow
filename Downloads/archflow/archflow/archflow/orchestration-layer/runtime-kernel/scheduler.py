from __future__ import annotations

PHASE_ORDER = [
    "human.intent.interpretation",
    "world.context.analysis",
    "design.intent.generation",
    "design.synthesis",
    "geometry.execution",
    "interaction.update",
    "workspace.update",
    "design.flow.update",
    "building.systems.analysis",
    "spatial.cognition.analysis",
    "project.consciousness.update",
    "reflection.analysis",
    "human.feedback",
]


def event_phase_index(event_name: str) -> int:
    if event_name in PHASE_ORDER:
        return PHASE_ORDER.index(event_name)
    return len(PHASE_ORDER)
