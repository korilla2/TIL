# Numpy 넘파이

- 수치해석용으로 만들어진 모듈
- 머신러닝과 같은 데이터 분석을 위해서 만들어진 것은 아님
- 분야를 가리지 않고 많이 사용됨
- ML / DL 에서도 많이 사용
- 판다스도 자료의 기본 타입은 numpy를 사용
- 수학적 계산을 돕기 위한 라이브러리

```python
import numpy as np
```

## 넘파이에서 지원하는 타입

1. array 배열
   - 주로 통계분석이나, ML / DL에서 사용하는 타입
   - 배열이라고 부릅니다
   - 파이썬의 리스트와는 다릅니다
2. matrix
   - 수학적 계산이 필요한 경우에 많이 사용
   - 수업 시간에는 사용하지 않습니다

### 배열의 기본 속성

- ndim : 배열의 차원을 나타내는 속성
- shape : 배열의 모양을 나타내는 속성
  - 배열의 크기를 나타내고, 배열의 크기는 원소의 개수와 동일
  - 1차원 배열인 경우에는 행이 1이고, 열이 n인 배열을 의미
  - 배열의 모양은 튜플로 효현이 됩니다

### 1차원 배열

- 파이썬의 리스트와 거의 동일

```python
arr1D = np.array([1, 2, 3, 4])
print(arr1D) # [1, 2, 3, 4]
display(arr1D) # array([1, 2, 3, 4])
```

- 배열의 차원
  - 자료의 차원을 확인하는 것은 매우 중요
  - 자료의 차원이 다르면, 알고리즘이 동작하지 않는 경우가 발생
  - 알고리즘을 직접 작성하지는 않고, 잘 만들어진 라이브러리를 이용
  - 자료의 차원을 고려해서 사용

```python
print(arr1D.ndim) # 1
print(arr1D.shape) # (4,)
```

###  2차원 배열

- 주로 다루게 되는 배열이 2차원 배열
- 자료가 대부분 2차원으로 되어있음
- 수업시간에도 2차원 배열 까지만 다룰 예정
- 리스트와 동일하게, 배열의 원소로 배열을 갖는 배열

```python
arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

```python
print(arr2D.ndim) # 2
print(arr2D.shape) # (3, 3) 행은 자료의 개수, 열은 변수의 개수
```

## 배열의 특징

- 인덱싱, 슬라이싱 매우 중요
- 팬시 인덱싱
- 배열의 타입
- 넘파이에서만 정의된 특별한 타입 존재

### 배열의 인덱싱과 슬라이싱

- 리스트와 비슷하지만 표현이 다름
- 기본적인 개념은 동일

#### 1차원 배열

```python
arr1D = np.array([1, 2, 3, 4])
print(arr1D) # [1, 2, 3, 4]
print(arr1D[0]) # 1
print(arr1D[-1]) # 4
```

- 배열도 이터러블 객체

```python
for x in arr1D:
    print(x)
    # 1
    # 2
    # 3
    # 4
```

- 내장함수 사용 가능

```python
print(min(arr1D)) # 1
print(max(arr1D)) # 4
```

- 슬라이스도 사용 가능

```python
print(arr1D[:]) # [1, 2, 3, 4]
print(arr1D[::-1]) # [4, 3, 2, 1]
```

#### 2차원 배열

```python
arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

- 인덱싱 슬라이싱

```python
array[행, 열]
array[행시작:행끝, 열시작:열끝]
```

```python
print(arr2D[0, 1]) # 1
print(arr2D[1, 1]) # 5
```

```python
print(arr2D[0]) # [1, 2, 3]
print(arr2D[0,]) # [1, 2, 3]
print(arr2D[:, 1]) # [2, 5, 8]
print(arr2D[1:,1:])
'''
[[5 6]
 [8 9]]
'''
```

### 연습

