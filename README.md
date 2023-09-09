# OpenData-Bridge-DataNorm

## 都知事杯 OpenDataHackathon 2023   

## 概要

OpenData Bridgeの検索で取得した様々なフォーマットのcsvファイルを一つのフォーマットに変換&結合するためのPythonコードと、変換定義(json)をChatGPTで生成するための方法を提示します。


##  バラバラのデータを統合する手順
1. ソースコードを取得(git clone)
2. 統合対象のcsvを配置
3. 変換定義のmapping_rules.json作成(prompt_creator & ChatGPT)
4. データ変換＆結合(datanorm.py)


## 実行方法
### 1. ソースコードを取得
変換定義を作り出すChatGPT用のプロンプト生成と、データ変換を行うpythonコードを入手する。
```
git clone https://github.com/dx-junkyard/OpenData-Bridge-DataNorm.git && cd ./OpenData-Bridge-DataNorm
```

追加のライブラリのインストール
```Python
pip install -r requirements.txt
```

### 2. 統合対象のcsvを配置
OpenDataの検索で取得したcsvファイルをディレクトリ（ここでは./data）にまとめて配置

### 3. 変換定義のmapping_rules.json作成
#### 3-1. 変換定義を生成するためのChatGPT用プロンプト生成(prompt_creator.py)
異なるCSV形式からなる項目の対応関係をmapping_rules.jsonで定義し、pythonで変換&結合を行う。
ここでは、ChatGPTにmapping_rules.jsonを生成させるための適切なプロンプトを./data/*.csvから生成する。
例えば./data以下に変換対象のcsvファイルが複数あり、その中のhoikuen.csvの形式に合わせたい場合
```
python prompt_creator.py -dir ./data -m hoikuen.csv
```
を実行すると、ChatGPT(gpt4)に入れるプロンプトが生成される。
#### 3-2. ChatGPT(gpt4) でmapping_rules.jsonを生成する
前述のpythonコード実行結果をChatGPT(gpt4)の命令文として貼り付けると、jsonが生成される
#### 3-3. mapping_rules.jsonの調整
現状、完璧な変換定義を一回で作成することができないため、定義に問題のある箇所は手直しする。


### 4. データ変換＆結合

- ChatGPTで作成したmapping_rules.jsonをOpenData-Bridge-DataNorm以下に配置
- 以下のコマンドを実行
```Python
python datanorm.py ./data
```
./dataは変換＆結合するcsvファイルがあるディレクトリ


## ChatGPT用プロンプトテンプレート
- [input]のmaster.csvにデータを集約するcsvファイル、slave[n].csvに項目をmasterに合わせて変換するcsvファイルのヘッダーとデータをそれぞれ１行ずつ記載する（以下の中身を書き換える）。
- slave[n]は変換するフォーマットの数だけ増やす。
- [rule]以下は基本的には変更しなくてよい。

上記の要領で以下のテンプレートを編集( 3-1. prompt_creator.pyを使えばここを自動化できる）。

```
異なる複数のフォーマットからなるcsvファイルを一つのフォーマットに統合したい。複数ファイルのうち、一つをmaster.csvとして、残りをslave[n].csvとする。このとき[n]は1以上の数字を想定する。
入力[input]としてmaster.csvとslave[n].csvを与えるので[rule]以下のルールに基づき、mapping_rules.jsonを作成してほしい。

[input]
master.csv
---
"施設種別","地区","保育園名","所在地","緯度","経度","種別","電話番号","入園可能月齢","保育年齢別定員　0歳","保育年齢別定員　1歳","保育年齢別定員　2歳","保育年齢別定員　3歳","保育年齢別定員　4歳","保育年齢別定員　5歳","保育年齢別定員　合計","短時間保育開始時間","短時間保育終了時間","標準時間開始時間","標準時間終了時間","延長保育対象月齢","延長保育","休園日","運営事業者(指定管理者)","保育園ホームページ"
"認可保育園","芝","48保育園","東京都港区芝五丁目n番","35.8484","139.747716","区立","03-0000-0000","3か月","18","26","30","30","30","30","164","9:00","17:00","7:15","18:15","1歳の誕生日","22:00まで","日・祝・年末年始",,"https://www.xxxx.jp/index.html"
---

slave1.csv
---
名称,郵便番号,住所,電話番号,関連ホームページ,緯度,経度
児童館,1740051,板橋区小豆沢,03-0000-0000,http://www.xxxx.jp/index.html,35.58055254,139.6960174
---

slave2.csv
---
名称,所在地,URL,電話番号,FAX,緯度,経度
家庭支援センター,江戸川区船堀n丁目,http://www.xxxx.jp/index.html,03-0000-0000,03-0000-0000,35.685187,139.8653337
---

slave3.csv
---
施設名,カテゴリ,所在地,方書,郵便番号,電話番号,開所時刻,閉所時刻,備考,緯度（施設出入口）,経度（施設出入口）,緯度（施設中心）,経度（施設中心）
市立第６保育園,子育て,稲城市坂浜,,2060822,042-000-000,7:00,19:00,,35.422436,139.484959,34.622479,139.485152
---


[rule]
1) 以下[input ex]のようにmaster.csvとslave[n].csvが与えられた場合、[output ex]のようなmapping_rules.jsonを出力する。
ここで注意してほしいのはそのような変換プログラムの作成ではなく、jsonファイル作成の依頼であるということ。
2) csvの項目名とデータの内容から、masterとslaveの項目の対応関係を推測し、同じと思われるmasterの項目１つと配列で与えられるslave[n]の項目の対応関係をjsonファイルにする。
3) masterの項目は必ず対応関係の配列の1番目に追加しておく。
4) 対応関係の配列に重複する項目は必要ない。
5) slaveに存在し、masterには存在しない項目は捨てて良い。
6) masterには存在し、slaveには存在しない項目は対応関係の配列に記載しなくてよい。
7) master.csvに存在する項目が、対応関係の配列で2番目以降に出現する場合、その項目は対応関係の配列から除外する。
8) 以下に示すのは１例であって、必要なのはrule 1〜7で示されたルールを厳守し、[input]の方で提示しているmasterの各項目へのslave[n]の対応関係を漏らさずmapping_rules.jsonとして出力することである。

[input ex]
master.csv
---
"施設種別","保育園名","所在地"
"認可保育園","shiba保育園","東京都港区芝五丁目"
---

slave1.csv
---
名称,住所,
さわ児童館,板橋区小豆沢
---

slave2.csv
---
施設名称,所在地,
家庭支援センター,江戸川区船堀4丁目2番
---

[output ex]
mapping_rules.json
---
{
    "保育園名":[
        "保育園名",
        "施設名",
        "施設名称"
    ],
    "所在地":[
        "所在地",
        "住所",
    ]
}
---
```

## 制限事項
- ChatGPT4推奨
- プロンプトテンプレートはまだ改善が必要なので、出力結果に不備がある場合は都度、修正してご利用ください

