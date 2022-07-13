from wallet.PassProps import Field


class PassInformation:
    """
    Basic Fields for Wallet Pass
    """

    def __init__(self):
        self.headerFields = []
        self.primaryFields = []
        self.secondaryFields = []
        self.backFields = []
        self.auxiliaryFields = []

    def add_header_field(self, **kwargs):
        """
        Add Simple Field to Header
        :param key:
        :param value:
        :param label: optional
        """
        self.headerFields.append(Field(**kwargs))

    def add_primary_field(self, **kwargs):
        """
        Add Simple Primary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.primaryFields.append(Field(**kwargs))

    def add_secondary_field(self, **kwargs):
        """
        Add Simple Secondary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.secondaryFields.append(Field(**kwargs))

    def add_back_field(self, **kwargs):
        """
        Add Simple Back Field
        :param key:
        :param value:
        :param label: optional
        """
        self.backFields.append(Field(**kwargs))

    def add_auxiliary_field(self, **kwargs):
        """
        Add Simple Auxilary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.auxiliaryFields.append(Field(**kwargs))

    def json_dict(self):
        """
        Create Json object of all Fields
        """
        data = {}
        for what in [
            "headerFields",
            "primaryFields",
            "secondaryFields",
            "backFields",
            "auxiliaryFields",
        ]:
            if hasattr(self, what):
                field_data = [f.json_dict() for f in getattr(self, what)]
                data.update({what: field_data})
        return data
