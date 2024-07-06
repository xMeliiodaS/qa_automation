import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_remove_elements_page import AddRemoveElementsPage
from logic.challenging_dom_page import ChallengingDomPage
from logic.check_boxes_page import CheckBoxesPage
from logic.context_menu_page import ContextMenuPage
from logic.drag_and_drop_page import DragAndDrop
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

    def test_challenging_dom(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_challenging_dom_link()

        time.sleep(0.5)
        cas = ChallengingDomPage(driver)
        cas.click_on_edit(5)
        time.sleep(0.5)

        time.sleep(153)

    def test_challenging_dom(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_checkboxes_link()

        time.sleep(0.5)
        cb = CheckBoxesPage(driver)
        cb.click_on_all_checkboxes()

        time.sleep(153)

    def test_context_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_context_menu_link()

        time.sleep(0.5)
        cb = ContextMenuPage(driver)
        cb.right_click_on_context_menu()

        time.sleep(153)

    def test_drag_and_drop_items(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_drag_and_drop_link()

        time.sleep(0.5)
        cb = DragAndDrop(driver)
        cb.drag_first_item_to_second_item()
        time.sleep(4)
        cb.drag_second_item_to_first_item()

        time.sleep(153)
