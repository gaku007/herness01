"""Tests for main.py."""
from fastapi.testclient import TestClient
from src.main import app


def test_hello_world() -> None:
    """Test the hello_world endpoint returns Hello World."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    # Verify the output contains "Hello World"
    assert "Hello World" in response.text
