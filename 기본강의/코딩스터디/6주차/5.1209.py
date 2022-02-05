def check_map(arr):  # 가로 줄 체크 함수
    result = []
    for i in range(len(arr)):  # 총 줄 수
        temp = 0
        for j in range(len(arr)):  # 가로 한 줄
            temp += arr[i][j]  # 한 줄 더해서
        result.append(temp)  # 밖에 모아둠
    return max(result)  # 젤 큰거 리턴


def check_map2(arr):  # 양쪽 대각선 체크 함수
    temp1 = 0  # 왼쪽 위에서 오른쪽 아래로
    temp2 = 0  # 오른쪽 위에서 왼쪽 아래로
    for i in range(len(arr)):
        temp1 += arr[i][i]
        temp2 += arr[i][99-i]
    return max(temp1, temp2)


T = 10

for i in range(T):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(100)]  # 기본 맵
    result1 = check_map(base)  # 가로 줄 검사
    base2 = list(zip(*base))  # 가로 세로 바꿈
    result2 = check_map(base2)  # 가로 줄 검사(가로 세로 바꿨으니 원래는 세로 검사와 같음)
    result3 = check_map2(base)  # 대각선 검사
    final_result = max(result1, result2, result3)  # 젤큰거 고름
    print(f'#{i+1} {final_result}')
