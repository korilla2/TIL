def is_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-1 - i]:
            return False
    return True


def change_map(arr):
    temp = list(zip(*arr))
    return temp


for i in range(10):
    stick = int(input())
    base = []
    for j in range(8):
        a = list(input())
        base.append(a)
    base2 = change_map(base)
    cnt = 0
    for k in range(8 - stick + 1):
        for l in range(8):
            result1 = base[l][k:stick+k]
            result2 = base2[l][k:stick+k]
            if is_palindrome(result1) == True:
                cnt += 1
            if is_palindrome(result2) == True:
                cnt += 1
    print(f'#{i+1} {cnt}')
