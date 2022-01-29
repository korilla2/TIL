T = int(input())

for i in range(T):
    N = int(input())
    for j in range(N):
        base = [[0 for _ in range(N)] for _ in range(N)]

    x = 0
    y = 0
    base[x][y] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    way = 0
    cnt = 2

    while cnt <= pow(N, 2):
        nx, ny = x + dx[way], y + dy[way]

        if -1 < nx < N and -1 < ny < N and base[nx][ny] == 0:
            base[nx][ny] = cnt
            cnt += 1
            x, y = nx, ny

        else:
            way = (way + 1) % 4

    print(f'#{i+1}')
    for k in base:
        for l in k:
            print(l, end=' ')
        print()
