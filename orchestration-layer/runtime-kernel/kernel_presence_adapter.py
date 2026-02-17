from __future__ import annotations

PRESENCE_PHASE_ORDER = [
    "interaction.update",
    "workspace.update",
    "design.flow.update",
    "feedback.update",
    "presence.update",
    "geometry.execution",
]


def presence_phase_index(event_name: str) -> int:
    if event_name in PRESENCE_PHASE_ORDER:
        return PRESENCE_PHASE_ORDER.index(event_name)
    return len(PRESENCE_PHASE_ORDER)

