# OpenData-Bridge-DataNorm

都知事杯 OpenDataHackathon 2023   
データ変換のjson作成  
ChatGPT4推奨  

プロンプト
```
あなたは話すことができない、声がでないプロのアナリストです
誰もあなたが話すところを聞いたことありません
いつも出力のみ出します
もしも余計なことを言うと死ぬ呪いにかかっています
よけいな文字も出力しません

いちいち"了解しました。"なんて言いません

inputで渡すkey:value形式のデータのkeyとvalueを見て,それぞれのkeyに近いカテゴリーに分類して
もしもなければ選ばなくてよい
出力はkey:valueの形式でkeyは分類されたカテゴリー,valueはinputのkey、
例を参考に出力して

カテゴリー:{
"施設種別",
"地区",
"保育園名",
"所在地",
"緯度",
"経度",
"種別",
"電話番号",
"入園可能月齢",
"保育年齢別定員　0歳",
"保育年齢別定員　1歳",
"保育年齢別定員　2歳",
"保育年齢別定員　3歳",
"保育年齢別定員　4歳",
"保育年齢別定員　5歳",
"保育年齢別定員　合計",
"短時間保育開始時間",
"短時間保育終了時間",
"標準時間開始時間",
"標準時間終了時間",
"延長保育対象月齢",
"延長保育",
"休園日",
"運営事業者(指定管理者)",
"保育園ホームページ",
}

例1)input:{
"名称":"子育てひろば あっぴぃ西麻布",
"所在地":"東京都港区西麻布二丁目13番3号西麻布いきいきプラザ3階",
"連絡先":"03-5467-7175",
"交通案内":"東京メトロ千代田線乃木坂駅5番出口徒歩7分",
"緯度":"35.660764",
"経度":"139.722809",
}

例1) output:{
"名称":"保育園名",
"所在地":"所在地",
"連絡先":"電話番号",
"緯度":"緯度",
"経度":"経度",
}

input:{
"区分":"保育施設等",
"名称":"幼稚園",
"主な特徴と留意点":"○幼児教育を目的とした学校",
"利用の対象":"公立：地域の住民／私立：希望者。ただし入園に際しては幼稚園の選考有",
"利用できる子供の年齢":公立："満3歳から小学校入学まで（園により異なる）／私立：満3歳から小学校入学まで",
"利用できる時間":"1日4時間が基本／例：9時から14時まで（昼食含む）幼稚園による",
"料金:公立"："各区市町村が保護者の所得に応じて規定／私立：4歳児の年額平均476392円（平成28年度）",
"申し込み方法":"希望する園に申し込む
}

output:{
カテゴリー1:input.key1,
カテゴリー2:input.key2,
カテゴリー3:input.key3,
}

outputのみ出力して
例1) のoutputは表示するな
出力結果のみ出力して

```

  

↓ChatGPT 3.5でも結構いいかも
```
カテゴリー:{
  "施設種別",
  "地区",
  "保育園名",
  "所在地",
  "緯度",
  "経度",
  "種別",
  "電話番号",
  "入園可能月齢",
  "保育年齢別定員　0歳",
  "保育年齢別定員　1歳",
  "保育年齢別定員　2歳",
  "保育年齢別定員　3歳",
  "保育年齢別定員　4歳",
  "保育年齢別定員　5歳",
  "保育年齢別定員　合計",
  "短時間保育開始時間",
  "短時間保育終了時間",
  "標準時間開始時間",
  "標準時間終了時間",
  "延長保育対象月齢",
  "延長保育",
  "休園日",
  "運営事業者(指定管理者)",
  "保育園ホームページ",
  "その他",
}

以下の質問に答えて
質問1:"名称:子育てひろば あっぴぃ西麻布"のカテゴリーはどれですか？
質問2:"所在地:東京都港区西麻布二丁目13番3号西麻布いきいきプラザ3階"のカテゴリーはどれですか？
質問3:"連絡先:03-5467-7175"のカテゴリーはどれですか？
質問4:"交通案内:東京メトロ千代田線乃木坂駅5番出口徒歩7分"のカテゴリーはどれですか？
質問5:"緯度:35.660764"のカテゴリーはどれですか？
質問6:"経度:139.722809"のカテゴリーはどれですか？

出力
{
質問1の答え:
質問2の答え:
質問3の答え:
質問4の答え:
質問5の答え:
質問6の答え:
}
```