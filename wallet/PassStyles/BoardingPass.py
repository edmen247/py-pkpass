from wallet.PassProps import TransitType
from wallet.PassInformation import PassInformation


class BoardingPass(PassInformation):
    """Wallet Boarding Pass"""

    def __init__(self, transitType=TransitType.AIR):
        super(BoardingPass, self).__init__()
        self.transitType = transitType
        self.jsonname = "boardingPass"

    def json_dict(self):
        data = super(BoardingPass, self).json_dict()
        data.update({"transitType": self.transitType})
        return data
