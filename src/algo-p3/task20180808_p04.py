# TODO:仮引数nameの初期値を「ゲスト」に設定してください
def print_hand(hand, name="ゲスト"):
    '''
    Parameters
    ----------
    hand
    ジャンケンを出す手
    name
    プレイヤー
    '''
    print(name + 'は' + hand + 'を出しました')

print_hand("グー")
