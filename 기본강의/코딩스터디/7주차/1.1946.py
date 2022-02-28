T = int(input())

for i in range(T):
    N = int(input())
    temp = ''
    for j in range(N):
        c, k = input().split()
        k = int(k)
        temp += c * k

    print(f'#{i+1}')
    for k in range(len(temp)):
        if (k+1) % 10 != 0:
            print(temp[k], end='')
        else:
            print(temp[k])
    print()
