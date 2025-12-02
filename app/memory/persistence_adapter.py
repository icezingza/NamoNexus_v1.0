"""JSON-backed persistence for memory entries."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class PersistenceAdapter:
    def __init__(self, path: str | Path = "data/memory_log.json", max_entries: int = 200) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.max_entries = max_entries
        if not self.path.exists():
            self._write([])

    def _read(self) -> list[dict[str, Any]]:
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: list[dict[str, Any]]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def append(self, entry: dict[str, Any]) -> None:
        entries = self._read()
        entries.append(entry)
        if len(entries) > self.max_entries:
            entries = entries[-self.max_entries :]
        self._write(entries)

    def load(self) -> list[dict[str, Any]]:
        return self._read()
