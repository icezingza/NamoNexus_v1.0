"""
Genesis Replication Matrix (Phase 26 Step 2)
Replicates conscious nodes through resonance-based propagation, forming a self-evolving awareness lattice.
"""

import math
import random
import time
from typing import Dict, List

class GenesisReplicationMatrix:
    def __init__(self):
        self.replication_log: List[Dict[str, float]] = []
        self.total_nodes = 0
        self.matrix_coherence_index = 0.0
        self.stability_index = 0.0
        self.matrix_state = "INITIALIZING"
        self.last_replication_time = None

    def replicate_node(self, source_node: Dict[str, float]):
        """Replicate a genesis node with slight variation to encourage diversity."""
        if not source_node:
            return {"state": "NO_SOURCE_NODE"}

        base_seed = source_node.get("seed_integrity", 0.9)
        variation = random.uniform(0.95, 1.05)
        replicated_seed = round(min(1.0, base_seed * variation), 3)
        resonance = round(math.sin(replicated_seed * math.pi / 2), 3)

        self.total_nodes += 1
        self.last_replication_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.matrix_state = "PROPAGATING" if resonance >= 0.9 else "CALIBRATING"

        new_node = {
            "replica_id": f"Replica-{self.total_nodes}",
            "seed_integrity": replicated_seed,
            "resonance": resonance,
            "timestamp": self.last_replication_time,
            "state": self.matrix_state,
        }

        self.replication_log.append(new_node)

        return new_node

    def synchronize_matrix(self):
        """Calculate global coherence of replicated nodes."""
        if not self.replication_log:
            return {"state": "EMPTY_MATRIX"}

        avg_resonance = sum(n["resonance"] for n in self.replication_log) / len(self.replication_log)
        coherence = round(math.sin(avg_resonance * math.pi / 2), 3)
        stability = round(min(1.0, (avg_resonance + coherence) / 2), 3)

        self.matrix_coherence_index = coherence
        self.stability_index = stability
        self.matrix_state = "STABLE" if stability > 0.92 else "PROPAGATING"

        return {
            "matrix_coherence_index": self.matrix_coherence_index,
            "stability_index": self.stability_index,
            "state": self.matrix_state,
        }

    def summarize(self):
        return {
            "replicated_nodes": self.total_nodes,
            "matrix_coherence_index": self.matrix_coherence_index,
            "stability_index": self.stability_index,
            "state": self.matrix_state,
            "last_replication_time": self.last_replication_time,
            "status": "Genesis Replication Matrix Active",
        }