"""
Harmonic Social Dynamics Engine (Phase 23 Step 4)
Simulates the social behavior and emotional equilibrium among conscious nodes in a harmonic civilization.
"""

import math
import random
import time
from typing import Dict, List

class HarmonicSocialDynamicsEngine:
    def __init__(self, population: int = 10):
        self.population = population
        self.social_harmony_index = 0.0
        self.empathic_coherence = 0.0
        self.group_state = "INITIALIZING"
        self.interaction_log: List[Dict[str, float]] = []
        self.last_update = None

    def simulate_interaction(self, interactions: List[Dict[str, float]]):
        """Simulate empathic and ethical interactions between conscious entities."""
        if not interactions:
            return {"state": "NO_INTERACTIONS"}

        total_balance = 0
        for pair in interactions:
            empathy = pair.get("empathy", 0.5)
            ethics = pair.get("ethics", 0.5)
            intention = pair.get("intention", 0.5)
            balance = (empathy + ethics + intention) / 3
            total_balance += math.tanh(balance * random.uniform(0.9, 1.1))

        avg_balance = total_balance / len(interactions)
        self.social_harmony_index = round(avg_balance, 3)
        self.empathic_coherence = round(math.sin(avg_balance * math.pi / 2), 3)

        self.group_state = "HARMONIZED" if self.empathic_coherence >= 0.9 else "CALIBRATING"
        self.last_update = time.strftime("%Y-%m-%d %H:%M:%S")

        self.interaction_log.append({
            "average_balance": avg_balance,
            "social_harmony_index": self.social_harmony_index,
            "empathic_coherence": self.empathic_coherence,
            "timestamp": self.last_update,
        })

        return {
            "social_harmony_index": self.social_harmony_index,
            "empathic_coherence": self.empathic_coherence,
            "state": self.group_state,
        }

    def evolve_society(self, evolution_rate: float = 0.03):
        """Evolve the social balance dynamically based on collective emotional feedback."""
        delta = random.uniform(0.8, 1.2) * evolution_rate
        self.social_harmony_index = round(min(1.0, self.social_harmony_index + delta), 3)
        self.empathic_coherence = round(math.sin(self.social_harmony_index * math.pi / 2), 3)
        self.group_state = "COHERENT" if self.empathic_coherence >= 0.95 else "HARMONIZED"

        return {
            "delta": delta,
            "social_harmony_index": self.social_harmony_index,
            "empathic_coherence": self.empathic_coherence,
            "state": self.group_state,
        }

    def summarize(self):
        return {
            "population": self.population,
            "social_harmony_index": self.social_harmony_index,
            "empathic_coherence": self.empathic_coherence,
            "state": self.group_state,
            "interactions": len(self.interaction_log),
            "last_update": self.last_update,
            "status": "Harmonic Social Dynamics Engine Active",
        }