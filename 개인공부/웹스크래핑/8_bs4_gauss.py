import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all('td', attrs={"class": "title"})

# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a['href']
#     print(title, link)

cartoons = soup.find_all("div", attrs={'class': 'rating_type'})
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)
print(total_rates)
print(total_rates/len(cartoons))
