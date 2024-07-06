import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_remove_elements_page import AddRemoveElementsPage
from logic.challenging_dom_page import ChallengingDomPage
from logic.check_boxes_page import CheckBoxesPage
from logic.context_menu_page import ContextMenuPage
from logic.drag_and_drop_page import DragAndDrop
from logic.dropdown_page import DropdownPage
from logic.dynamic_content_page import DynamicContentPage
from logic.dynamic_controls_page import DynamicControlsPage
from logic.home_page import HomePage


class Test(unittest.TestCase):
    config = BrowserWrapper().config
    driver = BrowserWrapper().get_driver(config["base_url"])

    def test_add_remove_element(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_add_remove_link()

        time.sleep(0.5)
        add_remove_elements = AddRemoveElementsPage(self.driver)
        add_remove_elements.click_on_add_elements_counts(5)
        time.sleep(0.5)

        add_remove_elements.click_on_delete(3)
        time.sleep(1)
        self.driver.quit()

    def test_challenging_dom(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_challenging_dom_link()

        time.sleep(0.5)
        cas = ChallengingDomPage(self.driver)
        cas.click_on_edit(5)
        time.sleep(0.5)
        self.driver.quit()

    def test_challenging_dom_a(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_checkboxes_link()

        time.sleep(0.5)
        cb = CheckBoxesPage(self.driver)
        cb.click_on_all_checkboxes()
        self.driver.quit()

    def test_context_menu(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_context_menu_link()

        time.sleep(0.5)
        cmp = ContextMenuPage(self.driver)
        cmp.right_click_on_context_menu()
        self.driver.quit()

    def test_drag_and_drop_items(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_drag_and_drop_link()

        time.sleep(0.5)
        drag_drop = DragAndDrop(self.driver)
        drag_drop.drag_first_item_to_second_item()
        time.sleep(4)
        drag_drop.drag_second_item_to_first_item()
        self.driver.quit()

    def test_select_dropdown(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_dropdown_link()

        time.sleep(0.5)
        dp = DropdownPage(self.driver)
        dp.select_dropdown_by_value()
        time.sleep(4)
        dp.select_dropdown_by_index(2)
        self.driver.quit()

    def test_dynamic_content_text(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_content_link()

        time.sleep(0.5)
        dcp = DynamicContentPage(self.driver)

        time.sleep(1)
        print(dcp.get_dynamic_content_text())
        dcp.click_on_here_button()
        time.sleep(1)
        print(dcp.get_dynamic_content_text())
        self.driver.quit()

    def test_dynamic_content_image(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_content_link()

        time.sleep(0.5)
        dcp = DynamicContentPage(self.driver)

        time.sleep(1)
        print(dcp.get_image_src())
        dcp.click_on_here_button()
        time.sleep(1)
        print(dcp.get_image_src())
        self.driver.quit()

    def test_dynamic_controls_checkbox(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_controls_link()

        time.sleep(0.5)
        dcp = DynamicControlsPage(self.driver)

        time.sleep(1)
        dcp.click_on_checkbox()
        time.sleep(1)
        dcp.click_on_remove_button()
        time.sleep(1)
        dcp.click_on_checkbox_forced()
        time.sleep(5)
        self.driver.quit()

    def test_dynamic_controls_input(self):
        time.sleep(0.1)
        home_page = HomePage(self.driver)
        home_page.click_on_dynamic_controls_link()

        time.sleep(0.5)
        dcp = DynamicControlsPage(self.driver)

        time.sleep(1)
        dcp.click_on_checkbox()
        time.sleep(1)
        dcp.click_on_remove_button()
        time.sleep(1)
        dcp.click_on_checkbox_forced()
        time.sleep(5)
        self.driver.quit()

