
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


def test_summarize_handles_non_iterable_entries():
    engine = RetrievalEngine()
    summary = engine.summarize(None)
    assert summary == "No prior reflections recorded."


def test_summarize_handles_mixed_shapes():
    engine = RetrievalEngine()
    entries = [
        {"reflection": ["direct string", {"reflection": {"reflection": "deep"}}]},
        "not a dict",
        {"reflection": {"reflection": 123}},
    ]
    summary = engine.summarize(entries)
    assert "direct string" in summary or "deep" in summary


if __name__ == "__main__":
    test_fix_type_error()
