'''
6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

6 2.00
'''

a, b, c = map(int, input().split())

d = a + b + c

result = d / 3
result = round(result, 2)

print(f'{d} {result:.2f}')
