from wallet.PassInformation import PassInformation


class EventTicket(PassInformation):
    """Wallet Event Ticket"""

    def __init__(self):
        super(EventTicket, self).__init__()
        self.jsonname = "eventTicket"
