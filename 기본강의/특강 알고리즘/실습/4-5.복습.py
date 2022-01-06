def is_que_empty():
    global size, queue, front, rear
    if rear == front:
        return True
    return False


def is_que_full():
    global size, queue, front, rear
    if (rear + 1) % size == front:
        return True
    else:
        return False


def en_que(data):
    global size, queue, front, rear
    if is_que_full():
        print('큐 풀!')
        return
    else:
        rear = (rear + 1) % size
        queue[rear] = data
        return


def de_que():
    global size, queue, front, rear
    if is_que_empty():
        print('큐 텅!')
        return
    else:
        front = (front + 1) % size
        data = queue[front]
        queue[front] = None
        return data


def peek():
    global size, queue, front, rear
    if is_que_empty():
        print('큐 텅!')
        return
    else:
        return queue[(front + 1) % size]


size = 5
queue = [None for _ in range(size)]
front = rear = 0

en_que('화사')
en_que('솔라')
en_que('문별')
en_que('휘인')
en_que('선미')
print(queue)

print('입장 손님', de_que())
print('입장 손님', de_que())

print(queue)

en_que('재남')
print(queue)

en_que('BTS')
print(queue)

en_que('울랄라')
print(queue)

print('입장 손님', de_que())
print('입장 손님', de_que())

print('입장 손님', de_que())
print('입장 손님', de_que())
print(queue)

en_que('선미')
print(queue)

en_que('문별')
en_que('휘인')
print(queue)
en_que('화사')
en_que('솔라')
print('입장 손님', de_que())
print('입장 손님', de_que())
print(queue)
