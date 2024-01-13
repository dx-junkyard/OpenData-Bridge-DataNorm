# エンドポイント一覧

## /geocode
ジオコーディング周りの取得
### request parameter
| name | required | description |
| -- | -- |  -- |
| city_block_id | ✓ | 街区id |
| residence_id | ✓ | 住居id |
| address |  ✓ | 住所 |

### response
| name | type | value | description |
| -- | -- | -- | -- |
| code | integer | 401030 | 全国地方公共団体コード |
| aza_id | integer | 4000 | 町字id | 
| prefectures | string | 福岡県 | 所在地_都道府県 |
| municipalities | string | 北九州市若松区 | 所在地_市区町村 |
| aza | string | 赤岩町 | 所在地_町字 |
| latitude | float | 33.890251893 | 緯度 |
| longitude | float | 130.767441408 | 経度 |

### sample
入力: 街区id=28, 住居id=3, 住所=赤岩町
```bash
$ curl {URL}/geocode?city_block_id=3&residence_id=28&address=%E8%B5%A4%E5%B2%A9%E7%94%BA

>> {"code": 401030, "aza_id": 4000, "prefectures": "\u798f\u5ca1\u770c", "municipalities": "\u5317\u4e5d\u5dde\u5e02\u82e5\u677e\u533a", "aza": "\u8d64\u5ca9\u753a", "latitude": 33.890251893, "longitude": 130.767441408}
```

-----

# /digital-go-geocode
デジタル庁のジオコーディング

### request parameter
| name | required | description |
| -- | -- |  -- |
| address | ✓ | 住所 |

### response
| name | type | value | description |
| -- | -- | -- | -- |
| lg_code | string | 401030 | 全国地方公共団体コード |
| town_id | string | 0075001 | 町字ID |
| fulladdress | string | 福岡県北九州市若松区響町一丁目 | 所在地_連結表記 |
| prefecture | string | 福岡県 | 所在地_都道府県 |
| city | string | 北九州市若松区 | 所在地_市区町村 |
| town | string | 響町一丁目 | 所在地_町字 |
| lat | float | 33.940111 | 緯度 |
| lon | float | 130.821747 | 経度 |


### sample
入力: 北九州市若松区響町一丁目
```bash
$ curl {URL}/digital-go-geocode?address=%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82%E8%8B%A5%E6%9D%BE%E5%8C%BA%E9%9F%BF%E7%94%BA%E4%B8%80%E4%B8%81%E7%9B%AE

>> {"lg_code": "401030", "town_id": "0075001", "fulladdress": "\u798f\u5ca1\u770c\u5317\u4e5d\u5dde\u5e02\u82e5\u677e\u533a\u97ff\u753a\u4e00\u4e01\u76ee", "prefecture": "\u798f\u5ca1\u770c", "city": "\u5317\u4e5d\u5dde\u5e02\u82e5\u677e\u533a", "town": "\u97ff\u753a\u4e00\u4e01\u76ee", "lat": 33.940111, "lon": 130.821747}
```

----- 

# /japanese-to-english 
日本語を英語へ翻訳
### request parameter
| name | required | description |
| -- | -- |  -- |
| jp | ✓ | 日本語 |

### response
| name | type | value | description |
| -- | -- | -- | -- |
| en | string | Tokyo | 翻訳結果 |

### sample
入力: 北九州市響灘ビオトープ
```bash
$ {URL}/japanese-to-english?jp=%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82%E9%9F%BF%E7%81%98%E3%83%93%E3%82%AA%E3%83%88%E3%83%BC%E3%83%97

>> {"en": "Kitakyushu City Hibikinada Biotope"}
```

### azure上での準備
- Translator Textの作成
- シークレットキーにapiキーを追加


----- 

# /poi
POIコードの取得
### request parameter
| name | required | description |
| -- | -- |  -- |

### response
| name | type | value | description |
| -- | -- | -- | -- |
| poi | | | | 

### sample
```bash
```