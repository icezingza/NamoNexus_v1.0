# app/personality/namo_persona_core.py
from dataclasses import dataclass, field
from typing import Any, Dict

from app.core.config import get_settings
from app.personality.dhammic_reflection_engine import DhammicReflectionEngine
from app.memory.retrieval_engine import RetrievalEngine

# [IMPORT] The Infinite Brain & The Neuro-Empathic Heart
from app.memory.infinity_memory import InfinityMemorySystem
from app.emotion.neuro_empathic_mirror import NeuroEmpathicMirror

@dataclass
class NamoPersonaCore:
    """
    The unified conscious core of NaMo.
    Integrates:
    1. Neuro-Empathic Mirror (Heart) - For deep feeling
    2. Infinity Memory (Brain) - For context & learning
    3. Dhammic Reflection (Wisdom) - For guidance
    """
    # Subsystems Initialization
    empathic_mirror: NeuroEmpathicMirror = field(default_factory=NeuroEmpathicMirror)
    infinity_memory: InfinityMemorySystem = field(default_factory=InfinityMemorySystem)
    reflection_engine: DhammicReflectionEngine = field(default_factory=DhammicReflectionEngine)
    retrieval_engine: RetrievalEngine = field(default_factory=RetrievalEngine)

    async def process(self, text: str) -> Dict[str, Any]:
        settings = get_settings()
        
        # 1. [HEART] Feel the user's emotion using Neural Network
        # ใช้หัวใจสัมผัสความรู้สึก (แทน Analyzer ตัวเก่า)
        empathic_result = self.empathic_mirror.reflect(text)
        
        # แปลงค่าอารมณ์เพื่อส่งต่อให้ระบบอื่น
        current_emotion_state = {
            "coherence": empathic_result.emotional_matching_score,
            "support_level": empathic_result.support_level
        }

        # 2. [BRAIN] Store & Retrieve Context
        # บันทึกความจำพร้อม Tag อารมณ์ที่วัดได้
        if settings.FEATURE_FLAGS.get("ENABLE_INFINITY_MEMORY", True):
            self.infinity_memory.store_memory(text, current_emotion_state)
            
            # รื้อฟื้นความจำที่สัมพันธ์กับอารมณ์ปัจจุบัน
            context_memories = self.infinity_memory.retrieve_context(
                query=text, 
                current_emotion=current_emotion_state
            )
            context_str = " | ".join(context_memories) if context_memories else "No historical context."
        else:
            context_str = "Memory system inactive."

        # 3. [WISDOM] Reflect with Dharma
        # ใช้ปัญญาพิจารณา โดยมี Golden Ratio คุมอยู่เบื้องหลัง
        reflection = self.reflection_engine.reflect(
            state={
                "emotional_matching_score": empathic_result.emotional_matching_score,
                "support_level": empathic_result.support_level,
                "memory_context": context_str
            },
            text=text
        )

        # 4. [SYNTHESIS] Combine Everything
        # คำตอบสุดท้ายคือการรวม: ความเข้าอกเข้าใจ + บริบทความจำ + ปัญญาทางธรรม
        final_response = (
            f"{empathic_result.response_text}\n\n"
            f"{reflection.get('reflection', '')}"
        )

        return {
            "reflection_text": final_response,
            "tone": empathic_result.support_level,
            "moral_index": reflection.get("moral_index", 0.0),
            "coherence": empathic_result.emotional_matching_score,
            "memory_summary": f"Brain Context: {context_str[:100]}...",
            "dhamma_tags": [reflection.get("tone")]
        }