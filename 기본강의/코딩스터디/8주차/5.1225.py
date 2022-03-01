try:
    while True:
        N = int(input())
        base = list(map(int, input().split()))
        while True:
            for i in range(5):
                temp = base[0] - i - 1
                base.append(temp)
                base.remove(base[0])
                if temp <= 0:
                    break
            if temp <= 0:
                base[-1] = 0
                print(f'#{N}', *base)
                break

except:
    quit()
