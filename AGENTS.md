# AGENTS.md

## Goal
このリポジトリは、FastAPIベースのAPIを開発するためのもの。

## Allowed changes
- `src/`, `tests/`, `docs/` のみ編集可
- 依存追加が必要なら理由をPR本文に記載
- 秘密情報や認証情報は絶対にコミットしない

## Coding rules
- Python 3.12
- Ruffでlint
- pytestでテスト
- 型ヒント必須
- 1機能追加ごとに最低1テスト追加

## Workflow
1. Issueを読む
2. issue内容から専用branchを作成し、専用branchにswitchする
3. 実装前に変更方針を `docs/plan.md` に短く書く
4. 実装
5. テスト実行
6. 失敗したら修正
7. 必要最低限のファイルだけpushするために.gitignoreを編集
8. PRを作成し発行
9. 元のbranchに戻る

## Constraints
- 既存の公開APIを壊さない
- 大規模リファクタは別Issueに分離
- 1PR 1目的を守る

## Done definition
- テスト通過
- lint通過
- 型チェック通過
- 変更理由が説明できる
- 作生物のサマリを日本語でレポート