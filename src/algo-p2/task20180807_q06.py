fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# :for文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「◯◯は△△という意味です」と出力させてください
# 例：「appleはりんごという意味です」
for i in fruits.keys():
    x = fruits[i]
    y = "{0}は{1}という意味です。".format(i, x)
    print(y)
