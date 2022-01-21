T = int(input())

for i in range(T):
    N = int(input())
    current = 0
    result = 0
    for j in range(N):
        speed = list(map(int, input().split()))
        if current < 0:
            current = 0
        if result < 0:
            result = 0
        if speed[0] == 0:
            result += current
        elif speed[0] == 1:
            current += speed[1]
            result += current
        else:
            current -= speed[1]
            result += current

    print(f'#{i+1} {result}')