```python
import numpy as np

arrN = np.arange(1, 31).reshape(3, 10)
'''
[[ 1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27 28 29 30]]
'''

# 16
print(arrN[1, 5])
# 29
print(arrN[2, 8])
# 14, 15, 16
print(arrN[1, 3:6])
# 18, 28
print(arrN[1:, 7])
# 9, 10, 19, 20
print(arrN[:2, 8:])
```

```python
import numpy as np

arrN = np.arange(1, 51).reshape(5, 10)
'''
[[14 15 16 17]
 [24 25 26 27]
 [34 35 36 37]]
''' 
print(arrN[1:4, 3:7])

# [12 22 32]
print(arrN[1:4, 1])
```

### 팬시 인덱싱(배열 인덱싱)

- 인덱스로 배열을 사용

  - 불리언 배열
    - 불리언 인덱싱 : 배열에서 True 에 해당하는 값만 선택

  ```python
  import numpy as np
  
  arr1D = np.array([1, 2, 3, 4])
  print(arr1D[np.array([True, False, False, False])]) # 크기가 맞아야 함
  # [1]
  print(arr1D > 2)
  # [False False  True  True]
  print(arr1D[arr1D > 2])
  # [3 4]
  ```

  

  - 정수 배열
    - 배열에서 원하는 인덱스를 배열로 생성
    - 중복 선택이 가능, 배열의 크기와 인덱스 배열의 크기가 달라도 상관 없음

```python
import numpy as np

arr1D = np.array([1, 2, 3, 4])

idx = np.array([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 2])

print(arr1D[idx])
# [2 2 2 2 3 3 3 4 4 4 1 1 1 3]
```

### 배열의 타입

- 리스트와는 다르게 배열은 타입을 가집니다
- 리스트는 여러개의 타입을 원소로 가질 수 있습니다
- 배열은 하나의 타입만 원소로 가질 수 있습니다
- 배열은 생성될 때 원소들의 타입을 보고 기본적인 자료의 타입을 결정하게 됩니다
- 원소의 타입이 여러개라면 가장 큰 타입을 기본 타입으로 결정

```python
import numpy as np

arr1D = np.array([1, 2, 3, 4, 5.0])

print(arr1D.dtype)
print(arr1D)

'''
float64
[1. 2. 3. 4. 5.]
'''
```

- 타입을 직접 결정

```python
import numpy as np

arr1D = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print(arr1D.dtype)
print(arr1D)
'''
float64
[1. 2. 3. 4. 5.]
'''
```

- 넘파이에서만 정의되어 있는 특별한 타입
  - 파이썬은 이런 타입을 갖지 않음
  - INF
    - 표현할 수 없는 값
    - 함수가 수렴하지 않고 발산하는 경우(inf, -inf)
  - NAN
    - 결측치를 표현(비어있는 값)
    - 값으로 표현할 수 없는 경우

```python
import numpy as np

arr1 = np.array([0])
arr2 = np.array([0])
print(arr1 / arr2)
#[nan]
print(np.log(0))
#-inf
```

## 배열을 생성하는 방법

### 초기화된 배열

- 0과 1만 특별히 취급
- 원소가 전부 0이거나, 전부 1인 경우에는 선형대수에서는 특별하게 취급

```python
import numpy as np

print(np.zeros(10))
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

print(np.ones(10))
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

- 0 과 1이 아닌 다른 값으로 초기화 하고 싶은 경우

```python
import numpy as np

print(np.full(10, 5))
# [5 5 5 5 5 5 5 5 5 5]
```

### 수열을 생성하는 방법

- arange
  - 실수(소수)에 대한 수열도 만들 수 있습니다

```python
import numpy as np

print(np.arange(1, 10)) # [1 2 3 4 5 6 7 8 9]
print(np.arange(1, 2, 0.1)) # [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]


```

- linspace
  - 주어진 구간에서 균등한 간격으로 수열을 생성
  - 마지막 원소 포함

```python
import numpy as np

