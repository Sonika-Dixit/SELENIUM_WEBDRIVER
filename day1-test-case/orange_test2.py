''' 
open web browser(chrome)
open url: https://opensource-demo.orangehrmlive.com/
provide username(Admin)
provide password(admin123)
click on login
capture tittle of the home page.(actual title)
verify title of the page: "OrangeHRM" (expected)
close browser
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# using time.sleep for waits
# time.sleep(10)
# driver.find_element(By.NAME,'username').send_keys("Admin")
# time.sleep(5)
# driver.find_element(By.NAME,'password').send_keys("admin123")
# time.sleep(5)
# driver.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
# time.sleep(5)
# actual_title=driver.title
# expected_title="OrangeHRM"
# if actual_title==expected_title:
#     print("test passed")
# else:
#     print("test failed")


##using explicit waits

usr_name=(By.NAME,"username")
usr_name1=WebDriverWait(driver,10).until(ec.element_to_be_clickable(usr_name))
usr_name1.send_keys("Admin")
password=(By.NAME,"password")
password_1=WebDriverWait(driver,4).until(ec.element_to_be_clickable(password))
password_1.send_keys("admin123")


try:
    lgn=driver.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']")
    time.sleep(10)
    # lgn1=WebDriverWait(driver,20).until(ec.element_to_be_clickable(lgn))
    lgn.click()
except TimeoutError:
    print("time not sufficient to load this btn")
# finally:
#     driver.quit()




                                                             

