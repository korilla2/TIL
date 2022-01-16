k = list(map(int, input().split()))


while k[0] != 0 or k[1] != 0 or k[2] != 0:
    k = sorted(k)
    a = k[0]
    b = k[1]
    c = k[2]
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')

    k = list(map(int, input().split()))
