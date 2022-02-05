'''
set 은 중복이 안되는 성질을 이용
1 부터 9 까지 잘 들어갔으면 갯수는 무조건
9개여야 정상
'''


def check_map(arr):
    for i in range(len(arr)):  # 총 줄 수
        temp = set()
        for j in range(len(arr)):  # 가로 한 줄
            temp.add(arr[i][j])  # set에 집어 넣음
        if len(temp) != 9:
            return False
    return True


def check_map2(arr):
    for i in range(0, 3, 9):  # 맵 가로 이동 범위
        for j in range(0, 3, 9):  # 맵 세로 이동 범위
            temp = set()
            for k in range(3):  # 실제 검사 가로 줄
                for l in range(3):  # 실제 검사 세로 줄
                    temp.add(arr[i + k][j + l])
            if len(temp) != 9:
                return False
    return True


T = int(input())

for i in range(T):
    base = [list(map(int, input().split())) for _ in range(9)]  # 기본 맵
    result1 = check_map(base)  # 가로 줄 검사
    base2 = list(zip(*base))  # 가로 세로 바꾸기
    result2 = check_map(base2)  # 바꾼 맵 가로 줄 검사
    result3 = check_map2(base)  # 부분검사

    if result1 == True and result2 == True and result3 == True:
        # 전부 검사를 통과 해야만 1 출력
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
