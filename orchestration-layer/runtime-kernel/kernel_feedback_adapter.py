from __future__ import annotations

FEEDBACK_PHASE_ORDER = [
    "interaction.update",
    "workspace.update",
    "design.flow.update",
    "feedback.update",
    "geometry.execution",
]


def feedback_phase_index(event_name: str) -> int:
    if event_name in FEEDBACK_PHASE_ORDER:
        return FEEDBACK_PHASE_ORDER.index(event_name)
    return len(FEEDBACK_PHASE_ORDER)
