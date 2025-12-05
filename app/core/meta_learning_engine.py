"""Adaptive meta learning engine for NaMoNexus."""
from __future__ import annotations

from dataclasses import dataclass, field

from app.core.config import get_settings


@dataclass
class MetaLearningEngine:
    phi: float = field(default_factory=lambda: get_settings().PHI)
    adaptive_factor: float = 1.0
    min_factor: float = 0.2
    max_factor: float = 2.0
    history: list[float] = field(default_factory=list)

    learning_rate: float = 0.381966

    def __post_init__(self) -> None:
        # self.learning_rate is now set at class level
        pass

    def adjust(self, feedback: float) -> float:
        """Adjust the adaptive factor based on feedback in a bounded manner."""
        delta = (feedback - 0.5) * self.learning_rate
        self.adaptive_factor = max(self.min_factor, min(self.max_factor, self.adaptive_factor + delta))
        self.history.append(self.adaptive_factor)
        return self.adaptive_factor
