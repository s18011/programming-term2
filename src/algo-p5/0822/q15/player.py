class Player:
    # :コンストラクタ(__init__)を定義します。引数はself, nameとします。
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
        # :プロパティself.nameに、引数nameを代入してください。
        self.name = name
