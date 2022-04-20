from cgitb import text
import json
import os
import pathlib

import pytest as pytest

from pyteledantic.models import Bot, MessageToSend, User, WebhookInfo

MOCK_DIR = os.path.join(pathlib.Path(__file__).parent, 'mocks')


@pytest.fixture
def user_json():
    with open(os.path.join(MOCK_DIR, 'user.json')) as json_file:
        user_data = json.load(json_file)
    return user_data


@pytest.fixture
def chat_photo_json():
    with open(os.path.join(MOCK_DIR, 'chat_photo.json')) as json_file:
        user_data = json.load(json_file)
    return user_data


@pytest.fixture
def location_json():
    with open(os.path.join(MOCK_DIR, 'location.json')) as json_file:
        user_data = json.load(json_file)
    return user_data


@pytest.fixture
def bot():
    token = os.environ.get('TEST_BOT_TOKEN')
    return Bot(token=token)


@pytest.fixture
def bot_as_user():
    user = User(id=1773461202, is_bot=True, first_name='testing_bot', last_name=None, username='testing123212bot',
                language_code=None, can_join_groups=True, can_read_all_group_messages=False, supports_inline_queries=False)
    return user


@pytest.fixture
def message_to_send():
    message = MessageToSend(chat_id=1040023542, text='Тестовое сообщение')
    return message