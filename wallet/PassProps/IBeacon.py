class IBeacon:
    """iBeacon"""

    def __init__(self, **kwargs):
        """
        Create Beacon
        :param proximity_uuid:
        :param major:
        :param minor:
        :param relevant_text: Option Text shown when near the ibeacon
        """

        self.proximityUUID = kwargs["proximity_uuid"]
        self.major = kwargs["major"]
        self.minor = kwargs["minor"]

        self.relevantText = kwargs.get("relevant_text", "")

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
