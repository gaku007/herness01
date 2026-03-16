# アイドルグッズ販売ECサイト仕様書

## 1. 概要

### 1.1 目的
20代向けアイドルグッズ販売を実現する小規模ECサイトを構築する。オンライン上で商品の閲覧、購入、注文管理を可能にするプラットフォーム。

### 1.2 対象ユーザー
- 20代のアイドルファン
- スマートフォン・PCでの購入を想定

### 1.3 主要機能
- 商品カタログの閲覧
- ショッピングカート機能
- 注文管理
- 注文前の確認画面

---

## 2. APIエンドポイント定義

### 2.1 商品関連API

#### 2.1.1 商品一覧取得
```
GET /api/v1/products
```

**クエリパラメータ:**
- `page`: ページ番号（デフォルト: 1）
- `limit`: 取得件数（デフォルト: 20、最大: 100）
- `category`: カテゴリフィルタ（optional）
- `sort`: ソート順（`newest`, `price_asc`, `price_desc`、デフォルト: `newest`）

**レスポンス (200 OK):**
```json
{
  "data": [
    {
      "id": "PROD001",
      "name": "推し推し缶バッジセット",
      "description": "推し推しメンバーの推し推し缶バッジセット",
      "price": 1500,
      "image_url": "https://example.com/images/product001.jpg",
      "category": "badge",
      "stock": 50,
      "rating": 4.5
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 145
  }
}
```

---

#### 2.1.2 商品詳細取得
```
GET /api/v1/products/{product_id}
```

**レスポンス (200 OK):**
```json
{
  "id": "PROD001",
  "name": "推し推し缶バッジセット",
  "description": "推し推しメンバーの推し推し缶バッジセット",
  "price": 1500,
  "image_url": "https://example.com/images/product001.jpg",
  "images": [
    {
      "url": "https://example.com/images/product001.jpg",
      "alt": "表面画像"
    },
    {
      "url": "https://example.com/images/product001_back.jpg",
      "alt": "裏面画像"
    }
  ],
  "category": "badge",
  "stock": 50,
  "rating": 4.5,
  "review_count": 128,
  "specifications": {
    "size": "32mm",
    "material": "金属",
    "quantity": 8
  }
}
```

**エラーレスポンス (404 Not Found):**
```json
{
  "error": "Product not found",
  "error_code": "PRODUCT_NOT_FOUND"
}
```

---

### 2.2 カート関連API

#### 2.2.1 カイアイテム追加
```
POST /api/v1/cart/items
```

**リクエストボディ:**
```json
{
  "product_id": "PROD001",
  "quantity": 2
}
```

**レスポンス (201 Created):**
```json
{
  "cart_id": "CART_123456",
  "items": [
    {
      "product_id": "PROD001",
      "name": "推し推し缶バッジセット",
      "price": 1500,
      "quantity": 2,
      "subtotal": 3000
    }
  ],
  "total_items": 1,
  "total_amount": 3000,
  "tax": 300,
  "grand_total": 3300
}
```

---

#### 2.2.2 カート内容取得
```
GET /api/v1/cart
```

**リクエストヘッダ:**
- `X-Cart-ID`: カートID（またはセッションCookieから取得）

**レスポンス (200 OK):**
```json
{
  "cart_id": "CART_123456",
  "items": [
    {
      "product_id": "PROD001",
      "name": "推し推し缶バッジセット",
      "price": 1500,
      "quantity": 2,
      "subtotal": 3000
    }
  ],
  "total_items": 1,
  "total_amount": 3000,
  "tax": 300,
  "grand_total": 3300
}
```

---

#### 2.2.3 カート内容削除
```
DELETE /api/v1/cart/items/{product_id}
```

**レスポンス (200 OK):**
```json
{
  "cart_id": "CART_123456",
  "items": [],
  "total_items": 0,
  "total_amount": 0,
  "tax": 0,
  "grand_total": 0
}
```

---

### 2.3 注文関連API

#### 2.3.1 注文確定
```
POST /api/v1/orders
```

**リクエストボディ:**
```json
{
  "customer": {
    "name": "山田 太郎",
    "email": "yamada.taro@example.com",
    "phone": "09012345678"
  },
  "shipping_address": {
    "postal_code": "100-0001",
    "prefecture": "東京都",
    "city": "千代田区",
    "address": "丸の内1-1-1",
    "building": "XX ビル 5F"
  },
  "payment_method": "credit_card",
  "cart_id": "CART_123456"
}
```

