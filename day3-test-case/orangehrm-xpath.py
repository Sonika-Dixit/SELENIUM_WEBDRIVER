from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
# time.sleep(5)

btn=(By.XPATH,"//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/a/button")
wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable(btn)).click()

time.sleep(2)

