import sys
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


all_list = [i for i in range(2, 246913)]
prime_list = []

for i in all_list:
    if is_prime(i):
        prime_list.append(i)

n = int(input())

while n != 0:
    count = 0
    for i in prime_list:
        if n < i <= 2*n:
            count += 1
    print(count)
    n = int(input())
