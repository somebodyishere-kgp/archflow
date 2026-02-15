from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RuntimeState:
    runtime_cycle_id: str = ""
    last_execution_id: str = ""
    last_view_revision: str = ""
    active_modules: list[str] = field(default_factory=lambda: ["intent-gateway", "proposal-executor", "core-twingraph", "rendering-client"])
    event_queue_depth: int = 0


class StateEngine:
    def __init__(self) -> None:
        self.state = RuntimeState()

    def update_from_event(self, event: dict) -> None:
        self.state.runtime_cycle_id = event.get("runtime_cycle_id") or self.state.runtime_cycle_id
        self.state.last_execution_id = event.get("execution_id") or self.state.last_execution_id
        if event.get("event_name") == "view.refresh":
            self.state.last_view_revision = event.get("event_id", "")
        self.state.event_queue_depth += 1

    def snapshot(self) -> dict:
        return {
            "runtime_cycle_id": self.state.runtime_cycle_id,
            "last_execution_id": self.state.last_execution_id,
            "last_view_revision": self.state.last_view_revision,
            "active_modules": self.state.active_modules,
            "event_queue_depth": self.state.event_queue_depth,
        }
