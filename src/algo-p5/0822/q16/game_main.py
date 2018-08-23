import field_map
from player import Player

# :変数定義部はごっそり消します。(cur_posはPlayerクラスのインスタンス変数にします。)
cur_pos = 0 # 現在の位置

if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、Start!!")

    # プレイヤーの名前を取得する
    p_name = input("プレイヤーの名前を教えてください>> ")

    # Playerクラスのオブジェクトを作成
    hero = Player(p_name)

    # ゲームからの呼びかけメッセージを表示
    print("やあ、" + hero.name + "!旅をはじめよう!")

    # ゴールに到達するまでサイコロを投げて進む行為を繰り返す
    # :cur_posをhero.cur_posに書き換えてください。
    while hero.cur_pos < field_map.goal_pos:
        # サイコロを振る
        dice_num = field_map.shake_dice()

        # 出た目の分だけ進む
        # :go_forwardをhero.go_forwardに書き換えてください。
        hero.go_forward(dice_num)

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
