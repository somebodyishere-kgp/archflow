from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EditHistoryManager:
    entries: list[dict[str, Any]] = field(default_factory=list)

    def record_edit(self, edit_id: str, payload: dict[str, Any], dependencies: list[str]) -> None:
        self.entries.append(
            {
                "edit_id": edit_id,
                "payload": payload,
                "dependencies": list(dependencies),
            }
        )

    def rollback_to(self, edit_id: str) -> list[dict[str, Any]]:
        if not self.entries:
            return []
        index = next((i for i, item in enumerate(self.entries) if item["edit_id"] == edit_id), None)
        if index is None:
            return list(self.entries)
        self.entries = self.entries[: index + 1]
        return list(self.entries)

    def lineage(self) -> list[str]:
        return [entry["edit_id"] for entry in self.entries]
