'''
6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

True
'''

a, b = map(int, input().split())

if bool(a) == bool(b):
    print('True')
else:
    print('False')
