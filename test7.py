arr = [1, 3, 5, 6, 11, 23]

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == 9:
            print(arr[i], arr[j])
            break
