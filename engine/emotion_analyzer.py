"""Lightweight emotion analyzer for runtime governor."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RuntimeEmotionAnalyzer:
    def score(self, text: str) -> float:
        tokens = [t.strip('.,!?').lower() for t in text.split()]
        positive = sum(1 for t in tokens if t in {"calm", "peace", "care", "kind"})
        negative = sum(1 for t in tokens if t in {"anger", "fear", "worry"})
        total = positive + negative or 1
        return round((positive - negative) / total * 0.5 + 0.5, 3)
