# 우선순위 큐 (Priority Queue)

우선순위가 가장 높은 데이터를 가장 먼저 삭제

우선순위에 따라 처리하고 싶을 때 사용

ex : 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

리스트, 힙(heap)을 이용하여 구현할 수 있다

## 힙의 특징

완전 이진 트리의 일종

항상 루트 노드를 제거

- 최소 힙
  - 루트 노드가 가장 작은 값을 가짐
  - 가장 작은 데이터가 우선적으로 제거

- 최대 힙
  - 루트 노드가 가장 큰 값을 가짐
  - 가장 큰 데이터가 우선적으로 제거

### 완전 이진 트리

루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로

데이터가 차례대로 삽입되는 트리

ex : 왼쪽, 오른쪽, 왼쪽, 오른쪽 ...

### 최소 힙 구성 함수

Min-Heapify()

부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체

### 힙 원소 삽입

삽입 O(logN)

새롭게 자식 노드가 생성되었다면, 해당 노드의 부모 노드와 비교하는 방식

### 힙 원소 삭제

삭제 O(logN)

맨 마지막 노드와 루트 노드의 위치에 놓는다

그 뒤 Min-Heapify() 함수를 수행해서 힙 형태로 만들어준다

### 우선순위 큐 라이브러리를 활용한 힙 정렬

```python
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    #min heap
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
    #max heap 을 원할 경우 -h, -heapq.heappop(h)

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
```

