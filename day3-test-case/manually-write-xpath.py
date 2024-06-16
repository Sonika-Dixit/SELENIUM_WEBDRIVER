from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

## manually written relative xpath
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")

## manually written relative xpath
# driver.find_element(By.XPATH,"//button[@name='login']").click()
# time.sleep(3)