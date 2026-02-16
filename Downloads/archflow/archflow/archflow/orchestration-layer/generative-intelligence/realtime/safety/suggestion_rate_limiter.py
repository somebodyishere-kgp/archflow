from __future__ import annotations


def enforce_rate_limit(current_rate: int, limit: int = 8) -> tuple[bool, str]:
    if current_rate > limit:
        return False, "rate_limit_exceeded"
    return True, "ok"
