numData = \
    [
        [5, 7, -5, 100, 73],
        [35, 23, 4, 190, 33],
        [49, 85, 662, 39, 81],
        [124, -59, 86, 46, 52],
        [27, 7, 8, 33, -56]
    ]


for i in range(len(numData)):
    for j in range(len(numData[i])):
        if numData[i][j] < 0:
            numData[i][j] = 0
        elif numData[i][j] > 100:
            numData[i][j] = numData[i][j] % 100
temp = 0
for j in range(len(numData) - 1):
    for i in range(len(numData) - 1):
        a = numData[j][i] + numData[j+1][i] + \
            numData[j][i+1] + numData[j+1][i+1]
        if a > temp:
            temp = a
print(temp)
