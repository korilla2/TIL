from selenium import webdriver
import time

browser = webdriver.Chrome(
    'C:/Users/BAUM/Desktop/multicampus/TIL/개인공부/웹스크래핑/chromedriver.exe')

browser.get('http://naver.com')

elem = browser.find_element_by_class_name('link_login')

elem.click()

browser.find_element_by_id('id').send_keys('my_id')
browser.find_element_by_id('pw').send_keys('my_pw!')


browser.find_element_by_id('log.login').click()
time.sleep(3)
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('naver_id')
browser.find_element_by_id('pw').send_keys('naver_pw')

print(browser.page_source)

# browser.close()
browser.quit()
