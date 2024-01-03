##########################
######## 使いかた #########
##########################
### 入力
#市区町村名 住居表示－街区マスター位置参照拡張 データセット
#"gaiku_url_list.txt　にURLを入力
#市区町村名 住居表示－住居マスター位置参照拡張 データセット
#"jyuukyo_url_list.txt"にURLを入力
###　出力
# 二つのデータセットを統合し、住居データとして出力
#'merged_jyuukyo.csv' ファイルが出力されます
# workフォルダには作業の状況が残ります
# ただし、work/extracted_filesフォルダ内は最後に作用した状況のみです

##################################################################
######### モジュール(module)やパッケージ(package)の読み込み #########
##################################################################
#Webページやデータを取得
import requests
#ZIPの圧縮・解凍
import zipfile
#OS依存機能を利用
import os
#データ分析作業を支援するためのモジュール
import pandas as pd
import shutil

###########################
######### 関数定義 #########
###########################
### ファイルのダウンロード
def download_file(url, local_filename):
    # URLからファイルをダウンロードし、特定のローカルファイルパスに保存する
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
### 住居表示ファイルの取得及び結合
def address_download(file_name,combined_data_file):
    ### work/extracted_files　フォルダのクリーニング
    ### ※注意！　フォルダ内全ての一括処理があるため必ずその都度クリーニングを行うこと
    extracted_folder_path = 'work/extracted_files'
    if os.path.exists(extracted_folder_path):
        shutil.rmtree(extracted_folder_path)
    os.makedirs(extracted_folder_path)
    print(f"work/extracted_filesフォルダのクリーニングが完了しました。")
    ### 指定ファイル内のファイル一覧を読み込む
    # ファイルを読み込みモードで開く
    with open(file_name, "r") as file:
        # ファイルから行を1行ずつ読み込む
        file_list = file.readlines()
    # 各行の末尾の改行文字を削除
    file_list = [line.strip() for line in file_list]
    ### 読み込んだファイル一覧を順次処理
    for file_path in file_list:
        print(file_path)
        ### ファイルのダウンロード
        url = file_path
        local_filename = 'work/download.zip'
        download_file(url, local_filename)
        ### ダウンロードしてZIPファイルを読み込みモードで開き解凍
        with zipfile.ZipFile(local_filename, 'r') as my_zip:
            # ZIPファイル内のファイル一覧を表示
            file_list = my_zip.namelist()
            print("ZIPファイル内のファイル一覧:")
            for file_name in file_list:
                print(file_name)
            # ZIPファイル内の全てのファイルを解凍
            my_zip.extractall('work/extracted_files')
            ### 所定のフォルダ内のすべてのCSVファイルを結合
            ### 最初のファイルの属性行を取得しそれ以降のファイルの属性行は無視
            # CSVファイルが保存されているディレクトリを指定
            csv_directory = 'work/extracted_files'
            # 最初のCSVファイルから列名を取得
            first_file = os.listdir(csv_directory)[0]
            first_file_path = os.path.join(csv_directory, first_file)
            first_df = pd.read_csv(first_file_path)
            column_names = first_df.columns.tolist()
            # 結合するための空のDataFrameを作成
            combined_data = pd.DataFrame(columns=column_names)
            # 指定したディレクトリ内のCSVファイルを結合
            for filename in os.listdir(csv_directory):
                if filename.endswith(".csv"):
                    file_path = os.path.join(csv_directory, filename)
                if file_path == first_file_path:
                    # 最初のファイルはスキップして、列名を引き継ぐ
                    continue
                df = pd.read_csv(file_path)
                # 列名を引き継いで結合
                combined_data = pd.concat([combined_data, df], ignore_index=True)
                # 結合したデータを1つのCSVファイルに保存
                combined_data.to_csv(combined_data_file, index=False)
            print(f"CSVファイルの結合が完了しました。")
    ### CSVファイルを文字列として読み込む
    df = pd.read_csv(combined_data_file,dtype=str)
    # 結合したい文字列の属性を選択し、新しい文字列の属性を作成する
    df['街区ユニークid'] = df['全国地方公共団体コード'] + df['町字id'] + df['街区id']
    # 新しいCSVファイルに保存する
    df.to_csv(combined_data_file, index=False)
    print(f"街区ユニークidを追加しました。")
    return

#########################
######## メイン #########
########################
try:
    ### work　フォルダのクリーニング
    work_folder_path = 'work'
    if os.path.exists(work_folder_path):
        shutil.rmtree(work_folder_path)
    os.makedirs(work_folder_path)
    print(f"workフォルダのクリーニングが完了しました。")
    ### 住居表示ファイルの取得及び結合
    # address_download("住居表示ファイル名一覧ファイル名を指定",'結合住居表示ファイル名')
    #市区町村名 住居表示－街区マスター位置参照拡張 データセット
    address_download("gaiku_url_list.txt",'work/combined_gaiku.csv')
    print(f"市区町村名 住居表示－街区マスターが作成されました。")
    #市区町村名 住居表示－住居マスター位置参照拡張 データセット
    address_download("jyuukyo_url_list.txt",'work/combined_jyuukyo.csv')
    print(f"市区町村名 住居表示－住居マスターが作成されました。")
    ###　住居マスターに街区マスターを結合する
    # 1つ目のCSVファイルを読み込む
    df1 = pd.read_csv('work/combined_jyuukyo.csv')
    # 2つ目のCSVファイルを読み込む
    df2 = pd.read_csv('work/combined_gaiku.csv')
    # 属性をキーにして結合
    # 結合方式はleftのすべての行が保持
    # 同じ属性が重複する場合は街区データ側に接尾辞を追加
    merged_df = pd.merge(df1, df2, on='街区ユニークid', how='left', suffixes=('', '_街区'))
    # 結合結果を新しいCSVファイルとして保存
    merged_df.to_csv('merged_jyuukyo.csv', index=False)
    print(f"居住データベースが作成されました。")
# エラー処理
except FileNotFoundError:
    print(f"ファイルが見つかりません。")
except Exception as e:
    print(f"エラーが発生しました: {e}")