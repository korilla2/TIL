'''
6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)

63
'''

a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)
