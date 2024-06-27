from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# driver.maximize_window()
driver.switch_to.frame("iframeResult")
textfiled1=driver.find_element(By.XPATH,"//*[@id='field1']")
textfiled1.clear()
textfiled1.send_keys("soni")
cpybtn=driver.find_element(By.XPATH,"/html/body/button")
action=ActionChains(driver)
action.double_click(cpybtn).perform()








