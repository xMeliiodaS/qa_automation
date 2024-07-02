import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Infra
driver = webdriver.Chrome()  # open a Chrome browser

# Infra   url -> Logic
driver.get("https://www.youtube.com/")

# Logic
search_input = driver.find_element(By.NAME, "search_query")
search_input.send_keys("mrbeast")
search_input.send_keys(Keys.RETURN)

time.sleep(10)
# Infra
driver.quit()
