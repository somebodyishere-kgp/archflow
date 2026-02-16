from __future__ import annotations

PHASE_ORDER = [
    "intent.proposed",
    "proposal.executed",
    "twingraph.mutation",
    "geometry.updated",
    "view.refresh",
    "render.sync",
    "reflection.analysis",
    "capability.refactor.proposal",
]


def event_phase_index(event_name: str) -> int:
    if event_name in PHASE_ORDER:
        return PHASE_ORDER.index(event_name)
    return len(PHASE_ORDER)


def sort_cycle_events(events: list[dict]) -> list[dict]:
    return sorted(events, key=lambda event: (event_phase_index(event.get("event_name", "")), event.get("timestamp", "")))
