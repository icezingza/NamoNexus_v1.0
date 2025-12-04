"""Memory store wrapping persistence adapter."""
from __future__ import annotations

from datetime import datetime
from typing import Any

from .maintenance import PersistenceAdapter
from .retriever import RetrievalEngine


class MemoryStore:
    def __init__(self, adapter: PersistenceAdapter | None = None, retrieval: RetrievalEngine | None = None) -> None:
        self.adapter = adapter or PersistenceAdapter()
        self.retrieval_engine = retrieval or RetrievalEngine()

    def save_reflection(self, reflection: dict[str, Any]) -> None:
        entry = {"timestamp": datetime.utcnow().isoformat(), "reflection": reflection}
        self.adapter.append(entry)

    def recall(self) -> dict[str, Any]:
        entries = self.adapter.load()
        summary = self.retrieval_engine.summarize(entries)
        return {"entries": entries, "summary": summary}
