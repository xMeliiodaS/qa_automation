import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.draw_a_card import DrawCards
from logic.api.reshuffle_cards import ReshuffleCards
from logic.api.shuffle_the_cards import ShuffleTheCards


class TestReshuffleCards(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()

        self.api_request = APIWrapper()
        self.api_shuffle = ShuffleTheCards(self.api_request)
        shuffle_result = self.api_shuffle.get_deck(self.config)
        self.shuffle_body = shuffle_result.json()
        self.deck_id = self.shuffle_body['deck_id']

        api_draw = DrawCards(self.api_request)
        self.draw_cards_body = api_draw.draw_cards(self.config["url"], self.config["num_of_draw_cards"],
                                                   self.deck_id).json()

    def test_reshuffle_the_cards(self):
        """
        Tests reshuffling the deck by calling the API and validating the response.
        """
        # Arrange
        is_remaining = True

        # Reshuffling the remaining cards
        # Act
        reshuffle_cards = ReshuffleCards(self.api_request)
        reshuffle_result = reshuffle_cards.reshuffle(self.config["url"], self.deck_id, is_remaining)
        reshuffle_body = reshuffle_result.json()

        # Assert
        self.assertTrue(reshuffle_result.ok)
        self.assertTrue(self.deck_id, reshuffle_body["deck_id"])
        self.assertTrue(reshuffle_body['shuffled'])
        if not is_remaining:
            self.assertEqual(reshuffle_body['remaining'], self.shuffle_body["remaining"])
        else:
            self.assertEqual(reshuffle_body['remaining'], self.draw_cards_body['remaining'])
