import requests

from infra.api.api_wrapper import APIWrapper
from infra.api.response_wrapper import ResponseWrapper


class BrandNewDeck:
    def __init__(self, request: APIWrapper):
        self._request = request

    # @staticmethod
    # def post_brand_new_deck(url, data=None):
    #     response = requests.post(f"{url}/new/?", json=data)
    #     return ResponseWrapper(ok=response.ok, status=response.status_code,
    #                            data=response.json())

    def get_brand_new_deck(self, url, is_joker):
        url = f"{url}/new/"
        if is_joker:
            url += "?jokers_enabled=true"
        return self._request.get_request(url)
