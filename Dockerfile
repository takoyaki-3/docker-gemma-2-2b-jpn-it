# ベースイメージの指定
FROM python:3.12

# 作業ディレクトリの作成と設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# 必要なパッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .

# コンテナ起動時のコマンドを指定
CMD ["python", "app.py"]
