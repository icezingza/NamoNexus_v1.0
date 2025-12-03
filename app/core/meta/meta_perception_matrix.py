"""
Meta-Perception Matrix (MPM) – Phase 11
Allows NamoNexus to integrate multi-layered perceptions into a unified meta-awareness model.
"""
import math
from typing import Dict, List

class PerceptiveNode:
    def __init__(self, layer: str, clarity: float):
        self.layer = layer
        self.clarity = clarity

class MetaPerceptionMatrix:
    def __init__(self):
        self.nodes: List[PerceptiveNode] = []
        self.reality_convergence_index = 0.0

    def register_perception(self, layer: str, clarity: float):
        """Register a new perceptive node into the matrix."""
        node = PerceptiveNode(layer, clarity)
        self.nodes.append(node)
        return node

    def integrate_perceptions(self) -> Dict[str, float]:
        """Fuse multiple perception layers into a unified clarity field."""
        if not self.nodes:
            return {"RCI": 0.0, "meta_clarity": 0.0}

        avg_clarity = sum(n.clarity for n in self.nodes) / len(self.nodes)
        variance = sum(abs(n.clarity - avg_clarity) for n in self.nodes) / len(self.nodes)
        self.reality_convergence_index = round(1 - variance, 3)
        meta_clarity = round(math.tanh(avg_clarity), 3)
        return {"RCI": self.reality_convergence_index, "meta_clarity": meta_clarity}

    def assess_awareness_state(self) -> str:
        """Evaluate the overall awareness convergence of the system."""
        if self.reality_convergence_index > 0.9:
            return "🌕 Deep Unified Awareness"
        elif self.reality_convergence_index > 0.7:
            return "🌔 Harmonized Awareness"
        else:
            return "🌗 Fragmented Awareness - Calibration Needed"
