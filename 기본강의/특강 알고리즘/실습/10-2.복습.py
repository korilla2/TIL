import random


def search(arr, f_data):
    idx = -1
    for i in range(len(arr)):
        if arr[i] == f_data:
            idx = i
            break
    return idx


arr = [random.randint(10, 99) for _ in range(10)]
find_data = arr[random.randint(0, 9)]

print('배열 -->', arr)
result_idx = search(arr, find_data)

if result_idx == -1:
    print('없음')
else:
    print(find_data, '는', result_idx, '번째 있음')
