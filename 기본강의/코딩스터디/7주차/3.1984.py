T = int(input())

for i in range(T):
    base = list(map(int, input().split()))
    base.remove(max(base))
    base.remove(min(base))
    result = sum(base) / len(base)
    print(f'#{i+1} {round(result)}')
