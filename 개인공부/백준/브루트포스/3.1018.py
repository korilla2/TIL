N, M = map(int, input().split())

base = []
for _ in range(N):
    base.append(list(input()))

result = []
for a in range(N - 7):
    for b in range(M - 7):
        cnt_w = 0
        cnt_b = 0
        for c in range(a, a+8):
            for d in range(b, b+8):
                if (c + d) % 2 == 0:
                    if base[c][d] != 'W':
                        cnt_w += 1
                    else:
                        cnt_b += 1
                else:
                    if base[c][d] != 'B':
                        cnt_w += 1
                    else:
                        cnt_b += 1
        result.append(cnt_w)
        result.append(cnt_b)
print(min(result))
