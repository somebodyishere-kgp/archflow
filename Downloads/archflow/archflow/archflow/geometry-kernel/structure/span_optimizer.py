from __future__ import annotations


def optimize_span(capacity: int, acoustic_priority: str) -> int:
    base_span = 8000 if capacity < 500 else 10000
    if acoustic_priority == "high":
        base_span += 1000
    return base_span
