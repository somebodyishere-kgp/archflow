from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from event_router import EventRouter
from runtime_models import RuntimeEvent
from scheduler import sort_cycle_events
from state_engine import StateEngine


class RuntimeKernel:
    def __init__(self, event_log_path: Path) -> None:
        self.router = EventRouter(event_log_path)
        self.state_engine = StateEngine()

    def start_cycle(self, seed_event_name: str, payload: dict) -> dict:
        cycle_id = f"cycle-{uuid4()}"
        event = RuntimeEvent(
            event_name=seed_event_name,
            payload=payload,
            runtime_cycle_id=cycle_id,
        )
        routed = self.router.publish(event)
        self.state_engine.update_from_event(routed)
        return routed

    def route_batch(self, events: list[dict]) -> list[dict]:
        ordered = sort_cycle_events(events)
        for event in ordered:
            self.state_engine.update_from_event(event)
        return ordered

    def runtime_state(self) -> dict:
        return self.state_engine.snapshot()
