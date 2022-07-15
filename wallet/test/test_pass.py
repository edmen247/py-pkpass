from wallet.PassStyles.StoreCard import StoreCard
from wallet.Pass import Pass
from pytest import raises

card = StoreCard()

optional_pass_info = {
    "logo_text": "Sharks",
    "description": "some discription",
    "background_color": "rgb(38, 93, 205)",
    "foreground_color": "rgb(255, 255, 255)",
    "label_color": "rgb(189, 189, 189)",
    "serial_number": "12345"
}

pass_file = Pass(
    card,
    "pass_type_identifier",
    "team_identifier",
    "organization_name",
    **optional_pass_info
)

pass_file_as_json = b'{"storeCard": {"headerFields": [], "primaryFields": [], "secondaryFields": [], "backFields": [], "auxiliaryFields": []}, "description": "some discription", "formatVersion": 1, "organizationName": "organization_name", "passTypeIdentifier": "pass_type_identifier", "serialNumber": "12345", "teamIdentifier": "team_identifier", "backgroundColor": "rgb(38, 93, 205)", "foregroundColor": "rgb(255, 255, 255)", "labelColor": "rgb(189, 189, 189)", "logoText": "Sharks"}'
pass_file_manifest = b'{"pass.json": "3642041e506fd6a623a0bb00eb4fb8584e0264f9", "icon.png": "f6d49b2c2c03d2ef82e4d11841b60b58c7f18979", "logo.png": "f6d49b2c2c03d2ef82e4d11841b60b58c7f18979", "strip.png": "bf930d6ba371b42a461655c4b9719398e2068702"}'
shark_icon = "wallet/test/test_assets/_shark-icon.png"
sea_img = "wallet/test/test_assets/_sea.jpg"


def test_add_files_to_pass():

    pass_file.add_file("icon.png", open(shark_icon, "rb"))
    pass_file.add_file("logo.png", open(shark_icon, "rb"))

    pass_file.add_file("strip.png", open(sea_img, "rb"))

    files = [file for file in pass_file._files.keys()]

    assert files[0] == "icon.png"
    assert files[1] == "logo.png"
    assert files[2] == "strip.png"


def test_add_bad_files_to_pass():
    with raises(FileNotFoundError):
        pass_file.add_file("icon.png", open("wallet/test/logo.png", "rb"))
    with raises(FileNotFoundError):
        pass_file.add_file("icon.png", open("", "rb"))


def test_create_pass_json():
    pass_as_json = pass_file._create_pass_json()
    assert pass_as_json == pass_file_as_json


def test_create_manifest():
    pass_manifest = pass_file._create_manifest(pass_file_as_json)
    assert pass_manifest == pass_file_manifest


def test_json_dict():
    json_pass = pass_file.json_dict()
    assert json_pass == {
        "storeCard": {
            "headerFields": [],
            "primaryFields": [],
            "secondaryFields": [],
            "backFields": [],
            "auxiliaryFields": [],
        },
        "description": "some discription",
        "formatVersion": 1,
        "organizationName": "organization_name",
        "passTypeIdentifier": "pass_type_identifier",
        "serialNumber": "12345",
        "teamIdentifier": "team_identifier",
        "backgroundColor": "rgb(38, 93, 205)",
        "foregroundColor": "rgb(255, 255, 255)",
        "labelColor": "rgb(189, 189, 189)",
        "logoText": "Sharks",
    }
