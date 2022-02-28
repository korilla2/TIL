T = int(input())

temp2 = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(T):
    N = list(map(int, input().split()))
    base = []
    result = dict()
    for j in range(N[0]):
        base.append(list(map(int, input().split())))

    for k in range(len(base)):
        result[k] = [base[k][0] * 0.35 +
                     base[k][1] * 0.45 + base[k][2] * 0.2]
    result = sorted(result.items(), key=lambda item: item[1], reverse=True)

    a = N[0] // 10
    cnt = 0
    for key, val in result:
        temp3 = cnt // a
        if N[1] - 1 == key:
            print(f'#{i+1} {temp2[temp3]}')
            break
        cnt += 1
