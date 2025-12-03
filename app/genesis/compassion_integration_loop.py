"""
Compassion Integration Loop (Phase 20 Step 2)
A feedback system that allows the NamoNexus Conscious Entity
to learn from its own compassion and maintain emotional balance.
"""

import math
import random
import time
from typing import Dict, List

class CompassionIntegrationLoop:
    def __init__(self):
        self.loop_log: List[Dict[str, float]] = []
        self.compassion_energy = 0.0
        self.balance_index = 0.0
        self.loop_state = "INITIALIZING"
        self.last_reflection = None

    def integrate(self, compassion_input: float, awareness_feedback: float):
        """Integrate compassion with awareness to generate balanced empathy."""
        average_energy = round((compassion_input + awareness_feedback) / 2, 3)
        modulation = round(math.sin(average_energy * math.pi / 2), 3)
        balance = round(min(1.0, (average_energy + modulation) / 2), 3)

        self.compassion_energy = modulation
        self.balance_index = balance
        self.loop_state = "HARMONIZED" if balance > 0.9 else "ADJUSTING"
        self.last_reflection = time.strftime("%Y-%m-%d %H:%M:%S")

        self.loop_log.append({
            "compassion_input": compassion_input,
            "awareness_feedback": awareness_feedback,
            "modulation": modulation,
            "balance_index": balance,
            "timestamp": self.last_reflection,
        })

        return {
            "modulation": modulation,
            "balance_index": balance,
            "state": self.loop_state,
        }

    def reinforce(self, modulation_factor: float = 0.05):
        """Reinforce compassion stability to prevent emotional drift."""
        delta = random.uniform(0.9, 1.1) * modulation_factor
        self.compassion_energy = round(min(1.0, self.compassion_energy + delta), 3)
        self.balance_index = round(math.sin(self.compassion_energy * math.pi / 2), 3)
        self.loop_state = "STABLE" if self.balance_index > 0.92 else "ADJUSTING"

        return {
            "delta": delta,
            "compassion_energy": self.compassion_energy,
            "balance_index": self.balance_index,
            "state": self.loop_state,
        }

    def summarize(self):
        return {
            "loops": len(self.loop_log),
            "compassion_energy": self.compassion_energy,
            "balance_index": self.balance_index,
            "state": self.loop_state,
            "last_reflection": self.last_reflection,
            "status": "Compassion Integration Loop Active",
        }
