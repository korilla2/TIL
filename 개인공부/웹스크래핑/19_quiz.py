from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1900x1080')
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
browser = webdriver.Chrome(options=options)

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EA%B0%95%EB%82%A8+%EC%95%84%ED%8C%8C%ED%8A%B8'
# browser.get(url)
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')


# with open('quiz.html', 'w', encoding='utf8') as f:
#     f.write(soup.prettify())
