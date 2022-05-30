from pyteledantic.models import Bot, Message, MessageToSend, User, WebhookInfo
from pyteledantic.utils import base_method


def get_me(bot: Bot) -> User:
    url = f'https://api.telegram.org/bot{bot.token}/getMe'
    user = base_method(url, response_model=User)
    assert isinstance(user, User)
    return user


def get_webhook_info(bot: Bot) -> WebhookInfo:
    url = f'https://api.telegram.org/bot{bot.token}/getWebhookInfo'
    webhook_info = base_method(url, response_model=WebhookInfo)
    assert isinstance(webhook_info, WebhookInfo)
    return webhook_info


def set_webhook(bot: Bot, webhook_url: str) -> bool:
    url = 'https://api.telegram.org/bot{}/setWebhook?url={}'
    url = url.format(bot.token, webhook_url)
    result = base_method(url)
    assert isinstance(result, bool)
    return result


def delete_webhook(bot: Bot) -> bool:
    url = f'https://api.telegram.org/bot{bot.token}/deleteWebhook'
    result = base_method(url)
    assert isinstance(result, bool)
    return result


def send_message(bot: Bot, message: MessageToSend) -> Message:
    url = f'https://api.telegram.org/bot{bot.token}/sendMessage'
    msg = base_method(url,
                      method='POST',
                      params=message.dict(),
                      response_model=Message)
    assert isinstance(msg, Message)
    return msg
