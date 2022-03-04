arr = list(range(1, 7))


def pick2(arr):
    temp = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            temp.append((arr[i], arr[j]))
    return temp


print(pick2(arr))
