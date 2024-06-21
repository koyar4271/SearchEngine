import spacy

# spaCyの英語モデルを読み込み
nlp = spacy.load("en_core_web_sm")

def tokenize_and_pos(text):
    # テキストを解析
    doc = nlp(text)
    
    # 単語とその品詞を抽出してリストに格納
    tokens_and_pos = [(token.text, token.pos_) for token in doc]
    
    return tokens_and_pos

# テスト用のテキスト
text = "SpaCy is an open-source library for Natural Language Processing in Python."

# 単語分解と品詞の抽出を実行
tokens_and_pos = tokenize_and_pos(text)

# 結果を出力
for token, pos in tokens_and_pos:
    print(f"{token}: {pos}")
