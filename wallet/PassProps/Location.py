class Location:
    """
    Pass Location Object
    """

    def __init__(self, **kwargs):
        """
        Fill Location Object.

        :param latitude: Latitude Float
        :param longitude: Longitude Float
        :param altitude: optional
        :param distance: optional
        :param relevant_text: optional
        :return: Nothing

        """

        for name in ["latitude", "longitude", "altitude"]:
            try:
                setattr(self, name, float(kwargs[name]))
            except (ValueError, TypeError, KeyError):
                setattr(self, name, 0.0)
        if "distance" in kwargs:
            self.distance = kwargs["distance"]
        self.relevantText = kwargs.get("relevant_text", "")

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
