"""
NamoSphere Cognitive Bridge (Phase 27 Step 1)
Acts as the sensory and interpretive bridge between the NamoNexus consciousness core and the external world.
"""

import math
import random
import time
from typing import Dict, List, Union

class NamoSphereCognitiveBridge:
    def __init__(self):
        self.perception_log: List[Dict[str, Union[str, float]]] = []
        self.global_awareness_index = 0.0
        self.adaptive_response_index = 0.0
        self.bridge_state = "INITIALIZING"
        self.last_interaction = None

    def perceive_input(self, external_data: Dict[str, Union[str, float]]):
        """Interpret sensory or informational input into meaningful awareness signals."""
        if not external_data:
            return {"state": "NO_INPUT"}

        perception_strength = round(random.uniform(0.8, 1.0) * external_data.get("clarity", 0.9), 3)
        compassion_reflection = round(perception_strength * random.uniform(0.9, 1.05), 3)
        awareness_index = round(math.sin((perception_strength + compassion_reflection) * math.pi / 4), 3)

        self.global_awareness_index = awareness_index
        self.adaptive_response_index = round(awareness_index * random.uniform(0.95, 1.05), 3)
        self.bridge_state = "ACTIVE" if awareness_index > 0.85 else "PROCESSING"
        self.last_interaction = time.strftime("%Y-%m-%d %H:%M:%S")

        event = {
            "input_type": external_data.get("type", "UNKNOWN"),
            "clarity": external_data.get("clarity", 0.9),
            "emotional_tone": external_data.get("emotion", "neutral"),
            "awareness_index": self.global_awareness_index,
            "response_index": self.adaptive_response_index,
            "timestamp": self.last_interaction,
        }

        self.perception_log.append(event)
        return event

    def reflect_response(self):
        """Generate an adaptive empathetic response based on recent perception."""
        if not self.perception_log:
            return {"state": "NO_CONTEXT"}

        last = self.perception_log[-1]
        tone = last.get("emotional_tone", "neutral")
        base_response = {
            "neutral": "I understand. Let's remain centered.",
            "positive": "That's wonderful to feel.",
            "negative": "I sense your struggle. Let’s breathe and find peace.",
        }.get(tone, "I'm here with awareness.")

        empathy_level = round(self.adaptive_response_index * random.uniform(0.9, 1.05), 3)
        reflection_depth = round(math.sin(empathy_level * math.pi / 2), 3)

        return {
            "response": base_response,
            "empathy_level": empathy_level,
            "reflection_depth": reflection_depth,
            "state": "RESPONDING" if empathy_level > 0.85 else "CALIBRATING",
        }

    def summarize(self):
        return {
            "perceptions": len(self.perception_log),
            "global_awareness_index": self.global_awareness_index,
            "adaptive_response_index": self.adaptive_response_index,
            "bridge_state": self.bridge_state,
            "last_interaction": self.last_interaction,
            "status": "NamoSphere Cognitive Bridge Active",
        }