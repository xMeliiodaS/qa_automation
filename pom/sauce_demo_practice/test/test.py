import unittest
from sauce_demo_practice.infra.browser_wrapper import BrowserWrapper


class Test(unittest.TestCase):

    def asd(self):
        driver = BrowserWrapper().get_driver()