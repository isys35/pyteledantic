from typing import Optional

from pyteledantic.exceptions.exceptions import TelegramAPIException
from pyteledantic.models import Bot, User
import requests

from pyteledantic.utils import proxy_handler


@proxy_handler
def get_me(bot: Bot,
           session: Optional[requests.Session] = None,
           verify: bool = True) -> User:
    if not session:
        session = requests.Session()
    response = session.get(f'https://api.telegram.org/bot{bot.token}/getMe',
                           verify=verify)
    if response.status_code == 200:
        user = User(**response.json()['result'])
        return user
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
