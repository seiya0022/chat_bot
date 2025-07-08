# ベースイメージ
FROM python:3.12-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存ファイルをコピー
COPY requirements.txt .

# 依存をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# Streamlitで起動
CMD ["python", "chatbot_app.py"]
