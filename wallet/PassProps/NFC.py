class NFC:
    def __init__(
        self, encryption_public_key, message, requires_authentication=False
    ) -> None:
        self.encryptionPublicKey = encryption_public_key
        self.message = message
        self.requiresAuthentication = requires_authentication

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
