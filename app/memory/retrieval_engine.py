"""Retrieval engine to summarize memory entries."""
from __future__ import annotations

from typing import Iterable


class RetrievalEngine:
    def summarize(self, entries: Iterable[dict] | None) -> str:
        if entries is None:
            return "No prior reflections recorded."

        try:
            entries_list = list(entries)
        except TypeError:
            return "No prior reflections recorded."

        if not entries_list:
            return "No prior reflections recorded."

        recent = entries_list[-3:]
        reflections = [self._extract_reflection(entry) for entry in recent]
        cleaned = [reflection for reflection in reflections if reflection]
        joined = " | ".join(cleaned)
        return f"Recent reflections: {joined}" if joined else "Reflections captured without content."

    def _extract_reflection(self, entry: dict) -> str:
        if not isinstance(entry, dict):
            return ""

        reflection_field = entry.get("reflection")
        if isinstance(reflection_field, list):
            for candidate in reflection_field:
                text = self._extract_reflection(candidate) if isinstance(candidate, dict) else None
                if isinstance(candidate, str):
                    return candidate
                if text:
                    return text

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
