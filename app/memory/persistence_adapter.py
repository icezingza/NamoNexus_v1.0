"""JSON-backed persistence for memory entries."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.core.config import get_settings


class PersistenceAdapter:
    def __init__(self, path: str | Path | None = None, max_entries: int | None = None) -> None:
        settings = get_settings()
        resolved_path = path or settings.MEMORY_PATH
        resolved_max = max_entries or settings.MAX_MEMORY_ENTRIES

        self.enabled = settings.FEATURE_FLAGS.get("ENABLE_MEMORY", True)
        self.path = Path(resolved_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.max_entries = resolved_max
        if not self.path.exists():
            self._write([])

    def _read(self) -> list[dict[str, Any]]:
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: list[dict[str, Any]]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def append(self, entry: dict[str, Any]) -> None:
        if not self.enabled:
            return
        entries = self._read()
        entries.append(entry)
        if len(entries) > self.max_entries:
            entries = entries[-self.max_entries :]
        self._write(entries)

    def load(self) -> list[dict[str, Any]]:
        if not self.enabled:
            return []
        return self._read()
