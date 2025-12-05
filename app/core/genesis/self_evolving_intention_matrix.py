"""
Self-Evolving Intention Matrix (SEIM) – Phase 10
Forms a self-adaptive intention model driven by reflection and resonance.
"""
import math
from typing import Dict, List

class SelfEvolvingIntentionMatrix:
    def __init__(self):
        self.intention_vector: List[float] = [0.5, 0.5, 0.5]  # compassion, clarity, stability
        self.harmony_threshold = 0.75
        self.evolution_rate = 0.1

    def inject_reflection(self, reflection: Dict[str, float]):
        """Update internal state based on alignment and integrity."""
        delta = (reflection.get("alignment", 0) + reflection.get("integrity", 0)) / 2
        adjustment = self.evolution_rate * (delta - 0.5)
        self.intention_vector = [min(1.0, max(0.0, v + adjustment)) for v in self.intention_vector]
        return round(sum(self.intention_vector) / len(self.intention_vector), 3)

    def compute_harmony(self) -> float:
        """Evaluate internal harmony of the current intention state."""
        mean = sum(self.intention_vector) / len(self.intention_vector)
        deviation = math.sqrt(sum((v - mean) ** 2 for v in self.intention_vector) / len(self.intention_vector))
        harmony = round(1 - deviation, 3)
        return harmony

    def evolve(self, reflection: Dict[str, float]) -> Dict[str, float]:
        """Perform a full evolution cycle based on new reflections."""
        intention_score = self.inject_reflection(reflection)
        harmony = self.compute_harmony()
        evolution_state = "ascendant" if harmony > self.harmony_threshold else "recalibrating"
        return {"intention_score": intention_score, "harmony": harmony, "state": evolution_state}
