from fastapi.testclient import TestClient
from app.api.gateway import app

client = TestClient(app, raise_server_exceptions=False)

def test_global_exception_handler():
    # Define a route that raises an exception
    @app.get("/force_error")
    def force_error():
        raise Exception("Forced error for testing")

    response = client.get("/force_error")

    assert response.status_code == 500
    data = response.json()
    assert data["message"] == "Internal Dharma imbalance detected."
    assert data["error"] == "Forced error for testing"
    assert data["resolution"] == "Supervisor will attempt recovery automatically."
