from pyteledantic.models import User


def test_user_model(user_json: dict):
    user = User(**user_json)
    assert user.id == 4123424123
    assert user.is_bot == False
    assert user.first_name == 'dimon'
