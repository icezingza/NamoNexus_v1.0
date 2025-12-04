import pytest
from namo_nexus.cog.meta_awareness import MetaAwareness

def test_meta_awareness_initialization():
    ma = MetaAwareness()
    assert ma._counter == 0

def test_meta_awareness_observe():
    ma = MetaAwareness()
    ma.observe(
        message="Hello",
        reply="Hi there",
        emotion={"happy": 0.8},
        dharma={"insight": "impermanence"}
    )
    assert ma._counter == 1

    ma.observe(
        message="How are you?",
        reply="I am fine",
        emotion={"neutral": 0.9},
        dharma={"insight": "suffering"}
    )
    assert ma._counter == 2
