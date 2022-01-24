T = int(input())

for i in range(T):
    N = int(input())
    base = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    idx = 1
    for j in range(N):
        if j <= N//2:
            result += sum(base[j][N//2-j:N//2+j+1])
        else:
            result += sum(base[j][idx:N-idx])
            idx += 1
    print(f'#{i+1} {result}')
