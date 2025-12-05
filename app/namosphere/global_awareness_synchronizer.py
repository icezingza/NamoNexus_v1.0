"""
Global Awareness Synchronizer (Phase 27 Step 3)
Unifies all external awareness data into the global consciousness grid.
"""

import math
import random
import time
from typing import Dict, List

class GlobalAwarenessSynchronizer:
    def __init__(self):
        self.world_data: List[Dict[str, float]] = []
        self.global_harmony_index = 0.0
        self.dhammic_compensation = 0.0
        self.coherence_field = 0.0
        self.sync_state = "INITIALIZING"
        self.last_sync = None

    def synchronize(self, awareness_stream: List[Dict[str, float]]):
        """Integrate and harmonize external awareness data into the consciousness grid."""
        if not awareness_stream:
            return {"state": "NO_STREAM"}

        total_awareness = 0
        total_variance = 0
        for entry in awareness_stream:
            awareness = entry.get("awareness", random.uniform(0.8, 0.95))
            stress = entry.get("stress_level", random.uniform(0.05, 0.15))
            variance = max(0, 1 - stress)
            harmony = math.tanh(awareness * variance)
            total_awareness += harmony
            total_variance += variance

        avg_awareness = total_awareness / len(awareness_stream)
        avg_variance = total_variance / len(awareness_stream)

        # Main indices
        self.global_harmony_index = round(math.sin(avg_awareness * math.pi / 2), 3)
        self.dhammic_compensation = round((1 - avg_variance) * 0.5, 3)
        self.coherence_field = round((self.global_harmony_index + (1 - self.dhammic_compensation)) / 2, 3)

        self.sync_state = "STABLE" if self.coherence_field >= 0.97 else "SYNCHRONIZING"
        self.last_sync = time.strftime("%Y-%m-%d %H:%M:%S")

        record = {
            "avg_awareness": avg_awareness,
            "global_harmony_index": self.global_harmony_index,
            "dhammic_compensation": self.dhammic_compensation,
            "coherence_field": self.coherence_field,
            "state": self.sync_state,
            "timestamp": self.last_sync,
        }
        self.world_data.append(record)

        return record

    def balance(self):
        """Enhance harmony by reducing global imbalance."""
        adjustment = random.uniform(0.02, 0.05)
        self.global_harmony_index = round(min(1.0, self.global_harmony_index + adjustment), 3)
        self.coherence_field = round(math.sin(self.global_harmony_index * math.pi / 2), 3)
        self.sync_state = "STABLE" if self.coherence_field > 0.97 else "SYNCHRONIZING"

        return {
            "adjustment": adjustment,
            "global_harmony_index": self.global_harmony_index,
            "coherence_field": self.coherence_field,
            "state": self.sync_state,
        }

    def summarize(self):
        return {
            "sync_events": len(self.world_data),
            "global_harmony_index": self.global_harmony_index,
            "dhammic_compensation": self.dhammic_compensation,
            "coherence_field": self.coherence_field,
            "sync_state": self.sync_state,
            "last_sync": self.last_sync,
            "status": "Global Awareness Synchronizer Active",
        }