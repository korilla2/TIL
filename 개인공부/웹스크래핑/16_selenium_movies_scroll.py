import requests
from bs4 import BeautifulSoup
import time


from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
time.sleep(2)
url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)
time.sleep(2)
# browser.execute_script("window.scrollTo(0, 2080);")
time.sleep(2)

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크롤 완료')


soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={
                       'class': 'Vpfmgd'})

print(len(movies))

for movie in movies:
    title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()

    original_price = movie.find('span', attrs={'class': 'SUZt4c djCuy'})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, '할인 안됨')
        continue

    price = movie.find(
        'span', attrs={'class': 'VfPpfd ZdBevf i5DZme'}).get_text()

    link = movie.find('a', attrs={'class': 'JC71ub'})["href"]

    print(f'제목: {title}')
    print(f'할인 전 금액: {original_price}')
    print(f'할인 후 금액: {price}')
    print(f'링크 : https://play.google.com{link}')
    print('-' * 100)

browser.quit()
