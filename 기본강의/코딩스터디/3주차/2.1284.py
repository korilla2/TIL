T = int(input())

for i in range(T):
    P, Q, R, S, W = map(int, input().split())

    price_a = P * W

    if R < W:
        price_b = Q + (W - R) * S
    else:
        price_b = Q

    if price_a < price_b:
        print(f'#{i+1} {price_a}')
    else:
        print(f'#{i+1} {price_b}')
