from typing import Optional, Union
import requests
from typing import Type

from pydantic import BaseModel
from requests import Response

from pyteledantic.exceptions.exceptions import TelegramAPIException


def get_response(url: str,
                 method: str = 'GET',
                 params: Optional[dict] = None) -> Response:
    session = requests.Session()
    response = session.request(method, url, params=params)
    if response.status_code == 200:
        return response
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)


def base_method(
        url: str,
        method: str = 'GET',
        params: Optional[dict] = None,
        response_model: Optional[Type[BaseModel]] = None) -> Union[BaseModel, bool]:
    response = get_response(url, method, params)
    if response_model:
        response_pydantic = response_model(**response.json()['result'])
        return response_pydantic
    else:
        return response.json()['result']
