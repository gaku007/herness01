# sayHello Agent

## Overview
このエージェントは、呼び出された際にルートディレクトリに出力ファイルを作成します。

## Purpose
`sayHello` コマンドが実行されると、タイムスタンプ付きの挨拶メッセージをファイルとして出力します。

## Behavior
1. エージェントが呼び出されるとトリガーします
2. ワークスペースのルートに `hello_output.md` ファイルを作成します
3. ファイルには現在の日時と挨拶メッセージを記録します

## Output File Format
ファイルパス: `/root/hello_output.md`

ファイル内容:
```markdown
# Hello Output

**Time**: [実行時刻]
**Message**: さようなら、エージェント呼び出し完了

---
Created by: sayHello Agent
```

## Usage
```bash
# このエージェントの実行
sayHello
```

## Files Modified
- Creates: `hello_output.md` (プロジェクトルート)
