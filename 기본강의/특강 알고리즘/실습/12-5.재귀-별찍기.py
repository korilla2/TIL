def printstar(num):

    if num > 0:

        printstar(num-1)
        print('*' * num)


printstar(5)
