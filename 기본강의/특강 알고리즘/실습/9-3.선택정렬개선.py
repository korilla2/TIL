import random


def selectionSort(arr):
    n = len(arr)
    for cycle in range(n - 1):
        for i in range(cycle+1, n):
            if arr[i] < arr[cycle]:
                arr[cycle], arr[i] = arr[i], arr[cycle]
    return arr


arr = [random.randint(10, 99) for _ in range(7)]
print('정렬 전 -->', arr)
arr = selectionSort(arr)
print('정렬 후 -->', arr)
