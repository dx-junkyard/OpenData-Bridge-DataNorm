
デジタル庁のジオコーディングをWebAPIで取得できる

https://github.com/digital-go-jp/abr-geocoder

# /digital_geocode

### request parameter
| name | required | description |
| -- | -- |  -- |
| address |  ✓ | 住所 |

### response

| name        | type   | value                          | description            |
| -- | -- | -- | -- |
| output      | str    | "東京都千代田区紀尾井町1-3"    | フルアドレス            |
| prefecture  | str    | "東京都"                        | 都道府県名              |
| match_level | int    | 8                              | マッチングレベル        |
| city        | str    | "千代田区"                      | 市区町村名              |
| town        | str    | "紀尾井町"                      | 町名                    |
| town_id     | str    | 0056000                        | 町字ID                  |
| lg_code     | str    | 131016                         | ローカルガバメントコード|
| other       | str    | ""                             | その他の情報            |
| lat         | float  | 35.679107172                   | 緯度                    |
| lon         | float  | 139.736394597                  | 経度                    |
| block       | str    | "1"                            | ブロック番号            |
| block_id    | str    | "001"                          | ブロックID              |
| addr1       | str    | "3"                            | 番地1                   |
| addr1_id    | str    | "003"                          | 番地1のID               |
| addr2       | str    | ""                             | 番地2                   |
| addr2_id    | str    | ""                             | 番地2のID               |

## ※ ログインできない場合
https://stackoverflow.com/questions/55330786/change-azure-directory-from-command-line

# デプロイ方法 & ローカルの実行方法
## 1. dockerコンテナのビルド
```bash
docker build -t {ImageName} .
```

## 2. ローカルでの実行
```bash
docker run -p 5000:5000 {ImageName}
```

## 2. Azure Container Registry(ACR)にイメージをプッシュ
1. Azure Container Registryの作成:
まず、Azure PortalまたはAzure CLIを使用してAzure Container Registryを作成します。これは、Dockerイメージを保存するためのプライベートコンテナレジストリです。

2. ロールの割り当て
1.で作成したAzure Container RegistryのIAMでロールの割り当てを行う
ロール名: AcrPush

3. 「設定」→「アクセスキー」→「管理者ユーザー」を有効

2. Dockerイメージのタグ付け:
ローカルでビルドしたDockerイメージにタグを付けます。タグは通常、レジストリのアドレスを含みます。
```bash
docker tag my [ACR名].azurecr.io/myapp:v1
```

3. ACRへのログイン
Azure CLIを使用してACRにログインします。
```bash
az acr login --name [ACR名]
```

4. イメージのプッシュ
タグ付けされたイメージをACRにプッシュします。
```bash
docker push [ACR名].azurecr.io/myapp:v1
```

## 3. Azure Container Instancesにデプロイ
CUIでもできます
UIでやりました
