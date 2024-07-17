import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.draw_a_card import APIDraw
from logic.api.shuffle_the_cards import APIShuffle


class TestAPIHarryPotter(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()

        self.api_request = APIWrapper()
        self.api_shuffle = APIShuffle(self.api_request)
        shuffle_result = self.api_shuffle.get_shuffle_the_deck(self.config)
        self.shuffle_body = shuffle_result.json()

    def test_shuffle_the_cards(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        print(self.shuffle_body)
        self.assertTrue(self.shuffle_body['success'])

    def test_draw_a_card(self):
        """
        Tests drawing cards from the deck by calling the API and validating the response.
        """
        api_draw = APIDraw(self.api_request)
        draw_result = api_draw.get_deck(self.config)
        draw_body = draw_result.json()
        print(draw_body)
        remaining_cards = self.shuffle_body['remaining']

        self.assertTrue(draw_result.ok)
        self.assertEqual(draw_body["remaining"], remaining_cards - int(self.config["draw_card"]))
