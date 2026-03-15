"""
test_hello.py - Hello World テストスイート
"""

import subprocess


def test_hello_world_output() -> None:
    """
    hello.js を実行して、標準出力に "Hello World" が含まれていることを確認
    """
    result = subprocess.run(
        ["node", "dist/hello.js"], capture_output=True, text=True, timeout=5
    )
    assert result.returncode == 0, f"Process failed with code {result.returncode}"
    assert "Hello World" in result.stdout, (
        f"Expected 'Hello World' in output, got: {result.stdout}"
    )


def test_hello_world_exact_output() -> None:
    """
    hello.js を実行して、標準出力が正確に "Hello World\n" であることを確認
    """
    result = subprocess.run(
        ["node", "dist/hello.js"], capture_output=True, text=True, timeout=5
    )
    assert result.returncode == 0, f"Process failed with code {result.returncode}"
    assert result.stdout.strip() == "Hello World", (
        f"Expected 'Hello World', got: {result.stdout!r}"
    )
