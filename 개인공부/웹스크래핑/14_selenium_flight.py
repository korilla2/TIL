from selenium import webdriver
import time


browser = webdriver.Chrome(
    'C:/Users/BAUM/Desktop/multicampus/TIL/개인공부/웹스크래핑/chromedriver.exe')
browser.maximize_window()

url = 'https://flight.naver.com/'

browser.get(url)

browser.find_element_by_class_name(
    'tabContent_option__2y4c6 select_Date__1aF7Y').click()
