import json
import pandas as pd
from collections import OrderedDict
import os
from glob import glob
import pandas as pd

def load_mapping_rules(path):
    mapping_rules = json.load(open(path, "r", encoding="utf-8"))
    mapping_rules = OrderedDict(mapping_rules)

    return mapping_rules

def load_csv(path):
    """pathのcsvを読み込む, encodingはutf-8またはANSI"""
    df = None
    try:
        df = pd.read_csv(path)
    except Exception as e:
        try:
            df = pd.read_csv(path, encoding="ANSI")            
        except Exception as e:     
           print(f"Could not read {path}: {e}")

    return df

def trans_column_name(df, mapping_rules):
    for column_name in df.columns:
        # key : 変更後
        # value : 変換前list
        for key, value in mapping_rules.items():
            if column_name in value:
                df.rename(columns={column_name: key}, inplace=True)
                break
        else:
            df.drop(column_name, axis=1, inplace=True)

    return df

# filepath : 
def main(filepath):
    mapping_rules = load_mapping_rules("mapping_rules.json")

    # ↓ 特定のフォルダ内にある.csvファイルを一括で処理できる
    # # パスを指定してCSVファイルの一覧を取得
    # csv_files = glob(os.path.join("data", "*.csv"))
    # print(csv_files)

    # # 空のDataFrameを作成
    # combined_csv = pd.DataFrame(columns=list(mapping_rules.keys()))

    # # 各CSVファイルを読み込み、結合
    # for cnt, file in enumerate(csv_files):
    #     df = load_csv(file)
    #     if df is None: continue

    #     df = trans_column_name(df, mapping_rules)    

    #     combined_csv = pd.concat([combined_csv, df], ignore_index=True, sort=False)


    # 空のDataFrameを作成
    combined_csv = pd.DataFrame(columns=list(mapping_rules.keys()))

    # 各CSVファイルを読み込み、結合
    df = load_csv(filepath)
    if df is None: return

    df = trans_column_name(df, mapping_rules)    

    combined_csv = pd.concat([combined_csv, df], ignore_index=True, sort=False)

    # 有効な列のみでDataFrameをフィルタ
    combined_csv = combined_csv[list(mapping_rules.keys())]

    # ダブルクォートを""へreplace
    combined_csv.replace(to_replace='"', value='', regex=True, inplace=True)

    # すべてがnaの場合削除
    combined_csv.dropna(how='all', inplace=True)

    # ないカラムについては空文字で埋める
    combined_csv.fillna('', inplace=True)

    # 結合したデータを新しいCSVファイルに出力
    combined_csv.to_csv("combined.csv", index=False)
