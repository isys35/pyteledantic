from pyteledantic.exceptions.exceptions import TelegramAPIException
from pyteledantic.models import Bot, User
import requests


def get_me(bot: Bot) -> User:
    response = requests.get(f'https://api.telegram.org/bot{bot.token}/getMe')
    if response.status_code == 200:
        user = User(**response.json()['result'])
        return user
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
