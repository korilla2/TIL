T = int(input())

for i in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    result = 0

    while len(price) > 1:
        max_idx = price.index(max(price))
        base = price[:max_idx]
        result += price[max_idx] * len(base) - sum(base)
        price = price[max_idx+1:]

    print(f'#{i+1} {result}')
