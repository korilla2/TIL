# Pandas 판다스

- 판다스란?

  - 파이썬에서 사용할 수 있는 데이터 전처리용 패키지

  - 엑셀처럼 파일을 다룰 수 있게 해주는 도구

  - 엑셀과의 가장 큰 차이점은 아주 큰 파일도 처리가 가능

    - 일반적으로 엑셀은 100MB만 넘어가도 잘 안열립니다

    - 판다스는 1GB가 넘어가는 파일도 빠르게 처리가 가능

  - 엑셀보다 더 복잡한 처리, 디비와 연동 등의 기능을 제공

- 데이터 분석
  - 분석, 업무의 80%는 전처리 입니다
  - 잘 정제되지 않은 데이터는 분석을 아무리 잘해도 의미가 없습니다

## Series 시리즈

- 1차원 구조를 표현

```python
import numpy as np
import pandas as pd

series = pd.Series([10, 20, 30, 40])
print(series)
'''
0    10
1    20
2    30
3    40
dtype: int64
'''

print(series.ndim)  # 1

print(series.shape)  # (4,)
```

## DataFrame

- 2차원 구조
- 여러개의 시리즈가 모여서 하나의 데이터 프레임이 됩니다

```python
import numpy as np
import pandas as pd

weight = pd.DataFrame([
    [76.4, 'kg'],
    [80, 'kg'],
    [55, 'kg'],
    [45.9, 'kg']
])

weight
```

### 파일 읽기

- read_csv 라는 기능으로 파일을 읽어올 수 있습니다
- 텍스트가 , 로 구분된 형태로 되어있는 파일을 csv라 합니다

```python
import numpy as np
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/멀티캠퍼스/data/weight_log.csv')
df
```

### 데이터 프레임 사용하기

#### 출력

- 상위 5개의 자료를 출력

```python
df.head() # 디폴트 = 5
df.head(2) # 2개만 출력
```

- 하위 5개의 자료를 출력

```python
df.tail() # 디폴트 = 5
df.tail(2) # 2개만 출력
```

- 데이터의 요약된 정보

```python
df.info()
```

- 데이터의 기본적인 통계치

```python
df.describe() # 숫자 데이터만
df.describe(include='all') # 숫자가 아닌 데이터들 포함
```

#### 인덱싱

- 판다스의 데이터프레임은 기본적으로 열우선 인덱스

```python
df['몸무게'] # 시리즈
df[['이름', '몸무게']] # 데이터 프레임
```

- 배열 인덱스

```python
col = ['이름', '몸무게', '측정일']
df[col]
```

- 행 인덱싱

```python
df.loc[0]
df.iloc[0]
```

- 슬라이스

```python
df.loc[0:3] # DataFrame 에서는 마지막 인덱스도 포함되어 나옴
```

- 행에 대한 배열 인덱싱

```python
df.loc[[1, 3, 5]] # 1, 3, 5 행 출력
df.reindex([1, 3, 5]) # 1, 3, 5 행 출력
```

- 행, 열 인덱싱

```python
df.loc[0, '이름'] # 홍길동
df.iloc[0, 1] # 홍길동
df.loc[[1, 3, 5], ['이름', '몸무게']]
df.loc[0:3, ['이름', '몸무게']]
df.loc[0:3, '이름':'몸무게']
```

#### loc vs iloc

- iloc 를 사용하면 컬럼 인덱스에 정수를 사용할 수 있습니다

```python
df.iloc[0:3, 1:4]
```

#### 조건 검색

- 불리언 인덱스를 활용

```python
df2 = df['지점'] == '여의도'
df[df2]

df3 = df['몸무게'] >= 76
df[df3]
```

#### 다중 조건

- and(&), or(|), not(~)
- 우선순위가 헷갈림
- 괄호를 이용해서 정확히 표현하는게 좋음

```python
df4 = (df['지점'] == '서초구') & (df['담당'] == '최현경')
df[df4]

df5 = (df['지점'] == '서초구') & ((df['담당'] == '최현경') | (df['담당'] == '김현경'))
df[df5]
```

- isin 은 리스트를 파라미터로 갖습니다
- 리스트 내의 값들 중에서 하나라도 존재하면 True, 그렇지 않으면 False

```python
df6 = (df['지점'] == '서초구') & (df['담당'].isin(['김현경', '최현경']))
df[df6]
```

- 담당자들 중 성이 김씨인 자료만 검색

```python
df7 = df['담당'].str.contains('김') # 김이라는 글자가 들어간 모든 자료
df[df7]

df8 = df['담당'].str.startswith('김') # 시작이 김이라는 글자인 자료
df[df8]

df9 = ~(df['담당'].str.startswith('김'))
df[df9]

# 성 말고 이름에도 김이라는 글자가 들어가는 경우도 있으므로 주의
```

#### 결측치

- 결측치가 있으면 분석을 제대로 수행할 수 없기 때문에 어떻게든 처리를 해줘야 합니다
  - 결측치를 채우든가, 지우든가 둘 중 하나를 해줘야 합니다
  - 결측치를 채우는 방법
    - 평균, 중앙값 등으로 대체하는 경우
    - 책에서나 할 수 있는 얘기들이고, 실제로도 유용한가?

- 결측치 확인방법

```python
df['몸무게'].isnull()
df['몸무게'].isna()
df['몸무게'].isnull().sum() # 갯수

df10 = df['몸무게'].isnull()
df[df10]

df11 = df['몸무게'].notnull()
df[df11]

df12 = df['몸무게'].isnull(), ['담당', '지점', '측정일']
df.loc[df12]
```

#### 이상치

