class BarcodeFormat:
    """Barcode Format"""

    PDF417 = "PKBarcodeFormatPDF417"
    QR = "PKBarcodeFormatQR"
    AZTEC = "PKBarcodeFormatAztec"


class Barcode:
    """
    Barcode Field
    """

    def __init__(self, **kwargs):
        """
        Initiate Field

        :param message: Message or Payload for Barcdoe
        :param format: pdf417/ qr/ aztec
        :param encoding: Default utf-8
        :param alt_text: Optional Text displayed near the barcode
        """
        self.format = {
            "pdf417": BarcodeFormat.PDF417,
            "qr": BarcodeFormat.QR,
            "aztec": BarcodeFormat.AZTEC,
        }.get(kwargs["format"], "qr")
        self.message = kwargs["message"]
        self.messageEncoding = kwargs.get("encoding", "iso-8859-1")
        self.altText = kwargs.get("alt_text", "")

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
