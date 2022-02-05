def check_map(arr, m):
    length = len(arr) - m + 1
    result = []
    for i in range(length):  # 가로줄 이동 횟수
        for j in range(length):  # 세로줄 이동 횟수
            temp = 0
            for k in range(m):  # 실제 검사할 가로 범위
                for l in range(m):  # 실제 검사할 세로 범위
                    temp += arr[i + k][j + l]
            result.append(temp)
    return max(result)


T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(N)]  # 기본 맵
    result = check_map(base, M)  # 함수에 넣기
    print(f'#{i+1} {result}')
