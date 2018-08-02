# 単語の出現回数をカウント
text = """
keep on asking, and it will be given you:
keep on seeking, and you will find:
keep on knocking, and it will be opened to you:
for everyone asking receives, and everyone seeking finds,
and to everyone konocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")
text = text.replace(";", "")
text = text.replace(";", "")
words = text.split()

# 単語を覚える
counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

# 結果を表示
for k,v in sorted(counter.items()):
    if v >= 3:
        print(k, v)
