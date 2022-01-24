T = int(input())

for i in range(T):
    word = input()
    length = 0

    for j in range(1, 31):
        if word[j] == word[0]:
            if word[:j] == word[j:2*j]:
                length = j
                break
    print(f'#{i+1} {length}')
