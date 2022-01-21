def check_map(arr, n, k):
    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1
    return result


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    base = []
    for j in range(N):
        temp = list(map(int, input().split()))
        base.append(temp)

    result1 = check_map(base, N, K)
    base2 = list(zip(*base))
    result2 = check_map(base2, N, K)

    print(f'#{i+1} {result1 + result2}')
