N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result = []
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
            cnt += 1
    result.append((i, cnt+1))
    print(result[i][1], end=' ')
