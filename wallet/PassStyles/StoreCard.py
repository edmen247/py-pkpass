from wallet.PassInformation import PassInformation


class StoreCard(PassInformation):
    """Wallet Store Card"""

    def __init__(self):
        super(StoreCard, self).__init__()
        self.jsonname = "storeCard"
