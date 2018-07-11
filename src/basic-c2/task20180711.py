janken = int(input("何を出しますか? 1:グー 2:チョキ 3:パー"))

is_task = janken
if janken == 1:
    is_task = "lose"
elif janken == 2:
    is_task = "lose"
elif janken == 3:
    is_task = "lose"
else:
    is_task = "error"

if is_task == "lose":
    if janken == 1:
        print("CPUがパーを出しました。あなたの負けです。")
    elif janken == 2:
        print("CPUがグーを出しました。あなたの負けです。")
    elif janken == 3:
        print("CPUがチョキを出しました。あなたの負けです。")

else:
    print("error")
