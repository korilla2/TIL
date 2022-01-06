def is_que_full():
    global size, queue, front, rear
    if rear == size - 1:
        return True
    else:
        return False


def enque(data):
    global size, queue, front, rear
    if is_que_full():
        print('큐 꽉!')
        return
    rear += 1
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
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_que_empty():
        print('큐 텅!')
        return None
    return queue[front+1]


size = 5
queue = [None for _ in range(size)]
front = rear = -1

enque('화사')
enque('솔라')
enque('문별')
enque('휘인')
enque('선미')
print(queue)
