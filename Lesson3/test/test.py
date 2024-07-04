import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_remove_elements_page import AddRemoveElementsPage
from logic.challenging_dom_page import ChallengingDomPage
from logic.home_page import HomePage


class Test(unittest.TestCase):
    browser = BrowserWrapper()
    config = browser.config

    def test_add_remove_element(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_add_remove_link()

        time.sleep(0.5)
        add_remove_elements = AddRemoveElementsPage(driver)
        add_remove_elements.click_on_add_elements_counts(5)
        time.sleep(0.5)

        add_remove_elements.click_on_delete(3)
        time.sleep(1)

    def test_add_remove_asdelement(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_challenging_dom_link()

        time.sleep(0.5)
        cas = ChallengingDomPage(driver)
        cas.click_on_edit(5)
        time.sleep(0.5)

        time.sleep(153)
