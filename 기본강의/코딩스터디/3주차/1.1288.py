T = int(input())


for i in range(T):
    N = int(input())

    result = set()
    cnt = 1
    while len(result) < 10:
        k = N * cnt
        temp = list(str(k))

        for j in temp:
            result.add(int(j))
        cnt += 1

    print(f'#{i+1} {k}')
