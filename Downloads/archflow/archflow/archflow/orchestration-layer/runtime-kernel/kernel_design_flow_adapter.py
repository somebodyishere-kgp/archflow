from __future__ import annotations

DESIGN_FLOW_PHASE_ORDER = [
    "interaction.update",
    "workspace.update",
    "design.flow.update",
    "building.systems.analysis",
    "spatial.cognition.analysis",
    "project.consciousness.update",
    "reflection.analysis",
]


def design_flow_phase_index(event_name: str) -> int:
    if event_name in DESIGN_FLOW_PHASE_ORDER:
        return DESIGN_FLOW_PHASE_ORDER.index(event_name)
    return len(DESIGN_FLOW_PHASE_ORDER)
