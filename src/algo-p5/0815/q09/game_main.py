import field_map
# :サイコロを振る処理がfield_map.pyに移動するため、randomモジュールの参照をカットしてください。

# 変数定義部
cur_pos = 0 # 現在の位置

# 関数定義部
# :shake_dice()関数全体をfield_map.pyに移動してください。
def shake_dice():
    """
    サイコロを振る
    Parameters
    ----------
    なし
    Returns
    -------
    int
        サイコロを振って出た目
    """
    # サイコロを振るため、Enterキーを入力待ちにする
    input("サイコロを振ります。Enterキーを押してください。")

    # 1〜6の任意の数字を取得する
    dice_num = random.randint(1, 6)

    # 出た目の数をコンソールに表示する
    print(str(dice_num) + "の目が出ました。")

    # 出た目を返す
    return dice_num

def go_forward(cells):
    """
    前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

# 以下メイン処理
# 開始メッセージを表示
print("すごろくゲーム、Start!!")

# ゴールに到達するまでサイコロを投げて進む行為を繰り返す
while cur_pos < field_map.goal_pos:
    # サイコロを振る
    # :shake_dice()関数をfield_mapモジュールから呼び出すよう変更してください。
    dice_num = field_map.shake_dice()

    # 出た目の分だけ進む
    go_forward(dice_num)

# ゴール到達のメッセージを表示
print("ゴールしました。おめでとうございます!")
