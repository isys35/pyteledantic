from pyteledantic.models import Bot, User, WebhookInfo
from pyteledantic.utils import base_method


def get_me(bot: Bot) -> User:
    url = f'https://api.telegram.org/bot{bot.token}/getMe'
    return base_method(url, User)


def get_webhook_info(bot: Bot) -> WebhookInfo:
    url = f'https://api.telegram.org/bot{bot.token}/getWebhookInfo'
    return base_method(url, WebhookInfo)


def set_webhook(bot: Bot, webhook_url: str) -> bool:
    url = 'https://api.telegram.org/bot{}/setWebhook?url={}'
    url = url.format(bot.token, webhook_url)
    return base_method(url)


def delete_webhook(bot: Bot) -> bool:
    url = f'https://api.telegram.org/bot{bot.token}/deleteWebhook'
    return base_method(url)
