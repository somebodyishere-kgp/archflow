from __future__ import annotations


def apply_context_decay(deltas: list[dict], max_history: int = 30) -> list[dict]:
    return deltas[-max_history:]
