def pow(n, x):
    if x <= 0:
        return 1
    return n * pow(n, x-1)


print(pow(3, 3))
