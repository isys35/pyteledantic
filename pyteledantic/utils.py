import urllib
from requests_kerberos import HTTPKerberosAuth  # type: ignore
from urllib3.util import parse_url
import requests
from requests.exceptions import ProxyError


class HTTPAdapterWithProxyKerberosAuth(requests.adapters.HTTPAdapter):
    def proxy_headers(self, proxy):
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
        return result

    return wrapper
