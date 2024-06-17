from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

## self
a1=driver.find_element(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/self::a").text
print(a1)

##parent
a1=driver.find_element(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/parent::td").text
print(a1)

##child using anscestor
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/child::td")
print(len(childs))

for i in childs:
    print(i.text)

##ancestor
ancestor_text=driver.find_element(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr").text
print(ancestor_text)


##Decendant
decendant_texts=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/descendant::*")
print(len(decendant_texts))
for i in decendant_texts:
    print(i.text)


#following
followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/following::*")
print(len(followings))

##following-sibling
followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/following-sibling::*")
print(len(followingsiblings))


# ##preceding
precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/preceding::*")
print(len(precedings))


##preceding-sibling
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Zen Technologies Ltd')]/ancestor::tr/preceding-sibling::")
print(len(precedingsiblings))
