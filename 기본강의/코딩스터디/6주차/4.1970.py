T = int(input())

for i in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 총 돈의 종류

    for j in money:  # 돈 종류 별로 하나씩 다 검사
        if N >= j:
            cnt = N // j  # 해당 돈으로 몇 번 가능한지
            N = N - j * cnt
            idx = money.index(j)
            money[idx] = cnt  # 해당 돈의 위치에 갯수로 바꿔버림
        else:
            idx = money.index(j)
            money[idx] = 0  # 안 쓴 애들은 0으로 바꿔버림
    print(f'#{i+1}')
    print(*money)
