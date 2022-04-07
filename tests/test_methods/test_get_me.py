from pyteledantic.methods import get_me

def test_get_me(bot, bot_as_user):
    assert bot_as_user == get_me(bot)