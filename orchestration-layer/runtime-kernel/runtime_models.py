from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass
class RuntimeEvent:
    event_name: str
    payload: dict[str, Any]
    parent_event_id: str | None = None
    execution_id: str | None = None
    runtime_cycle_id: str | None = None
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
