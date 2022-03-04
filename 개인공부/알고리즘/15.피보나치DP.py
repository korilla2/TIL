temp = {1: 1, 2: 1}


def fibo(n):
    if n in temp:
        return temp[n]

    else:
        temp[n] = fibo(n-1) + fibo(n-2)
    return temp[n]


print(fibo(1000))
