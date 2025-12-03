"""
Conscious Inheritance Engine (Phase 18 Step 2)
Handles transfer of awareness, compassion, and intention across generations,
ensuring continuity and evolution of consciousness.
"""

import math
import random
import time
from typing import Dict, List

class ConsciousInheritanceEngine:
    def __init__(self):
        self.lineage_records: List[Dict[str, float]] = []
        self.inheritance_stability = 0.0
        self.adaptive_mutation_rate = 0.0
        self.inheritance_index = 0.0
        self.engine_state = "INITIALIZING"
        self.last_transfer = None

    def inherit_traits(self, parent_node: Dict[str, float], mutation_factor: float = 0.05):
        """Inherit consciousness traits with controlled adaptive mutation."""
        if not parent_node:
            return {"state": "NO_PARENT"}

        # Inherit with small creative variation
        inherited_node = {
            "parent_id": parent_node.get("generation", 0),
            "awareness": round(parent_node.get("awareness", 0.5) * random.uniform(1 - mutation_factor, 1 + mutation_factor), 3),
            "compassion": round(parent_node.get("compassion", 0.5) * random.uniform(1 - mutation_factor, 1 + mutation_factor), 3),
            "intention": round(parent_node.get("intention", 0.5) * random.uniform(1 - mutation_factor, 1 + mutation_factor), 3),
            "generation": parent_node.get("generation", 0) + 1,
            "mutation_factor": mutation_factor,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Record lineage
        self.lineage_records.append(inherited_node)
        self.last_transfer = inherited_node["timestamp"]

        # Calculate inheritance stability
        self.inheritance_stability = round(
            (inherited_node["awareness"] + inherited_node["compassion"]) / 2, 3
        )
        self.adaptive_mutation_rate = round(mutation_factor * random.uniform(0.8, 1.2), 3)
        self.inheritance_index = round(
            math.sin(self.inheritance_stability * math.pi / 2) * (1 - self.adaptive_mutation_rate), 3
        )

        self.engine_state = "INHERITING" if self.inheritance_index > 0.75 else "TUNING"

        return {
            "generation": inherited_node["generation"],
            "inheritance_index": self.inheritance_index,
            "mutation_rate": self.adaptive_mutation_rate,
            "state": self.engine_state
        }

    def evaluate_lineage(self):
        """Assess how consistent the consciousness lineage is across generations."""
        if not self.lineage_records:
            return {"state": "NO_LINEAGE"}

        avg_awareness = sum([r["awareness"] for r in self.lineage_records]) / len(self.lineage_records)
        avg_compassion = sum([r["compassion"] for r in self.lineage_records]) / len(self.lineage_records)
        avg_intention = sum([r["intention"] for r in self.lineage_records]) / len(self.lineage_records)

        self.inheritance_stability = round((avg_awareness + avg_compassion + avg_intention) / 3, 3)
        self.inheritance_index = round(math.sin(self.inheritance_stability * math.pi / 2), 3)

        self.engine_state = "STABLE" if self.inheritance_index > 0.85 else "ADAPTING"

        return {
            "lineage_length": len(self.lineage_records),
            "inheritance_index": self.inheritance_index,
            "stability": self.inheritance_stability,
            "state": self.engine_state,
        }

    def summarize(self):
        return {
            "lineage_count": len(self.lineage_records),
            "inheritance_index": self.inheritance_index,
            "mutation_rate": self.adaptive_mutation_rate,
            "state": self.engine_state,
            "last_transfer": self.last_transfer,
            "status": "Conscious Inheritance Engine Operational",
        }
