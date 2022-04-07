from typing import Optional, Union
import urllib
from urllib3.util import parse_url
import requests
from requests.exceptions import ProxyError, SSLError

from pyteledantic.exceptions.exceptions import TelegramAPIException
from pyteledantic.models import User, WebhookInfo


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
        response_model: Union[User, WebhookInfo],
        session: Optional[requests.Session] = None,
        verify: bool = True) -> Union[User, WebhookInfo]:
    if not session:
        session = requests.Session()
    response = session.get(url, verify=verify)
    if response.status_code == 200:
        resppone_pydantic = response_model(**response.json()['result'])
        return resppone_pydantic
    else:
        description = response.json()['description']
        raise TelegramAPIException(description)
