import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.draw_a_card import DrawCards
from logic.api.shuffle_the_cards import ShuffleTheCards


class TestAPIDrawCard(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.cards_shuffle = ShuffleTheCards(self.api_request)
        shuffle_result = self.cards_shuffle.get_deck(self.config)
        self.shuffle_body = shuffle_result.json()
        self.deck_id = self.shuffle_body["deck_id"]

    def test_draw_a_card(self):
        """
        Tests drawing cards from the deck by calling the API and validating the response.
        """
        draw_cards = DrawCards(self.api_request)
        draw_result = draw_cards.draw_cards(self.config["url"], self.config["num_of_draw_cards"],
                                            self.deck_id)
        draw_body = draw_result.json()

        print(draw_body)

        # Take the original remaining cards value before drawing cards
        remaining_cards = self.shuffle_body['remaining']

        self.assertTrue(draw_result.ok)
        self.assertEqual(draw_body["remaining"], remaining_cards - int(self.config["num_of_draw_cards"]))
