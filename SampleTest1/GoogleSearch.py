from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("/Users/macbookpro/PycharmProjects/PythonProjectAutomation/drivers/chromedriver 2")
driver.get("https://www.google.com")
driver.maximize_window()
title = driver.title
print(title)
driver.find_element_by_name("q").send_keys("facebooklogin")
time.sleep(4)

driver.find_element_by_name("btnK").click()
driver.close()
#driver.quit()