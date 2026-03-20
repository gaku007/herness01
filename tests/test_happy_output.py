"""Tests for happy_output.ts file."""

import pathlib


def test_happy_output_file_exists() -> None:
    """Test that happy_output.ts file exists."""
    file_path = pathlib.Path("src/happy_output.ts")
    assert file_path.exists(), f"File {file_path} does not exist"


def test_happy_output_contains_import_react() -> None:
    """Test that happy_output.ts imports React."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "import React" in content, "React import not found in happy_output.ts"


def test_happy_output_contains_happy_app_component() -> None:
    """Test that happy_output.ts defines HappyApp component."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "HappyApp" in content, "HappyApp component not found in happy_output.ts"


def test_happy_output_contains_handle_click() -> None:
    """Test that happy_output.ts contains handleClick function."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "handleClick" in content, "handleClick function not found in happy_output.ts"


def test_happy_output_contains_happy_message() -> None:
    """Test that happy_output.ts contains the happiness message."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "幸せが届きました！" in content, (
        "Happiness message not found in happy_output.ts"
    )


def test_happy_output_contains_heart_button() -> None:
    """Test that happy_output.ts contains heart button."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "❤️" in content, "Heart button not found in happy_output.ts"


def test_happy_output_has_default_export() -> None:
    """Test that happy_output.ts exports HappyApp as default."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "export default HappyApp" in content, (
        "Default export of HappyApp not found in happy_output.ts"
    )


def test_happy_output_contains_use_state() -> None:
    """Test that happy_output.ts uses useState hook."""
    file_path = pathlib.Path("src/happy_output.ts")
    content = file_path.read_text()
    assert "useState" in content, "useState hook not found in happy_output.ts"
