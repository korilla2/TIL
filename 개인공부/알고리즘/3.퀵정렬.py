numbers = [40, 35, 27, 50, 75]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [number for number in arr[1:] if number <= pivot]
        right = [number for number in arr[1:] if number > pivot]
        print('left =', left)
        print('pivot =', pivot)
        print('right =', right)
        print('='*20)
        return quick_sort(left) + [pivot] + quick_sort(right)


result = quick_sort(numbers)
print(result)
