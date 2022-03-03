numbers = [7, 3, 2, 9, 20, 33, 93, 23, 1, 5]


def bubble_sort(arr):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubble_sort(numbers))
