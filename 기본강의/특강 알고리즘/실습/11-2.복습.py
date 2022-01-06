import random


def binary_search(arr, f_data):
    idx = -1
    start = 0
    end = len(arr)-1
    for i in range(len(arr)):
        mid = (start + end) // 2
        if arr[mid] == f_data:
            idx = mid
            return idx
        elif arr[mid] < f_data:
            start = mid + 1
        else:
            end = mid - 1
    return idx


arr = [random.randint(10, 99) for _ in range(10)]
arr.sort()
find_data = arr[random.randint(0, 9)]
# find_data = 999

print(arr)
print(find_data)

result_idx = binary_search(arr, find_data)

print(result_idx)
