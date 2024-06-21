import spacy
import pandas as pd
from collections import Counter

# spaCyの英語モデルを読み込み
nlp = spacy.load("en_core_web_sm")

def count_pos(text):
    # テキストを解析
    doc = nlp(text)
    
    # 各トークンの品詞をカウント
    pos_counts = Counter(token.pos_ for token in doc)
    
    return pos_counts

def process_csv(file_path):
    # CSVファイルを読み込み
    df = pd.read_csv(file_path)
    
    # 結果を格納するリスト
    results = []

    for index, row in df.iterrows():
        text = row['query']
        pos_counts = count_pos(text)
        
        # 結果を辞書形式に変換し、'sentence_id'を追加
        pos_counts_dict = dict(pos_counts)
        pos_counts_dict['sentence_id'] = index + 1  # 文のID（行番号）
        
        results.append(pos_counts_dict)
    
    # DataFrameに変換し、CSVファイルに出力
    result_df = pd.DataFrame(results)
    result_df.fillna(0, inplace=True)  # 欠損値を0に置換
    result_df.to_csv('pos_counts.csv', index=False)

def main():
    file_path = 'query.csv'  # ここにCSVファイルのパスを指定
    process_csv(file_path)

if __name__ == "__main__":
    main()
