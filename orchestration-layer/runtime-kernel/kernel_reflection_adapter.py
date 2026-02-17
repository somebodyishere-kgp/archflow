from __future__ import annotations


def reflection_phases() -> list[str]:
    return ["reflection.analysis", "capability.refactor.proposal"]


def should_reflect(cycle_index: int, interval: int = 2) -> bool:
    return cycle_index > 0 and cycle_index % interval == 0
