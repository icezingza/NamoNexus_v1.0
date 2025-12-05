from namo_nexus.cog.dharma_engine import DharmaEngine

def test_dharma_engine_stub():
    engine = DharmaEngine()
    context = {"user_id": "test_user"}

    # Test with metta principle
    result_metta = engine.apply_dharma("message", ["เมตตา"], context)
    assert result_metta["alignment_score"] == 0.9
    assert "เมตตา" in result_metta["principles"]

    # Test without metta
    result_other = engine.apply_dharma("message", ["other"], context)
    assert result_other["alignment_score"] == 0.7
