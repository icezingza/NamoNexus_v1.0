"""Retrieval engine to summarize memory entries."""
from __future__ import annotations

from typing import Iterable


class RetrievalEngine:
    def summarize(self, entries: Iterable[dict]) -> str:
        entries_list = list(entries)
        if not entries_list:
            return "No prior reflections recorded."
        recent = entries_list[-3:]
        reflections = [entry.get("reflection", {}).get("reflection", "") for entry in recent]
        joined = " | ".join(filter(None, reflections))
        return f"Recent reflections: {joined}" if joined else "Reflections captured without content."
