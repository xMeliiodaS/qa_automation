import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider


class Test(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

