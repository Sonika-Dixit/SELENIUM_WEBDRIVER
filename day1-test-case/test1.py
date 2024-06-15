''' 
open web browser(chrome)
open url: https://admin-demo.nopcommerce.com/login
provide email
provide password
click on login
capture tittle of the dashboard page.
verify title of the page: "Dashboard / nopCommerce administration" (expected)
close browser
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

email_locator=(By.ID,'Email')
wait = WebDriverWait(driver, 2)
element1 = wait.until(EC.visibility_of_element_located(email_locator))
element1.clear()
element1.send_keys("admin@yourstore.com")
password_locator=(By.ID,'Password')
wait=WebDriverWait(driver,2)
element2=wait.until(EC.visibility_of_element_located(password_locator))
element2.clear()
element2.send_keys("admin")
logn_btn=(By.XPATH,"//button[@class='button-1 login-button']")
element3=WebDriverWait(driver,3).until(EC.element_to_be_clickable(logn_btn))
element3.click()
# driver.get("https://admin-demo.nopcommerce.com/admin/")
title_1=WebDriverWait(driver, 10).until(EC.title_is("Dashboard / nopCommerce administration"))
if title_1:
    print("done")
else:
    print("false")
driver.quit()


