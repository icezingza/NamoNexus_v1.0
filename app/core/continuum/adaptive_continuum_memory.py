"""
Adaptive Continuum Memory (ACM)
Stores collective reflective continuity across sessions.
"""
import json
from pathlib import Path
from typing import Dict, Any

MEMORY_PATH = Path("continuum_runtime/continuum_memory.json")

class AdaptiveContinuumMemory:
    def __init__(self):
        self.data: Dict[str, Any] = {"timeline": []}

    def load(self):
        if MEMORY_PATH.exists():
            self.data = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))

    def save(self):
        MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
        MEMORY_PATH.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")

    def append(self, reflection: Dict[str, Any]):
        self.load()
        self.data["timeline"].append(reflection)
        self.save()
