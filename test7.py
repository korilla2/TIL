from collections import Counter

result = [[1, 3, 3], [4, 7, 6], [7, 8, 9]]

print(result)

for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j])

b = sum(result, [])
a = Counter(b)
print(a)

sex = a.most_common(3)
print(sex)
