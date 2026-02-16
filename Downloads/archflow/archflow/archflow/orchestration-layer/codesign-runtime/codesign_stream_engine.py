from __future__ import annotations

from codesign_models import CoDesignState
from delta_context_builder import build_delta_context
from interaction_listener import listen_interactions


def update_codesign_state(state: CoDesignState, events: list[dict], current_context: dict) -> CoDesignState:
    relevant = listen_interactions(events)
    previous_context = state.recent_deltas[-1]["after"] if state.recent_deltas else {}
    delta = build_delta_context(previous_context, current_context)
    next_deltas = list(state.recent_deltas)
    if delta["change_count"] > 0:
        next_deltas.append({"events": relevant, "after": current_context, "delta": delta})
    return CoDesignState(
        context_id=state.context_id,
        revision=state.revision + 1,
        recent_deltas=next_deltas[-20:],
        suggestion_count=state.suggestion_count,
    )
