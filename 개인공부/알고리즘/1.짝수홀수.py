# 짝수
def is_even(num):
    # 홀수인지 짝수인지 판단
    # 2로 나누어서 나머지로 판단
    if num % 2 == 0:
        return '짝수'
    else:
        return '홀수'


print(is_even(3))
print(is_even(6))
