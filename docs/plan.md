# Current task plan - Issue #14: sayHello Agent

## Goal
sayHelloカスタムエージェントを呼び出し、ワークスペースルートに`hello_output.md`ファイルを生成する機能を実装

## Implementation Details
1. `src/agents/say_hello.py`: sayHello エージェントのメイン実装
   - エージェント呼び出し時にトリガー
   - ルートディレクトリに `hello_output.md` を生成
   - ファイルに現在の日時と挨拶メッセージを記録
2. `tests/test_say_hello.py`: エージェント機能のテスト
   - ファイル生成確認
   - ファイル内容確認

## Files to change
- src/agents/__init__.py (新規/更新)
- src/agents/say_hello.py (新規)
- tests/test_say_hello.py (新規)

## Risks
- 既存レスポンス形式を変えない
- 既存テストを壊さない
- ルートに意図しないファイルを生成しない