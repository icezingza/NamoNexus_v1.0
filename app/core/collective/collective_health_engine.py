"""
Collective Health Engine (CHE)
Monitors the health and stability of the collective consciousness.
"""
import statistics
from typing import List

class CollectiveHealthEngine:
    def __init__(self):
        self.health_scores: List[float] = []

    def register_agent_health(self, score: float):
        """Add agent's health score to global record."""
        self.health_scores.append(score)

    def get_overall_health(self) -> float:
        if not self.health_scores:
            return 0.0
        return round(statistics.mean(self.health_scores), 3)

    def assess(self) -> str:
        avg = self.get_overall_health()
        if avg < 0.4:
            return "⚠️ Collective instability detected."
        elif avg < 0.8:
            return "💠 Collective moderately stable."
        else:
            return "🌈 Collective stability optimal."
