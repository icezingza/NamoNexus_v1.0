from fastapi.testclient import TestClient
from app.api.http_server import app

client = TestClient(app)

def test_health():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chat():
    response = client.post(
        "/v1/chat",
        json={"message": "Hello", "user_id": "test_user"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["response"] == "Echo: Hello"
