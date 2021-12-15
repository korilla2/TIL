'''
6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)

1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''

n = int(input())
m = list(map(int, input().split()))
result = [0] * 24

for i in range(n):
    result[m[i]] += 1

for i in range(1, len(result)):
    print(result[i], end=' ')
