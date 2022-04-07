from pyteledantic.models import Bot, User, WebhookInfo
from pyteledantic.utils import base_method



def get_me(bot: Bot) -> User:
    url = f'https://api.telegram.org/bot{bot.token}/getMe'
    return base_method(url, User)



def get_webhook_info(bot: Bot) -> WebhookInfo:
    url = f'https://api.telegram.org/bot{bot.token}/getWebhookInfo'
    return base_method(url, WebhookInfo)