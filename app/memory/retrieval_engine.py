"""Retrieval engine to summarize memory entries."""
from __future__ import annotations

from typing import Iterable


class RetrievalEngine:
    def summarize(self, entries: Iterable[dict]) -> str:
        entries_list = list(entries)
        if not entries_list:
            return "No prior reflections recorded."
        recent = entries_list[-3:]
        reflections: list[str] = []
        for entry in recent:
            reflection_field = entry.get("reflection", {})
            text = ""
            if isinstance(reflection_field, dict):
                inner = reflection_field.get("reflection", "")
                if isinstance(inner, dict):
                    text = inner.get("reflection", "")
                elif isinstance(inner, str):
                    text = inner
            elif isinstance(reflection_field, str):
                text = reflection_field
            if text:
                reflections.append(text)

        joined = " | ".join(reflections)
        return f"Recent reflections: {joined}" if joined else "Reflections captured without content."
