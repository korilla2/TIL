'''
6079 : [기초-종합] 언제까지 더해야 할까?(py)

10
'''
n = int(input())
s = 0
a = 1
cnt = 0
while True:
    s += a
    a += 1
    cnt += 1
    if s >= n:
        break
print(cnt)
