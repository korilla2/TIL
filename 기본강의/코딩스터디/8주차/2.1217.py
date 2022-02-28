def recursive_func(a, b):
    if b < 1:
        return 1

    return a * recursive_func(a, b-1)


T = 10

for i in range(T):
    number = int(input())
    N, M = map(int, input().split())
    result = recursive_func(N, M)

    print(f'#{number} {result}')
