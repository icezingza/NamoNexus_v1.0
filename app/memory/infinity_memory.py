"""Lightweight infinity memory wrapper around the existing memory store."""
from __future__ import annotations

from typing import Any, Dict, List

from .store import MemoryStore
from .retrieval_engine import RetrievalEngine


class InfinityMemorySystem:
    """Stores interactions and returns brief contextual summaries."""

    def __init__(self, store: MemoryStore | None = None, retrieval_engine: RetrievalEngine | None = None) -> None:
        self.store = store or MemoryStore()
        self.retrieval_engine = retrieval_engine or RetrievalEngine()

    def store_memory(self, text: str, emotion: Dict[str, Any]) -> None:
        entry = {"input": text, "emotion": emotion}
        self.store.save_reflection(entry)

    def retrieve_context(self, query: str, current_emotion: Dict[str, Any]) -> List[str]:
        recall = self.store.recall()
        entries = recall.get("entries")
        summary = self.retrieval_engine.summarize(entries)
        return [summary] if summary else []
