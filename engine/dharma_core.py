"""Lightweight dharma reasoning core."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DharmaCore:
    def reason(self, prompt: str) -> str:
        prompt_clean = prompt.strip() or "silence"
        return f"Respond to '{prompt_clean}' with balance and compassion."
