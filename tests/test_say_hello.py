"""
Tests for sayHello Agent

sayHello エージェントのテストモジュール
"""

import tempfile
from pathlib import Path

import pytest

from src.agents import say_hello


class TestSayHello:
    """sayHello エージェントのテストクラス"""
    
    def test_say_hello_creates_file(self) -> None:
        """
        say_hello が指定ディレクトリに hello_output.md を生成することを確認
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            result = say_hello(root_dir=tmpdir)
            
            # ファイルが生成されていることを確認
            output_file = Path(tmpdir) / "hello_output.md"
            assert output_file.exists(), "hello_output.md ファイルが生成されていません"
            
            # 結果メッセージが返されていることを確認
            assert "hello_output.md generated" in result
            assert str(output_file) in result
    
    def test_say_hello_file_content(self) -> None:
        """
        生成されたファイルの内容が正しいことを確認
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            say_hello(root_dir=tmpdir)
            
            output_file = Path(tmpdir) / "hello_output.md"
            content = output_file.read_text(encoding="utf-8")
            
            # ファイル内容に必要な要素が含まれていることを確認
            assert "# Hello Output" in content
            assert "**Time**:" in content
            assert "**Message**: さようなら、エージェント呼び出し完了" in content
            assert "Created by: sayHello Agent" in content
    
    def test_say_hello_file_has_timestamp(self) -> None:
        """
        生成されたファイルにタイムスタンプが含まれていることを確認
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            say_hello(root_dir=tmpdir)
            
            output_file = Path(tmpdir) / "hello_output.md"
            content = output_file.read_text(encoding="utf-8")
            
            # タイムスタンプが含まれていることを確認（YYYY-MM-DD HH:MM:SS形式）
            import re
            timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
            assert re.search(timestamp_pattern, content), "タイムスタンプが見つかりません"
    
    def test_say_hello_default_dir(self) -> None:
        """
        say_hello が引数なしで呼び出された場合、カレントディレクトリに生成されることを確認
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # 一時ディレクトリをカレントディレクトリにして実行
            import os
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                result = say_hello()
                
                # ファイルが生成されていることを確認
                output_file = Path(tmpdir) / "hello_output.md"
                assert output_file.exists(), "hello_output.md ファイルが生成されていません"
                assert "hello_output.md generated" in result
            finally:
                os.chdir(original_cwd)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
