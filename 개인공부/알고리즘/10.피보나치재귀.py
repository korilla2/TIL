def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
