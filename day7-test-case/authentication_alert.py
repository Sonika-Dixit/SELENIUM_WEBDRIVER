from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='pass_div']/input[3]").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# # myalert.accept()
# time.sleep(4)

