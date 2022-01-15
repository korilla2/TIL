def is_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-1 - i]:
            return False
    return True


T = int(input())

for i in range(T):
    words = list(input().strip())

    result = is_palindrome(words)

    if result == False:
        print(f'#{i+1} 0')
    else:
        print(f'#{i+1} 1')
