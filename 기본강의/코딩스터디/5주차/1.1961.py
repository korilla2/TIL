T = int(input())

for i in range(T):
    N = int(input())
    base = []
    for j in range(N):
        a = list(map(str, input().split()))
        base.append(a)
    result = []
    for k in range(len(base)):
        temp_90 = ''
        temp_180 = ''
        temp_270 = ''
        for l in range(len(base)):
            temp_90 += base[N-1-l][k]
            temp_180 += base[N-1-k][N-1-l]
            temp_270 += base[l][N-1-k]
        result.append([temp_90, temp_180, temp_270])

    print(f'#{i+1}')
    for q in result:
        for r in q:
            print(r, end=' ')
        print()
