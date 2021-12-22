'''
6098 : [기초-리스트] 성실한 개미(py)

1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
result = []
for i in range(10):
    m = list(map(int, input().split()))
    result.append(m)

x = 2
y = 2
a = x - 1
b = y - 1
result[a][b] = 9
while True:
    if result[a][b] == 0:
        result[a][b] = 9
    elif result[a][b] == 2:
        result[a][b] = 9
        break

    elif result[a][b + 1] != 1:
        b += 1
    elif result[a + 1][b] != 1:
        a += 1

    elif result[a][b + 1] == 1 and result[a + 1][b] == 1:
        break


for i in result:
    for j in i:
        print(j, end=' ')
    print()
