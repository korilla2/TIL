arr = [1, 2, 3, 4]


def sum_arr(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        return arr[-1] + sum_arr(arr[:-1])


print(sum_arr(arr))
