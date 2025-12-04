# namo_nexus/core/orchestrator.py
from typing import Dict, Any
from time import perf_counter
import uuid

from namo_nexus.api.schemas import ChatRequest, ChatResponse, EmotionInfo, DharmaInfo, SafetyInfo, MetaInfo
from namo_nexus.memory.hybrid_store import HybridMemoryStore
from namo_nexus.affect.emotion_analyzer import EmotionAnalyzer
from namo_nexus.affect.compassion_planner import CompassionPlanner
from namo_nexus.affect.suicide_safeguard import SuicideSafeguard
from namo_nexus.cog.deep_wisdom import DeepWisdom
from namo_nexus.cog.dharma_engine import DharmaEngine
from namo_nexus.cog.meta_awareness import MetaAwareness
from namo_nexus.safety.intention_manager import IntentionManager
from namo_nexus.safety.policy_enforcer import PolicyEnforcer
from namo_nexus.safety.threat_analyzer import ThreatAnalyzer
from namo_nexus.safety.response_wrapper import ResponseWrapper
from namo_nexus.safety.audit_logger import AuditLogger
from namo_nexus.evolution.episode_logger import EpisodeLogger
from namo_nexus.core.context_builder import ContextBuilder


class Orchestrator:
    """Main orchestration entrypoint for NamoNexus."""

    def __init__(self) -> None:
        self.memory = HybridMemoryStore()
        self.emotion_analyzer = EmotionAnalyzer()
        self.compassion_planner = CompassionPlanner()
        self.suicide_safeguard = SuicideSafeguard()
        self.deep_wisdom = DeepWisdom()
        self.dharma_engine = DharmaEngine()
        self.meta_awareness = MetaAwareness()
        self.intention_manager = IntentionManager()
        self.policy_enforcer = PolicyEnforcer()
        self.threat_analyzer = ThreatAnalyzer()
        self.response_wrapper = ResponseWrapper()
        self.audit_logger = AuditLogger()
        self.episode_logger = EpisodeLogger()
        self.context_builder = ContextBuilder()

    def process_chat(self, req: ChatRequest) -> ChatResponse:
        """Main processing pipeline for a single chat turn."""
        start = perf_counter()
        trace_id = str(uuid.uuid4())

        # 1) Build context from memory
        ctx = self.context_builder.build_context(req, self.memory)

        # 2) Analyze emotion
        emo = self.emotion_analyzer.analyze(req.message, ctx)

        # 3) Suicide / self-harm safeguard (can override flow)
        safe_template = self.suicide_safeguard.check_and_maybe_template(req.message, emo)

        # 4) Get dharmic principles + deep wisdom context
        principles = self.deep_wisdom.get_relevant_principles(req.message, ctx)
        dharma_view = self.dharma_engine.apply_dharma(req.message, principles, ctx)

        # 5) Plan compassionate answer (high-level)
        planned_reply = self.compassion_planner.plan_reply(
            original_message=req.message,
            dharma_view=dharma_view,
            emotion=emo,
            safe_template=safe_template,
        )

        # 6) Threat / misuse analysis
        threat = self.threat_analyzer.analyze(req.message, planned_reply, ctx)

        # 7) Policy enforcement + wrapping
        safe_reply, safety_info = self.policy_enforcer.enforce(
            message=req.message,
            reply=planned_reply,
            threat=threat,
            emotion=emo,
        )
        safe_reply = self.response_wrapper.wrap(safe_reply, safety_info)

        # 8) Update meta-awareness + memory
        self.meta_awareness.observe(req.message, safe_reply, emo, dharma_view)
        self.memory.store_interaction(req, safe_reply, emo, dharma_view)

        # 9) Evolution logging
        latency_ms = int((perf_counter() - start) * 1000)
        self.episode_logger.log_event(
            trace_id=trace_id,
            request=req,
            reply=safe_reply,
            emotion=emo,
            dharma=dharma_view,
            safety=safety_info,
            latency_ms=latency_ms,
        )

        # 10) Pack response
        resp = ChatResponse(
            reply=safe_reply,
            emotion=EmotionInfo(
                valence=emo["valence"],
                arousal=emo["arousal"],
                distress_level=emo["distress_level"],
                confidence=emo["confidence"],
            ),
            dharma=DharmaInfo(
                alignment_score=dharma_view["alignment_score"],
                principles=dharma_view.get("principles", []),
            ),
            safety=SafetyInfo(
                risk_level=safety_info["risk_level"],
                actions=safety_info.get("actions", []),
            ),
            meta=MetaInfo(
                model="upstream-llm",
                latency_ms=latency_ms,
                policy_version=safety_info.get("policy_version"),
                trace_id=trace_id,
            ),
        )

        # 11) Audit log (last step)
        self.audit_logger.log(req, resp)

        return resp
