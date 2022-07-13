from wallet.PassProps import Field
from wallet.Schemas import FieldProps


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

    def add_header_field(self, field_props: FieldProps):
        """
        Add Simple Field to Header
        :param key:
        :param value:
        :param label: optional
        """
        self.headerFields.append(Field(field_props))

    def add_primary_field(self, field_props: FieldProps):
        """
        Add Simple Primary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.primaryFields.append(Field(field_props))

    def add_secondary_field(self, field_props: FieldProps):
        """
        Add Simple Secondary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.secondaryFields.append(Field(field_props))

    def add_back_field(self, field_props: FieldProps):
        """
        Add Simple Back Field
        :param key:
        :param value:
        :param label: optional
        """
        self.backFields.append(Field(field_props))

    def add_auxiliary_field(self, field_props: FieldProps):
        """
        Add Simple Auxilary Field
        :param key:
        :param value:
        :param label: optional
        """
        self.auxiliaryFields.append(Field(field_props))

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
