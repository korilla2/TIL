def gugudan(dan, num):
    print(f'{dan} x {num} = {dan*num}')
    if num < 9:
        gugudan(dan, num+1)


for dan in range(2, 10):
    gugudan(dan, 1)