**レスポンス (201 Created):**
```json
{
  "order_id": "ORD20260317001",
  "status": "pending_payment",
  "order_date": "2026-03-17T14:30:00Z",
  "customer_name": "山田 太郎",
  "items": [
    {
      "product_id": "PROD001",
      "name": "推し推し缶バッジセット",
      "price": 1500,
      "quantity": 2,
      "subtotal": 3000
    }
  ],
  "subtotal": 3000,
  "tax": 300,
  "shipping_fee": 500,
  "grand_total": 3800,
  "payment_url": "https://payment.example.com/invoice/ORD20260317001"
}
```

---

#### 2.3.2 注文履歴取得
```
GET /api/v1/orders
```

**クエリパラメータ:**
- `customer_email`: 顧客メールアドレス（必須）

**レスポンス (200 OK):**
```json
{
  "orders": [
    {
      "order_id": "ORD20260317001",
      "status": "delivered",
      "order_date": "2026-03-17T14:30:00Z",
      "items_count": 1,
      "grand_total": 3800
    },
    {
      "order_id": "ORD20260310001",
      "status": "shipped",
      "order_date": "2026-03-10T10:15:00Z",
      "items_count": 3,
      "grand_total": 12500
    }
  ]
}
```

---

#### 2.3.3 注文詳細取得
```
GET /api/v1/orders/{order_id}
```

**レスポンス (200 OK):**
```json
{
  "order_id": "ORD20260317001",
  "status": "delivered",
  "order_date": "2026-03-17T14:30:00Z",
  "customer_name": "山田 太郎",
  "customer_email": "yamada.taro@example.com",
  "shipping_address": {
    "postal_code": "100-0001",
    "prefecture": "東京都",
    "city": "千代田区",
    "address": "丸の内1-1-1",
    "building": "XX ビル 5F"
  },
  "items": [
    {
      "product_id": "PROD001",
      "name": "推し推し缶バッジセット",
      "price": 1500,
      "quantity": 2,
      "subtotal": 3000
    }
  ],
  "subtotal": 3000,
  "tax": 300,
  "shipping_fee": 500,
  "grand_total": 3800,
  "payment_status": "completed",
  "shipping_status": "delivered",
  "tracking_number": "1234567890ABCD",
  "delivered_date": "2026-03-20T15:45:00Z"
}
```

---

## 3. データモデル設計

### 3.1 Product（商品）
```sql
CREATE TABLE products (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price INTEGER NOT NULL,
  category VARCHAR(50) NOT NULL,
  stock INTEGER NOT NULL DEFAULT 0,
  image_url VARCHAR(500),
  rating DECIMAL(3,2),
  review_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  is_deleted BOOLEAN DEFAULT FALSE
);
```

