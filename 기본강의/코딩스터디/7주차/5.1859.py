T = int(input())

for i in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    temp = 0
    cnt = 0
    result = 0

    for j in range(len(price)):
        max_idx = price.index(max(price))
        base = price[:max_idx]

        result += price[max_idx] * len(base) - sum(base)
        price = price[max_idx:]

        print(price)

    print(result)
