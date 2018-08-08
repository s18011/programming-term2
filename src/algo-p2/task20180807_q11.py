items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    # :inputを用いて入力を受け取り、変数input_countに代入してください
input_count = input()
    # :キーと変数input_countを用いて「購入する◯◯の個数は△△個です」となるように出力してください
price = "購入する{0}の個数は{1}個です".format(item_name, input_count)
print(price)
    # :input_countを数値として変数countに代入してください
count = float(input_count)
    # :変数total_priceに果物1個の値段と変数countを掛けた値を代入してください
total_price = items[item_name] * count
    # :変数total_priceと型変換を用いて、「支払い金額は◯◯円です」となるように出力してください
total = "支払い金額は{0}円です".format(total_price)
print(total)