print(np.linspace(0, 10, 5)) # [ 0.   2.5  5.   7.5 10. ]
print(np.linspace(1, 2, 5)) # [1.   1.25 1.5  1.75 2.  ]
```

### 무작위 배열을 생성하는 방법

- 랜덤
  - 파이썬(넘파이)은 랜덤은 '균등분포'를 의미합니다
- 갯수만큼 랜덤한 값을 생성, 랜덤이므로 매번 값이 달라짐

```python
import numpy as np

print(np.random.rand(4))
# [0.21018373 0.03058015 0.48128362 0.36093266]
```

- 정수 형태로 무작위 수를 생성

```python
import numpy as np

print(np.random.randint(0, 10, size=10))
# [9 2 0 8 6 3 6 4 8 4]
```

- 생성되는 수를 고정

```python
np.random.seed(123)
np.random.rand(10)
```

- 중복되지 않은 무작위 수를 생성

```python
import numpy as np

arr = np.arange(1, 11)
print(np.random.choice(arr, size=5, replace=False))
# [2 1 7 8 5]
```

## <실습> 로또 번호 생성기

- 로또는 1부터 45까지의 수 중에서 6개의 수가 무작위로 선택
- 중복은 허용되지 않음

```python
import numpy as np

arr = np.arange(1, 46)
result = np.random.choice(arr, 6, replace=False)
result.sort()
print(result)
```

## 배열의 모양

- 저차원의 배열을 고차원의 배열로 변경
- 고차원의 배열을 저차원의 배열로 변경
  - 저차원은 1차원 배열로 변경이 가능
- 변경전의 크기와 변경 후의 크기가 달라지면 안됩니다
  - 자료의 개수가 반드시 일치

### 저차원 배열을 고차원의 배열로 변경

```python
import numpy as np

arr = np.random.randint(0, 4, 4)
print(arr)
# [2 1 2 3]

print(arr.reshape(2, 2))
'''
[[2 1]
 [2 3]]
'''
print(arr.reshape(-1, 2))
'''
[[2 1]
 [2 3]]
'''
print(arr.reshape(4, 1))
'''
[[2]
 [1]
 [2]
 [3]]
'''
print(arr.reshape(-1, 1))
'''
[[2]
 [1]
 [2]
 [3]]
'''
```

- 크기가 반드시 일치해야 합니다

```python
import numpy as np

arr = np.random.randint(0, 4, 4)
print(arr)
# [0 3 0 3]

print(arr.reshape(5, 5))
'''
Traceback (most recent call last):
  File "c:\Users\BAUM\Desktop\multicampus\TIL\연습장.py", line 7, in <module>
    print(arr.reshape(5, 5))
ValueError: cannot reshape array of size 4 into shape (5,5)
'''
```

### 고차원의 배열을 저차원으로 변경

```python
import numpy as np

arr = np.random.randint(1, 10, (3, 3))
print(arr)
'''
[[1 9 1]
 [3 9 2]
 [3 1 2]]
'''

print(arr.flatten())
print(arr.ravel())

'''
[1 9 1 3 9 2 3 1 2]
[1 9 1 3 9 2 3 1 2]
'''

# 열 기준으로 변경
print(arr.flatten(order='F'))

'''
[1 3 3 9 9 1 1 2 2]
'''
```

## 넘파이를 이용한 연산

### 기본적인 연산

#### 자료의 형태

- 스칼라
  - 물리학에서 양을 표현
  - 방향이 없고, 물리적인 ' 양'만을 표현
  - 파이썬에서는 변하지 않는 상수 정도로 이해
  - 행과 열이 1개 [[1]]
- 벡터
  - 물리학에서는 방향성을 가지고 있는 형태
  - 파이썬에서는 행이 n개이고 열이 1인 형태의 배열
    - 행벡터와 열벡터가 있는데, 일반적으로 벡터라 하면 열벡터를 의미
    - 넘파이 에서는 1차원 배열이 행벡터

```python
import numpy as np

vector = np.random.randint(1, 10, 5)
print(vector)
# 행백터
# [9 8 7 9 7]

