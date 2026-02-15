from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from .db import PostGISAdapter
from .transport.base import EventTransport
from .validation import load_schema, validate_node


@dataclass
class TwinGraphIngestService:
    schema_path: Path
    adapter: PostGISAdapter
    transport: EventTransport
    author: str = "core-twingraph"

    def ensure_ready(self) -> None:
        self.adapter.ensure_schema()

    def ingest_node(
        self,
        node: dict[str, Any],
        proposal_id: str | None = None,
        execution_id: str | None = None,
        intent_source: str | None = None,
        parent_event_id: str | None = None,
    ) -> None:
        schema = load_schema(self.schema_path)
        validate_node(node, schema)

        previous = self.adapter.upsert_node(node)
        mutation_type = "create" if previous is None else "update"
        now = datetime.now(UTC).isoformat()

        self.transport.emit(
            "twingraph.mutation",
            {
                "mutation_id": str(uuid4()),
                "node_id": node["id"],
                "operation": mutation_type,
                "proposal_id": proposal_id,
                "execution_id": execution_id,
                "intent_source": intent_source,
                "timestamp": now,
            },
            parent_event_id=parent_event_id,
        )

        previous_wkb = None if previous is None else previous["geometry_wkb"]
        new_wkb = node["geometry"]["wkb"]
        if previous_wkb != new_wkb:
            self.transport.emit(
                "geometry.updated",
                {
                    "node_id": node["id"],
                    "proposal_id": proposal_id,
                    "execution_id": execution_id,
                    "intent_source": intent_source,
                    "diff": {
                        "before": previous_wkb,
                        "after": new_wkb,
                    },
                    "author": self.author,
                    "timestamp": now,
                },
                parent_event_id=parent_event_id,
            )
