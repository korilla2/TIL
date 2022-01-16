import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    elif r2 + r1 == d:
        print(1)
    elif abs(r2 - r1) == d:
        print(1)

    elif abs(r2 - r1) < d < abs(r2 + r1):
        print(2)

    else:
        print(0)
