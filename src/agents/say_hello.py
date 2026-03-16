"""SayHello agent implementation."""

from datetime import datetime
from pathlib import Path
from typing import Optional


class SayHelloAgent:
    """Custom agent that creates a hello output file in the project root."""

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """Initialize the SayHelloAgent.

        Args:
            output_dir: Directory to output the file. Defaults to project root.
        """
        self.output_dir: Path = output_dir or Path(__file__).parent.parent.parent
        self.output_file: Path = self.output_dir / "hello_output.md"

    def run(self) -> Path:
        """Execute the agent and create hello output file.

        Returns:
            Path to the created output file.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content = f"""# Hello Output

**Time**: {current_time}
**Message**: さようなら、エージェント呼び出し完了

---
Created by: sayHello Agent
"""

        self.output_file.write_text(content)
        return self.output_file
