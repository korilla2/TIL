from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(
    executable_path='C:/Users/BAUM/Desktop/multicampus/TIL/chromedriver.exe')
browser = webdriver.Chrome(service=service, options=options)

url = 'https://lc.multicampus.com/k-digital/#/login'
browser.get(url)
time.sleep(3)
review_button = browser.find_elements(By.CSS_SELECTOR,
                                      'div.v-input__control input')
review_button[0].send_keys('kingdoss01')
review_button[1].send_keys('qkrgytls007!')
time.sleep(1)
review_button2 = browser.find_element(By.CSS_SELECTOR,
                                      'div.btn-row button')
review_button2.click()
time.sleep(2)


last_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    new_height = browser.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

articles = browser.find_elements(
    By.CSS_SELECTOR, 'article section div.feed-cont')

for article in articles:
    print(article.text)
