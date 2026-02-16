from __future__ import annotations


class DomainContextManager:
    def __init__(self) -> None:
        self._domain_contexts: dict[str, dict] = {}

    def upsert(self, context_id: str, domain: str, metadata: dict | None = None) -> None:
        self._domain_contexts[context_id] = {
            "domain": domain,
            "metadata": metadata or {},
        }

    def get(self, context_id: str) -> dict | None:
        return self._domain_contexts.get(context_id)
