#print((200*2)+(100)+((100*0.8)*2)-150)
beer_v = 200
otumami_v = 100
yakitori_v = 100

beer_c = 2
otumami_c = 1
yakitori_c = 2

rate = 0.2

point_nebiki = -150
sum_v = (beer_v * beer_c) + (otumami_v * otumami_c) + (yakitori_v * yakitori_c * (1-rate))
payment = sum_v + point_nebiki

print("買い物の合計は", sum_v, "円")
print("割引してもらうと", payment, "円")
