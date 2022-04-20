from pyteledantic.methods import get_me, get_webhook_info, send_message, set_webhook, delete_webhook


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


def test_send_message(bot, message_to_send):
    message = send_message(bot, message_to_send)
    bot_as_user = get_me(bot)
    assert message.text == message_to_send.text
    assert message.from_user.id == bot_as_user.id