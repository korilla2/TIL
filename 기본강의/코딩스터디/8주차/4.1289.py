T = int(input())

for i in range(T):
    length = input()
    rule = '0'
    cnt = 0
    for j in length:
        if j != rule:
            rule = j
            cnt += 1
    print(f'#{i+1} {cnt}')
