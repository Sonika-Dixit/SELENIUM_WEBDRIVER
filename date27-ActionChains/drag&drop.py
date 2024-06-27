from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/drag-and-drop-demo.html")
driver.maximize_window()
source1=driver.find_element(By.XPATH,"//*[@id='todrag']/span[4]")
source2=driver.find_element(By.XPATH,"//*[@id='todrag']/span[1]")
target=driver.find_element(By.XPATH,"//*[@id='mydropzone']")

act=ActionChains(driver)
act.drag_and_drop(source1,target)
act.drag_and_drop(source2,target)
time.sleep(10)











