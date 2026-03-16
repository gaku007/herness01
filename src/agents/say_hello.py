"""
sayHello Agent Module

このモジュールは、sayHelloエージェントを実装しています。
呼び出されると、ワークスペースのルートに hello_output.md ファイルを生成します。
"""

from datetime import datetime
from pathlib import Path
from typing import Optional


def say_hello(root_dir: Optional[str] = None) -> str:
    """
    sayHello エージェントの実行関数
    
    エージェント呼び出し時にトリガーし、ワークスペースのルートに
    hello_output.md ファイルを生成します。
    
    Args:
        root_dir: ファイル生成先のルートディレクトリ。
                  Noneの場合はカレントワーキングディレクトリを使用。
    
    Returns:
        実行結果メッセージ
    """
    if root_dir is None:
        root_dir = "."
    
    # ルートディレクトリのパスを設定
    root_path = Path(root_dir)
    output_file = root_path / "hello_output.md"
    
    # 現在の日時を取得
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ファイルの内容を生成
    content = f"""# Hello Output

**Time**: {current_time}
**Message**: さようなら、エージェント呼び出し完了

---
Created by: sayHello Agent
"""
    
    # ファイルを生成
    output_file.write_text(content, encoding="utf-8")
    
    return f"hello_output.md generated at {output_file.absolute()}"


if __name__ == "__main__":
    result = say_hello()
    print(result)
