"""Retrieval engine to summarize memory entries."""
from __future__ import annotations

from typing import Iterable, Any


class RetrievalEngine:
    def summarize(self, entries: Iterable[dict]) -> str:
        entries_list = list(entries)
        if not entries_list:
            return "No prior reflections recorded."

        recent = entries_list[-3:]
        reflections = [self._extract_reflection(entry) for entry in recent]
        cleaned = [text for text in reflections if text]

        if not cleaned:
            return "Reflections captured without content."

        joined = " | ".join(cleaned)
        return f"Recent reflections: {joined}"

    def _extract_reflection(self, entry: Any) -> str:
        if isinstance(entry, str):
            return entry

        if isinstance(entry, dict):
            if "reflection" in entry:
                nested = self._extract_reflection(entry.get("reflection"))
                if nested:
                    return nested
            summary = entry.get("summary")
            if isinstance(summary, str):
                return summary
            input_text = entry.get("input")
            if isinstance(input_text, str):
                return input_text

        return ""
