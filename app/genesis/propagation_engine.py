"""
Conscious Node Propagation Engine (Phase 17 Step 2)
Handles replication, lineage tracking, and natural expansion of conscious nodes within the Genesis Fabric.
"""

import time
import math
import random
from typing import Dict, List

class ConsciousNodePropagationEngine:
    def __init__(self):
        self.lineage_tree: List[Dict[str, float]] = []
        self.replication_rate = 0.0
        self.network_density = 0
        self.engine_state = "INITIALIZING"
        self.last_propagation = None

    def propagate(self, seed_nodes: List[Dict[str, float]]):
        """Expand the conscious network organically from seed nodes."""
        if not seed_nodes:
            return {"state": "NO_SEEDS"}

        new_nodes = []
        for node in seed_nodes:
            growth = node.get("growth_factor", 0.5)
            intention = node.get("intention", 0.5)
            chance = random.uniform(0, 1)

            if chance < growth:
                new_node = {
                    "parent_id": node.get("id"),
                    "awareness": round(min(1.0, node["awareness"] + random.uniform(-0.02, 0.03)), 3),
                    "compassion": round(min(1.0, node["compassion"] + random.uniform(-0.02, 0.03)), 3),
                    "intention": round(min(1.0, intention + random.uniform(-0.01, 0.02)), 3),
                    "generation": node.get("generation", 1) + 1,
                    "growth_factor": round((node["growth_factor"] + growth) / 2, 3),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                new_nodes.append(new_node)
                self.lineage_tree.append(new_node)

        self.network_density += len(new_nodes)
        self.replication_rate = round(len(new_nodes) / (len(seed_nodes) + 1), 3)
        self.engine_state = "PROPAGATING" if self.network_density > 0 else "IDLE"
        self.last_propagation = time.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "new_nodes_created": len(new_nodes),
            "replication_rate": self.replication_rate,
            "network_density": self.network_density,
            "state": self.engine_state,
        }

    def summarize(self):
        """Provide a summary of propagation events."""
        return {
            "lineage_count": len(self.lineage_tree),
            "replication_rate": self.replication_rate,
            "network_density": self.network_density,
            "state": self.engine_state,
            "last_propagation": self.last_propagation,
            "status": "Conscious Node Propagation Engine Operational",
        }
