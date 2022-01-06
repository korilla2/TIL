import random


def seqSearch(arr, f_data):
    pos = -1
    for i in range(len(arr)):
        if arr[i] == f_data:
            pos = i
            break
    return pos


arr = [random.randint(10, 99) for _ in range(10)]

find_data = arr[random.randint(0, 9)]

print('배열-->', arr)

position = seqSearch(arr, find_data)

if position == -1:
    print(find_data, '없음')
else:
    print(find_data, '는', position, '위치에 있음')
