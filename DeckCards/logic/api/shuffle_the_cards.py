from infra.api.api_wrapper import APIWrapper


class APIShuffle:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_shuffle_the_deck(self, config):
        url = f"{config['url']}/new/shuffle/?deck_count={config['deck_count']}"
        return self._request.get_request(url)
