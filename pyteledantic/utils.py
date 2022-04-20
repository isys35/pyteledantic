from typing import Optional, Union
import urllib
from pydantic import BaseModel
from urllib3.util import parse_url
import requests
from requests.exceptions import ProxyError, SSLError

from pyteledantic.exceptions.exceptions import TelegramAPIException


class HTTPAdapterWithProxyKerberosAuth(requests.adapters.HTTPAdapter):
    def proxy_headers(self, proxy):
        from requests_kerberos import HTTPKerberosAuth  # type: ignore
        headers = {}
        auth = HTTPKerberosAuth()
        negotiate_details = auth.generate_request_header(None,
                                                         parse_url(proxy).host,
                                                         is_preemptive=True)
        headers['Proxy-Authorization'] = negotiate_details
        return headers


def proxy_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ProxyError:
            session = requests.Session()
            session.proxies = urllib.request.getproxies()
            session.mount('https://', HTTPAdapterWithProxyKerberosAuth())
            verify = False
            result = func(*args, session=session, verify=verify, **kwargs)
        except SSLError:
            verify = False
            result = func(*args, verify=verify, **kwargs)
        return result

    return wrapper


@proxy_handler
def base_method(
        url: str,
        method: str = 'GET',
        params: Optional[dict] = None,
        response_model: Optional[type[BaseModel]] = None,
        session: Optional[requests.Session] = None,
        verify: bool = True) -> Union[BaseModel, bool]:
    if not session:
        session = requests.Session()
    response = session.request(method, url, params=params, verify=verify)
    if response.status_code == 200:
        if response_model:
            resppone_pydantic = response_model(**response.json()['result'])
            return resppone_pydantic
        else:
            return response.json()['result']
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
