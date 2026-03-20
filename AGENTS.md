# AGENTS.md

## Goal
このリポジトリは、React TypeScriptでWebアプリケーションを開発するためのもの。

## Allowed changes
- `src/`, `tests/`, `docs/` のみ編集可
- 依存追加が必要なら理由をPR本文に記載
- 秘密情報や認証情報は絶対にコミットしない

## Coding rules
- TypeScript 5.x
- Biomeでlint・format
- React 18.x（FC型、hooks推奨）
- 型ヒント必須
- 1機能追加ごとに最低1テスト追加

## Workflows

### Workflow 1: 実装優先型（Execution-First）
Issue から直接実装へ進むフロー（小規模機能向け）

1. Issueを読む
2. issue内容から専用branchを作成し、専用branchにswitchする
3. 実装前に変更方針を `docs/plan.md` に短く書く
4. 実装
5. テスト実行
6. 失敗したら修正
7. 必要最低限のファイルだけpushするために.gitignoreを編集
8. PRを作成し発行
9. 元のbranchに戻る

### Workflow 2: 仕様書優先型（Design-First）
仕様書作成 → PR発行のフロー（複雑な機能・API設計の仕様策定向け）

1. Issueを読む
2. issue内容から専用branchを作成し、専用branchにswitchする
3. 仕様書を `docs/design/` に作成
   - APIエンドポイント定義
   - データモデル設計
   - 実装方針
4. 必要最低限のファイルだけpushするために.gitignoreを編集
5. PRを作成し発行（ドラフトまたはレビュー用）
6. 元のbranchに戻る

## Workflow Selection Guide（使い分けガイド）

### Workflow 1 を選ぶべき場合
- UI修正、バグ修正などの小規模変更
- 既存機能への追加・拡張（大きな設計変更がない）
- 実装内容が明確に決まっている

### Workflow 2 を選ぶべき場合
- 新しいAPIエンドポイント追加
- データベーススキーマの大きな変更
- マイクロサービスの連携設計
- パフォーマンスに関わる実装
- 複数チームに影響する変更

## Constraints
- 日本語で応答
- 既存の公開APIを壊さない
- 大規模リファクタは別Issueに分離
- 1PR 1目的を守る

## Done definition
- テスト通過
- lint通過
- 型チェック通過
- 変更理由が説明できる
- 作生物のサマリをレポート