# Emotional Dynamics

The emotional engine centers on `TransformerEmotionModel`, which tracks five dimensions: joy, sadness, anger, calm, and compassion.

- **EmotionAnalyzer** (`app/emotion/analyzer.py`): tokenizes incoming text and derives stimuli adjustments.
- **TransformerEmotionModel** (`app/emotion/transformer_emotion_model.py`): updates internal state with bounded increments and computes coherence as 1 minus the state spread.
- **DhammicReflectionEngine** (`app/personality/dhammic_reflection_engine.py`): translates emotional state into tone and moral index before crafting a response.

Coherence scores guide downstream tone selection and memory reflections, encouraging balanced responses rooted in compassion.
