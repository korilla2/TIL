from collections import deque

c = deque()
d = deque()
for i in range(3):
    a = list(map(int, input().split()))

    c.append(a[0])
    d.append(a[1])

while c[0] != c[1]:
    k = c.popleft()
    c.append(k)


while d[0] != d[1]:
    k = d.popleft()
    d.append(k)


print(c[-1], d[-1])
