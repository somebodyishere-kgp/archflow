from __future__ import annotations


def rewrite_dependencies(capabilities: list[str]) -> list[str]:
    return sorted(set(capabilities))
