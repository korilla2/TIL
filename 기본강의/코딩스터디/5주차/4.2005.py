T = int(input())

for i in range(T):
    N = int(input())

    base = [[1], [1, 1]]

    for j in range(N-2):
        temp1 = []
        temp2 = base[-1]
        for k in range(len(temp2)-1):
            temp1.append(temp2[k] + temp2[k+1])
        temp1.insert(0, 1)
        temp1.append(1)
        base.append(temp1)

    if N == 1:
        base = [[1]]

    print(f'#{i+1}')
    for q in base:
        for r in q:
            print(r, end=' ')
        print()
