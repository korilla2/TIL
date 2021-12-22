'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
'''
26
'''


import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, key=lambda x: x, reverse=True)


for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
