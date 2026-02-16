from __future__ import annotations


def find_redundant_capabilities(usage: dict[str, int]) -> list[str]:
    return sorted([name for name, count in usage.items() if count <= 1])
