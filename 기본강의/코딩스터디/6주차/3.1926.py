N = int(input())

for i in range(1, N+1):
    temp = str(i)  # 문자로 변경

    if '3' in temp or '6' in temp or '9' in temp:  # 문자가 있는지 검사
        # 있다면 문자 갯수만큼 '-' 출력
        print('-' * (temp.count('3') + temp.count('6') + temp.count('9')), end=' ')
    else:
        print(temp, end=' ')  # 아니면 그냥 숫자형태로 출력
