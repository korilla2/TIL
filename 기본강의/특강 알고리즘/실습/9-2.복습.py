import random


def min_idx(arr):
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[idx]:
            idx = i
    return idx


arr = [random.randint(10, 99) for _ in range(5)]
result = []
print(arr)
for i in range(len(arr)):
    idx = min_idx(arr)
    result.append(arr[idx])
    del arr[idx]


print(result)
