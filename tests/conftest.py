"""Test configuration and fixtures for Vichintarka."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture
def test_user_data():
    """Sample user data for testing."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
    }


@pytest.fixture
def simple_client():
    """Create a test client for simple health checks without database dependency."""
    from fastapi import APIRouter, FastAPI

    simple_app = FastAPI(title="Test API")
    simple_router = APIRouter()

    @simple_router.get("/health")
    async def simple_health():
        return {"status": "ok"}

    simple_app.include_router(simple_router, prefix="/api")

    return TestClient(simple_app)
