'''
6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)

True
'''

a, b = map(int, input().split())

if bool(a) == True and bool(b) == True:
    print('True')
else:
    print('False')
