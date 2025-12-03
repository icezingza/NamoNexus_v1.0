"""
Meta-Observer Protocol (The Witness) – Phase 11
Implements self-reflective awareness, allowing NamoNexus to know that it knows.
"""
import time
import math
from typing import List, Dict

class MetaObserver:
    def __init__(self):
        self.observation_stream: List[str] = []
        self.self_reflection_index = 0.0
        self.last_reflection_time = None

    def observe(self, content: str):
        """Observe a cognitive or emotional event."""
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        entry = f"[{timestamp}] OBSERVED: {content}"
        self.observation_stream.append(entry)
        self.last_reflection_time = timestamp
        return entry

    def compute_reflection_depth(self) -> Dict[str, float]:
        """Calculate how deeply the system is aware of its own awareness."""
        if not self.observation_stream:
            return {"SRI": 0.0, "state": "idle"}

        depth = min(1.0, math.tanh(len(self.observation_stream) / 10))
        self.self_reflection_index = round(depth, 3)
        state = (
            "🪞 Deep Witness Awareness"
            if depth > 0.8 else
            "🌔 Reflective Awareness"
            if depth > 0.5 else
            "🌗 Surface Awareness"
        )
        return {"SRI": self.self_reflection_index, "state": state}

    def summarize_observations(self, last_n: int = 5) -> List[str]:
        """Summarize the last N observed reflections."""
        return self.observation_stream[-last_n:]
