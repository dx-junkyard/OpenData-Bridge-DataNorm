エンドポイント

# /geocoding
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
街区id=28, 住居id=3, 住所=赤岩町
```bash
curl  "https://datanorm.azurewebsites.net/api/geocode?city_block_id=3&residence_id=28&address=%E8%B5%A4%E5%B2%A9%E7%94%BA"

{"code": 401030, "aza_id": 4000, "prefectures": "\u798f\u5ca1\u770c", "municipalities": "\u5317\u4e5d\u5dde\u5e02\u82e5\u677e\u533a", "aza": "\u8d64\u5ca9\u753a", "latitude": 33.890251893, "longitude": 130.767441408}

```

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

----- 

# /facilityname 
施設名称をカタカナと英字変換
### request parameter
| name | required | description |
| -- | -- |  -- |
| name | ✓ | 施設名称 |

### response
| name | type | value | description |
| -- | -- | -- | -- |
| name_kana | string | | 施設名称(カナ) |
| name_en | string | | 施設名称(英字) |

### sample
```bash
```