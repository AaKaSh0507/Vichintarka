"""Test the health endpoint."""

from fastapi.testclient import TestClient


def test_simple_health_endpoint(simple_client: TestClient):
    """Test the health check endpoint without database dependency."""
    response = simple_client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_simple_health_endpoint_content_type(simple_client: TestClient):
    """Test that health endpoint returns JSON."""
    response = simple_client.get("/api/health")

    assert response.headers["content-type"] == "application/json"
