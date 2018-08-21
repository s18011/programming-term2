# :randomモジュールを参照してください
import random

# 変数定義部
goal_pos = 100  # ゴールの位置

# 関数定義部
# :shake_dice()関数を定義ごと下記に移動してください。
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
