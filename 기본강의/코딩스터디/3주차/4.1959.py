from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    list_a = deque(map(int, input().split()))
    list_b = deque(map(int, input().split()))

    if len(list_a) >= len(list_b):
        pass
    else:
        list_a, list_b = list_b, list_a
    result = []
    for j in range(len(list_a) - len(list_b) + 1):

        s = 0
        for k in range(len(list_b)):
            s += list_a[k] * list_b[k]
        result.append(s)
        list_a.popleft()
    print(f'#{i+1} {max(result)}')
