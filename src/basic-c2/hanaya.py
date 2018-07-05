#値段を求める
print(((500*18)+(400*(8-2))+(700*(21-5)))*(1-0.1))
rose_v = 500
sun_v = 400
tulip_v =700

rose_c = 18
sun_c = 8-2
tulip_c =21-5

rate = 1-0.1

sum_v = (rose_v * rose_c) + (sun_v * sun_c) + (tulip_v * tulip_c)
payment = sum_v * rate

print("買い物の合計は", sum_v, "円")
print("割引してもらうと", payment, "円")
