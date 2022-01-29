T = int(input())

for i in range(T):
    N = int(input())

    result = [[1], [1, 1]]
    cnt = 2
    idx = 0
    while cnt <= N:

        temp = []
        temp.append(result[cnt-1][idx] + result[cnt-1][idx+1])
        temp.insert(0, 1)
        temp.append(1)
        result.append(temp)

        idx += 1
        cnt += 1
    print(result)
