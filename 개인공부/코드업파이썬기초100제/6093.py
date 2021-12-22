'''
6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)

5 8 9 7 6 6 3 2 4 10
'''

a = int(input())
b = list(map(int, input().split()))

result = b[-1::-1]

for i in result:
    print(i, end=' ')
