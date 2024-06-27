from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

minimum_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")

maximum_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print("location of sliders before moving .....")
print(minimum_slider.location)
print(maximum_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(minimum_slider,100,0).perform()
act.drag_and_drop_by_offset(maximum_slider,-39,0).perform()

print("location of sliders after moving .....")
print(minimum_slider.location)
print(maximum_slider.location)
