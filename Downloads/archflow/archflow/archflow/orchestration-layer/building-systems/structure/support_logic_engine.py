from __future__ import annotations


def detect_support_risks(spans: list[int], support_count: int) -> dict:
    long_spans = [span for span in spans if span >= 12000]
    risk = "high" if long_spans and support_count < len(long_spans) * 2 else "moderate"
    return {"support_risk": risk, "long_span_count": len(long_spans)}
