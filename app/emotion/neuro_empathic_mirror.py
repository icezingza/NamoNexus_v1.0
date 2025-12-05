import hashlib
import logging
import os
import psutil
from importlib.util import find_spec
from typing import Dict, List
from dataclasses import dataclass

logger = logging.getLogger(__name__)

HAS_TRANSFORMERS = find_spec("transformers") is not None
if HAS_TRANSFORMERS:
    try:
        from transformers import pipeline
    except Exception:
        HAS_TRANSFORMERS = False
        logger.warning(
            "Transformers library detected but pipeline import failed. Running in simulation mode."
        )

@dataclass
class EmpathicResponse:
    """Data structure for the empathic response output."""
    response_text: str
    emotional_matching_score: float
    support_level: str

class NeuroEmpathicMirror:
    """
    Advanced emotion processing unit using Neural Networks (Transformers).
    It acts as a mirror, reflecting the user's deep emotional state with empathy.
    """

    def __init__(self):
        self.analyzer = self._init_model()
        self.empathy_templates = self._load_templates()
        logger.info("Neuro-Empathic Mirror initialized.")

    def _init_model(self):
        """
        Initializes the Hugging Face emotion classification pipeline.
        Uses a DistilBERT model optimized for emotion detection.
        """
        if not HAS_TRANSFORMERS:
            logger.warning("Transformers library not found. Running in simulation mode.")
            return None

        if os.getenv("NAMO_EMOTION_SIM_MODE", "").lower() in {"1", "true", "yes"}:
            logger.warning("Emotion model load skipped via NAMO_EMOTION_SIM_MODE; running in simulation mode.")
            return None

        # Avoid loading the model on constrained machines to prevent crashes.
        if psutil.virtual_memory().available < 2_000_000_000:
            logger.warning("Emotion model load skipped due to low available memory; running in simulation mode.")
            return None
        
        try:
            # Using a robust, lightweight model for emotion detection
            # You can swap this with 'airesearch/wangchanberta...' for Thai-specific optimization
            return pipeline(
                "text-classification", 
                model="bhadresh-savani/distilbert-base-uncased-emotion", 
                top_k=None
            )
        except Exception as e:
            logger.error(f"Failed to load emotion model: {e}")
            return None

    def _load_templates(self) -> Dict[str, List[str]]:
        """Loads empathetic response templates from policies.json."""
        try:
            from pathlib import Path
            import json
            base_dir = Path(__file__).resolve().parent.parent # app/
            policy_path = base_dir / "core" / "policies.json"
            
            with open(policy_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("empathy_templates", {})
        except Exception as e:
            logger.error(f"Failed to load policies.json: {e}")
            return {"joy": ["I am happy for you."]}

    def analyze_emotion_depth(self, text: str) -> Dict[str, float]:
        """
        Analyzes text to extract a 5-dimensional emotional vector.
        Returns a dictionary of {emotion: score}.
        """
        # Default neutral state
        default_state = {'joy': 0.1, 'sadness': 0.1, 'anger': 0.1, 'fear': 0.1, 'love': 0.1}
        
        if self.analyzer:
            try:
                results = self.analyzer(text)[0]
                # Normalize scores to dictionary format
                scores = {item['label']: item['score'] for item in results}
                return {**default_state, **scores}
            except Exception as e:
                logger.error(f"Analysis failed: {e}")
                pass
        
        # Fallback simulation logic (Keyword based) if model fails
        text_lower = text.lower()
        if 'happy' in text_lower or 'good' in text_lower:
            default_state['joy'] = 0.8
        if 'sad' in text_lower or 'bad' in text_lower:
            default_state['sadness'] = 0.8
        if 'angry' in text_lower or 'hate' in text_lower:
            default_state['anger'] = 0.8
        if 'afraid' in text_lower or 'scared' in text_lower or 'fear' in text_lower:
            default_state['fear'] = 0.8
        if 'love' in text_lower or 'loved' in text_lower or 'caring' in text_lower:
            default_state['love'] = 0.8
        
        return default_state

    def _select_template(self, templates: List[str], user_text: str) -> str:
        """Selects a deterministic template based on user input to avoid randomness."""
        if not templates:
            return "I am listening deeply."

        digest = hashlib.sha256(user_text.encode("utf-8")).digest()
        index = int.from_bytes(digest[:2], byteorder="big") % len(templates)
        return templates[index]

    def reflect(self, user_text: str) -> EmpathicResponse:
        """
        Main processing loop: Analyzes input and generates a mirrored response.
        """
        emotions = self.analyze_emotion_depth(user_text)
        
        # Identify dominant emotion
        primary_emotion = max(emotions, key=emotions.get)
        intensity = emotions[primary_emotion]
        
        # Select appropriate response template
        templates = self.empathy_templates.get(primary_emotion, ["I am listening deeply."])
        selected_response = self._select_template(templates, user_text)
        
        # Determine support level based on intensity
        support_level = "High" if intensity > 0.7 else "Medium"
        
        return EmpathicResponse(
            response_text=f"{selected_response}",
            emotional_matching_score=intensity,
            support_level=support_level
        )
