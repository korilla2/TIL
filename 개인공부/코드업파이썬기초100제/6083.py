'''
6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8
'''

a, b, c = map(int, input().split())
cnt = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            cnt += 1
print(cnt)
