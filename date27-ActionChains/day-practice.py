from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

##scroll till double click
click_element=driver.find_element(By.XPATH,"//*[@id='HTML10']/h2")
driver.execute_script("arguments[0].scrollIntoView();",click_element)
time.sleep(2)


action=ActionChains(driver)
##double click
element1=driver.find_element(By.XPATH,"//*[@id='field1']")
element1.clear()
element1.send_keys("soni")

btn=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
action.context_click(btn)
# time.sleep(10)
time.sleep(10)

##drag and drop
src=driver.find_element(By.XPATH,"//*[@id='draggable']/p")
target=driver.find_element(By.XPATH,"//*[@id='droppable']")
action.drag_and_drop(src,target)
# time.sleep(10)
time.sleep(2)
##slider
slider=driver.find_element(By.XPATH,"//*[@id='slider']/span")
action.drag_and_drop_by_offset(slider,40,0)
time.sleep(3)
