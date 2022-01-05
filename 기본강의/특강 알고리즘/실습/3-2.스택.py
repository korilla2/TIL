def isStackFull():
    global size, stack, top
    if top >= size - 1:
        return True
    else:
        return False


def push(data):
    global size, stack, top
    if isStackFull():
        print('스택 꽉!')
        return
    else:
        top += 1
        stack[top] = data


def isStackEmpty():
    global size, stack, top
    if top <= -1:
        return True
    else:
        return False


def pop():
    global size, stack, top
    if isStackEmpty():
        print('스택 텅!')
        return None
    else:
        temp = stack[top]
        stack[top] = None
        top -= 1
        return temp


def peek():
    global size, stack, top
    if isStackEmpty():
        print('스택 텅!')
        return None
    else:
        return stack[top]


size = 5
top = -1
stack = [None for _ in range(size)]


if __name__ == '__main__':
    select = input('삽입(I)/추출(E)/확인(V)/종료(X)==>')

    while select != 'X' and select != 'x':
        if select == 'I' or select == 'i':
            data = input('입력할 데이터 ==>')
            push(data)
            print('스택상태 ==>', stack)

        elif select == 'E' or select == 'e':
            data = pop()
            print('추출된 데이터==>', data)
            print('스택상태 ==>', stack)

        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터==>', data)
            print('스택상태 ==>', stack)

        else:
            print('다시 입력하세요')

        select = input('삽입(I)/추출(E)/확인(V)/종료(X)==>')

    print('프로그램 종료')
