from infra.api.api_wrapper import APIWrapper


class APIDraw:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_draw_the_card(self, config):
        """Requests to draw a specified number of cards from the deck.

        Args:
            config (dict): The configuration dictionary containing the URL and the number of cards to draw.

        Returns:
            Response: The response from the API.
        """
        url = f"{config['url']}/new/draw/?count={config['num_of_draw_cards']}"
        return self._request.get_request(url)
