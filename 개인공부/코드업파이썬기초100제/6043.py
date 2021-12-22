'''
6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)

3.333
'''

a, b = map(float, (input().split()))

c = a / b

c = round(c, 3)

print(f'{c:.3f}')
