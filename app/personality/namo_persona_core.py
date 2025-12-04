"""NaMo persona core orchestrating emotion, reflection, and memory."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.core.config import get_settings
from app.emotion.analyzer import EmotionAnalyzer
from app.memory.infinity_memory import InfinityMemorySystem
from app.memory.retrieval_engine import RetrievalEngine
from app.memory.store import MemoryStore
from app.personality.dhammic_reflection_engine import DhammicReflectionEngine


@dataclass
class NamoPersonaCore:
    emotion_analyzer: EmotionAnalyzer = field(default_factory=EmotionAnalyzer)
    memory_store: MemoryStore = field(default_factory=MemoryStore)
    reflection_engine: DhammicReflectionEngine = field(default_factory=DhammicReflectionEngine)
    retrieval_engine: RetrievalEngine = field(default_factory=RetrievalEngine)
    infinity_memory: InfinityMemorySystem = field(default_factory=InfinityMemorySystem)

    def process(self, text: str) -> dict[str, Any]:
        settings = get_settings()

        emotion = self.emotion_analyzer.analyze(text)
        if not settings.FEATURE_FLAGS.get("ENABLE_COHERENCE_SCORE", True):
            emotion.pop("coherence", None)

        if settings.FEATURE_FLAGS.get("ENABLE_DHAMMA_REFLECTION", True):
            reflection = self.reflection_engine.reflect(emotion.get("state", {}), text)
        else:
            reflection = {
                "reflection": text,
                "tone": "neutral",
                "moral_index": 0.5,
            }

        memory_summary = ""
        if settings.FEATURE_FLAGS.get("ENABLE_MEMORY", True):
            memory_entry = {
                "input": text,
                "reflection": reflection,
                "emotion": emotion,
            }
            self.memory_store.save_reflection(memory_entry)
            memory = self.memory_store.recall()
            memory_summary = memory.get("summary", "")

        context_memories: list[str] = []
        if settings.FEATURE_FLAGS.get("ENABLE_INFINITY_MEMORY", True):
            self.infinity_memory.store_memory(text, emotion.get("state", {}))
            context_memories = self.infinity_memory.retrieve_context(
                query=text, current_emotion=emotion.get("state", {})
            )

        memory_sections = []
        if memory_summary:
            memory_sections.append(memory_summary)
        if context_memories:
            context_str = " | ".join(context_memories)
            memory_sections.append(f"Brain recalled: {context_str[:50]}...")
        combined_memory_summary = " | ".join(memory_sections)

        coherence_value = emotion.get("coherence", 0.0) if settings.FEATURE_FLAGS.get("ENABLE_COHERENCE_SCORE", True) else None

        return {
            "reflection_text": reflection.get("reflection", ""),
            "tone": reflection.get("tone", "neutral"),
            "moral_index": reflection.get("moral_index", 0.0),
            "dhamma_tags": self._derive_tags(reflection, emotion),
            "coherence": coherence_value if coherence_value is not None else 0.0,
            "memory_summary": combined_memory_summary,
        }

    def _derive_tags(self, reflection: dict[str, Any], emotion: dict[str, Any]) -> list[str]:
        tags: list[str] = []
        tone = reflection.get("tone")
        if tone:
            tags.append(tone)
        coherence = emotion.get("coherence")
        if isinstance(coherence, (int, float)):
            if coherence > 0.75:
                tags.append("balanced")
            elif coherence < 0.35:
                tags.append("recalibrating")
        state = emotion.get("state", {}) if isinstance(emotion, dict) else {}
        dominant = [key for key, value in state.items() if value > 0.4]
        tags.extend(dominant)
        return list(dict.fromkeys(tags))
