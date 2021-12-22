'''
6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)

B
'''

a = int(input())

if 100 >= a >= 90:
    print('A')
elif 90 > a >= 70:
    print('B')
elif 70 > a >= 40:
    print('C')
else:
    print('D')
