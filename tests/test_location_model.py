from pyteledantic.models import Location


def test_chat_photo_model(location_json: dict):
    location = Location(**location_json)
    assert location.longitude == 54.293232
    assert location.latitude == 24.2333443