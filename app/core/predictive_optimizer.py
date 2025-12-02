"""Predictive optimizer using simple numeric modeling."""
from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from typing import Iterable


@dataclass
class PredictiveOptimizer:
    window: int = 5
    history: list[float] = field(default_factory=list)

    def predict(self, signal: float) -> float:
        """Predict next state based on recent signal history."""
        self.history.append(signal)
        if len(self.history) > self.window:
            self.history.pop(0)
        return self._smoothed_average(self.history)

    def _smoothed_average(self, signals: Iterable[float]) -> float:
        values = list(signals)
        if not values:
            return 0.0
        baseline = mean(values)
        return round(baseline, 4)

    def reset(self) -> None:
        """Reset internal history."""
        self.history.clear()
