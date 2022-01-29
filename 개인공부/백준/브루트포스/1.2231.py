N = int(input())


for i in range(1, N + 1):
    int_i = i
    str_i = list(map(int, str(i)))

    result = int_i + sum(str_i)

    if result == N:
        print(int_i)
        break
    if i == N:
        print(0)
