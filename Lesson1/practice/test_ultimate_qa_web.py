from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

driver.find_element(By.CLASS_NAME, "buttonClass").click()
driver.implicitly_wait(1)
success = driver.find_element(By.CLASS_NAME, "entry-title")
print(success.text)
driver.back()

driver.implicitly_wait(1)

driver.find_element(By.NAME, "button1").click()
driver.implicitly_wait(1)
success = driver.find_element(By.XPATH, "//h1[contains(text(), 'Button success')]")
print(success.text)
driver.back()

driver.implicitly_wait(1)

driver.find_element(By.XPATH, "//a[contains(text(), 'Go to login page')]").click()
driver.find_element(By.ID, "user[email]").send_keys("Bahaa.abozlf57@gmail.com")
driver.find_element(By.ID, "user[password]").send_keys("HiiGuys912")
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()
driver.implicitly_wait(1)
failed = driver.find_element(By.CLASS_NAME, "form-error__list-item")
print(failed.text)
driver.back()

if driver.current_url != "https://ultimateqa.com/simple-html-elements-for-automation/":
    driver.back()

driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//input[@name='gender'][1]").click()
driver.find_element(By.XPATH, "//input[@name='vehicle'][1]").click()
option = driver.find_element(By.XPATH, "//option[contains(text(), Audi)][4]")
option.click()
print(option.is_selected())

driver.find_element(By.XPATH, "//a[contains(text(), 'Tab 2')]").click()
table_content = driver.find_element(By.XPATH, "//div[contains(text(), 'Tab 2')]").text
print(table_content)

driver.implicitly_wait(1)

