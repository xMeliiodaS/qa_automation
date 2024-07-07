import time
import unittest
from infra.browser_wrapper import BrowserWrapper

class Test(unittest.TestCase):
    config = BrowserWrapper().config
    driver = BrowserWrapper().get_driver(config["base_url"])


