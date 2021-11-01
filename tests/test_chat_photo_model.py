from pyteledantic.models import ChatPhoto


def test_chat_photo_model(chat_photo_json: dict):
    user = ChatPhoto(**chat_photo_json)
    assert user.small_file_id == "12qwe"
    assert user.small_file_unique_id == "10uew"
    assert user.big_file_id == "10uew"
    assert user.big_file_unique_id == "45yer"