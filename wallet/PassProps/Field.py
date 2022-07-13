from .Alignment import Alignment
from .DateStyle import DateStyle
from .NumberStyle import NumberStyle


class Field:
    """Wallet Text Field"""

    def __init__(self, **kwargs):
        """
         Initiate Field

        :param key: The key must be unique within the scope
        :param value: Value of the Field
        :param attributed_value: Optional. Attributed value of the field.
        :param label: Optional Label Text for field
        :param change_message: Optional. update message
        :param text_alignment: left/ center/ right, justified, natural
        :return: Nothing

        """

        self.key = kwargs["key"]
        if "attributed_value" in kwargs:
            self.attributedValue = kwargs["attributed_value"]
        self.value = kwargs["value"]
        self.label = kwargs.get("label", "")
        if "change_message" in kwargs:
            self.changeMessage = kwargs[
                "change_message"
            ]  # Don't Populate key if not needed
        self.textAlignment = {
            "left": Alignment.LEFT,
            "center": Alignment.CENTER,
            "right": Alignment.RIGHT,
            "justified": Alignment.JUSTIFIED,
            "natural": Alignment.NATURAL,
        }.get(kwargs.get("text_alignment", "left"))

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__


class DateField(Field):
    """Wallet Date Field"""

    def __init__(self, **kwargs):
        """
        Initiate Field

        :param key: The key must be unique within the scope
        :param value: Value of the Field
        :param label: Optional Label Text for field
        :param change_message: Optional. Supdate message
        :param text_alignment: left/ center/ right, justified, natural
        :param date_style: none/short/medium/long/full
        :param time_style: none/short/medium/long/full
        :param is_relativ: True/False
        """

        super(DateField, self).__init__(**kwargs)
        styles = {
            "none": DateStyle.NONE,
            "short": DateStyle.SHORT,
            "medium": DateStyle.MEDIUM,
            "long": DateStyle.LONG,
            "full": DateStyle.FULL,
        }

        self.dateStyle = styles.get(kwargs.get("date_style", "short"))
        self.timeStyle = styles.get(kwargs.get("time_style", "short"))
        self.isRelative = kwargs.get("is_relativ", False)

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__


class NumberField(Field):
    """Number Field"""

    def __init__(self, **kwargs):
        """
        Initiate Field

        :param key: The key must be unique within the scope
        :param value: Value of the Field
        :param label: Optional Label Text for field
        :param change_message: Optional. update message
        :param text_alignment: left/ center/ right, justified, natural
        :param number_style: decimal/percent/scientific/spellout.
        """

        super(NumberField, self).__init__(**kwargs)
        self.numberStyle = {
            "decimal": NumberStyle.DECIMAL,
            "percent": NumberStyle.PERCENT,
            "scientific": NumberStyle.SCIENTIFIC,
            "spellout": NumberStyle.SPELLOUT,
        }.get(kwargs.get("number_style", "decimal"))
        self.value = float(self.value)

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__


class CurrencyField(Field):
    """Currency Field"""

    def __init__(self, **kwargs):
        """
        Initiate Field

        :param key: The key must be unique within the scope
        :param value: Value of the Field
        :param label: Optional Label Text for field
        :param change_message: Optional. update message
        :param text_alignment: left/ center/ right, justified, natural
        :param currency_code: ISO 4217 currency Code
        """

        super(CurrencyField, self).__init__(**kwargs)
        self.currencyCode = kwargs["currency_code"]
        self.value = float(self.value)

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
