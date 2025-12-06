"""Minimal API tests for health and reflect endpoints."""
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_endpoint_returns_ok():
    # The application exposes /healthz and /api/status, but not /health
    response = client.get("/healthz")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload.get("status"), str)
    assert payload["status"] == "alive"


def test_reflect_endpoint_basic():
    response = client.post("/reflect", json={"text": "I feel calm and open today."})
    assert response.status_code == 200
    payload = response.json()
    assert "reflection_text" in payload
    assert "tone" in payload
