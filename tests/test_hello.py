"""Tests for hello module."""

from src.hello import hello


def test_hello_returns_correct_message() -> None:
    """Test that hello function returns 'Hello World'."""
    result = hello()
    assert result == "Hello World", f"Expected 'Hello World', got '{result}'"


def test_hello_is_string() -> None:
    """Test that hello function returns a string."""
    result = hello()
    assert isinstance(result, str), f"Expected str, got {type(result)}"
