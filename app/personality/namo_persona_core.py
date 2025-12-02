"""NaMo persona core orchestrating emotion, reflection, and memory."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.emotion.analyzer import EmotionAnalyzer
from app.memory.store import MemoryStore
from app.personality.dhammic_reflection_engine import DhammicReflectionEngine
from app.memory.retrieval_engine import RetrievalEngine


@dataclass
class NamoPersonaCore:
    emotion_analyzer: EmotionAnalyzer = field(default_factory=EmotionAnalyzer)
    memory_store: MemoryStore = field(default_factory=MemoryStore)
    reflection_engine: DhammicReflectionEngine = field(default_factory=DhammicReflectionEngine)
    retrieval_engine: RetrievalEngine = field(default_factory=RetrievalEngine)

    def process(self, text: str) -> dict[str, Any]:
        emotion = self.emotion_analyzer.analyze(text)
        reflection = self.reflection_engine.reflect(text, emotion)
        self.memory_store.save_reflection(reflection)
        memory = self.memory_store.recall()
        return {
            "reflection": reflection,
            "memory": memory,
            "coherence": emotion.get("coherence", 0.0),
        }
