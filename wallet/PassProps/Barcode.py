class BarcodeFormat:
    """Barcode Format"""

    PDF417 = "PKBarcodeFormatPDF417"
    QR = "PKBarcodeFormatQR"
    AZTEC = "PKBarcodeFormatAztec"


class Barcode:
    """
    Barcode Field
    """

    def __init__(self, message: str, qr_format=BarcodeFormat.QR, alt_text=''):
        """
        Initiate Field

        :param message: Message or Payload for Barcdoe
        :param format: pdf417/ qr/ aztec
        :param encoding: Default utf-8
        :param alt_text: Optional Text displayed near the barcode
        """
        self.format = qr_format
        self.message = message  # Required. Message or payload to be displayed
        self.messageEncoding = (
            "iso-8859-1"  # Required. Text encoding
        )
        self.altText = alt_text  # Optional. Text displayed near the barcode

    def json_dict(self):
        """Return dict object from class"""
        return self.__dict__
