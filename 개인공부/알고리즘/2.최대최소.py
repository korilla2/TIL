list = [9, 22, 3, 7, 4, 5]


def max_solution(arr):
    result = arr[0]
    for num in arr:
        if result < num:
            result = num

    return result


def min_solution(arr):
    result = arr[0]
    for num in arr:
        if result > num:
            result = num

    return result


print(max_solution(list))
print(min_solution(list))
