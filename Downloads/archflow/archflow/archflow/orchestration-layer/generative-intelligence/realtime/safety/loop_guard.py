from __future__ import annotations


def detect_loop_risk(revision: int, max_revision: int = 500) -> bool:
    return revision > max_revision
