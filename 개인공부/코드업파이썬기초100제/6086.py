'''
6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)

66
'''

n = int(input())

a = 1
sum = 0

while True:
    sum += a
    a += 1

    if sum >= n:
        break
print(sum)
