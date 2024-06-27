from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/#the-internet-heroku-app")
# time.sleep(10)


##scroll page down by pixel

# driver.execute_script("window.scrollBy(0,5000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved: ",value)
# time.sleep(5)

## Scroll down page till the element is visible
# swab=driver.find_element(By.XPATH,"//*[@id='swag-labs']")
# driver.execute_script("arguments[0].scrollIntoView();",swab)
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved: ",value)


## Scroll page till end

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixel moved: ",value)

##scroll page up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")