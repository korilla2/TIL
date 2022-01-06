import random


def sum_array(arr, n):
    if n <= 0:
        return arr[n]
    return arr[n] + sum_array(arr, n-1)


arr = [random.randint(10, 99) for _ in range(10)]
arr = list(range(1, 11))
print(arr)
print(sum_array(arr, len(arr)-1))
