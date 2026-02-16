from __future__ import annotations


def append_partial_intent(stream: list[dict], text_fragment: str, timestamp: str) -> list[dict]:
    next_stream = list(stream)
    next_stream.append({"fragment": text_fragment, "timestamp": timestamp})
    return next_stream[-100:]
