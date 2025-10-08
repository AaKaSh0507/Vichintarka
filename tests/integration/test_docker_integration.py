"""Integration tests for the Docker environment."""

import time

import pytest
import requests


@pytest.fixture(scope="session")
def app_url():
    """Return the application URL."""
    return "http://localhost:8000"


def test_app_is_running(app_url):
    """Test that the application is running and accessible."""
    # Wait a bit for the app to start
    time.sleep(2)

    try:
        response = requests.get(f"{app_url}/api/health", timeout=10)
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    except requests.ConnectionError:
        pytest.skip("Application is not running - integration test skipped")


def test_app_docs_accessible(app_url):
    """Test that the API documentation is accessible."""
    try:
        response = requests.get(f"{app_url}/docs", timeout=10)
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
    except requests.ConnectionError:
        pytest.skip("Application is not running - integration test skipped")
