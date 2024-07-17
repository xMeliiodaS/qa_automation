import unittest

from infra.api.api_wrapper import APIWrapper
from infra.browser.configure_provider import ConfigProvider
from logic.api.draw_a_card import APIDraw
from logic.api.shuffle_the_cards import APIShuffle


class TestAPIHarryPotter(unittest.TestCase):

    def test_shuffle_the_cards(self):
        self.config = ConfigProvider.load_config_json()

        api_request = APIWrapper()
        api_house = APIShuffle(api_request)
        result = api_house.get_shuffle_the_deck(self.config)
        body = result.json()
        print(body)

        self.assertTrue(result.ok)

    def test_draw_a_card(self):
        self.config = ConfigProvider.load_config_json()

        api_request = APIWrapper()
        api_house = APIDraw(api_request)
        result = api_house.get_deck(self.config)
        body = result.json()
        print(body)

        self.assertTrue(result.ok)
        print(body["remaining"])
        print(52 - int(self.config["draw_card"]))
        self.assertEqual(body["remaining"], 52 - int(self.config["draw_card"]))
