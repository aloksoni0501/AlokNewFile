from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("/Users/macbookpro/PycharmProjects/PythonProjectAutomation/drivers/chromedriver 2")
driver.get("https://www.facebook.com")
driver.maximize_window()
title = driver.title
print(title)
driver.find_element_by_name("firstname").send_keys("alok")
driver.find_element_by_name("lastname").send_keys("jain")
driver.find_element_by_id("u_0_q").send_keys("alok0505@gmail.com")
driver.find_element_by_id("u_0_t").send_keys("alok0505@gmail.com")
driver.find_element_by_id("u_0_x").send_keys("alok@123")

#for drop down fields
Select(driver.find_element_by_xpath("//select[@id='day']")).select_by_value('1')
Select(driver.find_element_by_xpath("//select[@id='month']")).select_by_index(1)
Select(driver.find_element_by_xpath("//select[@id='year']")).select_by_value('1999')
time.sleep(5)

driver.find_element_by_xpath("//input[@id='u_0_6']").click()
time.sleep(4)
driver.find_element_by_xpath("//button[@id='u_0_15']").click()

#assert "Facebook – log in or sign up" in title
#driver.maximize_window()

driver.quit()