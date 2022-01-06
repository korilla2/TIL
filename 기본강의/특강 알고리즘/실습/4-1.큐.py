queue = [None, None, None, None, None]
front = rear = -1

rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print(queue)


front += 1
data = queue[front]
queue[front] = None
print(data)
print(queue)

front += 1
data = queue[front]
queue[front] = None
print(data)
print(queue)

front += 1
data = queue[front]
queue[front] = None
print(data)
print(queue)
