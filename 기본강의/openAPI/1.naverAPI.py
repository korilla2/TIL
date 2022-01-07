import json
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

header = {
    "X-Naver-Client-Id": "FnT9nTr1sVRosbbfEtzQ",
    "X-Naver-Client-Secret": "YbHWba99oO",
    "Content-Type": "application/json"
}

url = "https://openapi.naver.com/v1/datalab/search"
body = {
    'startDate': '2021-01-01',
    'endDate': '2021-12-31',
    'timeUnit': 'month',
    'keywordGroups': [
        {
            'groupName': '이재명',
            'keywords': ['더불어민주당', '이재명']
        },
        {
            'groupName': '윤석열',
            'keywords': ['국민의힘', '윤석열']
        },
        {
            'groupName': '허경영',
            'keywords': ['국가혁명당', '허경영']
        },
        {
            'groupName': '안철수',
            'keywords': ['국민의당', '안철수']
        },
        {
            'groupName': '심상정',
            'keywords': ['정의당', '심상정']
        }
    ],
    "ages": ["3", "4", "5", "6", "7", "8", "9", "10", "11"],


}
json_dump = json.dumps(body)

response = requests.post(url, data=json_dump, headers=header)

print(response.status_code)

result = response.json()
lee = pd.DataFrame(result['results'][0]['data'], columns=['period', 'ratio'])
lee.rename(columns={'ratio': 'lee'}, inplace=True)

yoon = pd.DataFrame(result['results'][1]['data'], columns=['period', 'ratio'])
yoon.rename(columns={'ratio': 'yoon'}, inplace=True)

huh = pd.DataFrame(result['results'][2]['data'], columns=['period', 'ratio'])
huh.rename(columns={'ratio': 'huh'}, inplace=True)

ahn = pd.DataFrame(result['results'][3]['data'], columns=['period', 'ratio'])
ahn.rename(columns={'ratio': 'ahn'}, inplace=True)

sim = pd.DataFrame(result['results'][4]['data'], columns=['period', 'ratio'])
sim.rename(columns={'ratio': 'sim'}, inplace=True)

final = pd.merge(left=lee, right=yoon, on='period')
final = pd.merge(left=final, right=huh, on='period')
final = pd.merge(left=final, right=ahn, on='period')
final = pd.merge(left=final, right=sim, on='period')
print(final)

plt.figure(figsize=(20, 5))
sns.lineplot(data=final, x='period', y='lee')
sns.lineplot(data=final, x='period', y='yoon')
sns.lineplot(data=final, x='period', y='huh')
sns.lineplot(data=final, x='period', y='ahn')
sns.lineplot(data=final, x='period', y='sim')
plt.xticks(rotation=30)
plt.legend()
plt.show()
