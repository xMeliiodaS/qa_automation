from infra.api.api_wrapper import APIWrapper


class DrawCards:
    def __init__(self, request: APIWrapper):
        self._request = request

    def draw_cards(self, url, cards_count, deck_id):
        """Requests to draw a specified number of cards from the deck.
        Returns:
            Response: The response from the API.
        """
        url = f"{url}/{deck_id}/draw/?count={cards_count}"
        return self._request.get_request(url)
