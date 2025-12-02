"""Retrieval engine to summarize memory entries."""
from __future__ import annotations

from typing import Iterable


class RetrievalEngine:
    def summarize(self, entries: Iterable[dict]) -> str:
        entries_list = list(entries)
        if not entries_list:
            return "No prior reflections recorded."
        recent = entries_list[-3:]
        reflections = [self._extract_reflection(entry) for entry in recent]
        joined = " | ".join(filter(None, reflections))
        return f"Recent reflections: {joined}" if joined else "Reflections captured without content."

    def _extract_reflection(self, entry: dict) -> str:
        if not isinstance(entry, dict):
            return ""

        reflection_field = entry.get("reflection")
        if isinstance(reflection_field, dict):
            nested = reflection_field.get("reflection")
            if isinstance(nested, dict):
                value = nested.get("reflection")
                return value if isinstance(value, str) else ""
            if isinstance(nested, str):
                return nested
        elif isinstance(reflection_field, str):
            return reflection_field

        return ""
