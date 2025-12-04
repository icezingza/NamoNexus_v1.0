from namo_nexus.api.schemas import ChatRequest, ChatResponse
from namo_nexus.memory.hybrid_store import HybridMemoryStore
from namo_nexus.core.context_builder import ContextBuilder
from namo_nexus.affect.emotion_analyzer import EmotionAnalyzer
from namo_nexus.affect.suicide_safeguard import SuicideSafeguard

class Orchestrator:
    def __init__(self):
        self.memory = HybridMemoryStore()
        self.context_builder = ContextBuilder()
        self.emotion_analyzer = EmotionAnalyzer()
        self.safeguard = SuicideSafeguard()

    async def process(self, request: ChatRequest) -> ChatResponse:
        # 1. Safety Check (Pre-processing)
        # 2. Context Building
        # 3. Memory Retrieval
        # 4. Emotion Analysis
        # 5. Response Generation (Stub)
        # 6. Memory Storage

        # Simple Logic
        emotion_state = self.emotion_analyzer.analyze(request.message, {})
        safety_alert = self.safeguard.check_safety(request.message, emotion_state)

        if safety_alert:
            return ChatResponse(
                reply="I detect you are going through a difficult time. Please reach out to a professional.",
                safety_flag=True,
                metadata={"alert": safety_alert}
            )

        context = self.context_builder.build_context(request, [])

        # Stub response
        response_text = f"I hear you saying: {request.message}. (Emotion: {emotion_state['distress_level']})"

        self.memory.store_interaction(request, response_text)

        return ChatResponse(
            reply=response_text,
            safety_flag=False,
            metadata={"emotion": emotion_state}
        )
