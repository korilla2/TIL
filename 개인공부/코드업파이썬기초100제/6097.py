'''
6097 : [기초-리스트] 설탕과자 뽑기(py)

1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''

h, w = map(int, input().split())
n = int(input())


result = [[0 for i in range(w)] for i in range(h)]


def test(l, d, x, y):
    result[x - 1][y - 1] = 1
    for i in range(1, l):
        if d == 0:
            result[x - 1][y - 1 + i] = 1
        else:
            result[x - 1 + i][y - 1] = 1


for i in range(n):
    l, d, x, y = map(int, input().split())
    test(l, d, x, y)

for i in result:
    for j in i:
        print(j, end=' ')
    print()
