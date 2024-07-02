import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Infra
driver = webdriver.Chrome()  # open a Chrome browser

# Infra   url -> Logic
driver.get("https://www.Google.com")

search_input = driver.find_element(By.CLASS_NAME, "gLFyf")

search_input.send_keys("Mr beast")
search_input.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()
