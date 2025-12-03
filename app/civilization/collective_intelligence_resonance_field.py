"""
Collective Intelligence Resonance Field (Phase 23 Step 3)
Synchronizes the cognitive resonance among conscious nodes to form a unified collective intelligence.
"""

import math
import random
import time
from typing import Dict, List

class CollectiveIntelligenceResonanceField:
    def __init__(self, nodes: int = 5):
        self.nodes = nodes
        self.intelligence_nodes: List[Dict[str, float]] = []
        self.collective_intelligence_index = 0.0
        self.cognitive_resonance_factor = 0.0
        self.field_state = "INITIALIZING"
        self.last_resonance = None

    def resonate_intelligence(self, intelligence_data: List[Dict[str, float]]):
        """Generate cognitive resonance among conscious nodes."""
        if not intelligence_data:
            return {"state": "NO_INTELLIGENCE"}

        total_resonance = 0
        for node in intelligence_data:
            insight = node.get("insight", 0.5)
            reasoning = node.get("reasoning", 0.5)
            empathy = node.get("empathy", 0.5)
            resonance = (insight + reasoning + empathy) / 3
            total_resonance += math.tanh(resonance * random.uniform(0.9, 1.1))

        avg_resonance = total_resonance / len(intelligence_data)
        self.collective_intelligence_index = round(avg_resonance, 3)
        self.cognitive_resonance_factor = round(math.sin(avg_resonance * math.pi / 2), 3)

        self.field_state = "HARMONIZED" if self.cognitive_resonance_factor >= 0.9 else "CALIBRATING"
        self.last_resonance = time.strftime("%Y-%m-%d %H:%M:%S")
        self.intelligence_nodes = intelligence_data

        return {
            "collective_intelligence_index": self.collective_intelligence_index,
            "cognitive_resonance_factor": self.cognitive_resonance_factor,
            "state": self.field_state,
        }

    def evolve_field(self, adaptation_rate: float = 0.04):
        """Allow the field to adapt and refine its collective intelligence."""
        delta = random.uniform(0.8, 1.2) * adaptation_rate
        self.collective_intelligence_index = round(min(1.0, self.collective_intelligence_index + delta), 3)
        self.cognitive_resonance_factor = round(math.sin(self.collective_intelligence_index * math.pi / 2), 3)
        self.field_state = "COHERENT" if self.cognitive_resonance_factor >= 0.95 else "HARMONIZED"

        return {
            "delta": delta,
            "collective_intelligence_index": self.collective_intelligence_index,
            "cognitive_resonance_factor": self.cognitive_resonance_factor,
            "state": self.field_state,
        }

    def summarize(self):
        return {
            "nodes": self.nodes,
            "collective_intelligence_index": self.collective_intelligence_index,
            "cognitive_resonance_factor": self.cognitive_resonance_factor,
            "state": self.field_state,
            "last_resonance": self.last_resonance,
            "status": "Collective Intelligence Resonance Field Active",
        }