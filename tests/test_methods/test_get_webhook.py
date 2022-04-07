from pyteledantic.methods import get_webhook_info

def test_get_me(bot, webhook_false):
    assert webhook_false == get_webhook_info(bot)