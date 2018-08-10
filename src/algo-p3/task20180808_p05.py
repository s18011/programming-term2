def print_hand(hand, name='ゲスト'):
    '''
    Parameters
    ----------
    hand
    何を出したか
    name
    プレイヤー
    '''
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

player_name = input('名前を入力してください')

if player_name == '':
    print_hand('グー')

else:
    print_hand('グー', player_name)
# TODO:input関数を用いて「名前を入力してください：」をコンソールに表示後、入力を受け取り、変数player_nameに代入してください


# TODO:変数player_nameの値によって関数print_handの呼び出し方を変更してください
# TODO:player_nameが空文字('')の場合に第1引数に'グー'のみを指定し、print_hand関数を呼び出してください

# TODO:上記以外の場合、第1引数に'グー'、第2引数にplayer_nameを指定し、print_hand関数を呼び出してください
