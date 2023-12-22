import camelot
import pandas as pd

def clean_table(df):
    # 施設名が空の行を前の行と結合
    for i in df.index:
        if pd.isna(df.at[i, 0]) or df.at[i, 0].strip() == '':
            df.at[i-1, 0] += df.at[i, 0]

    # 結合後の行を削除
    df = df[df[0].str.strip() != '']
    return df

def extract_and_clean_tables(pdf_path, start_page, end_page):
    tables = camelot.read_pdf(pdf_path, pages=f'{start_page}-{end_page}', flavor='lattice')
    for i, table in enumerate(tables):
        cleaned_df = clean_table(table.df)
        cleaned_df.to_csv(f'cleaned_table_{start_page + i}.csv', index=False)

# ページ6から8までの表を抽出し、クリーンアップしてCSV形式で保存
extract_and_clean_tables('./A_public_facility.pdf', 6, 8)

