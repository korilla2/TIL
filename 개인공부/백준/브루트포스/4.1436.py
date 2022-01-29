N = int(input())
cnt = 1
i = 1
result = []
while cnt <= N:
    temp = list(str(i))
    for j in range(len(temp)-2):
        if temp[j] == '6' and temp[j+1] == '6' and temp[j+2] == '6':
            result.append(i)
            cnt += 1
            break
    i += 1
print(result[-1])
