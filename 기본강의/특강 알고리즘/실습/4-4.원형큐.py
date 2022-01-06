def is_que_full():
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False


def enque(data):
    global size, queue, front, rear
    if is_que_full():
        print('큐 꽉!')
        return
    rear = (rear + 1) % size
    queue[rear] = data


def is_que_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def deque():
    global size, queue, front, rear
    if is_que_empty():
        print('큐 텅!')
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_que_empty():
        print('큐 텅!')
        return None
    return queue[(front + 1) % size]


size = 5
queue = [None for _ in range(size)]
front = rear = 0

enque('화사')
enque('솔라')
enque('문별')
enque('휘인')
enque('선미')
print(queue)

print('입장 손님', deque())
print('입장 손님', deque())

print(queue)

enque('재남')
print(queue)

enque('BTS')
print(queue)

enque('울랄라')
print(queue)

print('입장 손님', deque())
print(queue)
print(queue)

enque('재남')
print(queue)

enque('BTS')
print(queue)

enque('울랄라')
print(queue)

print('입장 손님', deque())
print(queue)
