from wallet.PassInformation import PassInformation


class Coupon(PassInformation):
    """Wallet Coupon Pass"""

    def __init__(self):
        super(Coupon, self).__init__()
        self.jsonname = "coupon"
