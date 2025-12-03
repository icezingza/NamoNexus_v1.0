"""
Adaptive Cloud Memory — Shared memory layer across AI instances.
"""
import asyncio
import json
from typing import Dict, Any
from pathlib import Path

MEMORY_FILE = Path("cloud_runtime/global_memory.json")

class AdaptiveCloudMemory:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    async def load(self):
        if MEMORY_FILE.exists():
            self.data = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        else:
            self.data = {"reflections": []}

    async def sync(self, agent_id: str, reflection: str):
        await self.load()
        self.data["reflections"].append({
            "agent": agent_id,
            "reflection": reflection
        })
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")

    async def get_collective_reflection(self) -> str:
        await self.load()
        total = len(self.data["reflections"])
        if total == 0:
            return "No shared reflections yet."
        return f"{total} shared reflections synchronized."
