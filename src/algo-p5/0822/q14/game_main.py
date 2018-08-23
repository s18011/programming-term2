import field_map
# :fromとimportを用いて、playerというモジュール「から」Playerというクラスを「インポート」インポートしてください
from player import Player

# 変数定義部
cur_pos = 0 # 現在の位置

# 関数定義部
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

    # 止まったマス目のイベントを取得する
    event_nm = field_map.get_event(cur_pos)

    if event_nm == "GoMoreForward":
        # 2マスさらに前に進む
        go_more_forward(2)
    elif event_nm == "GoBack":
        # 3マス戻る
        go_back(3)
    elif event_nm == "GoBackToStart":
        # 振り出しに戻る
        go_back_to_start()

def go_more_forward(cells):
    """
    出た目の分さらに前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    print("イベント発生！" + str(cells) + "マスさらに進みます。")

    # 引数で渡された目の分だけ前に進む
    go_forward(cells)

def go_back(cells):
    """
    出た目の分後ろに戻る
    Parameters
    ----------
    cells : int
        戻るマス目の数
    Returns
    -------
    なし
    """
    print("イベント発生！" + str(cells) + "マス後ろに戻ります。")

    # 引数で出た目の分だけ前に戻る(引数に-1を掛けることで戻る動作をしている)
    go_forward((cells * -1))

def go_back_to_start():
    """
    出た目の分後ろに戻る
    Parameters
    ----------
    なし
    Returns
    -------
    なし
    """
    # cur_posをグローバル参照
    global cur_pos

    print("イベント発生！振り出しに戻ってしまいます！")

    # 現在位置の分だけ前に戻ることで振り出しに戻る動作をする(引数に-1を掛けることで戻る動作をしている)
    go_forward((cur_pos * -1))

# 以下メイン処理
if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、Start!!")

    # :Playerクラスのオブジェクトを変数heroに代入してください。
    hero = Player

    # :hero.nameに"たろう"を代入してください。
    hero.name = "たろう"

    # :「やあ、(hero.name)!旅をはじめよう!」の形式で主人公の名前をメッセージ中に表示してください。
    print('やあ、' + str(hero.name) + '!旅を始めよう!')

    # ゴールに到達するまでサイコロを投げて進む行為を繰り返す
    while cur_pos < field_map.goal_pos:
        # サイコロを振る
        dice_num = field_map.shake_dice()

        # 出た目の分だけ進む
        go_forward(dice_num)

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
