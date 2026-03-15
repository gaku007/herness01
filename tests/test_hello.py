"""Tests for hello world functionality."""

from src.hello import hello_world


class TestHelloWorld:
    """Test cases for hello_world function."""

    def test_hello_world_returns_greeting(self) -> None:
        """Test that hello_world returns the expected greeting."""
        result = hello_world()
        assert result == "Hello World"

    def test_hello_world_is_string(self) -> None:
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)
