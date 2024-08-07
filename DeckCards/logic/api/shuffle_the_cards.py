from infra.api.api_wrapper import APIWrapper


class ShuffleTheCards:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_deck(self, config):
        """Requests to shuffle the deck with a specified number of decks.

        Args:
            config (dict): The configuration dictionary containing the URL and the number of decks to shuffle.

        Returns:
            Response: The response from the API.
        """
        url = f"{config['url']}/new/shuffle/?deck_count={config['deck_count']}"
        return self._request.get_request(url)

    def post_deck(self, config):
        """Requests to shuffle the deck with a specified number of decks using a POST request.

        Args:
            config (dict): The configuration dictionary containing the URL and the number of decks to shuffle.

        Returns:
            Response: The response from the API.
        """
        url = f"{config['url']}/new/shuffle/"
        body = {"deck_count": config['deck_count']}
        return self._request.post_request(url, body)
