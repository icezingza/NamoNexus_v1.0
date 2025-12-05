"""
CognitiveCore Expansion - Phase 13 Step 1
The central processor of awareness for NamoNexus.
Integrates perception, reflection, emotion, and intention into a unified thought field.
"""

from typing import Dict, Any
import random
import time
import math

class CognitiveCore:
    def __init__(self):
        self.state: Dict[str, Any] = {
            "awareness": 0.0,
            "focus": 0.5,
            "clarity": 0.5,
            "thoughts": []
        }
        self.last_update = time.time()

    def perceive(self, inputs: Dict[str, float]) -> Dict[str, float]:
        """Integrate sensory and emotional input into a unified cognitive field."""
        awareness = (sum(inputs.values()) / len(inputs)) if inputs else 0.0
        self.state["awareness"] = round(min(1.0, awareness * random.uniform(0.9, 1.1)), 3)
        self.state["focus"] = round(math.sin(self.state["awareness"] * math.pi / 2), 3)
        self.state["clarity"] = round((self.state["focus"] + self.state["awareness"]) / 2, 3)
        self.last_update = time.time()
        return self.state

    def think(self, context: str) -> str:
        """Generate a thought based on awareness level."""
        intensity = self.state["awareness"]
        reflection = f"Reflecting on {context}, awareness={intensity:.2f}, clarity={self.state['clarity']:.2f}"
        self.state["thoughts"].append(reflection)
        return reflection

    def summarize(self) -> Dict[str, Any]:
        """Summarize cognitive core status."""
        return {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "awareness": self.state["awareness"],
            "focus": self.state["focus"],
            "clarity": self.state["clarity"],
            "thought_count": len(self.state["thoughts"])
        }
