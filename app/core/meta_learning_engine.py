"""Adaptive meta learning engine for NaMoNexus."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MetaLearningEngine:
    learning_rate: float = 0.1
    adaptive_factor: float = 1.0
    min_factor: float = 0.2
    max_factor: float = 2.0
    history: list[float] = field(default_factory=list)

    def adjust(self, feedback: float) -> float:
        """Adjust the adaptive factor based on feedback in a bounded manner."""
        delta = self.learning_rate * feedback
        self.adaptive_factor = max(self.min_factor, min(self.max_factor, self.adaptive_factor + delta))
        self.history.append(self.adaptive_factor)
        return self.adaptive_factor

    def reset(self) -> None:
        """Reset internal state to defaults."""
        self.adaptive_factor = 1.0
        self.history.clear()
