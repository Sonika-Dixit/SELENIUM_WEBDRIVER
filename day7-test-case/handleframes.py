from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='all-packages-table']/div[2]/div[3]/a").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='class-summary.tabpanel']/div/div[151]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='navbar-top-firstrow']/li[8]/a").click()



time.sleep(5)
