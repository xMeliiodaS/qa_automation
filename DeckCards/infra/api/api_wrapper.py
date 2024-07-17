import requests
from infra.browser.configure_provider import ConfigProvider


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, body=None):
        return requests.get(url, json=body)
