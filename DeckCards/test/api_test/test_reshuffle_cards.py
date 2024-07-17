import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.draw_a_card import APIDraw
from logic.api.reshuffle_cards import ReshuffleCards
from logic.api.shuffle_the_cards import APIShuffle


class TestReshuffleCards(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()

        self.api_request = APIWrapper()
        self.api_shuffle = APIShuffle(self.api_request)
        shuffle_result = self.api_shuffle.get_deck(self.config)
        self.shuffle_body = shuffle_result.json()
        self.deck_id = self.shuffle_body['deck_id']

    def test_reshuffle_the_cards(self):
        """
        Tests reshuffling the deck by calling the API and validating the response.
        """
        # Arrange
        api_draw = APIDraw(self.api_request)
        draw_cards = api_draw.drwa_cards(self.config).json()

        # Reshuffling the remaining cards
        # Act
        reshuffle_cards = ReshuffleCards(self.api_request)
        reshuffle_result = reshuffle_cards.reshuffle(self.config, self.deck_id, True)
        reshuffle_body = reshuffle_result.json()

        # Assert
        self.assertTrue(reshuffle_result.ok)
        self.assertTrue(reshuffle_body['shuffled'])
        self.assertEqual(reshuffle_body['remaining'], self.shuffle_body["remaining"])
        self.assertNotEqual(reshuffle_body['remaining'], draw_cards['remaining'])
