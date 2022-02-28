def check(f_stack, f_lst):
    if f_stack[0] == 'I':
        sp = int(f_stack[1])
        f_lst = f_lst[:sp] + f_stack[3:] + f_lst[sp:]
    elif f_stack[0] == 'D':
        sp = int(f_stack[1])
        num = int(f_stack[2])
        f_lst = f_lst[:sp] + f_lst[sp+num:]
    elif f_stack[0] == 'A':
        f_lst = f_lst + [stack[2:]]
    return f_lst


# for tc in range(1, 11):
N = int(input())
lst = list(input().split())
P = int(input())
stack = []
p_lst = input().split()
for i in p_lst:
    if i in ['I', 'D', 'A']:
        if stack:
            lst = check(stack, lst)
            stack.clear()
    stack.append(i)
lst = check(stack, lst)
print(f'#{tc}', *lst[:10])
