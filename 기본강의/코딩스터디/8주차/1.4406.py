T = int(input())

for i in range(T):
    word = input()
    base = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for j in word:
        if j in base:
            pass
        else:
            result += j
    print(f'#{i+1} {result}')
