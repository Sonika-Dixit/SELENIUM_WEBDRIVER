from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)
##tag and id combination
##using css selector as: tag and id: synatx: tag#id (or you can use id also like #id ,tag is optaional)

# driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,'#email').send_keys("abc")

##tag and class combination
# driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('xyc')
# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('soni')

#combination of tag and attribute :synatx: tag[attribute=value]

# driver.find_element(By.CSS_SELECTOR,'input[data-testid="royal_email"]').send_keys('soni')
# driver.find_element(By.CSS_SELECTOR,'[data-testid="royal_email"]').send_keys('soni')


##tag,class,attribute: syntax: tag.class[attrubutr=value]
driver.find_element(By.CSS_SELECTOR,'input.inputtext[placeholder="Password"]').send_keys('soni')
time.sleep(2)