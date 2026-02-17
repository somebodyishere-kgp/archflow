from __future__ import annotations

from typing import Any

import httpx


class LocalTransportAdapter:
    """Reads intent events and emits execution events through local HTTP transport endpoints."""

    def __init__(
        self,
        intent_gateway_base_url: str,
        event_sink_path: str = "/intent/events/audit",
    ) -> None:
        self.intent_gateway_base_url = intent_gateway_base_url.rstrip("/")
        self.event_sink_path = event_sink_path
        self._last_seen = 0

    def poll_intent_events(self) -> list[dict[str, Any]]:
        with httpx.Client(timeout=5.0) as client:
            response = client.get(f"{self.intent_gateway_base_url}{self.event_sink_path}")
            response.raise_for_status()
            payload = response.json()

        events = payload.get("events", [])
        fresh = events[self._last_seen :]
        self._last_seen = len(events)
        return [event for event in fresh if event.get("event_name") == "intent.proposed"]
