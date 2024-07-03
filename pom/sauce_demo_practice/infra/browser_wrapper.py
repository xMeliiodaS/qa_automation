from selenium import webdriver


class BrowserWrapper:

    # Just to open the page
    @staticmethod
    def get_driver():
        temp_driver = webdriver.Chrome()
        temp_driver.get("URL")
        return temp_driver
