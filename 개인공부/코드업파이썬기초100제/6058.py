'''
6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)

True
'''

a, b = map(int, input().split())

if bool(a) == False and bool(b) == False:
    print('True')
else:
    print('False')