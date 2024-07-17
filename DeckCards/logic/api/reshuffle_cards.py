from infra.api.api_wrapper import APIWrapper


class ReshuffleCards:
    def __init__(self, request: APIWrapper):
        self._request = request

    def reshuffle(self, config, deck_id, remaining=False):
        """Requests to reshuffle the cards in the specified deck.

        Args:
            deck_id (str): The ID of the deck to reshuffle.
            remaining (bool): If True, only shuffle the remaining cards in the deck.

        Returns:
            Response: The response from the API.
        """
        url = f"{config['url']}/{deck_id}/shuffle"
        if remaining:
            url += "/?remaining=true"
        return self._request.get_request(url)
