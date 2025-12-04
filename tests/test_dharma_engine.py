from namo_nexus.cog.dharma_engine import DharmaEngine

def test_apply_dharma_metta():
    engine = DharmaEngine()
    message = "Hello"
    principles = ["เมตตา", "wisdom"]
    context = {}

    result = engine.apply_dharma(message, principles, context)

    assert result["alignment_score"] == 0.9
    assert result["principles"] == principles

def test_apply_dharma_no_metta():
    engine = DharmaEngine()
    message = "Hello"
    principles = ["wisdom"]
    context = {}

    result = engine.apply_dharma(message, principles, context)

    assert result["alignment_score"] == 0.7
    assert result["principles"] == principles
