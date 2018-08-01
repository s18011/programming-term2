# 所持金からりんごが買えるかどうか判断しよう(if,elif,elseステートメントを使ってみよう)
apple_price = 200
# 変数moneyに数値1000を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# おつりがあれば、買った個数と残金をそれぞれ「りんごを(個数)個買いました」「残金は(残り)円です」を表示してください。
# 所持金が支払い金額「より大きければ」残金が残ります。
if money > total_price:
    print('りんごを' + str(count) + '個買いました' + '残金は' + str(money - total_price) + '円です')
# TODO:おつりがなければ、買った個数を「りんごを(個数)個買いました」と表示し、「財布が空になりました」と表示してください。
# NOTE:所持金と支払い金額が「等しければ」りんごが買えて残金が残りません。
elif money == total_price:
    print('りんごを' + str(count) + '個買いました' + '残金は' + str(money - total_price) + '円です')
    print('財布が空になりました')
# TODO:指定した個数を買うのに所持金が足りなければ、「お金が足りません」「りんごを買えませんでした」を表示してください。
# NOTE:上記に示した2つの条件どちらも満たさない場合にお金が足りないと判断してください
else:
    print('お金が足りません' 'りんごを買えませんでした')
