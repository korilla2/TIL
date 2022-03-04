n = 1000
temp = [None] * (n+1)
temp[1] = 1
temp[2] = 1


def fibo(n):
    if temp[n] is not None:
        return temp[n]
    else:
        temp[n] = fibo(n-1) + fibo(n-2)
    return temp[n]


print(fibo(n))
