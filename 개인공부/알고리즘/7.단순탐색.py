arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def simple_search(arr, num):
    for idx in range(len(arr)):
        if arr[idx] == num:
            return idx
    return -1


print(simple_search(arr, 6))
print(simple_search(arr, 9))
