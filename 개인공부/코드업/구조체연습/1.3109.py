n = int(input())

base = [input().split() for _ in range(n)]

code = tuple(map(int, input().split()))
result = {}
for i in base:
    if i[0] == 'I':
        if i[1] in result:
            result[i[1]].insert(0, i[2])
        else:
            result[i[1]] = [i[2]]
    elif i[0] == 'D':
        if i[1] in result:
            if len(result[i[1]]) > 1:
                del result[i[1]][0]
            else:
                del result[i[1]]
        else:
            pass

result = sorted(result.items(), key=lambda x: int(x[0]))
result2 = {}
for i in range(len(result)):
    result2[i+1] = result[i]

result3 = {}
for i in code:
    result3[i] = result2[i]

result4 = {}
for i in result3.values():
    result4[i[0]] = i[1]


cnt = 0
for key, val in result4.items():
    if cnt == len(code):
        break
    elif len(val) > 1:
        for i in range(len(val)):
            print(key, val[i])
            cnt += 1
            if cnt == len(code):
                break
    else:
        print(key, *val)
        cnt += 1
        if cnt == len(code):
            break
