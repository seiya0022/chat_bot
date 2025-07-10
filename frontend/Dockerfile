# ベースイメージ
FROM python:3.12-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存ファイルをコピー
COPY requirements.txt .

# アプリケーションのコードをコピー
COPY . .

# 依存をインストール
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# Streamlitで起動
CMD ["streamlit", "run", "app_test.py", "--server.port=8501", "--server.address=0.0.0.0"]
