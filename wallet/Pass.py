import decimal
import hashlib
from io import BytesIO
import json
import subprocess
import zipfile
import tempfile

from .exceptions import PassParameterException


def pass_handler(obj):
    """Pass Handler"""
    if hasattr(obj, "json_dict"):
        return obj.json_dict()
    # For Decimal latitude and logitude etc.
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    return obj


class Pass:
    def __init__(self, **kwargs):
        """
        Prepare Pass
        :params pass_information:
        :params pass_type_identifier:
        :params organization_name:
        :params team_identifier:
        """

        self._files = {}  # Holds the files to include in the .pkpass
        self._hashes = {}  # Holds the SHAs of the files array

        # Standard Keys

        # Required. Team identifier of the organization that originated and
        # signed the pass, as issued by Apple.
        self.teamIdentifier = kwargs["team_identifier"]
        # Required. Pass type identifier, as issued by Apple. The value must
        # correspond with your signing certificate. Used for grouping.
        self.passTypeIdentifier = kwargs["pass_type_identifier"]
        # Required. Display name of the organization that originated and
        # signed the pass.
        self.organizationName = kwargs["organization_name"]
        # Required. Serial number that uniquely identifies the pass.
        self.serialNumber = ""
        # Required. Brief description of the pass, used by the iOS
        # accessibility technologies.
        self.description = ""
        # Required.
        self.formatVersion = 1

        # Visual Appearance Keys
        self.backgroundColor = None  # Optional. Background color of the pass
        self.foregroundColor = None  # Optional. Foreground color of the pass,
        self.labelColor = None  # Optional. Color of the label text
        self.logoText = None  # Optional. Text displayed next to the logo
        self.barcode = None  # Optional. Information specific to barcodes.
        self.barcodes = []

        # Optional. If true, the strip image is displayed
        self.suppressStripShine = False

        # Web Service Keys

        # Optional. If present, authenticationToken must be supplied
        self.webServiceURL = None
        # The authentication token to use with the web service
        self.authenticationToken = None

        # Relevance Keys

        # Optional. Locations where the pass is relevant.
        # For example, the location of your store.
        self.locations = []
        # Optional. IBeacons data
        self.ibeacons = []
        # Optional. Date and time when the pass becomes relevant
        self.relevantDate = None

        # Optional. A list of iTunes Store item identifiers for
        # the associated apps.
        self.associatedStoreIdentifiers = None
        self.appLaunchURL = None
        # Optional. Additional hidden data in json for the passbook
        self.userInfo = None

        self.exprirationDate = None
        self.voided = None

        self.passInformation = kwargs["pass_information"]

    def add_file(self, name, file_handle):
        """
        Add file to the file
        :params name: String name
        :params file_handle: File Handle
        """
        self._files[name] = file_handle.read()

    # Creates the actual .pkpass file
    def create(
        self,
        certificate,
        key,
        wwdr_certificate,
        password=False,
        file_name=None,
        filemode=True,
    ):
        """
        Create .pkass File
        """
        pass_json = self._create_pass_json()
        manifest = self._create_manifest(pass_json)
        signature = self._create_signature(
            manifest, certificate, key, wwdr_certificate, password, filemode
        )
        if not file_name:
            file_name = BytesIO()
        datei = self._create_zip(
            pass_json,
            manifest,
            signature,
            file_name=file_name
        )
        return datei

    def _create_pass_json(self):
        """
        Create Json Pass Files
        """
        return json.dumps(self, default=pass_handler).encode("utf-8")

    def _create_manifest(self, pass_json):
        """
        Creates the hashes for the files and adds them
        into a json string
        """
        # Creates SHA hashes for all files in package
        self._hashes["pass.json"] = hashlib.sha1(pass_json).hexdigest()
        for filename, filedata in self._files.items():
            self._hashes[filename] = hashlib.sha1(filedata).hexdigest()
        return json.dumps(self._hashes).encode("utf-8")

    def _create_signature(
        self, manifest, certificate, key, wwdr_certificate, password, filemode
    ):
        """Create and Save Signature"""
        if not filemode:
            # Use Tempfile
            cert_file = tempfile.NamedTemporaryFile(mode="w")
            cert_file.write(certificate)
            cert_file.flush()
            key_file = tempfile.NamedTemporaryFile(mode="w")
            key_file.write(key)
            key_file.flush()
            wwdr_file = tempfile.NamedTemporaryFile(mode="w")
            wwdr_file.write(wwdr_certificate)
            wwdr_file.flush()
            certificate = cert_file.name
            key = key_file.name
            wwdr_certificate = wwdr_file.name

        openssl_cmd = [
            "openssl",
            "smime",
            "-binary",
            "-sign",
            "-certfile",
            wwdr_certificate,
            "-signer",
            certificate,
            "-inkey",
            key,
            "-outform",
            "DER",
            "-passin",
            f"pass:{password}",
        ]

        process = subprocess.Popen(
            openssl_cmd,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        process.stdin.write(manifest)
        der, error = process.communicate()
        if process.returncode != 0:
            raise Exception(error)

        return der

    # Creates .pkpass (zip archive)
    def _create_zip(self, pass_json, manifest, signature, file_name=None):
        """
        Creats .pkass ZIP Archive
        """
        z_file = zipfile.ZipFile(file_name or "pass.pkpass", "w")
        z_file.writestr("signature", signature)
        z_file.writestr("manifest.json", manifest)
        z_file.writestr("pass.json", pass_json)
        for filename, filedata in self._files.items():
            z_file.writestr(filename, filedata)
        z_file.close()
        return file_name

    def json_dict(self):
        """
        Return Pass as JSON Dict
        """
        simple_fields = [
            "description",
            "formatVersion",
            "organizationName",
            "passTypeIdentifier",
            "serialNumber",
            "teamIdentifier",
            "suppressStripShine" "relevantDate",
            "backgroundColor",
            "foregroundColor",
            "labelColor",
            "logoText",
            "ibeacons",
            "userInfo",
            "voided",
            "associatedStoreIdentifiers",
            "appLaunchURL",
            "exprirationDate",
            "webServiceURL",
            "authenticationToken",
        ]
        data = {}
        data[self.passInformation.jsonname] = self.passInformation.json_dict()
        for field in simple_fields:
            if hasattr(self, field):
                content = getattr(self, field)
                if content:
                    data[field] = content

        if self.barcodes:
            data["barcodes"] = []
            for barcode in self.barcodes:
                data["barcodes"].append(barcode.json_dict())

        if self.locations:
            data["locations"] = []
            for location in self.locations:
                data["locations"].append(location.json_dict())
            if len(data["locations"]) >= 10:
                raise PassParameterException("Field locations has<10 entries")

        if self.ibeacons:
            data["ibeacons"] = []
            for ibeacon in self.ibeacons:
                data["ibeacons"].append(ibeacon.json_dict())

        requied_fields = [
            "description",
            "formatVersion",
            "organizationName",
            "organizationName",
            "serialNumber",
            "teamIdentifier",
        ]
        for field in requied_fields:
            if field not in data:
                raise PassParameterException(f"Field {field} missing")
        return data
