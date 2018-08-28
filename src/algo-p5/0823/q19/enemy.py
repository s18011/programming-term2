# :Enemyクラスを定義してください。
class Enemy:
    # TODO:コンストラクタ(__init__)の引数はPlayer同様、self, nameとします。
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
        # :self.nameに引数nameを代入してください。
        self.name = name
        # :self.hpに初期値10を代入してください。
        self.hp = 10
        # :相手に与えるダメージの最小値として、self.min_damegeに初期値2を代入してください。
        self.min_damege = 2
        # :相手に与えるダメージの最大値として、self.max_damegeに初期値4を代入してください。
        self.max_damege = 4
        # :「つうこんのいちげき!」が出る頻度として、self.freqの初期値に20を代入してください。
        self.freq = 20
