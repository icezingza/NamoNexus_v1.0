"""Minimal API tests for health and reflect endpoints without external clients."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import sitecustomize  # noqa: F401
from fastapi import HTTPException

from app.api.gateway import ReflectionRequest, create_app


class DummyResponse:
    def __init__(self, status_code: int, data):
        self.status_code = status_code
        self._data = data

    def json(self):
        return self._data


class DummyClient:
    def __init__(self):
        self.app = create_app()

    def _find_route(self, path: str, method: str):
        for route in self.app.router.routes:
            if getattr(route, "path", None) == path and method in getattr(route, "methods", set()):
                return route
        raise AssertionError(f"Route {method} {path} not found")

    def get(self, path: str) -> DummyResponse:
        route = self._find_route(path, "GET")
        try:
            result = route.endpoint()
            return DummyResponse(200, result)
        except HTTPException as exc:  # pragma: no cover
            return DummyResponse(exc.status_code, exc.detail)

    def post(self, path: str, json: dict | None = None) -> DummyResponse:
        route = self._find_route(path, "POST")
        payload = json or {}
        try:
            request = ReflectionRequest(**payload)
            result = route.endpoint(request)
            return DummyResponse(200, result)
        except HTTPException as exc:
            return DummyResponse(exc.status_code, exc.detail)


client = DummyClient()


def test_health_endpoint_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload.get("status"), str)
    assert payload["status"]


def test_reflect_endpoint_basic():
    response = client.post("/reflect", json={"text": "I feel calm and open today."})
    assert response.status_code == 200
    payload = response.json()
    assert "reflection_text" in payload
    assert "tone" in payload
