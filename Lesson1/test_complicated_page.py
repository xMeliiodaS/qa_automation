import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/complicated-page")

buttons_count = len(driver.find_elements(By.XPATH, "//a[contains(text(), 'Button')]"))
print(buttons_count)

# for i in range(1, buttons_count+1):
#     driver.find_element(By.XPATH, f"//a[@class='et_pb_button et_pb_button_{i-1} et_pb_bg_layout_light']").click()
#     time.sleep(0.1)

driver.find_element(By.XPATH, "//li[contains(@class, 'et_pb_social_media_follow_network_0' )]"
                              "//a[@class='icon et_pb_with_border' and @title='Follow on Twitter']").click()

time.sleep(8)
while driver.current_url != "https://ultimateqa.com/complicated-page":
    driver.back()

driver.find_element(By.XPATH, "//li[contains(@class, 'et_pb_social_media_follow_network_1' )]"
                              "//a[@class='icon et_pb_with_border' and @title='Follow on Facebook']").click()

time.sleep(5)
while driver.current_url != "https://ultimateqa.com/complicated-page":
    driver.back()

driver.quit()
