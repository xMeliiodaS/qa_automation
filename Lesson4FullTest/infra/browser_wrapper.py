from selenium import webdriver
from infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider().load_config_json()

    def get_driver(self, url):
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "Firefox":
            self._driver = webdriver.Firefox()
        else:
            print("Browser does not exist")

        self._driver.get(url)
        return self._driver
