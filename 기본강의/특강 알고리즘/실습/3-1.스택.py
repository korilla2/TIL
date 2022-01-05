size = 5
stack = [None for _ in range(size)]
top = -1

top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print(stack)

data = stack[top]
stack[top] = None
top -= 1
print(data)
data = stack[top]
stack[top] = None
top -= 1
print(data)
data = stack[top]
stack[top] = None
top -= 1
print(data)
print(stack)
