from infra.api.api_wrapper import APIWrapper


class APIDraw:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_deck(self, config):
        url = f"{config['url']}/new/draw/?count={config['draw_card']}"
        return self._request.get_request(url)
