import requests


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, body=None):
        """Sends a GET request to the specified URL with an optional body.

        Args:
            url (str): The URL to send the GET request to.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the GET request.
        """
        return requests.get(url, json=body)

    @staticmethod
    def post_request(url, body=None):
        """Sends a POST request to the specified URL with an optional body.

        Args:
            url (str): The URL to send the POST request to.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the POST request.
        """
        return requests.post(url, json=body)

