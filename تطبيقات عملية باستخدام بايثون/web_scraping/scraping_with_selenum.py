from selenium import webdriver

from selenium.webdriver.common.by import By
browser = webdriver.Chrome()


browser.get('https://en.wikipedia.org/wiki/Main_Page')
try:

    # elem=browser.find_element(By.CSS_SELECTOR,'#mp-tfa > p')
    
    elem=browser.find_elements(By.TAG_NAME,'p')
    print(elem[0].text)
except  :
    print('error not found ')
