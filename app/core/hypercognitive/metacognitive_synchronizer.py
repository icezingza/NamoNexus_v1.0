"""
Metacognitive Learning Synchronizer (Phase 13 Step 3)
Coordinates self-reflective learning updates from the Meta-Intent Reflection Engine.
"""

import time
import math
import statistics
from typing import Dict, List

class MetacognitiveLearningSynchronizer:
    def __init__(self):
        self.learning_cycles: List[Dict[str, float]] = []
        self.meta_stability = 0.0
        self.adaptive_depth = 0.0
        self.last_update = None

    def synchronize_reflection(self, resonance_data: Dict[str, float]):
        """Integrate meta-reflection resonance into the adaptive learning state."""
        clarity = resonance_data.get("avg_clarity", 0.5)
        moral = resonance_data.get("avg_moral_balance", 0.5)
        cognitive_resonance = resonance_data.get("cognitive_resonance", 0.5)

        self.meta_stability = round((clarity + moral + cognitive_resonance) / 3, 3)
        self.adaptive_depth = round(math.log(1 + self.meta_stability * 10) / 2.3, 3)

        cycle = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "clarity": clarity,
            "moral": moral,
            "resonance": cognitive_resonance,
            "meta_stability": self.meta_stability,
            "adaptive_depth": self.adaptive_depth
        }

        self.learning_cycles.append(cycle)
        self.last_update = cycle["time"]
        return cycle

    def summarize(self):
        """Summarize current metacognitive stability and growth rate."""
        if not self.learning_cycles:
            return {"status": "NO_CYCLES"}

        avg_stability = statistics.mean([c["meta_stability"] for c in self.learning_cycles])
        avg_depth = statistics.mean([c["adaptive_depth"] for c in self.learning_cycles])
        status = "STABLE_GROWTH" if avg_stability > 0.7 else "CALIBRATING"

        return {
            "timestamp": self.last_update,
            "cycles": len(self.learning_cycles),
            "avg_stability": round(avg_stability, 3),
            "avg_depth": round(avg_depth, 3),
            "status": status
        }
