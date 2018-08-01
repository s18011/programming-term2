# 購入するりんごの個数を、プログラム実行時に入力しよう。
apple_price = 200

# inputを用いて入力を受け取り、変数input_countに代入してください
input_count = input()

# input_countを数値として、変数countに代入してください(ヒント：型変換)
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')
