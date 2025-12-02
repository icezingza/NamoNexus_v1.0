"""Runtime governor aggregating core metrics."""
from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from typing import Any


@dataclass
class RuntimeGovernor:
    energy_state: float = 1.0
    history: list[dict[str, float]] = field(default_factory=list)

    def composite_score(self, metrics: dict[str, float]) -> float:
        weights = {"clarity": 0.3, "coherence": 0.3, "stability": 0.2, "growth_index": 0.2}
        score = 0.0
        for key, weight in weights.items():
            score += weight * metrics.get(key, 0.0)
        self.energy_state = max(0.0, min(1.0, self.energy_state * 0.99 + score * 0.01))
        self.history.append({"score": score, "energy_state": self.energy_state})
        return round(score, 3)

    def snapshot(self) -> dict[str, Any]:
        return {"energy_state": self.energy_state, "history": self.history[-5:]}

    def reset(self) -> None:
        """Reset internal state."""
        self.energy_state = 1.0
        self.history.clear()
