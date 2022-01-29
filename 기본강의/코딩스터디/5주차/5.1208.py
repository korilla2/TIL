T = 10

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for j in range(1, N+1):
        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))

        arr[max_idx] -= 1
        arr[min_idx] += 1

    print(f'#{i+1} {max(arr) - min(arr)}')
