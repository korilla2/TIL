from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome(
    'C:/Users/BAUM/Desktop/multicampus/TIL/개인공부/웹스크래핑/chromedriver.exe')
browser.maximize_window()

url = 'https://flight.naver.com/'

browser.get(url)
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b').click()
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[6]/button/b').click()
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,
                            '//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input')
time.sleep(2)
elem.send_keys('제주도')
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/div/a').click()
time.sleep(2)
browser.find_element(By.XPATH,
                     '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()
time.sleep(10)

el = browser.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/button')
el.click()

print(el.text)

# ex = browser.find_element(
#     By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/button')

# print(ex.text)
