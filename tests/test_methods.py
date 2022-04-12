from pyteledantic.methods import get_me, get_webhook_info, set_webhook, delete_webhook


def test_get_me(bot, bot_as_user):
    assert bot_as_user == get_me(bot)


def test_set_webhook(bot):
    assert True == set_webhook(bot, 'https://google.com/')
    assert 'https://google.com/' == get_webhook_info(bot).url
    assert True == delete_webhook(bot)
    

def test_delete_webhook(bot):
    url_webhook = get_webhook_info(bot).url
    assert True == delete_webhook(bot)
    assert '' == get_webhook_info(bot).url
    assert True == set_webhook(bot, url_webhook)