"""Tests for hello module."""

from src.hello import main


def test_main_prints_hello_world(capsys: object) -> None:
    """Test that main() prints Hello World."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
