
from app.memory.retrieval_engine import RetrievalEngine

def test_fix_type_error():
    # Simulate the structure saved by NamoPersonaCore and MemoryStore

    # Dict returned by DhammicReflectionEngine.reflect
    dhammic_reflection = {
        "tone": "compassionate",
        "moral_index": 0.8,
        "reflection": "With a compassionate spirit, I hear: hello",
        "coherence": 0.9
    }

    # Dict created in NamoPersonaCore.process
    memory_entry = {
        "input": "hello",
        "reflection": dhammic_reflection,
        "emotion": {"joy": 0.5}
    }

    # Dict created in MemoryStore.save_reflection
    stored_entry = {
        "timestamp": "2024-01-01T00:00:00",
        "reflection": memory_entry
    }

    entries = [stored_entry]

    engine = RetrievalEngine()
    try:
        summary = engine.summarize(entries)
        print(f"Summary: {summary}")
        assert "With a compassionate spirit, I hear: hello" in summary
    except TypeError as e:
         raise AssertionError(f"Caught TypeError: {e}")

if __name__ == "__main__":
    test_fix_type_error()
