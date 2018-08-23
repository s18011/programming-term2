# :field_mapモジュールをimportしてください(このクラス内でイベントの名称を取得したいため)
import field_map

class Player:
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            プレイヤーの名前
        Returns
        -------
        自分自身のインスタンス
        """
        self.name = name
        # :プロパティself.cur_pos(プレイヤーの現在位置)に0を代入してください。
        self.cur_pos = 0
    def go_forward(self, cells):
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

    # 引数のマス目だけ進む
        self.cur_pos += cells

    # 現在位置を表示
        print("現在位置は" + str(self.cur_pos) + "です。")

    # 止まったマス目のイベントを取得する
        event_nm = field_map.get_event(self.cur_pos)

        if event_nm == "GoMoreForward":
            # 2マスさらに前に進む
            self.go_more_forward(2)
        elif event_nm == "GoBack":
            # 3マス戻る
            self.go_back(3)
        elif event_nm == "GoBackToStart":
            # 振り出しに戻る
            self.go_back_to_start()

    def go_more_forward(self, cells):
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
        self. go_forward(cells)

    def go_back(self, cells):
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

    def go_back_to_start(self):
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

        print("イベント発生！振り出しに戻ってしまいます！")

    # 現在位置の分だけ前に戻ることで振り出しに戻る動作をする(引数に-1を掛けることで戻る動作をしている)
        self.go_forward((self.cur_pos * -1))
    # :game_main.pyの関数定義部のコードを以下に移動してください。但し、下記の手順を踏んでください。
    # :各関数(メソッド)の第1引数にはselfを追加してください。
    # :cur_posのグローバル参照をカットし、残りのcur_posをself.cur_posに変更してください。
    # :同じクラス内の関数(メソッド)を呼び出す際、self.を付けて呼び出してください。
