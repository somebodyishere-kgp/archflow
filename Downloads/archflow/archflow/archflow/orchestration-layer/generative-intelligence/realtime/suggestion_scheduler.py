from __future__ import annotations


def schedule_suggestion_ticks(revision: int) -> dict:
    return {"tick": revision, "suggestion_window_ms": 1500, "mode": "deterministic-paced"}
