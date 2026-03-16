import subprocess
from pathlib import Path


def test_sayhello_creates_output_file() -> None:
    """Test that sayHello agent creates hello_output.md file"""
    # Get project root
    project_root: Path = Path(__file__).parent.parent
    output_file: Path = project_root / "hello_output.md"

    # Remove the file if it exists from previous runs
    if output_file.exists():
        output_file.unlink()

    # Run the sayHello script
    script_path: Path = project_root / "scripts" / "sayHello.sh"
    result: subprocess.CompletedProcess[str] = subprocess.run(
        ["bash", str(script_path)],
        cwd=str(project_root),
        capture_output=True,
        text=True,
    )

    # Check that script executed successfully
    assert result.returncode == 0, f"Script failed: {result.stderr}"

    # Check that the file was created
    assert output_file.exists(), f"hello_output.md was not created at {output_file}"


def test_sayhello_file_format() -> None:
    """Test that hello_output.md has the correct format"""
    project_root: Path = Path(__file__).parent.parent
    output_file: Path = project_root / "hello_output.md"

    # The file should exist from the previous test
    assert output_file.exists(), f"hello_output.md does not exist at {output_file}"

    # Read the file
    content: str = output_file.read_text()

    # Check required content
    assert "# Hello Output" in content, "Missing heading"
    assert "**Time**:" in content, "Missing Time field"
    assert "**Message**:" in content, "Missing Message field"
    assert "さようなら、エージェント呼び出し完了" in content, "Missing message text"
    assert "Created by: sayHello Agent" in content, "Missing creator info"


def test_sayhello_executes_without_error() -> None:
    """Test that the sayHello script executes without errors"""
    project_root: Path = Path(__file__).parent.parent
    script_path: Path = project_root / "scripts" / "sayHello.sh"

    result: subprocess.CompletedProcess[str] = subprocess.run(
        ["bash", str(script_path)],
        cwd=str(project_root),
        capture_output=True,
        text=True,
    )

    # Check successful execution
    assert result.returncode == 0, f"Script failed with exit code {result.returncode}"
    assert "sayHello agent executed successfully" in result.stdout, (
        f"Expected success message not found. Output: {result.stdout}"
    )
