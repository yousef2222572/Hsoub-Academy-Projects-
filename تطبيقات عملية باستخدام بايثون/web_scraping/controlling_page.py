from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()

browser.get('https://chatgpt.com')
try:


    
    el=browser.find_element(By.CSS_SELECTOR,'#mobile-composer-prompt')
    el.send_keys('web development')
    time.sleep(7)
    
    Btn=browser.find_element(By.CSS_SELECTOR,'#mobile-composer-submit-button')
    Btn.click()
    time.sleep(5)
    
    # time.sleep(3)
    # html_el=browser.find_element(By.TAG_NAME,'html')
    # html_el.send_keys(Keys.END)
    # time.sleep(3)
    # html_el.send_keys(Keys.HOME)
    # time.sleep(3)
    
except Exception as e:
    print(e)