print(vector.reshape(-1, 1))
# 열벡터
'''
[[9]
 [8]
 [7]
 [9]
 [7]]
'''
```

- 특별한 벡터 (영벡터 일벡터)

  ```python
  import numpy as np
  
  print(np.ones((4, 1)))
  '''
  [[1.]
   [1.]
   [1.]
   [1.]]
  '''
  
  print(np.ones((4, 1), dtype=int))
  '''
  [[1]
   [1]
   [1]
   [1]]
  '''
  
  print(np.ones((4, 1), dtype=bool))
  '''
  [[ True]
   [ True]
   [ True]
   [ True]]
  '''
  
  
  print(np.zeros((4, 1)))
  '''
  [[0.]
   [0.]
   [0.]
   [0.]]
  '''
  
  ```

  

- 행렬
  - 여러개의 벡터가 모여서 하나의 행렬을 이루게 됩니다
  - 행이 n개이고, 열이 m개인 배열을 행렬이라고 보면 됩니다

```python
import numpy as np

mat = np.random.randint(1, 10, (3, 5))
print(mat)
'''
[[8 8 2 3 5]
 [6 9 1 9 6]
 [3 4 2 9 3]]
'''
```

### 타입이 다른 피연산자간의 연산

- 사칙연산만 다룹니다
- 크기가 서로 같다면 문제가 없습니다
- 크기가 다르면 문제가 됩니다
  - 브로드캐스팅이 되는 경우와 그렇지 않은 경우로 나눠서 보면 됩니다
  - 작은 쪽의 크기를 큰 쪽으로 맞춰서 확장하여 계산 : 브로드 캐스팅

```python
import numpy as np

vector = np.random.randint(1, 10, (4, 1))
print(vector)
'''
[[2]
 [8]
 [6]
 [3]]
'''

# 연산 하려는 벡터의 크기에 맞춰서 사칙연산 (브로드 캐스팅)
print(2 * vector)
'''
[[ 4]
 [16]
 [12]
 [ 6]]
'''
```

```python
import numpy as np

mat = np.random.randint(1, 10, (3, 4))

print(mat)
'''
[[7 8 5 9]
 [2 3 4 2]
 [5 5 7 9]]
'''

print(2 * mat)
'''
[[14 16 10 18]
 [ 4  6  8  4]
 [10 10 14 18]]
'''
```

```python
import numpy as np

vector = np.random.randint(1, 10, (4, 1))
print(vector)
'''
[[8]
 [8]
 [4]
 [2]]
'''

mat = np.random.randint(1, 10, (3, 4))
print(mat)
'''
[[1 8 5 3]
 [4 5 6 8]
 [5 5 4 3]]
'''

print(vector * mat)
'''
Traceback (most recent call last):
  File "c:\Users\BAUM\Desktop\multicampus\TIL\연습장.py", line 9, in <module>
    print(vector * mat)
ValueError: operands could not be broadcast together with shapes (4,1) (3,4)
'''
```

```python
import numpy as np

vector = np.random.randint(1, 10, (3, 1))
print(vector)
'''
[[9]
 [4]
 [3]]
'''

mat = np.random.randint(1, 10, (3, 4))
print(mat)
'''
[[1 8 1 8]
 [6 4 8 5]
 [4 7 2 7]]
'''

print(vector * mat)
'''
[[ 9 72  9 72]
 [24 16 32 20]
 [12 21  6 21]]
'''

```

### 행렬과 행렬의 연산

- 크기가 같아야 연산가능

```python
import numpy as np

mat = np.random.randint(1, 10, (3, 4))
print(mat)
'''
[[6 8 5 8]
 [5 9 8 8]
 [9 7 2 6]]
'''

mat2 = np.random.randint(1, 10, (3, 4))
print(mat2)
'''
[[3 3 6 7]
 [4 1 6 1]
 [8 8 5 3]]
'''

print(mat * mat2)
'''
[[18 24 30 56]
 [20  9 48  8]
 [72 56 10 18]]
'''

```

