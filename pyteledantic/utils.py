from typing import Optional, Union
from pydantic import BaseModel
import requests

from pyteledantic.exceptions.exceptions import TelegramAPIException


def base_method(
        url: str,
        method: str = 'GET',
        params: Optional[dict] = None,
        response_model: Optional[type[BaseModel]] = None) -> Union[BaseModel, bool]:
    session = requests.Session()
    response = session.request(method, url, params=params)
    if response.status_code == 200:
        if response_model:
            response_pydantic = response_model(**response.json()['result'])
            return response_pydantic
        else:
            return response.json()['result']
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