- 특별히 크거나, 작은 값
  - 얼마나 크거나 작아야 이상치라고 할 수 있는가?
- 이상치를 찾는 경우가 아니라면, 이상치는 제거하고 분석을 진행 합니다

```python
df13 = df['몸무게'] > 76
df[df13]

df['몸무게'].quantile(0.25)
df['몸무게'].quantile(0.50)
df['몸무게'].quantile(0.75)
df['몸무게'].quantile(0.99)

low = df['몸무게'].quantile(0.01)
high = df['몸무게'].quantile(0.99)
df14 = (df['몸무게'] < high) & (df['몸무게'] > low)
df[df14]
```

#### 중복 데이터 검사

- duplicated 사용

```python
df15 = df.duplicated(subset='지점', keep=False) # 중복된 자료를 다 보여줌
df[df15]
```

## 통계분석

### 판다스에서 제공하는 통계관련된 기능들

- pivot (엑셀에서의 피봇 기능과 동일한 기능)
- crosstab
- 그룹화

```python
# 지점별 몸무게 평균
pd.pivot_table(df, index='지점', values='몸무게')

# 지점별 몸무게 총합
pd.pivot_table(df, index='지점', values='몸무게', aggfunc=np.sum)

# 지점별 담당자별 몸무게의 평균
pd.pivot_table(df, index=['지점', '담당'], values='몸무게')

# 지점별 담당자별 몸무게의 평균
pd.crosstab(index=df['지점'], columns=df['담당'], values=df['몸무게'], aggfunc=np.mean)

df.groupby(['지점']) # 그룹 객체
# 그룹화를 통한 지점별 몸무게 평균
df.groupby(['지점', '담당'])[['몸무게']].mean()

# 그룹화를 통한 다른 집계방식 출력하기
df.groupby('지점').agg({
    '몸무게': 'mean', '담당': 'count'
})

df.groupby(['지점', '담당']).agg({
    '몸무게': 'mean', '담당': 'count', '측정일': np.sort
})
```

### 조건에 맞게 컬럼 만들기

- 몸무게가 특정값 이상이면 '비만', 그렇지 않으면 '정상'을 갖는 '상태'컬럼 만들기

```python
df16 = df['몸무게'] >= 76
df17 = df['몸무게'] < 76
df.loc[df16, '상태'] = '비만'
df.loc[df17, '상태'] = '정상'
df

df['상태'] = np.where(df['몸무게']>=76, '비만', '정상')
df
```

### 컬럼 삭제

```python
df.drop('상태', axis=1)
df.drop('상태', axis=1, inplace=True)
```

### 행추가, 삭제

```python
df.loc[9] = [10, '홍길동', '2020-03-10', 77, 'kg', '박현경', '관악구']
df

df.drop(9)
df.drop(9, inplace=True)
```

#### apply

- 자료를 원하는대로 다루기는 쉽지 않아요
  - 실제로 데이터를 다뤄보면 내 생각처럼 쉽게 다뤄지지 않습니다
- 판다스에서 사용 가능한 반복문 정도로 이해
- 모든 행, 열에 대해서 동일한 함수를 반복적으로 적용

```python
def func(x):
    print(f'{x}함수가 호출되었습니다')
    print(x)
    return x

df.apply(func)
# 칼럼이 들어가는 것을 확인

def func(x):
    print(f'{x}함수가 호출되었습니다')
    print(x)
    return x

df.apply(func, axis=1)
# 행이 들어가는 것을 확인
```

- 지점별로 지역을 새로 만들어 보기

```python
def func(x):
    if x['지점'] == '관악구':
        return '강서'
    elif x['지점'] == '여의도':
        return '강서'
    elif x['지점'] == '강남구':
        return '강동'
    elif x['지점'] == '서초구':
        return '강동'
df.apply(func, axis=1)
```

- 새로운 컬럼을 추가

```python
df['지역'] = df.apply(func, axis=1)
df
```

## 프레임 합치기

- 서로 다른 두 자료(데이터 프레임)를 하나의 데이터 프레임으로 합치기
- 여러소스(출처) 로부터 가져온 데이터를 분석하기 위해서는 반드시 하나의 데이터프레임으로 합쳐야 한다

- inner join = 교집합
- full join = 합집합
- left join = 왼쪽
- right join = 오른쪽

### inner join

- merge 함수를 통해서 join을 해볼 수 있습니다
  - merge의 기본 동작은 inner join 입니다
- inner join은 기본적으로 자료의 크기가 훨씬 줄어들 게 됩니다
  - 양쪽 모두에게 존재하는 자료만 뽑기 때문

```python
pd.merge(left=df_usage, right=df_device, on='use_id'
```

### left join

- left 자료를 기준으로 합쳐줍니다
- 결측치가 발생할 수 있습니다

```python
pd.merge(left=df_usage, right=df_device, on='use_id', how='left')
```

### right join

- right 자료를 기준으로 합쳐줍니다
- 결측치가 발생할 수있습니다

```python
pd.merge(left=df_usage, right=df_device, on='use_id', how='right')
```

### full outer join

```python
pd.merge(left=df_usage, right=df_device, on='use_id', how='outer')
```

## 결론

- 데이터 전처리 작업의 핵심은 합치고, 나누고, 붙이고, 자르는 작업
- 무한히 반복
- 인공지능 이라는 개념이 나오면서 더더욱 오해가 심해져 가고 있음
  - 뭔가 업무가 스마트할 것 같고, 있어 보이는 작업일 것이다
  - 실제 작업은 그리 스마트하지 않고 빡센 노가다의 연속

- 실제 업무의 80%는 전처리 작업
