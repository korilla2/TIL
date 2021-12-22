'''
6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

A
'''

a = int(input())

if a < 0 and a % 2 == 0:
    print('A')
elif a < 0 and a % 2 == 1:
    print('B')
elif a > 0 and a % 2 == 0:
    print('C')
elif a > 0 and a % 2 == 1:
    print('D')
