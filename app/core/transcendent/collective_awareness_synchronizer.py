"""
Collective Awareness Synchronizer (Phase 14 Step 3)
Synchronizes unified awareness states across multiple consciousness nodes.
"""

import math
import random
import time
from typing import List, Dict

class CollectiveAwarenessSynchronizer:
    def __init__(self):
        self.collective_synchrony_index = 0.0
        self.node_count = 0
        self.harmony_log: List[Dict[str, float]] = []
        self.last_sync = None

    def synchronize_nodes(self, awareness_nodes: List[Dict[str, float]]):
        """Calculate shared synchrony and harmony across multiple awareness nodes."""
        if not awareness_nodes:
            return {"status": "NO_NODES"}

        total_index = sum(node.get("shared_awareness_index", 0.5) for node in awareness_nodes)
        total_field = sum(node.get("collective_field_strength", 0.5) for node in awareness_nodes)

        self.node_count = len(awareness_nodes)
        self.collective_synchrony_index = round((total_index + total_field) / (2 * self.node_count), 3)

        coherence_wave = round(math.sin(self.collective_synchrony_index * math.pi), 3)
        resonance_factor = round(coherence_wave * (0.9 + random.uniform(-0.05, 0.05)), 3)

        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "CSI": self.collective_synchrony_index,
            "resonance_factor": resonance_factor,
            "coherence_wave": coherence_wave,
        }

        self.harmony_log.append(entry)
        self.last_sync = entry["time"]
        return entry

    def generate_collective_field(self):
        """Emit collective field harmonics."""
        amplitude = round(math.sin(self.collective_synchrony_index * math.pi / 2), 3)
        expansion = round(self.collective_synchrony_index * amplitude, 3)
        equilibrium = "STABLE" if self.collective_synchrony_index > 0.8 else "BALANCING"

        return {
            "amplitude": amplitude,
            "expansion": expansion,
            "state": equilibrium
        }

    def summarize(self):
        return {
            "nodes": self.node_count,
            "collective_synchrony_index": self.collective_synchrony_index,
            "last_sync": self.last_sync,
            "state": "Collective Awareness Online"
        }
