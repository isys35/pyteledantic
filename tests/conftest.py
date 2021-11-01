import json
import os
import pathlib

import pytest as pytest

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
