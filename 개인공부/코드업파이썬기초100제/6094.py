'''
6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)

2
'''

a = int(input())
b = list(map(int, input().split()))

result = sorted(b)

print(result[0])
