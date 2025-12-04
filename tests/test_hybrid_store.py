import pytest
from namo_nexus.api.schemas import ChatRequest
from namo_nexus.memory.hybrid_store import HybridMemoryStore

def test_hybrid_store_operations():
    store = HybridMemoryStore()

    # Create a request
    req = ChatRequest(user_id="user123", session_id="sessABC", message="Hello world")

    # Store interaction
    emotion = {"happiness": 0.8}
    dharma = {"insight": "impermanence"}
    reply = "Hello there!"

    store.store_interaction(req, reply, emotion, dharma)

    # Retrieve
    results = store.retrieve(query="hello", user_id="user123", k=1, weights={})

    assert len(results) == 1
    item = results[0]
    assert item["user_id"] == "user123"
    assert item["text"] == "Hello world"
    assert item["reply"] == "Hello there!"
    assert item["emotion"] == emotion
    assert item["dharma"] == dharma

def test_retrieve_filtering():
    store = HybridMemoryStore()

    req1 = ChatRequest(user_id="user1", session_id="s1", message="Hi 1")
    req2 = ChatRequest(user_id="user2", session_id="s2", message="Hi 2")

    store.store_interaction(req1, "Reply 1", {}, {})
    store.store_interaction(req2, "Reply 2", {}, {})

    # Retrieve for user1
    results = store.retrieve("query", user_id="user1", k=5, weights={})
    assert len(results) == 1
    assert results[0]["user_id"] == "user1"

    # Retrieve for user2
    results = store.retrieve("query", user_id="user2", k=5, weights={})
    assert len(results) == 1
    assert results[0]["user_id"] == "user2"
