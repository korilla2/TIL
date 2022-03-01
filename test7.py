N = int(input())
base = list(map(int, input().split()))
for i in range(5):

    temp = base[i] - i - 1

    if temp <= 0:
        base = base.append(temp)
        print(f'#{N}', *base)
        break
    base.append(temp)


for j in range(5):
    base.remove(base[i])
