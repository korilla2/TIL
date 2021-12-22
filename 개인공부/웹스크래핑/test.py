from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome(
    'C:/Users/BAUM/Desktop/multicampus/TIL/개인공부/웹스크래핑/chromedriver.exe')

browser.get('http://naver.com')

elem = browser.find_element_by_class_name('input_text')
elem.send_keys('신잔디맘')
elem.send_keys(Keys.ENTER)

time.sleep(2)

elem2 = browser.find_element_by_xpath('//*[@id="web_4"]/div/div[2]/div[2]/a')
elem2.click()

time.sleep(1)


browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
time.sleep(1)
