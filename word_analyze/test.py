import spacy

# spaCyの英語モデルを読み込み
nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    # テキストを解析
    doc = nlp(text)
    
    # 単語に分解してリストに格納
    tokens = [token.text for token in doc]
    
    return tokens

# テスト用のテキスト
text = "SpaCy is an open-source library for Natural Language Processing in Python."

# 単語分解の実行
tokens = tokenize_text(text)
print(tokens)
