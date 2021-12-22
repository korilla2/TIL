'''
6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)

True
'''

a, b = map(int, input().split())

if bool(a) == True or bool(b) == True:
    print('True')
else:
    print('False')
