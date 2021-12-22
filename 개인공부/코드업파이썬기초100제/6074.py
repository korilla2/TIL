'''
6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)

a b c d e f
'''
s = ord(input())
k = ord('a')
while True:

    l = chr(k)
    print(l, end=' ')
    k += 1
    if k > s:
        break
