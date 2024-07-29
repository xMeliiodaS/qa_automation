import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.shuffle_the_cards import ShuffleTheCards


class TestAPIShuffleCard(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()

        self.api_request = APIWrapper()

    def test_shuffle_the_cards(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        api_shuffle = ShuffleTheCards(self.api_request)
        shuffle_result = api_shuffle.get_deck(self.config)
        shuffle_body = shuffle_result.json()

        print(shuffle_body)
        self.assertTrue(shuffle_body['success'])

