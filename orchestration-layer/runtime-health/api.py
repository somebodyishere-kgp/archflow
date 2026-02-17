from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI


def create_app(event_log_path: Path) -> FastAPI:
    app = FastAPI(title="Runtime Health", version="0.1.0")

    @app.get("/runtime/status")
    def runtime_status() -> dict[str, Any]:
        events: list[dict[str, Any]] = []
        if event_log_path.exists():
            with event_log_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    line = line.strip()
                    if line:
                        events.append(json.loads(line))

        last_view_revision = ""
        for event in reversed(events):
            if event.get("event_name") == "view.refresh":
                last_view_revision = event.get("event_id", "")
                break

        return {
            "transport_status": "healthy",
            "event_queue_depth": len(events),
            "last_view_revision": last_view_revision,
            "executor_state": "active",
        }

    return app
