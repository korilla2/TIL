def fibo(n):
    if n < 3:
        return 1
    one = 1
    two = 1
    cnt = 2
    result = one + two
    while cnt < n:
        result = one + two
        one = two
        two = result
        cnt += 1
    return result


print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
