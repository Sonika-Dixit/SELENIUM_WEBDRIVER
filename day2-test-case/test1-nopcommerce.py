from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(4)

#finding element using id and name locators

# driver.find_element(By.ID,"small-searchterms").send_keys("cap")
# driver.find_element(By.NAME,"q").send_keys("cap")

#finding locators using link text and partial link text

# driver.find_element(By.LINK_TEXT,'Register').click()
# # time.sleep(3)

# driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
# time.sleep(5)

# driver.close() #it only closes the current browser
# driver.quit()  #it closes all the browsers 

##finding multiple elements or group of element or more than one element at a time

#1.using class

lst_of_grp=driver.find_elements(By.CLASS_NAME,'item-grid')
for item in lst_of_grp:
    print(item)
print(len(lst_of_grp))

# 2.using tagname
lst1=driver.find_elements(By.TAG_NAME,'a')
print(len(lst1))