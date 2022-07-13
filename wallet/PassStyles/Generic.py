from wallet.PassInformation import PassInformation


class Generic(PassInformation):
    """Wallet Generic Pass"""

    def __init__(self):
        super(Generic, self).__init__()
        self.jsonname = "generic"
