# makeHappy Agent

## Overview
このエージェントは、TypeScriptで小さな幸せを届けるWebアプリを作成します

## Purpose
`makeHappy` コマンドが実行されると、Webアプリの基本的な構造を持つ `happy_output.ts` ファイルを生成し、現在の日時と挨拶メッセージを記録します。そして、ユーザがハートをクリックすると、画面に「幸せが届きました！」と表示されるようにします。

## Behavior
1. エージェントが呼び出されるとトリガーします
2. `docs/happy_output.ts` ファイルを作成します
3. ファイルには現在の日時と挨拶メッセージを記録します
4. Webアプリの基本的な構造を持ち、ユーザがハートをクリックすると「幸せが届きました！」と表示されるようにします
5. 実行方法をREADME.mdに記載します
6. 変更内容をサマリとしてレポートします。settings.jsonの発動有無に関わらずレポートします。

## Output File Format
ファイルパス: `/src/happy_output.ts`
ファイル内容:
```typescript
import React, { useState } from 'react';

const HappyApp: React.FC = () => {
  const [message, setMessage] = useState('');

  const handleClick = () => {
    setMessage('幸せが届きました！');
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>こんにちは！</h1>
      <p>現在の日時: {new Date().toLocaleString()}</p>
      <button onClick={handleClick} style={{ fontSize: '24px', padding: '10px 20px' }}>
        ❤️
      </button>
      {message && <p style={{ marginTop: '20px', fontSize: '18px' }}>{message}</p>}
    </div>
  );
};

## Usage
```bash
# このエージェントの実行
makeHappy
```

## Files Modified
- Creates: `happy_output.ts` (プロジェクトルート)
