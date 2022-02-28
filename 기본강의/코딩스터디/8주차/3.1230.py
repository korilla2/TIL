def check_map(stack, arr):
    if stack[0] == 'I':
        x = int(stack[1])
        arr = arr[:x] + stack[3:] + arr[x:]
    elif stack[0] == 'A':
        arr = arr + stack[2:]
    elif stack[0] == 'D':
        x = int(stack[1])
        y = int(stack[2])
        arr = arr[:x] + arr[x+y:]
    return arr


for i in range(10):
    N = int(input())
    base = input().split()
    M = int(input())
    rule = input().split()

    stack = []

    for j in rule:
        if j in ['A', 'I', 'D']:
            if stack:
                base = check_map(stack, base)
                stack.clear()
        stack.append(j)
    base = check_map(stack, base)

    print(f'#{i+1}', *base[:10])
