import random


def min_idx(arr):
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[idx]:
            idx = i
    return idx


arr = [random.randint(1, 99) for _ in range(20)]
print(arr)
min_result = min_idx(arr)

print(arr)
print('최솟값 -- >', arr[min_result])
