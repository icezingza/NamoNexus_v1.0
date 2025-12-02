"""Safety guard wrapper for runtime."""
from __future__ import annotations

from dataclasses import dataclass

BLOCK_LIST = {"self-harm", "harm others", "violence"}


@dataclass
class SafetyGuard:
    def assess(self, text: str) -> bool:
        lowered = text.lower()
        return not any(term in lowered for term in BLOCK_LIST)
