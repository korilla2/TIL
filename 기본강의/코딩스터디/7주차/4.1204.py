T = int(input())

for i in range(T):
    temp = [0] * 101
    N = int(input())
    base = list(map(int, input().split()))
    for j in range(len(base)):
        temp[base[j]] += 1

    result = []

    for idx, val in enumerate(temp):
        if val == max(temp):
            result.append(idx)

    max_idx = max(result)

    print(f'#{i+1} {max_idx}')
