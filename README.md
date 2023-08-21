# Discord Image Similarity Bot

Discord上で投稿された画像が特定のスタンプと似ているかを判定するおふざけbotです。

## アプリケーションの起動
```bash
uvicorn src.app.main:app --reload
```

## テストの実行
```bash
pytest
```

## 開発方法

### 1. 仮想環境のセットアップ

以下のコマンドで仮想環境を作成します。

```bash
# windowsの場合
py -m venv env

# macOS/Linuxの場合
python3 -m venv env
```

### 2. 仮想環境の有効化

```bash
# Windowsの場合
env\Scripts\activate

# macOS/Linuxの場合
source env/bin/activate
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

## ディレクトリ構造

```bash
src/
├── app/
│   ├── api/            - エンドポイントのコード
│   ├── logic/          - 画像処理関連のロジック関数
│   ├── main.py         - FastAPIアプリケーションのエントリポイント
│   └── config.py       - 設定情報
│
requirements.txt    - 依存関係
README.md           - このドキュメント
```
