from namo_nexus.cog.deep_wisdom import DeepWisdom

def test_deep_wisdom_initialization():
    dw = DeepWisdom()
    assert dw._principles == [
        "อนิจจัง",
        "ทุกข์",
        "อนัตตา",
        "เมตตา",
        "กรุณา",
    ]

def test_get_relevant_principles():
    dw = DeepWisdom()
    message = "I feel sad"
    context = {}
    principles = dw.get_relevant_principles(message, context)
    assert principles == ["เมตตา", "เห็นทุกข์", "ไม่โทษตัวเอง"]
