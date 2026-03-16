"""Tests for SayHelloAgent."""

import sys
from pathlib import Path
import tempfile

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents import SayHelloAgent


def test_say_hello_agent_creates_file() -> None:
    """Test that SayHelloAgent creates hello_output.md file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        agent = SayHelloAgent(output_dir=Path(tmpdir))
        output_file = agent.run()

        assert output_file.exists(), "hello_output.mdファイルが生成されていません"
        assert output_file.name == "hello_output.md"


def test_say_hello_agent_file_content() -> None:
    """Test that the generated file has correct content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        agent = SayHelloAgent(output_dir=Path(tmpdir))
        output_file = agent.run()

        content = output_file.read_text()
        assert "# Hello Output" in content
        assert "**Time**:" in content
        assert "さようなら、エージェント呼び出し完了" in content
        assert "Created by: sayHello Agent" in content


def test_say_hello_agent_root_file() -> None:
    """Test that SayHelloAgent creates file in project root when no dir specified."""
    agent = SayHelloAgent()
    # Verify the output directory is set to project root
    assert agent.output_dir.name == "herness01" or agent.output_dir.parent.name == "herness01"
