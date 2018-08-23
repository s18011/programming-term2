import field_map
from player import Player

# 以下メイン処理
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
    while hero.cur_pos < field_map.goal_pos:
        # :フィールド上のコマンドを選択します。hero.choose_action_in_field()を呼び出してください。
        hero.choose_action_in_field()

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
