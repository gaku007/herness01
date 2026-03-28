from pathlib import Path


def test_happy_output_file_exists():
    """happy_output.ts ファイルが作成されていることをテスト"""
    happy_file = Path(__file__).parent.parent / "src" / "happy_output.ts"
    assert happy_file.exists(), "happy_output.ts が存在しません"


def test_happy_output_contains_component():
    """happy_output.ts が React コンポーネントを含むことをテスト"""
    happy_file = Path(__file__).parent.parent / "src" / "happy_output.ts"
    with open(happy_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "HappyApp" in content, "HappyApp コンポーネントが見つかりません"
    assert "useState" in content, "useState フックが見つかりません"
    assert "handleClick" in content, "handleClick 関数が見つかりません"


def test_happy_output_contains_message():
    """happy_output.ts が幸せメッセージを含むことをテスト"""
    happy_file = Path(__file__).parent.parent / "src" / "happy_output.ts"
    with open(happy_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "幸せが届きました！" in content, "幸せメッセージが見つかりません"
    assert "こんにちは！" in content, "挨拶メッセージが見つかりません"
    assert "❤️" in content, "ハートボタンが見つかりません"


def test_happy_output_contains_datetime():
    """happy_output.ts が現在の日時を表示することをテスト"""
    happy_file = Path(__file__).parent.parent / "src" / "happy_output.ts"
    with open(happy_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "toLocaleString()" in content, "日時フォーマット関数が見つかりません"
    assert "new Date()" in content, "日時取得が見つかりません"
