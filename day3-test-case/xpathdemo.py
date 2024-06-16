from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
# time.sleep(2)
driver.maximize_window()
# time.sleep(2)

##absolute/full xpath
elmt1=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input")
elmt1.send_keys("Purse")
elmt2=driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/ul/li[1]/div/a/div[2] or @class='x6GwIv _2Ipp17']").click()



time.sleep(2)