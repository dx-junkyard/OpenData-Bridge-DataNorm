# ベースイメージを指定（Node.js 18を含むイメージ）
FROM node:18

# Python 3.11のインストール
RUN apt-get update && apt-get install -y python3.11 python3-pip python3.11-venv

# 作業ディレクトリの設定
WORKDIR /app

RUN python3.11 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# アプリケーションのコードをコピー（あなたのプロジェクトに合わせて変更してください）
COPY . /app

RUN pip install -r requirements.txt

# デジタル庁のジオコーディングのリポジトリをクローン
RUN git clone https://github.com/digital-go-jp/abr-geocoder.git
# クローンしたリポジトリのディレクトリに移動し、そこで依存関係をインストール
WORKDIR /app/abr-geocoder
RUN npm install -g @digital-go-jp/abr-geocoder

RUN abrg download
COPY . /app

# 作業ディレクトリを戻す
WORKDIR /app

# TODO
# CMDでabrgを動かす（初回だけ遅い）

CMD ["python3", "function_app.py"]
