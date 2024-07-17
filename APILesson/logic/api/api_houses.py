from infra.api.api_wrapper import APIWrapper


class APIHouses:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_houses_by_id(self, id):
        return self._request.get_request(f"https://wizard-world-api.herokuapp.com/Houses/{id}")
        # return self._request.get_request(f"{config}/Houses/{id}")
