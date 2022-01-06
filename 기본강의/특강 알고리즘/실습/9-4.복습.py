import random


def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [random.randint(10, 99) for _ in range(5)]

print('정렬 전-->', arr)
arr = selection_sort(arr)
print('정렬 후-->', arr)
