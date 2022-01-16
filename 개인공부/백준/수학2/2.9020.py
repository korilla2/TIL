import sys
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


all_list = [i for i in range(2, 10001)]
result = []

for i in all_list:
    if is_prime(i):
        result.append(i)

T = int(input())

for i in range(T):
    n = int(input())
    temp = []
    a = n//2
    b = n - a

    for j in range(b, n):
        if (j in result) and (n-j in result):
            temp.append((n-j, j))
            break
    print(temp[0][0], temp[0][1])
