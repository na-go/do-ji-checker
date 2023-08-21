# Python 3.11.4をベースにする
FROM python:3.11.4

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピーして依存関係をインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# src以下のコードをコピー
COPY src/ ./src/

# uvicornでアプリを実行 (アプリの場所に応じてパスを変更)
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
