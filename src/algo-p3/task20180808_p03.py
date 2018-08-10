# :じゃんけんのプレイヤーの名前を第2引数で、nameという引数名で受け取れるように書き換えてください
def print_hand(hand, name):
    '''
    Parameters
    ----------
    hand
    ジャンケンで出した手
    name
    プレイヤーの名前
    '''
    print(name, "は", hand, "を出しました")

print_hand('グー', 'ななしのたろう')

print_hand('パー', 'コンピューター')
