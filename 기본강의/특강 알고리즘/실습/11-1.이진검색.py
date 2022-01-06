import random


def binary_search(arr, f_data):
    idx = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == f_data:
            return mid
        elif arr[mid] < f_data:
            start = mid + 1
        else:
            end = mid - 1
    return idx


arr = [random.randint(10, 99) for _ in range(10)]
find_data = arr[random.randint(0, 9)]
arr.sort()


print('arr-->', arr)
print('find_data-->', find_data)
pos = binary_search(arr, find_data)
if pos == -1:
    print('없음')
else:
    print(pos, '위치에 있음')
