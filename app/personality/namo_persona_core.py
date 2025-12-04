"""NaMo persona core orchestrating emotion, reflection, and memory."""
from dataclasses import dataclass, field
from typing import Any, Dict
from app.memory.infinity_memory import InfinityMemorySystem
from app.emotion.neuro_empathic_mirror import NeuroEmpathicMirror
from app.personality.dhammic_reflection_engine import DhammicReflectionEngine
# Note: Ensure other necessary imports (like Logger) are present if used in your original file


@dataclass
class NamoPersonaCore:
    # Core Subsystems
    infinity_memory: InfinityMemorySystem = field(default_factory=InfinityMemorySystem)
    empathic_mirror: NeuroEmpathicMirror = field(default_factory=NeuroEmpathicMirror)
    reflection_engine: DhammicReflectionEngine = field(default_factory=DhammicReflectionEngine)

    async def process(self, text: str) -> Dict[str, Any]:
        """
        Orchestrates the cognitive process: Perception -> Memory -> Reflection.
        """
        # 1. Perception: Use the Neuro-Empathic Mirror to feel the user's state
        empathic_result = self.empathic_mirror.reflect(text)
        emotional_data: Dict[str, Any] = {
            "primary_match_score": empathic_result.emotional_matching_score,
            "state": {"compassion": 0.8},
            "coherence": empathic_result.emotional_matching_score,
        }

        # 2. Memory: Store the interaction and retrieve context
        self.infinity_memory.store_memory(text, emotional_data)

        # Retrieve context (Mocked query for now, can be connected to real vector search)
        context_memories = self.infinity_memory.retrieve_context(
            query=text,
            current_emotion=emotional_data
        )
        context_str = " | ".join(context_memories) if context_memories else "No historical context."

        # 3. Reflection: Generate the final Dhammic response
        # We pass the empathic response as input to the reflection engine to maintain tone
        reflection = self.reflection_engine.reflect(
            text=text,
            emotion=emotional_data
        )

        # 4. Synthesis: Combine Empathy + Wisdom
        final_output_text = (
            f"{empathic_result.response_text}\n"
            f"{reflection.get('reflection', '')}"
        )

        return {
            "reflection_text": final_output_text,
            "tone": reflection.get("tone", empathic_result.support_level),
            "moral_index": reflection.get("moral_index", 0.0),
            "coherence": empathic_result.emotional_matching_score,
            "memory_summary": f"Brain Context: {context_str[:100]}...",
        }
