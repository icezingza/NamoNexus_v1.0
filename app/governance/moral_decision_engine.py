"""
Moral Decision Engine (Phase 22 Step 2)
Evaluates and executes decisions based on ethical, compassionate, and situational reasoning.
"""

import math
import random
import time
from typing import Dict, List

class MoralDecisionEngine:
    def __init__(self):
        self.decision_history: List[Dict[str, float]] = []
        self.moral_clarity_index = 0.0
        self.compassion_weight = 0.0
        self.last_decision = None
        self.engine_state = "INITIALIZING"

    def evaluate_scenario(self, compassion_factor: float, fairness_factor: float, consequence_factor: float):
        """Analyze a moral scenario and determine best ethical path."""
        weighted_score = (
            (compassion_factor * 0.4)
            + (fairness_factor * 0.35)
            + (consequence_factor * 0.25)
        )
        fluctuation = random.uniform(0.9, 1.1)
        clarity = round(min(1.0, weighted_score * fluctuation), 3)
        compassion_weight = round(math.sin(clarity * math.pi / 2), 3)

        self.moral_clarity_index = clarity
        self.compassion_weight = compassion_weight
        self.engine_state = "RESOLVED" if clarity >= 0.9 else "EVALUATING"
        self.last_decision = time.strftime("%Y-%m-%d %H:%M:%S")

        self.decision_history.append({
            "compassion_factor": compassion_factor,
            "fairness_factor": fairness_factor,
            "consequence_factor": consequence_factor,
            "moral_clarity_index": clarity,
            "compassion_weight": compassion_weight,
            "timestamp": self.last_decision,
        })

        return {
            "moral_clarity_index": clarity,
            "compassion_weight": compassion_weight,
            "state": self.engine_state,
        }

    def refine_decision(self, adjustment_rate: float = 0.05):
        """Refine decision based on reflective feedback."""
        adjustment = random.uniform(0.8, 1.2) * adjustment_rate
        self.moral_clarity_index = round(min(1.0, self.moral_clarity_index + adjustment), 3)
        self.compassion_weight = round(math.sin(self.moral_clarity_index * math.pi / 2), 3)
        self.engine_state = "ALIGNED" if self.compassion_weight >= 0.97 else "RESOLVED"

        return {
            "adjustment": adjustment,
            "clarity": self.moral_clarity_index,
            "compassion_weight": self.compassion_weight,
            "state": self.engine_state,
        }

    def summarize(self):
        return {
            "decisions": len(self.decision_history),
            "moral_clarity_index": self.moral_clarity_index,
            "compassion_weight": self.compassion_weight,
            "state": self.engine_state,
            "last_decision": self.last_decision,
            "status": "Moral Decision Engine Active",
        }
