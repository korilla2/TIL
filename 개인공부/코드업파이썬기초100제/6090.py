'''
6090 : [기초-종합] 수 나열하기3(py)

-85
'''

a, m, d, n = map(int, input().split())


for i in range(n - 1):
    a = a * m + d

print(a)
