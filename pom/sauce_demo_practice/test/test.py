import time
import unittest
from sauce_demo_practice.infra.browser_wrapper import BrowserWrapper
from sauce_demo_practice.infra.config_provider import ConfigProvider
from sauce_demo_practice.logic.inventory_page import InventoryPage
from sauce_demo_practice.logic.login_page import LoginPage
from sauce_demo_practice.logic.shopping_cart import ShoppingCart


class Test(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def test_login_successfully(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])

        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")

        driver.implicitly_wait(2)

        inventory_page = InventoryPage(driver)
        result = inventory_page.header_text_string()
        print(result)

    def test_login_unsuccessful(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user345", "34534ewr")

        time.sleep(5)

        inventory_page = InventoryPage(driver)
        result = inventory_page.header_text_string()
        print(result)

    def test_add_item_to_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")

        time.sleep(1)

        inventory_page = InventoryPage(driver)
        inventory_page.add_three_items_to_cart()
        time.sleep(1)

        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_cart_button()
        driver.quit()
