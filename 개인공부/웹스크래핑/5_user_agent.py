import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53"}

url = "http://nadocoding.tistory.com"

res = requests.get(url, headers=headers)
res.raise_for_status()

with open('korilla.html', 'w', encoding='utf8')as f:
    f.write(res.text)
