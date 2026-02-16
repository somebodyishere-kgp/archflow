from __future__ import annotations


def classify_span(span_mm: int) -> str:
    if span_mm >= 12000:
        return "long-span"
    if span_mm >= 8000:
        return "medium-span"
    return "short-span"
