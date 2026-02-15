from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from runtime_models import RuntimeEvent


class EventRouter:
    def __init__(self, event_log_path: Path) -> None:
        self.event_log_path = event_log_path
        self.replay_buffer: list[dict[str, Any]] = []

    def publish(self, event: RuntimeEvent) -> dict[str, Any]:
        payload = {
            "event_id": event.event_id,
            "parent_event_id": event.parent_event_id,
            "execution_id": event.execution_id,
            "runtime_cycle_id": event.runtime_cycle_id,
            "source_module": "runtime-kernel",
            "event_name": event.event_name,
            "payload": event.payload,
            "timestamp": event.timestamp,
        }
        self.replay_buffer.append(payload)
        self.event_log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.event_log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload) + "\n")
        return payload