### 3.2 Cart（カート）
```sql
CREATE TABLE carts (
  id VARCHAR(50) PRIMARY KEY,
  session_id VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  expires_at TIMESTAMP
);

CREATE TABLE cart_items (
  id AUTO_INCREMENT PRIMARY KEY,
  cart_id VARCHAR(50) NOT NULL,
  product_id VARCHAR(50) NOT NULL,
  quantity INTEGER NOT NULL,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (cart_id) REFERENCES carts(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### 3.3 Order（注文）
```sql
CREATE TABLE orders (
  id VARCHAR(50) PRIMARY KEY,
  order_number VARCHAR(20) UNIQUE NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(20),
  status ENUM('pending_payment', 'payment_confirmed', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending_payment',
  subtotal INTEGER NOT NULL,
  tax INTEGER NOT NULL,
  shipping_fee INTEGER NOT NULL,
  grand_total INTEGER NOT NULL,
  payment_method VARCHAR(50),
  payment_status ENUM('pending', 'completed', 'failed') DEFAULT 'pending',
  shipping_status ENUM('pending', 'picking', 'shipped', 'delivered') DEFAULT 'pending',
  tracking_number VARCHAR(100),
  postal_code VARCHAR(10),
  prefecture VARCHAR(50),
  city VARCHAR(100),
  address VARCHAR(255),
  building VARCHAR(100),
  ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  shipped_at TIMESTAMP,
  delivered_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
  id AUTO_INCREMENT PRIMARY KEY,
  order_id VARCHAR(50) NOT NULL,
  product_id VARCHAR(50) NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  price INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  subtotal INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id)
);
```

---

## 4. 実装方針

### 4.1 技術スタック
| カテゴリ | 技術・ツール |
|---------|-------------|
| バックエンド | FastAPI (Python 3.12) |
| ORM | SQLAlchemy |
| データベース | PostgreSQL |
| 認証 | JWT トークン（将来拡張） |
| テスト | pytest |
| ビルド・デプロイ | Docker |

### 4.2 プロジェクト構成
```
src/
├── api/
│   ├── routes/
│   │   ├── products.py        # 商品関連エンドポイント
│   │   ├── cart.py            # カート関連エンドポイント
│   │   └── orders.py          # 注文関連エンドポイント
│   └── dependencies.py         # 依存注入（DBセッション等）
├── models/
│   ├── product.py             # 商品モデル
│   ├── cart.py                # カートモデル
│   ├── order.py               # 注文モデル
│   └── __init__.py
├── schemas/
│   ├── product.py             # 商品スキーマ（Pydantic）
│   ├── cart.py                # カートスキーマ
│   ├── order.py               # 注文スキーマ
│   └── __init__.py
├── services/
│   ├── product_service.py     # 商品ビジネスロジック
│   ├── cart_service.py        # カート管理ロジック
│   ├── order_service.py       # 注文処理ロジック
│   └── __init__.py
├── database.py                 # DB接続設定
├── config.py                   # 環境設定
├── main.py                     # アプリケーションエントリポイント
└── __init__.py

tests/
├── test_products.py
├── test_cart.py
├── test_orders.py
└── conftest.py

docs/
└── design/
    └── ec-site-specification.md (このファイル)
```

### 4.3 開発フェーズ

#### フェーズ 1: 基本API実装（Week 1-2）
- [ ] FastAPI プロジェクト初期化
- [ ] Product API の実装（GET一覧、詳細取得）
- [ ] 基本的なテスト実装
- [ ] Linting と型チェック

#### フェーズ 2: カート・注文機能（Week 3-4）
- [ ] Cart API の実装
- [ ] Order API の実装（確定、履歴取得、詳細取得）
- [ ] トランザクション処理の実装
- [ ] エラーハンドリング

#### フェーズ 3: 拡張・最適化（Week 5-6）
- [ ] 認証機能の追加（JWT）
- [ ] ページング・キャッシング最適化
- [ ] フロントエンド統合テスト
- [ ] パフォーマンス最適化

### 4.4 使用外部サービス（予定）
- **決済システム**: Stripe / PayPal（将来統合）
- **送料自動計算**: ヤマト運輸等の連携API（将来統合）

### 4.5 HTTP ステータスコード規約
| ステータス | 用途 |
|-----------|------|
| 200 | 成功（GET, PUT, PATCH） |
| 201 | 作成成功（POST） |
| 204 | 削除成功 |
| 400 | バリデーションエラー |
| 401 | 認証エラー |
| 403 | 権限なし |
| 404 | リソース不在 |
| 409 | 在庫不足等の競合 |
| 500 | サーバーエラー |

### 4.6 セキュリティ対策
- CORS設定（フロントエンドオリジン指定）
- CSRF トークン実装
- SQL インジェクション対策（SQLAlchemy ORM 使用）
- レート制限実装（APIGateway またはミドルウェア）
- 入力バリデーション（Pydantic スキーマ）

---

## 5. 受け入れ基準

このドキュメントが以下の条件を満たしたとき、仕様書完成とする：

- [x] ECサイトの仕様書がmarkdownファイルで出力されています
- [x] APIエンドポイント定義が記載されています
- [x] データモデル設計が記載されています
- [x] 技術スタック等の実装方針が明確です

---

## 6. 補足

### 6.1 将来の拡張機能
- ウィッシュリスト機能
- レビュー・レーティング機能
- マイページ機能（注文管理、プロフィール編集）
- 在庫最適化ロジック
- メール通知機能（注文確認、発送通知等）
- CMS 管理画面（商品マスタ管理）

### 6.2 本ドキュメント更新ポリシー
- API仕様の変更は必ずドキュメント更新を伴う
- マイナーアップデートは月1回レビュー予定
