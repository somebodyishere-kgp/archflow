from __future__ import annotations


def listen_interactions(events: list[dict]) -> list[dict]:
    return [event for event in events if event.get("source") in {"desktop", "human-interface"}]
