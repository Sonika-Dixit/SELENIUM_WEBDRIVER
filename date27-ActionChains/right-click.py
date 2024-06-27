from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains 

driver=webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
btn=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
act=ActionChains(driver)
act.context_click(btn).perform()
time.sleep(3)
cpy_elmnt=driver.find_element(By.XPATH,"/html/body/ul/li[3]")
cpy_elmnt.click()
time.sleep(3)