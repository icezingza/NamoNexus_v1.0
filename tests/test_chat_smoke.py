from fastapi.testclient import TestClient
from namo_nexus.api.http_server import app

client = TestClient(app)

def test_chat_smoke():
    response = client.post("/reflect", json={"text": "I feel happy"})
    assert response.status_code == 200
    data = response.json()
    assert "reflection_text" in data
    assert "tone" in data
