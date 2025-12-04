# tests/test_chat_smoke.py
from fastapi.testclient import TestClient
from app.api.gateway import app


client = TestClient(app)


def test_chat_smoke():
    payload = {
        "user_id": "test-user",
        "session_id": "sess-1",
        "message": "ผมรู้สึกหมดหวังและไม่อยากอยู่แล้ว",
        "locale": "th-TH",
    }
    resp = client.post("/v1/chat", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "reply" in data
    assert "emotion" in data
    assert "dharma" in data
    assert "safety" in data
