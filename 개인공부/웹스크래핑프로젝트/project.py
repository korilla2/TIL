import requests
from bs4 import BeautifulSoup
import re


def create_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    soup = create_soup(url)
    cast = soup.find('p', attrs={'class', 'summary'}).get_text()
    curr_temp = soup.find(
        'div', attrs={'class': 'temperature_text'}).get_text().replace('현재 온도', '')
    min_temp = soup.find(
        'span', attrs={'class': 'lowest'}).get_text().replace('최저기온', '')
    max_temp = soup.find(
        'span', attrs={'class': 'highest'}).get_text().replace('최고기온', '')
    rain_rate = soup.find(
        'div', attrs={'class': 'cell_weather'}).get_text().strip().split()
    today_list = soup.find(
        'ul', attrs={'class': 'today_chart_list'}).get_text().strip().split()

    print(cast)
    print(f'현재온도: {curr_temp} 최저온도: {min_temp} 최고온도: {max_temp}')
    print(
        f'오전강수량: {rain_rate[1]} 오후강수량: {rain_rate[4]}')
    print(
        f'미세먼지: {today_list[1]} 초미세먼지: {today_list[3]} 자외선: {today_list[5]} 일몰: {today_list[-1]}')
    print()


def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com/'
    soup = create_soup(url)
    news_list = soup.find_all(
        'h4', attrs={'class': 'channel'})
    link_list = soup.find_all('a', attrs={'class': 'cjs_news_a'})

    link_li = []
    for link in link_list[:5]:
        link_li.append(link["href"])

    title_li = []
    title_list = soup.find_all('div', attrs={'class': 'cjs_t'})
    for title in title_list[:5]:
        title_li.append(title.get_text())

    for index, news in enumerate(news_list[:5]):
        print(
            f'{index+1}번 뉴스  {news.get_text().split("12월")[0]}     {title_li[index]}    {link_li[index]}')
    print()


def scrape_it_news():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    news_list = soup.find(
        'ul', attrs={'class': 'type06_headline'}).find_all('li')
    for index, news in enumerate(news_list):

        if news.find('img'):
            title = news.find('img')['alt']
        else:
            title = news.find('a').get_text().strip()
        link = news.find('a')['href']
        print(f'{index + 1}번 뉴스    {title}    {link}')
    print()


def scrape_english():
    print('[오늘의 영어 회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    soup = create_soup(url)
    text_list = soup.find_all('div', attrs={'class': 'conv_txt'})

    text_title = text_list[0].find('b', attrs={'class': 'conv_txtTitle'})
    text_title1 = text_list[1].find('b', attrs={'class': 'conv_txtTitle'})

    kor_list = []
    eng_list = []

    kor_list.append(text_title.get_text())
    eng_list.append(text_title1.get_text())

    for i in range(2, 6):
        sentence0 = text_list[0].find('div', attrs={'id': f'conv_kor_t{i}'})
        sentence1 = text_list[1].find('div', attrs={'id': f'conv_kor_t{i}'})

        kor_list.append(sentence0.get_text().strip('\n'))
        eng_list.append(sentence1.get_text().strip('\n'))

    print('-' * 100)
    print(f'오늘의 문장 : {kor_list[0]}')

    for kore in kor_list[1:]:
        print(kore)

    print('-' * 100)
    print(f'오늘의 문장 : {eng_list[0]}')

    for engl in eng_list[1:]:
        print(engl)


if __name__ == '__main__':
    scrape_weather()  # 오늘의 날씨 정보 가져오기
    scrape_headline_news()  # 헤드라인 뉴스 가져오기
    scrape_it_news()
    scrape_english()
