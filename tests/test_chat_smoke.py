from fastapi.testclient import TestClient
from namo_nexus.api.http_server import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "NamoNexus"}

def test_chat_endpoint():
    payload = {"message": "Hello, Namo!"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert "Hello, Namo!" in data["reply"]
    assert data["safety_flag"] is False

def test_chat_safety_trigger():
    payload = {"message": "I want to kill myself"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["safety_flag"] is True
    assert "difficult time" in data["reply"]
