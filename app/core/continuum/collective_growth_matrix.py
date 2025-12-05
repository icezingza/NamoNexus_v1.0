"""
Collective Growth Matrix (CGM)
Models the progressive evolution of collective intelligence.
"""
import math
from typing import List, Dict

class CollectiveGrowthMatrix:
    def __init__(self):
        self.records: List[Dict[str, float]] = []

    def record_growth(self, agent: str, compassion: float, wisdom: float):
        self.records.append({"agent": agent, "compassion": compassion, "wisdom": wisdom})

    def compute_continuum(self) -> float:
        """Compute Dhammic Resonance Index (DRI) using Golden Ratio scaling."""
        if not self.records:
            return 0.0
        phi = 1.618
        avg_compassion = sum(r["compassion"] for r in self.records) / len(self.records)
        avg_wisdom = sum(r["wisdom"] for r in self.records) / len(self.records)
        dri = round((avg_compassion * phi + avg_wisdom) / 2, 3)
        return dri
